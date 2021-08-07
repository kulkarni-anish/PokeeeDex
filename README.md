# Pokedex

This is a Pokedex created using Django which displays data of pokemon with their sprites using the public API https://pokeapi.co/ 

## Navigation bar

A fixed navigation bar can be used to browse through the different pages.

![image](https://user-images.githubusercontent.com/80095817/128553096-d0472d00-64cc-42a6-8925-202b018d59ab.png)

## Search Bar
You can search for a Pokemon or a type and you'll be redirected to their respective pages. An alternate sprite of the pokemon is also displayed simultaneously from a different source.
An invalid query will raise an Http404 error.

![image](https://user-images.githubusercontent.com/80095817/128554935-9618b772-6234-4646-bd3c-1918a48b71e8.png)
![image](https://user-images.githubusercontent.com/80095817/128605263-06125d51-7452-4c81-887b-4f25bbd361bd.png)
![image](https://user-images.githubusercontent.com/80095817/128558585-825d39d5-9665-46c0-9e2a-8cdff1d4c9c0.png)

## Pages
'Pokemon Types' lists all 20 types and one can click on any type to view a list of all Pokemon of that type

![image](https://user-images.githubusercontent.com/80095817/128559086-9fb6c9e0-01fc-4c7a-a6b1-1ce833585739.png)
![image](https://user-images.githubusercontent.com/80095817/128603603-e2121929-6999-4463-8897-e6bbfb21e98b.png)
![image](https://user-images.githubusercontent.com/80095817/128605175-7e1c860f-8b7f-4923-ab14-c549849b4ca6.png)

## MyPokemon Model
Any valid query of a Pokemon in the search bar not only displays its data but also adds the Pokemon as a new object in the MyPokemon model.
A repeat of any previous successful query increments the Level field of the Pokemon in the model by 1 .
All these successful queries are shown as a list of 'Pokemon Caught' on the respective page along with images of the pokemon.

![image](https://user-images.githubusercontent.com/80095817/128605535-fd7a7210-ab1d-442d-b7bf-6dda2078df8c.png)
![image](https://user-images.githubusercontent.com/80095817/128605573-0d248bc7-eced-4f00-89db-1391a6cb588e.png)
![image](https://user-images.githubusercontent.com/80095817/128605609-5a524228-0a70-4528-92b5-c64a737a9b32.png)
