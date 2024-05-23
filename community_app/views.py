from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Community, News

# Create your views here.
def registred_communities(request): 
    communities = get_list_or_404(Community, category='COMMUNITY')
    return render(request, 'registred_communities.html', {'communities' : communities})

def single_community(request, id):
    community = get_object_or_404(Community, pk=id)
    return render(request, 'single_community.html', {'community': community} )
