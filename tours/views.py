from django.shortcuts import render

# Create your views here.
from tours.models import Tour, RegularTour
from django.http import Http404
def get_tour_list(request):
    tours = Tour.objects.filter(is_active=True)
    context = {
        "tours":tours,
    }
    return render(request, 'tour_list.html', context=context)


def get_tour_detail(request, pk):
    try:
        tour = Tour.objects.get(id=pk)
    except Tour.DoesNotExist: 
        raise Http404
    context ={
        "tour":tour
    }
    return render(request, 'tour_detail.html', context)
