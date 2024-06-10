from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Community, News
from .forms import CommunityForm, NewsForm
from core.forms import ImageForm
from core.models import Imagem
from django.forms import modelformset_factory
from .serializers import CommunitySerializer, NewsSerializer
from rest_framework import viewsets

class CommunityViewSet(viewsets.ModelViewSet):  
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# Create your views here.
def registred_communities(request): 
    communities = get_list_or_404(Community, category='COMMUNITY')
    return render(request, 'registred_communities.html', {'communities' : communities})


def single_community(request, id):
    community = get_object_or_404(Community, pk=id)
    news = News.objects.filter(community_key=id)
    images = Imagem.objects.filter(community=community)
    return render(request, 'single_community.html', {'community': community, 'news': news, 'images': images})



def community_create(request):
    ImageFormSet = modelformset_factory(Imagem, form=ImageForm, extra=5)

    if request.method == "POST":
        form = CommunityForm(request.POST, request.FILES)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Imagem.objects.none())

        if form.is_valid() and formset.is_valid():
            community = form.save()
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = Imagem(community=community, image=image)
                    photo.save()

            if community.category == 'TOURIST SPOT':
                return redirect('registred_tourist_spot')
            else:
                return redirect('registred_communities')
    else:
        form = CommunityForm()
        formset = ImageFormSet(queryset=Imagem.objects.none())

    return render(request, 'cadastros/formulario.html', {"form": form, "formset": formset})

def news_create(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save()
        return redirect(reverse('single_community', args=[news.community_key.id]))
    else:
        form = NewsForm()
        return render(request, 'cadastros/news_form.html', {"form" : form} )
 
def community_delete(request, id):
    community = get_object_or_404(Community, id=id)
    community.delete()
    # Redireciona para a lista correta
    if community.category == 'TOURIST SPOT':
        return redirect('registred_tourist_spot')
    else:
        return redirect('registred_communities')

def community_update(request, id):
    community = get_object_or_404(Community, id=id)
    if request.method == "POST":
        form = CommunityForm(request.POST, request.FILES, instance=community)
        if form.is_valid():
            form.save()
            # Redireciona para a lista correta após a atualização
            if community.category == 'TOURIST SPOT':
                return redirect('registred_tourist_spot')
            else:
                return redirect('registred_communities')
    else:
        form = CommunityForm(instance=community)
    return render(request, 'cadastros/form_att.html', {"form": form})


def news_update(request, id):
    news = get_object_or_404(News, pk=id)
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect(reverse('single_community', args=[news.community_key.id]))
    else:
        form = NewsForm(instance=news)
    return render(request, 'cadastros/news_form_att.html', {"form": form})

def news_delete(request, id):
    news = get_object_or_404(News, id=id)
    community_id = news.community_key.id
    news.delete()
    return redirect(reverse('single_community', args=[community_id]))

def news_detail(request, id):
    news = get_object_or_404(News, pk=id)
    return render(request, 'news_detail.html', {'news': news})


def registred_tourist_spot(request):
    tourist_spot = get_list_or_404(Community, category='TOURIST SPOT')
    return render(request, 'registred_communities.html', {'communities' : tourist_spot})