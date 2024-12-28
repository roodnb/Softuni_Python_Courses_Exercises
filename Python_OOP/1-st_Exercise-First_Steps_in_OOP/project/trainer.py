from .pokemon import Pokemon
from typing import List


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        for p in self.pokemons:
            if pokemon_name == p.name:
                self.pokemons.remove(p)
                return f"You have released {pokemon_name}"
        else:
            return f"Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}"
        result += f"\nPokemon count {len(self.pokemons)}"
        for element in self.pokemons:
            result += f"\n- {element.pokemon_details()}"
        return result