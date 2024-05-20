from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from .models import Community, News

# Create your views here.
def communit_list(request):
    communities = get_list_or_404(Community, category='COMMUNITY')
    return render(request, 'community_list.html', {'communities' : communities})
