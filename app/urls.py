from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('about', about, name='about'),
    path('editing', editing, name='editing'),
    path('publishing', publishing, name='publishing'),
    path('design', design, name='design'),
    path('marketing', marketing, name='marketing'),
    path('blog', blog, name='blog'),
    path('contact', contact, name='contact'),
]