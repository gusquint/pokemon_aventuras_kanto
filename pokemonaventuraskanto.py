import csv
import random


def read_csv_to_dict(file_path):
    data_dict = {}
    
    with open(file_path, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter = ";")
        
        for row in csvreader:
            # Assuming the first column is the key
            key = row[csvreader.fieldnames[0]]
            data_dict[key] = row
    
    return data_dict


def roll_three_dice():
    # Roll three six-sided dice
    dice_results = [random.randint(1, 6) for _ in range(3)]
    
    # Organize the results from lowest to highest
    sorted_results = sorted(dice_results)
    
    # Create a dictionary with keys "B", "I", "A"
    result_dict = {"B": sorted_results[0], "I": sorted_results[1], "A": sorted_results[2]}
    
    return result_dict


natures={"Fuerte":("Neutra"),
        "Osada":("+Defensa","-Ataque"),
        "Modesta":("+At. Especial","-Ataque"),
        "Serena":("+Def. Especial","-Ataque"),
        "Miedosa":("+Velocidad","-Ataque"),
        "Huraña":("+Ataque","-Defensa"),
        "Docil":("Neutra"),
        "Afable":("+At. Especial","-Defensa"),
        "Amable":("+Def. Especial","-Defensa"),
        "Activa":("+Velocidad","-Defensa"),
        "Firme":("+Ataque","-At. Especial"),
        "Agitada":("+Defensa","-At. Especial"),
        "Timida":("Neutra"),
        "Cauta":("+Def. Especial","-At. Especial"),
        "Alegre":("+Velocidad","-At. Especial"),
        "Picara":("+Ataque","-Def. Especial"),
        "Floja":("+Defensa","-Def. Especial"),
        "Alocada":("+At. Especial","-Def. Especial"),
        "Rara":("Neutra"),
        "Ingenua":("+Velocidad","-Def. Especial"),
        "Audaz":("+Ataque","-Velocidad"),
        "Placida":("+Defensa","-Velocidad"),
        "Mansa":("+At. Especial","-Velocidad"),
        "Grosera":("+Def. Especial","-Velocidad"),
        "Seria":("Neutra")}


tipos_pokemon = {
    "Acero": {"Acero": 0.5, "Agua": 0.5, "Electrico": 0.5, "Fuego": 0.5, "Hada": 2.0, "Hielo": 2.0, "Roca": 2.0},
    "Agua": {"Agua": 0.5, "Dragon": 0.5, "Electrico": 0.5, "Fuego": 2.0, "Planta": 0.5, "Roca": 2.0, "Tierra": 0.5},
    "Bicho": {"Acero": 0.5, "Fantasma": 0.5, "Lucha": 0.5, "Planta": 0.5, "Psiquico": 0.5, "Siniestro": 2.0, "Tierra": 0.5},
    "Dragon": {"Agua": 0.5, "Dragon": 2.0, "Electrico": 0.5, "Fuego": 0.5, "Planta": 0.5},
    "Electrico": {"Electrico": 0.5, "Normal": 0.5, "Tierra": 0.0, "Volador": 0.5},
    "Fantasma": {"Bicho": 0.5, "Fantasma": 0.5, "Siniestro": 2.0, "Veneno": 0.5},
    "Fuego": {"Bicho": 2.0, "Fuego": 0.5, "Hielo": 0.5, "Planta": 0.5, "Roca": 0.5, "Agua": 0.5},
    "Hada": {"Acero": 2.0, "Bicho": 0.5, "Dragon": 0.0, "Hada": 0.5, "Lucha": 0.5, "Siniestro": 0.5},
    "Hielo": {"Fuego": 0.5, "Hielo": 0.5, "Planta": 2.0, "Tierra": 2.0},
    "Lucha": {"Acero": 2.0, "Bicho": 0.5, "Lucha": 0.5, "Normal": 2.0, "Roca": 0.5, "Siniestro": 0.5},
    "Normal": {"Fantasma": 0.5, "Normal": 0.5},
    "Planta": {"Agua": 2.0, "Electrico": 0.5, "Fuego": 0.5, "Planta": 0.5, "Roca": 2.0, "Tierra": 0.5},
    "Psiquico": {"Bicho": 2.0, "Lucha": 0.5, "Psiquico": 0.5, "Siniestro": 2.0},
    "Roca": {"Fuego": 0.5, "Normal": 0.5, "Planta": 2.0, "Roca": 0.5, "Veneno": 0.5, "Volador": 0.5},
    "Siniestro": {"Fantasma": 2.0, "Psiquico": 0.0, "Siniestro": 0.5},
    "Tierra": {"Agua": 2.0, "Electrico": 0.0, "Hielo": 2.0, "Planta": 0.5, "Roca": 0.5, "Veneno": 0.5},
    "Veneno": {"Bicho": 0.5, "Planta": 0.5, "Psiquico": 2.0, "Veneno": 0.5, "Tierra": 0.5},
    "Volador": {"Bicho": 0.5, "Lucha": 0.5, "Planta": 0.5, "Tierra": 0.0, "Volador": 0.5},
}


def stats_from_nature(nature, stat):
    changes = natures.get(nature)    
    if len(changes) == 2:
        positive_change, negative_change = changes
        if stat == positive_change[1:]:
            return 35
        elif stat == negative_change[1:]:
            return 15
        else:
            return 25
    else:
        return 25
    

class Pokemon:
    def __init__(self, name, level, nature=""):
        self.name = pokemon_result_dict[name.lower()]['Pokemon']
        self.level = int(level) 

        if nature == "":
            # Choose a random nature if there is none
            self.nature = random.choice(list(natures.keys()))
        else:
            self.nature = nature.capitalize()
        
        # Set the main statistics according to the nature of the pokemon
        self.attack = int(pokemon_result_dict[self.name]['Ataque']) + stats_from_nature(self.nature, "Ataque")
        self.special_attack = int(pokemon_result_dict[self.name]['At. Esp']) + stats_from_nature(self.nature, "At. Especial")
        self.defense = int(pokemon_result_dict[self.name]['Defensa']) + stats_from_nature(self.nature, "Defensa")
        self.special_defense = int(pokemon_result_dict[self.name]['Def. Esp']) + stats_from_nature(self.nature, "Def. Especial")
        self.speed = int(pokemon_result_dict[self.name]['Velocidad']) + stats_from_nature(self.nature, "Velocidad")
        self.health_points = int(pokemon_result_dict[self.name]['Pts. Salud'])
        self.power_points = int(pokemon_result_dict[self.name]['Pts. Poder'])
        self.health_upgrade = pokemon_result_dict[self.name]['Mejora de Salud']
        self.power_upgrade = pokemon_result_dict[self.name]['Mejora de Poder']
        self.type1 = pokemon_result_dict[self.name]['Tipo 1']
        self.type2 = pokemon_result_dict[self.name]['Tipo 2']

    def __str__(self):
        return  f'''
This level {poke.level} {poke.name} is a {poke.type1}/{poke.type2} type Pokemon with a nature of {self.nature} {natures.get(self.nature)}.  Its statistics are as follows: 
Attack {poke.attack}.  Special attack {poke.special_attack}.  Defence {poke.defense}.  Special defense {poke.special_defense}. and Speed {poke.speed}  (After nature bonuses).  
Health points {poke.health_points}.  Power points {poke.power_points}.
'''

    def level_up(self):
        for _ in range(self.level - 5):
            results=roll_three_dice()

            if self.health_upgrade[0].isdigit():
                # If the first character is a number, multiply it by the value of the letter
                self.health_points += int(self.health_upgrade[0]) * results.get(self.health_upgrade[1])
            else:
                # If both characters are letters, add their values
                self.health_points += results.get(self.health_upgrade[0]) + results.get(self.health_upgrade[1])
            
            # Then increase the power points value
            self.power_points += results.get(self.power_upgrade)

            # Then increase the main statistics according to the nature of the pokemon
            self.attack += int(stats_from_nature(self.nature, "Ataque")/5)
            self.special_attack += int(stats_from_nature(self.nature, "At. Especial")/5)
            self.defense += int(stats_from_nature(self.nature, "Defensa")/5)
            self.special_defense += int(stats_from_nature(self.nature, "Def. Especial")/5)
            self.speed  += int(stats_from_nature(self.nature, "Velocidad")/5)


if __name__ == "__main__":
    file_path = 'pokemon.csv'  # Replace with the actual path to the CSV file
    pokemon_result_dict = read_csv_to_dict(file_path)
    mon=input("What is the pokemon? >>>")
    lvl=input("What level is the pokemon? >>>")
    naturaleza=input("What is the nature of the pokemon? >>>")

    poke = Pokemon(mon, lvl, naturaleza)
    poke.level_up()

    print(poke)




