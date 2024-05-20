from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Community, News

# Create your views here.
def community_list(request): 
    communities = get_list_or_404(Community, category='COMMUNITY')
    return render(request, 'community_list.html', {'communities' : communities})

def community_unique(request, id):
    community = get_object_or_404(Community, pk=id)
    print(community.id, community.name)
    return render(request, 'unique.html', {'community': community} )
