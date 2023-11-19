from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['title','publication','category','available']
    list_filter=['available','category']
    prepopulated_fields={"slug" : ['title']}
    list_editable=["available"]