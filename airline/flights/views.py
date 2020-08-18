from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Passenger, Airport

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all(),
    })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all(),
    })

def book(request, flight_id):
    if request.method =="POST":
        flight = Flight.objects.get(pk=flight_id)
        # name of input POST form is passenger
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))