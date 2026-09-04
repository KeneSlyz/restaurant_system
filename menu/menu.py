from comida import procedimientos


def menu():
    return {
    "steak": ["green beans", "root vegetables"],
    "salmon": ["beurre blanc sauce", "potatoes", "green beans"],
    "chicken sandwich" : ["bread", "Lettuce", "green sauce", "bacon", "avocado"],
    "fish and chips" : ["fries", "tartar Sauce", "lemon"]}


def mostrar_menu():
    for i, comida in enumerate(menu()):
        print (i, ".", comida,)

opciones = menu()
def prevencion(opciones):
   
    while True:
        ticket_comanda = input("Que desea ordenar?").lower()
        
        if ticket_comanda in opciones:
            return ticket_comanda
        print("Esto no esta en el menu")


opciones = menu()
def prevencion(opciones):
   
    while True:
        ticket_comanda = input("Que desea ordenar?").lower()
        
        if ticket_comanda in opciones:
            return ticket_comanda
        print("Esto no esta en el menu")
    







