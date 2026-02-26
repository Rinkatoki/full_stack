from django.shortcuts import render, redirect
from .models import Person

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            Person.objects.create(name=name)
            return redirect("home")

    people = Person.objects.all()
    return render(request, "home.html", {"people": people})