import random
from django.shortcuts import render
from . import util
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages 
import markdown2

class NewSearchForm(forms.Form):
    title = forms.CharField(
        label="", 
        required=False, 
        widget=forms.TextInput(attrs={'placeholder':'Search Encyclopedia','style': 'width:100%'}),
    )

class NewPageForm(forms.Form):
    newtitle = forms.CharField(
        label="", 
        required=False,
        widget=forms.TextInput(attrs={'placeholder':'Title of page'})
    )
    newcontent = forms.CharField(
        label="", 
        required=False, 
        widget=forms.Textarea(attrs={'placeholder':'Contents of page', 'style' : 'width: 80%'})
    )

class NewEditForm(forms.Form):
    newcontent = forms.CharField(
        label="", 
        required=False, 
        widget=forms.Textarea(attrs={'style' : 'width: 80%'})
    )

def index(request):

    # search is used
    if request.method == "POST":
        form = NewSearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]

            # if search has exact match
            if util.get_entry(title)!=None:
                return render(request, "encyclopedia/entry.html", {
                    "title": title.upper(),
                    "form": NewSearchForm,
                    "content": markdown2.markdown(util.get_entry(title)),
                })

            # if search has non-exact match    
            else:
                return render(request, "encyclopedia/search.html", {
                    "form": form,
                    "entries": search(title),
                })

        # non-valid search result        
        else:
            return render(request, "encyclopedia/index.html", {
                "form": form,
                "entries": util.list_entries()
            })

    # search is not used, initialise page
    return render(request, "encyclopedia/index.html", {
        "form": NewSearchForm,
        "entries": util.list_entries()
    })

def entry(request, title):
    form = NewSearchForm(request.POST)

    if util.get_entry(title) != None:
        return render(request, "encyclopedia/entry.html", {
            "form" : form,
            "title": title.upper(),
            "content": markdown2.markdown(util.get_entry(title)),
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "form" : form,
            "title": title.upper(),
            "content": None,
        })

def search(title):
    title = title.lower()
    #returns search_results=[]
    search_results = []
    for entry in util.list_entries():
        if title in entry.lower():
            search_results.append(entry)
    return search_results

def newpage(request):
    form = NewSearchForm(request.POST)
    pageform = NewPageForm(request.POST)

    if request.method == "POST":
        if pageform.is_valid():
            newtitle = pageform.cleaned_data["newtitle"]
            newcontent = pageform.cleaned_data["newcontent"]
            if newtitle not in util.list_entries():
                util.save_entry(newtitle, newcontent)
            else:
                # error message
                return render(request, "encyclopedia/newpage.html", {
                    "form" : form,
                    "pageform" : pageform.as_p,
                    "page_exists": True
                })  
            return render(request, "encyclopedia/entry.html", {
                "form" : form,
                "title": newtitle.upper(),
                "content": markdown2.markdown(util.get_entry(newtitle)),
            })  

    return render(request, "encyclopedia/newpage.html", {
        "form" : form,
        "pageform" : pageform,
    })

def edit(request, title):
    form = NewSearchForm(request.POST)
    editform = NewEditForm(initial = {"newcontent": util.get_entry(title)})
    # if request is posted
    if request.method == "POST":
        editform = NewEditForm(request.POST)
        if editform.is_valid():
            newcontent = editform.cleaned_data["newcontent"]
            util.save_entry(title, newcontent)
            return render(request, "encyclopedia/entry.html", {
                    "form" : form,
                    "title": title.upper(),
                    "content": markdown2.markdown(util.get_entry(title)),
                })
    # no request
    return render(request, "encyclopedia/edit.html", {
        "title": title.upper(),
        "editform" : editform,
        "form" : form,
    })

def random_entry(request):
    entries = util.list_entries()
    title = random.choice(entries)
    form = NewSearchForm(request.POST)
    return render(request, "encyclopedia/entry.html", {
        "form" : form,
        "title": title.upper(),
        "content": markdown2.markdown(util.get_entry(title)),
    })