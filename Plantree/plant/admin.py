from django.contrib import admin
from .models import Plants #class name


class PlantAdmin(admin.ModelAdmin):
    list_display= ("name", "category", "created_at") # display this attribute in admin dashboard
    list_filter= ("category",) # filter the table by it's category. you can filter two table with two attribute


admin.site.register(Plants,PlantAdmin)



