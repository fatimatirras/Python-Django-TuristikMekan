from ckeditor_uploader.forms import SearchForm
from django.contrib import messages
import json

from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormMessage, ContactFormu
from place.models import Place, Category, Images, Comment


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Place.objects.all()[:4]
    category = Category.objects.all()
    popularplaces = Place.objects.all()[:4]
    lastplaces = Place.objects.all().order_by('-id')[:10]
    randomplaces = Place.objects.all().order_by('?')[:12]



    context = {'setting': setting, 'category': category, 'page': 'home', 'sliderdata':sliderdata,
               'popularplaces': popularplaces,
               'lastplaces': lastplaces,
               'randomplaces': randomplaces, }
    return render(request, 'index.html', context)


def contact(request):

    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "mesajınız alındı")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    category = Category.objects.all()
    context = {'setting': setting, 'form': form, 'category': category}
    return render(request, 'contact.html', context)


def aboutus(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'page': 'aboutus', 'category': category}
    return render(request, 'aboutus.html', context)


def references(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'page': 'references', 'category': category}
    return render(request, 'references.html', context)

def category_places(request, id, slug):
    setting = Setting.objects.get(pk=1)
    categorydata = Category.objects.get(pk=id)
    places = Place.objects.filter(category_id=id, status='True')
    category = Category.objects.all()
    context = {'setting': setting, 'places': places, 'category': category, 'categorydata': categorydata, }
    return render(request, 'places.html', context)

def place_detail(request, id, slug):
    category = Category.objects.all()
    place = Place.objects.get(pk=id)
    images = Images.objects.filter(place_id=id)
    comments = Comment.objects.filter(place_id=id, status='True')
    context = {'category': category, 'place': place, 'images': images, 'comments': comments, }
    return render(request, 'place_detail.html', context)



def place_search(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            if catid == 0:
                places = Place.objects.filter(title__icontains=query)
            else:

                places = Place.objects.filter(title__icontains=query, category_id=catid)

            context = {'places': places,
                       'category': category,
                       }
            return render(request, 'place_search.html', context)
    return HttpResponseRedirect('/')

def place_search_auto(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    places = Place.objects.filter(city__icontains=q)
    results = []
    for rs in places:
      place_json = {}
      place_json = rs.title
      results.append(place_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "lütfen bilgilerinizi kontrol ediniz")
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    context = {'category': category, }
    return render(request, 'login.html', context)