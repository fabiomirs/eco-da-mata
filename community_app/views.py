from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Community, News
from .forms import CommunityForm


# Create your views here.
def registred_communities(request): 
    communities = get_list_or_404(Community, category='COMMUNITY')
    return render(request, 'registred_communities.html', {'communities' : communities})


def single_community(request, id):
    community = get_object_or_404(Community, pk=id)
    news = News.objects.filter(community_key=id)
    return render(request, 'single_community.html', {'community': community, 'news': news} )


def community_create(request):
    if request.method == "POST":
        form = CommunityForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect ("registred_communities")
    else:
        form = CommunityForm()
        return render(request, 'cadastros/formulario.html', {"form" : form} )    
 