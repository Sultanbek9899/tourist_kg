from django.shortcuts import render

# Create your views here.
from tours.models import Tour, RegularTour

def get_tour_list(request):
    tours = Tour.objects.filter(is_active=True)
    context = {
        "tours":tours,
    }
    return render(request, 'tour_list.html', context=context)

