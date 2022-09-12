from django.contrib import admin
from .models import Trip, Stopover

# Register your models here.


class StopoverInline(admin.TabularInline):
    model = Stopover


class TripAdmin(admin.ModelAdmin):
    list_display = ("tripname", "traveller", "start_date", "end_date")
    list_filter = ("traveller", "start_date")
    inlines = [StopoverInline]


class StopoverAdmin(admin.ModelAdmin):
    list_display = ("city", "start_date", "end_date")


admin.site.register(Trip, TripAdmin)
admin.site.register(Stopover, StopoverAdmin)
