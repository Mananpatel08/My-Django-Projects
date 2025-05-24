from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Track(models.Model):
    date = models.DateField()
    tiffin_price = models.DecimalField(max_digits=6, decimal_places=2, default=120)
    total_tiffins = models.PositiveIntegerField()
    eat_by = models.ManyToManyField(Member, related_name="tiffins")
    
    
    notes = models.TextField(blank=True, null=True)

    @property
    def weekday(self):
        return self.date.strftime('%A')

    @property
    def total_price(self):
        return self.tiffin_price * self.total_tiffins

    @property
    def eat_by_count(self):
        return self.eat_by.count()

    @property
    def eat_by_details(self):
        members = self.eat_by.all()
        count = members.count()
        names = ", ".join(member.name for member in members)
        return f"{count} ({names})" if count > 0 else "No members selected"
    
    @property
    def per_person_price(self):
        if self.eat_by_count > 0:
            return round((self.tiffin_price * self.total_tiffins) / self.eat_by_count, 2)
        return 0  

    def __str__(self):
        return f"Tiffin on {self.date} ({self.weekday})"

class Wallet(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.member.name} - ₹{self.total_amount}"
