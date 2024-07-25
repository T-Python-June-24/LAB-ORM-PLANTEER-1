from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    list_filter = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')

admin.site.register(Contact)