from django.shortcuts import render, get_object_or_404
import requests
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
#from django.template.loader import render_to_string

# Create your views here.

def home_view(request):
    response = requests.get('https://pokeapi.co/api/v2/type/')
    context = response.json()
    data    = context['results']
    newdata=[]
    for pokemon_type in data:
        newdata.append(pokemon_type['name'])

    #rendered = render_to_string('home.html', {'data':data})
    #return HttpResponse(rendered)
    rendered = render(request, 'home.html', {'newdata': newdata})
    return HttpResponse(rendered)


def dynamic_view(request):
    type_id=request.POST['title']
    print(type_id)
    context  = requests.get('https://pokeapi.co/api/v2/type/{}'.format(type_id)).json()
    data     = context['pokemon']

    newdata=[]
    for pokemon in data:
        newdata.append(pokemon['pokemon'])
    pokemon_list=[]
    for pokemon_name in newdata:
        pokemon_list.append(pokemon_name['name'])
    
    rendered = render(request, 'listofpokemon.html', {'pokemon_list': pokemon_list, 'type_id':type_id})
    return HttpResponse(rendered)

def type_view(request):
    response = requests.get('https://pokeapi.co/api/v2/type/')
    context = response.json()
    data    = context['results']
    newdata=[]
    for pokemon_type in data:
        newdata.append(pokemon_type['name'])

    #rendered = render_to_string('home.html', {'data':data})
    #return HttpResponse(rendered)
    rendered = render(request, 'types.html', {'newdata': newdata})
    return HttpResponse(rendered)

def search_view(request):
    
    return render(request,'search.html')

#def dynamic_view(request):
    type_id=request.POST['title']
    print(type_id)
    response = requests.get('https://pokeapi.co/api/v2/type/{}'.format(type_id))
    context  = response.json()
    data     = context['pokemon']
    
    newdata=[]
    for pokemon in data:
        newdata.append(pokemon['pokemon'])
    pokemon_list=[]
    for pokemon_name in newdata:
        pokemon_list.append(pokemon_name['name'])
    
    rendered = render(request, 'listofpokemon.html', {'pokemon_list': pokemon_list})
    return HttpResponse(rendered)