from . import views
from django.urls import path


urlpatterns=[
    path('',views.home,name = 'home'),
    path('comp/',views.comp,name = 'comp'),
     path('extract-text/', views.extract_text, name='extract_text'),
]




