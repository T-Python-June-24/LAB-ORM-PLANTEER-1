from django.contrib import admin
from .models import Plant, Reivew, Countries

# Register your models here.

class PlantAdmin(admin.ModelAdmin):

    list_display = ("name", "about")
    list_filter = ("category",)


class ReviewAdmin(admin.ModelAdmin):

    list_display =  ("name", "message")
    list_filter = ("plant",)

admin.site.register(Plant, PlantAdmin)
admin.site.register(Reivew, ReviewAdmin)
admin.site.register(Countries)