from django import forms
from .models import Lift_data

class Lift_form(forms.ModelForm):
    class Meta:
        model = Lift_data
        fields = [ 'current_floor' , 'target_floor' , 'passenger_count' ]
        
    
    # def clean_passenger_count(self):
    #     passenger_count = self.cleaned_data.get('passenger_count')
    #     current_floor = self.cleaned_data.get( 'current_floor' )
    #     target_floor = self.cleaned_data.get( 'target_floor')
        
    #     if current_floor == target_floor:
    #         raise forms.ValidationError("You are already on your target floor.")
    #     if passenger_count > 10:
    #         raise forms.ValidationError('Passenger Capacity is 10 Persons.')
    #     return passenger_count
    
    