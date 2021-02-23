from django.contrib import admin
from . models import Location,Image,Category


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    filter_horizontal =('image',)

admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)
