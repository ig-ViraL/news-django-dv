from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('sports',views.sports,name='sports'),
    path('entertaimnet',views.entertainment,name='entertainment'),
    path('national',views.national,name='national'),
    path('automobile',views.automobile,name='automobile'),
    path('business',views.business,name='business'),
    path('miscellaneous',views.miscellaneous,name='miscellaneous'),
    path('politics',views.politics,name='politics'),
    path('science',views.science,name='science'),
    path('startup',views.startup,name='startup'),
    path('technology',views.technology,name='technology'),
    path('world',views.world,name='world'),
]
