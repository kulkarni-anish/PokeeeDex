"""unicodehome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Pokedex.views import common_dynamic_view,home_view,type_view,pokemon_view,mypokemon_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view),
    path('types/',type_view, name='type'),
    path('types/<slug:type_id>/',type_view),
    path('pokemon/',pokemon_view),
    path('pokemon/<slug:id>/', pokemon_view, name='pokemon'),
    path('search/<>',common_dynamic_view, name='common_search'),
    path('mypokemon/',mypokemon_list_view),
]