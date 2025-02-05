import pokemon_class as po, random as ran, list_pokemon as lp

players = []

class PLAYER:
    def __init__(self):
        self.name = ""
        self.pokemons = []
        self.items = []
        self.turn = True

    def choosing_pokemon(self, pokemon):
        if len(self.pokemons) < 1:
            pokemon = po.Pokemon(lp.list_of_pokemon[ran.randint(0, 150)])
            pokemon.chosen = True
            self.pokemons.append(pokemon)
        elif len(self.pokemons) >= 1:
            if pokemon not in self.pokemons:
                newpok = po.Pokemon(pokemon)
                self.pokemons.append(newpok)
            else:
                self.choosing_pokemon(lp.list_of_pokemon[ran.randint(0, 150)])
                # pokemon = lp.list_of_pokemon[ran.randint(0, 151)]
                # self.pokemons.append(pokemon)

    def active_pokemon(self) :
        active_pokemon = self.pokemons[0]
        for i in self.pokemons:
            if i.chosen and i.status != 12:
                active_pokemon = i
            elif i.chosen and i.status == 12:
                i.chosen = False
                try:
                    active_pokemon = self.pokemons[self.pokemons.index(i) + 1]
                except:
                    for i in self.pokemons :
                        if i.status != 12:
                            active_pokemon = self.pokemons[self.pokemons.index(i) + 1]
                            i.chosen = True
                else:
                    active_pokemon = self.pokemons[self.pokemons.index(i) + 1]
                    self.pokemons[self.pokemons.index(i) + 1].chosen = True
        return active_pokemon

