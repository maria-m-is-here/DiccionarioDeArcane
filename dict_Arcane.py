arcane_characters = {
                     "Vi": "Es uno de los personajes principales, y es la hermana mayor de Powder/Jinx.",
                     "Jinx": "Antes conocida como Powder, es la hermana menor de Vi, es la causa de muchos problemas.",
                     "Caitlyn": "Pertenece al clan Kiramman, una de las casas gobernantes de Piltover. Tiene un fuerte sentido de justicia.",
                     "Ekko": "Su nombre también hace referencia a su capacidad de rebobinar el tiempo, ya que él crea un artefacto que le otorga dicha capacidad."
}
character = input("Elije un personaje, primera letra en mayuscula:")

if character in arcane_characters.keys():
    print(arcane_characters[character])
else:
    print("Ese personaje no esta registrado")
