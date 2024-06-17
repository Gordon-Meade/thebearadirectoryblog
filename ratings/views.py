from django.shortcuts import render

# Create your views here.
# ratings/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Area, Rating

@login_required
def rate_area(request, area_id):
    if request.method == 'POST':
        stars = int(request.POST.get('stars', 0))
        area = Area.objects.get(pk=area_id)
        user = request.user

        # Check if the user has already rated this area
        existing_rating = Rating.objects.filter(user=user, area=area).first()

        if existing_rating:
            existing_rating.stars = stars
            existing_rating.save()
        else:
            new_rating = Rating(user=user, area=area, stars=stars)
            new_rating.save()

        return redirect('area_detail', area_id=area_id)  # Redirect to area detail page or any other page
    else:
        return redirect('home')  # Redirect to home or appropriate page if not POST request

def area_detail(request, area_id):
    area = Area.objects.get(pk=area_id)
    ratings = Rating.objects.filter(area=area)
    context = {
        'area': area,
        'ratings': ratings,
    }
    return render(request, 'ratings/area_detail.html', context)
