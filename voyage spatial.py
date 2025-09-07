import random

masse_astronautes = 80
module_spatiale = 500

def astronaute(masse,nb_astronautes):
    masse_total_astronautes = nb_astronautes * masse
    return masse_total_astronautes,nb_astronautes

def module(masse,nb_module):
    masse_total_module = nb_module * masse
    return masse_total_module

def carburant_avant(masse):
    carburant = masse * 2
    return carburant

def masse_finale(masse1, masse2):
    masse_fin =  masse1 + masse2
    return masse_fin

def vip(carburant:int):

    vip_status = input("etes vous VIP? (o/n)")
    if vip_status == "o":
        nouveau_carburant = carburant + 50
        return nouveau_carburant

    else:
        print("vous etes pas eligible")
        return carburant

def tempete_solaire(tempete):
    nombre = random.randint(1,2)
    if nombre == 1:
        tempete = "interdit (tempete solaire)"
    elif nombre == 2:
        tempete = "autorise"
    return tempete




if __name__ == "__main__":
    nom_mission = input("quel est le nom de la mission?: ").upper()
    nombre_astronautes = int(input("Combien d'astronautes y-a-t-il?: "))
    nombre_module = int(input("Combien de modules y-a-t-il?: "))
    masse_final_astronautes = astronaute(masse_astronautes, nombre_astronautes)
    masse_final_module = module(module_spatiale,nombre_module)

    masse_total = masse_finale(masse_final_astronautes, masse_final_module)

    carburant_initial = carburant_avant(masse_total)
    carburant_final = vip(carburant_initial)
    tempete = ""
    tempete_solaire(tempete)
    mission = "Non-realisable (carburant insufisant)"

    if carburant_final == masse_total *2:
        mission = "Realisable (carburant sufisant)"


    print(
        f"================================================"
        f"RAPPORT DE MISSION : {nom_mission}"
        f"Nombres d'astronautes : {nombre_astronautes}(masse totale{masse_final_astronautes} Kg) "
        f"Modules disponibles : {nombre_module}((masse totale {masse_final_module} kg)) "
        f"Masse totale du vaisseau : {masse_total} Kg"
        f"Carburant nécessaire : {carburant_initial}L"
        f"Mission VIP, bonus VIP applicable"
        f"  Carburant après bonus VIP : {carburant_final}L"
        f"Mission {mission}"
        f"Depart {tempete} "
    )







