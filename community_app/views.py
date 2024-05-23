from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .models import Community, News
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
def registred_communities(request): 
    communities = get_list_or_404(Community, category='COMMUNITY')
    return render(request, 'registred_communities.html', {'communities' : communities})

def single_community(request, id):
    community = get_object_or_404(Community, pk=id)
    news = News.objects.filter(community_key=id)
    return render(request, 'single_community.html', {'community': community, 'news': news} )


class CommunityCreate(CreateView):
    model = Community
    fields = ["name", "link", "latitude", "longitude", "description",
              "category", "logo"]
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('comunidade/')

class NewsCreate(CreateView):
    model = News
    fields = ["title", "link", "text", "date",
              "category"]
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('comunidade/')