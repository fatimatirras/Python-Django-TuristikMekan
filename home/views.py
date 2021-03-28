from django.core.checks import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from home.models import Setting, ContactFormMessage, ContactFormu
from place.models import Place, Category


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Place.objects.all()[:4]
    category = Category.objects.all()


    context = {'setting': setting, 'category': category, 'page': 'home', 'sliderdata':sliderdata}
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
         #   messages.success(request, "mesajınız alındı")
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
