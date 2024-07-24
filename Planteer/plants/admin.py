from django.contrib import admin
from .models import Plant ,Review
# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    list_display=("name","comment","created_at","plant")
    list_filter=("created_at","name",)
admin.site.register(Plant)
admin.site.register(Review,ReviewAdmin) 