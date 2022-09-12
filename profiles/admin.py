from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name",
                    "last_name", "birth_date")

    def username(self, obj):
        return obj.user.username

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name


admin.site.register(Profile, ProfileAdmin)
