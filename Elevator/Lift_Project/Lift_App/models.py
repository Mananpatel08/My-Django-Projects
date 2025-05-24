from django.db import models

# Create your models here.
class Lift_data(models.Model):
    
    FLOOR_CHOICES = [(i, i) for i in range(0, 10)]  # Floors 1 to 10

    current_floor = models.IntegerField(choices=FLOOR_CHOICES)
    target_floor = models.IntegerField(choices=FLOOR_CHOICES)

    passenger_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
                 
    def __str__(self):
        return f'{self.current_floor} -> {self.target_floor} with {self.passenger_count} passenger '
     
