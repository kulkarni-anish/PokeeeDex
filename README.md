# Pokedex

This is a Pokedex which dispays data of pokemon with their sprites using the public API https://pokeapi.co/ created using Django

## Navigation bar

A navigation bar can be used to browse through the different pages.

![image](https://user-images.githubusercontent.com/80095817/128553096-d0472d00-64cc-42a6-8925-202b018d59ab.png)

## Search Bar
You can query a name of a pokemon or a type and you'll be redirected to their respective pages. An alternate sprite of the pokemon is also displayed.
An invalid query will raise an Http404 error.

![image](https://user-images.githubusercontent.com/80095817/128554935-9618b772-6234-4646-bd3c-1918a48b71e8.png)
![image](https://user-images.githubusercontent.com/80095817/128558000-4b295805-a694-4346-ac42-58e60b00af70.png)
![image](https://user-images.githubusercontent.com/80095817/128558585-825d39d5-9665-46c0-9e2a-8cdff1d4c9c0.png)

## Pages
Pokemon Types lists all 20 types and one can click on any type to view a list of all pokemon of that type

![image](https://user-images.githubusercontent.com/80095817/128559086-9fb6c9e0-01fc-4c7a-a6b1-1ce833585739.png)

## My Pokemon Model
Any valid query of a pokemon in the search bar not only displays its data but also adds the pokemon as a new object in the MyPokemon model.
A repeat of the same successful query increments the Level field in the model by 1 .
All these successful queries are shown as a list Pokemon caught on the respective page along with images of the pokemon.




