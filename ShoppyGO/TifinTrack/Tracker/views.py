from django.shortcuts import render, redirect
from .forms import TrackForm
from .models import Wallet, Track


def home(request):
    if request.method == "POST":
        form = TrackForm(request.POST)
        if form.is_valid():
            track = form.save(commit=False) 
            track.save()  
            form.save_m2m()  

            per_person_price = track.per_person_price 

            for member in track.eat_by.all():
                wallet, created = Wallet.objects.get_or_create(member=member)
                
                if created:
                    wallet.total_amount = per_person_price 
                else:
                    wallet.total_amount += per_person_price

                wallet.save()
        
            return redirect("home") 
        
    else:
        form = TrackForm()

    return render(request, "home.html", {"form": form})


def wallet_history(request):
    data = Wallet.objects.all()
    return render(request, "wallet_history.html" , {"data": data})

def track_history(request):
    data = Track.objects.all().order_by("-date")
    return render(request, "track_history.html" , {"data": data})