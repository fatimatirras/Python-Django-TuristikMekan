
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
import place
from content.models import Menu, Content, ContentForm, ContentImageForm, CImages, UserPlacesForm, UserPlaces
from home.models import UserProfile, Setting
from place.models import Category, Comment, Place, PlaceForm, Images
from user.forms import UserUpdateForm, ProfileUpdateForm



def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category,
               'profile': profile
               }
    return render(request, 'user_profile.html', context)

def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'ok')
            return redirect('/user')

    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form,

        }
        return render(request, 'user_update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'şifreniz başarı bir şekilde kaydedilmiştir')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'ERROR<br>' + str(form.errors))
            return HttpResponseRedirect('/user/password')

    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {
            'form': form,
            'category': category,

        })



@login_required(login_url='/login')
def comments(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user)
    context = {
        'category': category,
        'comments': comments,
        'setting': setting,
    }
    return render(request, 'user_comments.html', context)


@login_required(login_url='/login')
def deletecomment(request, id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'comment deleted')
    return HttpResponseRedirect('/user/comments')


@login_required(login_url='/login')
def contents(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    current_user = request.user
    place = Place.objects.filter(user_id=current_user.id)
    context = {
        'category': category,
        'setting': setting,
        'place': place,

    }
    return render(request, 'user_contents.html', context)



@login_required(login_url='/login')
def addcontent(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Place()
            data.category = form.cleaned_data['category']
            data.user_id = current_user.id
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            data.city = form.cleaned_data['image']
            data.country = form.cleaned_data['image']
            data.location = form.cleaned_data['image']
            data.slug = form.cleaned_data['slug']
            data.detail = form.cleaned_data['detail']
            data.status = 'False'
            data.save()
            messages.success(request, 'Başarılı bir şekilde eklenmiştir')
            return HttpResponseRedirect('/user/contents')
        else:
            messages.error(request, 'Content Form Error: ' + str(form.errors))
            return HttpResponseRedirect('/user/addcontent')
    else:
        category = Category.objects.all()
        setting = Setting.objects.all()
        form = PlaceForm()
        context = {
            'setting': setting,
            'category': category,
            'form': form,
        }
        return render(request, 'user_addcontent.html', context)

@login_required(login_url='/login')
def contentedit(request, id):
    place = Place.objects.get(id=id)
    setting = Setting.objects.get(pk=1)
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            form.save()
            messages.success(request, 'Başarılı bir şekilde değiştirilmiştir')
            return HttpResponseRedirect('/user/contents')
        else:
            messages.error(request, 'Content Form Error: ' + str(form.errors))
            return HttpResponseRedirect('/user/contentedit/' + str(id))
    else:
        category = Category.objects.all()
        form = PlaceForm(instance=place)
        context = {
            'setting': setting,
            'category': category,
            'form': form,
        }
        return render(request, 'user_addcontent.html', context)



def contentdelete(request, id):
    current_user = request.user
    Place.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Content deleted.')
    return HttpResponseRedirect('/user/contents')


@login_required(login_url='/login')
def ccomments(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user)
    context = {
        'menu': menu,
        'category': category,
        'comments': comments,

    }
    return render(request, 'user_comments.html', context)


@login_required(login_url='/login')
def cdeletecomment(request, id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'comment deleted')
    return HttpResponseRedirect('/user/comments')

def contentaddimge(request,id):
    if request.method == 'POST':
        lasturl = request.META.get('HTTP_REFERER')
        form = ContentImageForm(request.POST, request.FILES)
        if form.is_valid():
            data = Images()
            data.place_id = id
            data.title = form.cleaned_data['title']
            data.image = form.cleaned_data['image']
            data.save()
            messages.success(request, 'your image has been successfully uploaded')
            return HttpResponseRedirect(lasturl)
        else:
            messages.warning(request, 'Form Error: ' + str(form.errors))
            return HttpResponseRedirect(lasturl)
    else:
        place = Place.objects.get(id=id)
        images = Images.objects.filter(place_id=id)
        form = ContentImageForm()
        context = {
            'place': place,
            'images': images,
            'form': form,
        }
        return render(request, 'content_gallery.html', context)


def contentimagedelete(request,id):
    place = Place.objects.filter(id=id)
    lasturl = request.META.get('HTTP_REFERER')
    Images.objects.filter(id=id, place_id=id).delete()
    messages.success(request,'Image Deleted')
    return HttpResponseRedirect(lasturl)











