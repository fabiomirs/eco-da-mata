from django.shortcuts import render

from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import People


def people_list(request):
    people_list = get_list_or_404(People)
    return render(request, 'people_list.html', {'people_list': people_list})


