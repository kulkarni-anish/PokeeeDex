from django.shortcuts import render
import requests
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from .models import MyPokemon

# Create your views here.

def home_view(request):
    
    rendered = render(request, 'home.html')
    return HttpResponse(rendered)


def type_view(request,type_id=0):
    if type_id==0:
        response = requests.get('https://pokeapi.co/api/v2/type/')
        context = response.json()
        data    = context['results']
        newdata=[]
        for pokemon_type in data:
            newdata.append(pokemon_type['name'])
        rendered = render(request, 'types.html', {'newdata': newdata})
        return HttpResponse(rendered)
        
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



def pokemon_view(request,id=0):
    if id==0:
        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=1118')
        context = response.json()
        data    = context['results']
        newdata=[]
        for pokemon_type in data:
            newdata.append(pokemon_type['name'])
            rendered = render(request, 'all_pokemon.html', {'newdata': newdata})
        return HttpResponse(rendered)

    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(id))
    context  = response.json()
    
    
    rendered = render(request, 'pokemon_display.html', context)
    return HttpResponse(rendered)


def common_dynamic_view(request):
    dict1={}
    dict2={}
    common_id=request.POST['title']
    if common_id=='':
        raise Http404
    print(common_id)
    response1  = requests.get('https://pokeapi.co/api/v2/type/{}'.format(common_id))
    response2 = requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(common_id))

    
    if response1.ok:
        context1 = response1.json()['pokemon']
        newdata=[]
        for pokemon in context1:
            newdata.append(pokemon['pokemon'])
        pokemon_list=[]
        for pokemon_name in newdata:
            pokemon_list.append(pokemon_name['name'])
        dict1 = {'pokemon_list': pokemon_list}
        
        common_context= dict1 | {'common_id':common_id}
        return render(request, 'common_display.html', common_context)

    elif response2.ok:
        dict2  = response2.json()
        types  = dict2['types']
        type_list=[]
        for items in types:
            type_list.append(items['type']['name'])

        dict2 = dict2 | {'types':','.join(type_list)}
        obj=MyPokemon.objects
        if obj.filter(name= common_id).exists():
            obj1=obj.get(name=common_id)
            obj1.level += 1
            obj1.save()
            #obj.get(name=common_id).level += 1    THIS FOR SOME REASON DOESNT WORK
            #obj.get(name=common_id).save()         
        else:
            obj.create(
                name= common_id,
                pokedex_id = dict2['id'],
                base_experience = dict2['base_experience'],
                height  = dict2['height'],
                weight  = dict2['weight'],
                type    = dict2['types'],
                sprite  = dict2['sprites']['front_default']
                )
            
        common_context= dict2 | {'common_id':common_id}
        return render(request, 'common_display.html', common_context)
            

    else:
        raise Http404



def mypokemon_list_view(request):
    queryset = MyPokemon.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request,"mypokemon_display.html",context)
    
def commonsearch_view(request):
    
    return render(request,'common_search.html')