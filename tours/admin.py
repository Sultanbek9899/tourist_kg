
from django.contrib import admin


# Register your models here.
from tours.models import Tour, RegularTour


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = [
        "title", 
        "price", 
        "created", 
        "updated" ,
        "is_active",
        ]
    list_filter = [
        "created",
        "is_active", 
        "price"]
    search_fields = [
        "title", 
        "created", 
        "description"
        ]
    list_editable = [
        "is_active",
        "price"    
    ]


@admin.register(RegularTour)
class RegularTourAdmin(admin.ModelAdmin):
    list_display = [
        'tour',
        'start',
        'end',
        'places_count',
        'status',
    ]
    list_filter = [
        "start",
        "end",
        "status",
    ]
    search_fields = [
        "tour__title",
        "start",
        "end",
    ]
    list_editabe = [
        "status", 
        "start",
        "end",
        "places_count",
    ]