from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Community, News

# Create your views here.
<<<<<<< HEAD
def registred_communities(request): 
=======
def community_list(request): 
>>>>>>> 773c73dd25dfdf1e3f91e2354979ca8422190c8f
    communities = get_list_or_404(Community, category='COMMUNITY')
    return render(request, 'registred_communities.html', {'communities' : communities})

def single_community(request, id):
    community = get_object_or_404(Community, pk=id)
<<<<<<< HEAD
    return render(request, 'single_community.html', {'community': community} )
=======
    print(community.id, community.name)
    return render(request, 'unique.html', {'community': community} )
>>>>>>> 773c73dd25dfdf1e3f91e2354979ca8422190c8f
