from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title' , 'price' , 'realtor' , 'list_date' , 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('realtor' ,) 
    search_fields = ('title', 'price', 'address', 'city','state','zip_code')
    list_per_page = 20


admin.site.register(Listing , ListingAdmin)