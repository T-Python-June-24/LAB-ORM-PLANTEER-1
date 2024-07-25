from django.contrib import admin

from .models import Plants, Reviews 




class PlantsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_edible', 'created_at')  # Remove 'rating'
    list_filter = ('category', 'is_edible')  # Remove 'rating'



class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'created_at')
    list_filter = ('rating','created_at')
    search_fields = ('name', 'rating')
    ordering = ('-created_at',)
    
    
# Register your models here.
admin.site.register(Plants,PlantsAdmin)
admin.site.register(Reviews,ReviewsAdmin)
