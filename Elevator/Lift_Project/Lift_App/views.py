from django.shortcuts import render
from .forms import Lift_form
from .models import Lift_data

def Lift(request):
    target_floor = None  # Default target floor

    if request.method == "POST":
        form = Lift_form(request.POST)
        if form.is_valid():
            lift_data = form.save()  # Save the submitted data
            target_floor = lift_data.target_floor  
            form = Lift_form()

    else:
        form = Lift_form()

    # Fetch the latest lift state if no new data is submitted
    if target_floor is None:
        latest_lift_data = Lift_data.objects.last()  # Get the most recent lift data
        if latest_lift_data:
            target_floor = latest_lift_data.target_floor

    return render(request, "Lift.html", {"form": form, "target_floor": target_floor})
