from django.contrib import admin
from models import *
from django import forms

class ResAdminInline(admin.TabularInline):
    model = Restaurant.admins.through
    extra = 1

class UserForm(forms.ModelForm):
    class Meta:
        model = User

class UserAd(admin.ModelAdmin):
    form = UserForm

class RestAdmin(admin.ModelAdmin):
    inlines = [ResAdminInline,
        ]

admin.site.register(Restaurant, RestAdmin)
admin.site.register(User, UserAd)
