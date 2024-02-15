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


def roll_three_dice(input_str=""):

    if input_str == "":        
        # Roll three six-sided dice
        dice_results = [random.randint(1, 6) for _ in range(3)]

    else:
        # Convert the input string to a list of integers
        dice_results = [int(num) for num in input_str]
    
    # Organize the results from lowest to highest
    sorted_results = sorted(dice_results)
    
    # Create a dictionary with keys "B", "I", "A"
    result_dict = {"B": sorted_results[0], "I": sorted_results[1], "A": sorted_results[2]}
    
    return result_dict


def random_pokemon():
    
    mon=input("What is the pokemon? >>>")
    lvl=input("What level is the pokemon? >>>")
    naturaleza=input("What is the nature of the pokemon? >>>")
    poke = Pokemon(mon, lvl, naturaleza)
    if lvl != "self":
        poke.level_up()
    return poke


def calculo_daño_pokemon(mon_attacking, mon_defending, move, dados):

    file_path = 'movimientos pokemon.csv'  # Replace with the actual path to the CSV file
    movimientos_result_dict = read_csv_to_dict(file_path)

    dados_dict = roll_three_dice(dados)
    damage_string = movimientos_result_dict[move.lower()]['Damage']

    if damage_string == "-":
        return 0
    if damage_string == "Variable":
        return 0
        
    # Initialize the total damage
    total_damage = 0    

    # Process the damage_string
    components = damage_string.split('+')
    for component in components:
        if component.isdigit():
            total_damage += int(component)
        else:
            for letter in ["B", "I", "A"]:
                if letter in component:
                    total_damage += dados_dict[letter]
            if component[0].isdigit():
                total_damage *= int(component[0])

    # Determine STAB
    tipo_movimiento = movimientos_result_dict[move.lower()]['Tipo'].strip()
    if tipo_movimiento == mon_attacking.type1 or tipo_movimiento == mon_attacking.type2:
        total_damage += 1 + mon_attacking.level // 10

    # Determine critical hit        
    # Get the first value in dados_dict
    first_value = next(iter(dados_dict.values()), None)
    # Check if all values are equal to the first value
    if all(value == first_value for value in dados_dict.values()):
        total_damage *= 2

    # Multiply damage according to the effectiveness
    total_damage *= tipos_pokemon.get(tipo_movimiento).get(mon_defending.type1)
    if mon_defending.type2:
        total_damage *= tipos_pokemon.get(tipo_movimiento).get(mon_defending.type2)

    # add attacker stats and substract defender stats
    clase_movimiento = movimientos_result_dict[move.lower()]['Movimiento'].strip()
    if clase_movimiento == "Fisico":
        total_damage += mon_attacking.attack // 10
        total_damage -= mon_defending.defense // 10
    elif clase_movimiento == "Especial":
        total_damage += mon_attacking.special_attack // 10
        total_damage -= mon_defending.special_defense // 10

    return total_damage


def daño_pokemon():
    
    print("***ATTACKING POKEMON***")
    mon_attacking = random_pokemon()

    print("***DEFENDING POKEMON***")
    mon_defending = random_pokemon()

    move = input(f"What movement is {mon_attacking.name} using? >>>")
    dados = input("Toss 3d6 and type the results >>>")
    damage = calculo_daño_pokemon(mon_attacking, mon_defending, move, dados)

    return f"{mon_attacking.name} hits {mon_defending.name} using {move} for {damage} points of damage"


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
    'Acero': {'Acero': 0.5, 'Agua': 0.5, 'Bicho': 1.0, 'Dragon': 1.0, 'Electrico': 0.5, 'Fantasma': 1.0, 'Fuego': 0.5, 'Hada': 2.0, 'Hielo': 2.0, 'Lucha': 1.0, 'Normal': 1.0, 'Planta': 1.0, 'Psiquico': 1.0, 'Roca': 2.0, 'Siniestro': 1.0, 'Tierra': 1.0, 'Veneno': 1.0, 'Volador': 1.0}, 
    'Agua': {'Acero': 1.0, 'Agua': 0.5, 'Bicho': 1.0, 'Dragon': 0.5, 'Electrico': 1.0, 'Fantasma': 1.0, 'Fuego': 2.0, 'Hada': 1.0, 'Hielo': 1.0, 'Lucha': 1.0, 'Normal': 1.0, 'Planta': 0.5, 'Psiquico': 1.0, 'Roca': 2.0, 'Siniestro': 1.0, 'Tierra': 2.0, 'Veneno': 1.0, 'Volador': 1.0}, 
    'Bicho': {'Acero': 0.5, 'Agua': 1.0, 'Bicho': 1.0, 'Dragon': 1.0, 'Electrico': 1.0, 'Fantasma': 0.5, 'Fuego': 0.5, 'Hada': 0.5, 'Hielo': 1.0, 'Lucha': 0.5, 'Normal': 1.0, 'Planta': 2.0, 'Psiquico': 2.0, 'Roca': 1.0, 'Siniestro': 2.0, 'Tierra': 1.0, 'Veneno': 0.5, 'Volador': 0.5}, 
    'Dragon': {'Acero': 0.5, 'Agua': 1.0, 'Bicho': 1.0, 'Dragon': 2.0, 'Electrico': 1.0, 'Fantasma': 1.0, 'Fuego': 1.0, 'Hada': 0.0, 'Hielo': 1.0, 'Lucha': 1.0, 'Normal': 1.0, 'Planta': 1.0, 'Psiquico': 1.0, 'Roca': 1.0, 'Siniestro': 1.0, 'Tierra': 1.0, 'Veneno': 1.0, 'Volador': 1.0}, 
    'Electrico': {'Acero': 1.0, 'Agua': 2.0, 'Bicho': 1.0, 'Dragon': 0.5, 'Electrico': 0.5, 'Fantasma': 1.0, 'Fuego': 1.0, 'Hada': 1.0, 'Hielo': 1.0, 'Lucha': 1.0, 'Normal': 1.0, 'Planta': 0.5, 'Psiquico': 1.0, 'Roca': 1.0, 'Siniestro': 1.0, 'Tierra': 0.0, 'Veneno': 1.0, 'Volador': 2.0}, 
    'Fantasma': {'Acero': 1.0, 'Agua': 1.0, 'Bicho': 1.0, 'Dragon': 1.0, 'Electrico': 1.0, 'Fantasma': 2.0, 'Fuego': 1.0, 'Hada': 1.0, 'Hielo': 1.0, 'Lucha': 1.0, 'Normal': 0.0, 'Planta': 1.0, 'Psiquico': 2.0, 'Roca': 1.0, 'Siniestro': 0.5, 'Tierra': 1.0, 'Veneno': 1.0, 'Volador': 1.0}, 
    'Fuego': {'Acero': 2.0, 'Agua': 0.5, 'Bicho': 2.0, 'Dragon': 0.5, 'Electrico': 1.0, 'Fantasma': 1.0, 'Fuego': 0.5, 'Hada': 1.0, 'Hielo': 2.0, 'Lucha': 1.0, 'Normal': 1.0, 'Planta': 2.0, 'Psiquico': 1.0, 'Roca': 0.5, 'Siniestro': 1.0, 'Tierra': 1.0, 'Veneno': 1.0, 'Volador': 1.0}, 
    'Hada': {'Acero': 0.5, 'Agua': 1.0, 'Bicho': 1.0, 'Dragon': 2.0, 'Electrico': 1.0, 'Fantasma': 1.0, 'Fuego': 0.5, 'Hada': 1.0, 'Hielo': 1.0, 'Lucha': 2.0, 'Normal': 1.0, 'Planta': 1.0, 'Psiquico': 1.0, 'Roca': 1.0, 'Siniestro': 2.0, 'Tierra': 1.0, 'Veneno': 0.5, 'Volador': 1.0}, 
    'Hielo': {'Acero': 0.5, 'Agua': 0.5, 'Bicho': 1.0, 'Dragon': 2.0, 'Electrico': 1.0, 'Fantasma': 1.0, 'Fuego': 0.5, 'Hada': 1.0, 'Hielo': 0.5, 'Lucha': 1.0, 'Normal': 1.0, 'Planta': 2.0, 'Psiquico': 1.0, 'Roca': 1.0, 'Siniestro': 1.0, 'Tierra': 2.0, 'Veneno': 1.0, 'Volador': 2.0}, 
    'Lucha': {'Acero': 2.0, 'Agua': 1.0, 'Bicho': 0.5, 'Dragon': 1.0, 'Electrico': 1.0, 'Fantasma': 0.0, 'Fuego': 1.0, 'Hada': 0.5, 'Hielo': 2.0, 'Lucha': 1.0, 'Normal': 2.0, 'Planta': 1.0, 'Psiquico': 0.5, 'Roca': 2.0, 'Siniestro': 2.0, 'Tierra': 1.0, 'Veneno': 0.5, 'Volador': 0.5}, 
    'Normal': {'Acero': 0.5, 'Agua': 1.0, 'Bicho': 1.0, 'Dragon': 1.0, 'Electrico': 1.0, 'Fantasma': 0.0, 'Fuego': 1.0, 'Hada': 1.0, 'Hielo': 1.0, 'Lucha': 1.0, 'Normal': 1.0, 'Planta': 1.0, 'Psiquico': 1.0, 'Roca': 0.5, 'Siniestro': 1.0, 'Tierra': 1.0, 'Veneno': 1.0, 'Volador': 1.0}, 
    'Planta': {'Acero': 0.5, 'Agua': 2.0, 'Bicho': 0.5, 'Dragon': 0.5, 'Electrico': 1.0, 'Fantasma': 1.0, 'Fuego': 0.5, 'Hada': 1.0, 'Hielo': 1.0, 'Lucha': 1.0, 'Normal': 1.0, 'Planta': 0.5, 'Psiquico': 1.0, 'Roca': 2.0, 'Siniestro': 1.0, 'Tierra': 2.0, 'Veneno': 0.5, 'Volador': 0.5}, 
    'Psiquico': {'Acero': 0.5, 'Agua': 1.0, 'Bicho': 1.0, 'Dragon': 1.0, 'Electrico': 1.0, 'Fantasma': 1.0, 'Fuego': 1.0, 'Hada': 1.0, 'Hielo': 1.0, 'Lucha': 2.0, 'Normal': 1.0, 'Planta': 1.0, 'Psiquico': 0.5, 'Roca': 1.0, 'Siniestro': 0.0, 'Tierra': 1.0, 'Veneno': 2.0, 'Volador': 1.0}, 
    'Roca': {'Acero': 0.5, 'Agua': 1.0, 'Bicho': 2.0, 'Dragon': 1.0, 'Electrico': 1.0, 'Fantasma': 1.0, 'Fuego': 2.0, 'Hada': 1.0, 'Hielo': 2.0, 'Lucha': 0.5, 'Normal': 1.0, 'Planta': 1.0, 'Psiquico': 1.0, 'Roca': 1.0, 'Siniestro': 1.0, 'Tierra': 0.5, 'Veneno': 1.0, 'Volador': 2.0},
    'Siniestro': {'Acero': 1.0, 'Agua': 1.0, 'Bicho': 1.0, 'Dragon': 1.0, 'Electrico': 1.0, 'Fantasma': 2.0, 'Fuego': 1.0, 'Hada': 0.5, 'Hielo': 1.0, 'Lucha': 0.5, 'Normal': 1.0, 'Planta': 1.0, 'Psiquico': 2.0, 'Roca': 1.0, 'Siniestro': 0.5, 'Tierra': 1.0, 'Veneno': 1.0, 'Volador': 1.0}, 
    'Tierra': {'Acero': 2.0, 'Agua': 1.0, 'Bicho': 0.5, 'Dragon': 1.0, 'Electrico': 2.0, 'Fantasma': 1.0, 'Fuego': 2.0, 'Hada': 1.0, 'Hielo': 1.0, 'Lucha': 1.0, 'Normal': 1.0, 'Planta': 0.5, 'Psiquico': 1.0, 'Roca': 2.0, 'Siniestro': 1.0, 'Tierra': 1.0, 'Veneno': 2.0, 'Volador': 0.0}, 
    'Veneno': {'Acero': 0.0, 'Agua': 1.0, 'Bicho': 1.0, 'Dragon': 1.0, 'Electrico': 1.0, 'Fantasma': 0.5, 'Fuego': 1.0, 'Hada': 2.0, 'Hielo': 1.0, 'Lucha': 1.0, 'Normal': 1.0, 'Planta': 2.0, 'Psiquico': 1.0, 'Roca': 0.5, 'Siniestro': 1.0, 'Tierra': 0.5, 'Veneno': 0.5, 'Volador': 1.0}, 
    'Volador': {'Acero': 0.5, 'Agua': 1.0, 'Bicho': 2.0, 'Dragon': 1.0, 'Electrico': 0.5, 'Fantasma': 1.0, 'Fuego': 1.0, 'Hada': 1.0, 'Hielo': 1.0, 'Lucha': 2.0, 'Normal': 1.0, 'Planta': 2.0, 'Psiquico': 1.0, 'Roca': 0.5, 'Siniestro': 1.0, 'Tierra': 1.0, 'Veneno': 1.0, 'Volador': 1.0}
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
    def __init__(self, name="", level="", nature=""):
        
        file_path = 'pokemon.csv'  # Replace with the actual path to the CSV file
        pokemon_result_dict = read_csv_to_dict(file_path)

        if name == "":
            # Choose a random pokemon if there is none
            self.name = random.choice(list(pokemon_result_dict.keys()))
        else:
            self.name = pokemon_result_dict[name.lower()]['Pokemon']

        if level == "":
            # Choose a random number between 5 and 100 if there is no level
            self.level = random.randint(5, 100)
        elif level == "self":
            # Set the level as the one registered in the csv file
            self.level = int(pokemon_result_dict[name.lower()]['Nivel'])
        else:
            self.level = int(level) 

        if nature == "":
            # Choose a random nature if there is none
            self.nature = random.choice(list(natures.keys()))
        elif level == "self":
            # Set the nature as the one registered in the csv file
            self.nature = pokemon_result_dict[name.lower()]['Naturaleza']
        else:
            self.nature = nature.capitalize()
        
        # Set the main statistics according to the nature of the pokemon
        self.attack = int(pokemon_result_dict[self.name]['Ataque']) 
        self.special_attack = int(pokemon_result_dict[self.name]['At. Esp'])
        self.defense = int(pokemon_result_dict[self.name]['Defensa'])
        self.special_defense = int(pokemon_result_dict[self.name]['Def. Esp'])
        self.speed = int(pokemon_result_dict[self.name]['Velocidad'])
        self.health_points = int(pokemon_result_dict[self.name]['Pts. Salud'])
        self.power_points = int(pokemon_result_dict[self.name]['Pts. Poder'])
        self.health_upgrade = pokemon_result_dict[self.name]['Mejora de Salud']
        self.power_upgrade = pokemon_result_dict[self.name]['Mejora de Poder']
        self.type1 = pokemon_result_dict[self.name]['Tipo 1']
        self.type2 = pokemon_result_dict[self.name]['Tipo 2']

        if level != "self":
            self.attack += stats_from_nature(self.nature, "Ataque")
            self.special_attack += stats_from_nature(self.nature, "At. Especial")
            self.defense += stats_from_nature(self.nature, "Defensa")
            self.special_defense += stats_from_nature(self.nature, "Def. Especial")
            self.speed += stats_from_nature(self.nature, "Velocidad")


    def __str__(self):
        return  f'''
This level {self.level} {self.name} is a {self.type1}/{self.type2} type Pokemon with a nature of {self.nature} {natures.get(self.nature)}.  Its statistics are as follows: 
Attack {self.attack}.  Special attack {self.special_attack}.  Defence {self.defense}.  Special defense {self.special_defense}. and Speed {self.speed}  (After nature bonuses).  
Health points {self.health_points}.  Power points {self.power_points}.
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
    
    user = int(input("Type 1 to create a random pokemon or 2 to acces the damage calculator>>>"))
    if user == 1:
        pokemon = random_pokemon()
        print(pokemon)
    elif user == 2:
        print(daño_pokemon())
    
    
    




