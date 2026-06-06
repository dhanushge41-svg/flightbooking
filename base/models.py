from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Flight(models.Model):
    airline = models.CharField(max_length=100)
    flight_no = models.CharField(max_length=20)
    from_city = models.CharField(max_length=100)
    to_city = models.CharField(max_length=100)
    departure_time = models.TimeField()
    date = models.DateField()
    price = models.IntegerField()
    host = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.airline} - {self.flight_no}"





class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
     
    booking_date = models.DateTimeField(auto_now_add=True)
    host = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} - {self.flight}"

# Create your models here.
class profile(models.Model):
    pimage = models.ImageField(upload_to='uploads/',default='dfimg.jpg.jpeg')
    host=models.ForeignKey(User,on_delete=models.CASCADE)