from lib2to3.fixes.fix_idioms import TYPE

from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm, TextInput, Select
from django.urls import reverse
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from place.models import Comment


class Menu(MPTTModel):

    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )

    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    link = models.CharField(max_length=100, unique=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])


class Content(models.Model):
    TYPE = (

        ('menu', 'menu'),
        ('place', 'place'),

    )
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    menu = models.OneToOneField(Menu, null=True, blank=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE)
    title = models.CharField(max_length=150)
    keywords = models.CharField(blank=True, max_length=255)
    description = models.CharField(blank=True, max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    detail = RichTextUploadingField()
    slug = models.SlugField(blank=False, unique=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('place_detail', kwargs={'slug': self.slug})

class CImages(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class ContentForm(ModelForm):
    class Meta:
        model = Content
        fields = ['type', 'title', 'slug', 'keywords', 'description', 'image', 'detail']
        widgets = {
            'title'   :TextInput(attrs={'style': 'width: 830px', 'class': 'input', 'placeholder': 'title'}),
            'slug'    : TextInput(attrs={'style': 'width: 830px', 'class': 'input', 'placeholder': 'slug'}),
            'keywords': TextInput(attrs={'style': 'width: 830px', 'class': 'input', 'placeholder': 'keywords'}),
            'description': TextInput(attrs={'style': 'width: 830px', 'class': 'input', 'placeholder': 'description'}),
            'type'    : Select(attrs={'style': 'width: 830px', 'class': 'input', 'placeholder': 'city'}, choices=TYPE),
            'detail'  : CKEditorWidget(),
        }


class ContentImageForm(ModelForm):
    class Meta:
        model = CImages
        fields = ['title', 'image']

