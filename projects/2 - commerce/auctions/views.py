from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms
from .models import User, Auction, Bid, WatchList, Comment

class CreateListing(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ['title' , 'description' , 'price', 'category' , 'image_url']

class CreateBid(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']

class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

def index(request):
    return render(request, "auctions/index.html", {
        "auctions": Auction.objects.filter(is_active=True),
    })

def categories(request):
    CATEGORY = ['clothes', 'shoes', 'electronics', 'food', 'displays', 'sports', 'health', 'furniture', 'miscellaneous']
    return render(request, "auctions/categories.html", {
        "categories": CATEGORY,
    })

def category(request, category):
    return render(request, "auctions/index.html", {
        "auctions": Auction.objects.filter(is_active=True, category=category),
    })

def viewlisting(request, listing_id):
    item = Auction.objects.get(pk=listing_id)
    newbid = CreateBid(request.POST or None)
    newcomment=CreateComment(request.POST or None)
    bid_error = already_watching = not_watching = add_success = remove_success = False

    if request.method == "POST" and 'add_bid' in request.POST:
        if newbid.is_valid():
            bid = newbid.cleaned_data['amount']
            if bid > item.price:
                # if  bid > price of item
                temp = newbid.save(commit=False)
                temp.bidder = request.user
                temp.listing = item
                temp.save()
                # change price of item to new bid
                item.price = bid
                item.highest_bidder = request.user
                item.save()
            else:
                bid_error = True
    
    elif request.method == "POST" and 'add_watchlist' in request.POST:
        if WatchList.objects.filter(user=request.user, listing=listing_id).exists():
            already_watching = True
        else:
            user_list, created = WatchList.objects.get_or_create(user=request.user)
            user_list.listing.add(item)
            add_success = True

    elif request.method == "POST" and 'remove_watchlist' in request.POST:
        if WatchList.objects.filter(user=request.user, listing=listing_id).exists():
            WatchList.objects.get(user=request.user).listing.remove(listing_id)
            remove_success = True
        else:
            not_watching = True
    
    elif request.method == "POST" and 'close_auction' in request.POST:
        item.is_active = False
        item.save()
    
    elif request.method == "POST" and 'post_comment' in request.POST:
        if newcomment.is_valid():
            temp = newcomment.save(commit=False)
            temp.user = request.user
            temp.listing = item
            temp.save()

    return render(request, "auctions/listing.html", {
        "listing": item, "newbid" : newbid, "bid_error": bid_error, "newcomment": newcomment,
        "add_success": add_success, "already_watching": already_watching, "remove_success": remove_success, "not_watching": not_watching,
        "comments": Comment.objects.filter(listing=listing_id),
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def watchlist(request):
    userlist = WatchList.objects.get(user=request.user)
    return render(request, "auctions/watchlist.html", {
        "watchlist": userlist.listing.all(),
    })


@login_required
def createlisting(request):
    newlisting = CreateListing()
    if request.method == "POST":
        newlisting = CreateListing(request.POST)
        if newlisting.is_valid():
            temp = newlisting.save(commit=False)
            temp.user = request.user
            temp.save()
            return HttpResponseRedirect(reverse("index"))
    return render(request, "auctions/createlisting.html",{
        "newlisting" : newlisting,
    })