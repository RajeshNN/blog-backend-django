from django.contrib import admin
from .models import post_list
from django.contrib.admin import AdminSite
from django.contrib.admin.forms import AuthenticationForm

class PostAdmin(admin.ModelAdmin):
    list_display = ('url',)

admin.site.register(post_list, PostAdmin)
