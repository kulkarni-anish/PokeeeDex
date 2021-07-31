from json.decoder import JSONDecodeError
from django.shortcuts import render
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
    response  = requests.get('https://pokeapi.co/api/v2/type/{}'.format(type_id))
    context   = response.json()
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

def commonsearch_view(request):
    
    return render(request,'common_search.html')


def pokemon_view(request):
    pokemon_id=request.POST['title']
    print(pokemon_id)
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon_id))
    context  = response.json()
    
    
    rendered = render(request, 'pokemon_display.html', context)
    return HttpResponse(rendered)



def common_dynamic_view(request):
    dict1={}
    dict2={}
    common_id=request.POST['title']
    print(common_id)
    response1  = requests.get('https://pokeapi.co/api/v2/type/{}'.format(common_id))
    response2 = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(common_id))
    
    if response1.ok:
        context1 = response1.json()
        data     = context1['pokemon']
        newdata=[]
        for pokemon in data:
            newdata.append(pokemon['pokemon'])
        pokemon_list=[]
        for pokemon_name in newdata:
            pokemon_list.append(pokemon_name['name'])
        dict1 = {'pokemon_list': pokemon_list}
    elif response2.ok:
        dict2  = response2.json()
    else:
        raise Http404

    common_context= dict1 | dict2 | {'common_id':common_id}
    return render(request, 'common_display.html', common_context)