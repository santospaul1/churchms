from django.contrib import admin

from .models import Admin, Member

# Register your models here.
admin.site.register(Member)
admin.site.register(Admin)