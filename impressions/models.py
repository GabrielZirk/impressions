from django.db import models
from profiles.models import Profile

# Create your models here.


class Trip(models.Model):
    tripname = models.CharField(
        'Tripname', max_length=200, blank=False, null=False, unique=True, help_text="Give your trip a fancy name")
    short_description = models.TextField('Trip description', blank=True, null=True,
                                         unique=True, help_text="Briefly describe your trip (optional)", max_length=1000)
    start_date = models.DateField(
        auto_now=False, auto_now_add=False, help_text="When did you leave?")
    end_date = models.DateField(
        auto_now=False, auto_now_add=False, help_text="When did you come back?")
    traveller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    companions = models.CharField(max_length=300)

    class Meta:
        ordering = ["start_date"]
        verbose_name_plural = "trips"

    def __str__(self):
        return f"{self.tripname} from {self.start_date} to {self.end_date}"


class Stopover(models.Model):
    city = models.CharField('City', max_length=100)
    trip = models.ForeignKey(
        'Trip', on_delete=models.CASCADE, related_name="stopovers")
    start_date = models.DateField(
        auto_now=False, auto_now_add=False, help_text="When did you arrive?")
    end_date = models.DateField(
        auto_now=False, auto_now_add=False, help_text="When did you leave")

    class Meta:
        ordering = ["city"]
