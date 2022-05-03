# web_app/routes/pokemon_routess.py



from flask import Blueprint, jsonify, request, render_template, redirect, flash



pokemon_routes = Blueprint("pokemon_routes", __name__)

@pokemon_routes.route("/api/pokemons")
@pokemon_routes.route("/api/pokemons.json")
def list_pokemons():
    print("pokemonS...")
    pokemons = [
        {"id": 1, "title": "pokemon 1", "year": 1957},
        {"id": 2, "title": "pokemon 2", "year": 1990},
        {"id": 3, "title": "pokemon 3", "year": 2031},
    ] # some dummy / placeholder data
    return jsonify(pokemons)

#if URL params are required, we will use this kind of approach: 
@pokemon_routes.route("/api/pokemons/<int:pokemon_id>")
@pokemon_routes.route("/api/pokemons/<int:pokemon_id>.json")
def get_pokemon(pokemon_id):
    print("pokemon...", pokemon_id)
    pokemon = {"id": pokemon_id, "title": f"Example pokemon", "year": 2000} # some dummy / placeholder data
    return jsonify(pokemon)