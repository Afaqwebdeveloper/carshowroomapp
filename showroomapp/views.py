from django.shortcuts import render, get_object_or_404
from .models import Brand, Staff

def home(request):
    brands = Brand.objects.all()
    return render(request, 'showroomapp/home.html', {'brands': brands})


def brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    models = brand.model_set.all()
    return render(request, 'showroomapp/brand.html', {'brand': brand, 'models': models})


def team(request):
    staff_members = Staff.objects.all()
    return render(request, 'showroomapp/team.html', {'staff_members': staff_members})

