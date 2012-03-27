from django.contrib import admin
from django import forms
from core.models import Beer, Brewery

class BeerAdmin(admin.ModelAdmin):
	fieldsets = [
	    ('Information', {'fields': ['name', 'brewery', 'ounces', 'price']}),
	]
	ordering = ('name', 'brewery',)
	list_display = ('name', 'brewery',)
	list_filter = ['brewery']
    
class BreweryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Information', {'fields': ['name']})
    ]
    ordering = ('name',)
    list_display = ('name',)
    
admin.site.register(Brewery, BreweryAdmin)
admin.site.register(Beer, BeerAdmin)