from django.shortcuts import render, redirect

# Create your views here.
from tours.models import Tour, RegularTour
from django.http import Http404
from tours.forms import TourBookingForm
from tours.utils import minus_place_count


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

    form = TourBookingForm()
    context ={
        "tour":tour,
        "form":form
    }
    return render(request, 'tour_detail.html', context)




def create_booking_tour(request, tour_pk):  
    if request.method == "POST": 
        form = TourBookingForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            minus_place_count(
                data["regular_tour"].id, 
                data["place_count"]
                )
            return redirect("tour_detail", pk=tour_pk)
    else:
        print("asdasd")
        return redirect("tour_detail", pk=tour_pk)