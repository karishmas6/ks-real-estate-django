from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
from .choices import price_choices, state_choices, bedroom_choices
from .models import Listing

def index(request):
     listings = Listing.objects.order_by('-list_date').filter(is_published = True) # Fetching data from db

     paginator = Paginator(listings,3) # Show 3 listings per page
     page_number = request.GET.get('page')
     paged_listings = paginator.get_page(page_number)

     context = {
          'listings': paged_listings
     }
     return render (request , 'listings/listings.html', context)


def listing(request,listing_id):
     #If user searches for an invalid listing , display a 404 error page

     listing = get_object_or_404(Listing , pk=listing_id)

     context = {
          'listing': listing
     }

     return render (request , 'listings/listing.html',context)

def search(request):
     query_setlist = Listing.objects.order_by('-list_date')

     #Keywords 
     if 'keywords' in request.GET:
          keywords = request.GET['keywords']
          if keywords:
               # To check if description contains a particular keyword 
               query_setlist = query_setlist.filter(description__icontains = keywords)

     #City 
     if 'city' in request.GET:
          city = request.GET['city']
          if city:
               query_setlist = query_setlist.filter(city__iexact = city)
     
     #State 
     if 'state' in request.GET:
          state = request.GET['state']
          if state:
               query_setlist = query_setlist.filter(state__iexact = state)

     #Bedrooms
     if 'bedrooms' in request.GET:
          bedrooms = request.GET['bedrooms']
          if bedrooms:
               query_setlist = query_setlist.filter(bedrooms__lte = bedrooms)

     #Price
     if 'price' in request.GET:
          price = request.GET['price']
          if price:
               query_setlist = query_setlist.filter(price__lte = price)

     context = {
        'price_choices': price_choices,
        'state_choices': state_choices,
        'bedroom_choices':  bedroom_choices,
        'listings': query_setlist,
        'values': request.GET # preserving form inputs 

     }
     return render (request , 'listings/search.html',context)
