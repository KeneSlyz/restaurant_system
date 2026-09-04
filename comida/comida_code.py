
def main():
    opciones = menu()
    mostrar_menu()
    ticket_comanda = prevencion(opciones)
    detecta_alergia()
    eliminar_(ticket_comanda)

def menu():
    return {
    "steak": ["green beans", "root vegetables"],
    "salmon": ["beurre blanc sauce", "potatoes", "green beans"],
    "chicken sandwich" : ["bread", "Lettuce", "green sauce", "bacon", "avocado"],
    "fish and chips" : ["fries", "tartar Sauce", "lemon"]}
    

def mostrar_menu():
    for i, comida in enumerate(menu()):
        print (i, ".", comida,)



def analizar_ticket(ticket_texto):
    #definimos alergenos
    alergenos = {
        "NUECES": ["nuez", "almendra", "pistacho", "mani", "cacahuate"],
        "GLUTEN": ["bread", "flour", "pasta", "crutones", "soy sauce"],
        "LACTOSA": ["cream", "butter", "cheese", "milk", "beurre blanc"]
    }

 #se convierte el ticket en minusculas para evitar errores
 
 
    ticket_limpio = ticket_texto.lower()
    alergias_detectadas = []
    #este codigo buscara alergias en el ticket
    for grupo, ingredientes in alergenos.items():
        for ingrediente in ingredientes:
            if ingrediente in ticket_limpio:
                alergias_detectadas.append(grupo)
                break

    return list(set(alergias_detectadas)) #se eliminan duplicados si los hay


opciones = menu()
def prevencion(opciones):
   
    while True:
        ticket_comanda = input("Que desea ordenar?").lower()
        
        if ticket_comanda in opciones:
            return ticket_comanda
        print("Esto no esta en el menu")


###======================================================
#AQUI ES EL SISTEMA DE ALERGIAS

def detecta_alergia():
    alergia_comanda = ""

    while alergia_comanda not in ["si", "no"]:
        alergia_comanda = input("tiene alguna alergia?").lower()
        if alergia_comanda == "si":
            alergia_alerta = input("que alergia tiene?").lower()
            alertas = analizar_ticket(alergia_alerta)

            if alertas:
                print(" ALERTA DE ALERGIA")
                for alerta in alertas:
                    print(f"CLIENTE ALERGICO A: {alerta}")
            else:
                print("platillo libre de alergias")

                
        elif alergia_comanda == "no":
            print ("continuando el pedido....")
#===========================================================



        
        


#ESTOS PROCEDIIENTOS SON UNICAMENTE PARA EL SALMON
def procedimientos():
    return {
    "salmon" :[
        "Stir the salmon",
        "Prepare the potatoes to roast in the oven",
        "Heat up the beurre blanc (milk) "],
    "steak" : [
        "Steak on the grill",
        "prepare the vegetables, oil and salt, then put inside the oven",
        "prepare the butter"]
}



#AQUI DEFINIMOS ELIMINAR Y LA PODEMOS VOLVER A USAR LUEGO


def eliminar_(ticket_comanda):
    if ticket_comanda in procedimientos():
#ACA HACEMOS UNA COPIA DE LS PROCEDIMIENTOS ORIGINALES PARA EVITAR DANAR LA ORIGINAL
            nuevo_procedimiento = procedimientos()[ticket_comanda].copy()
            print("llegue aqui")
            for i, procedimiento in enumerate(nuevo_procedimiento):
                print(i,".", procedimiento)


#ACA CAMBIAREMOS ALGO EN EL PLATO    
            opcion = input("Desea cambiar algo en el plato?")
            if opcion == "si":
                opcion_eliminar = int(input("que desea eliminar"))
                nuevo_procedimiento.pop(opcion_eliminar)
                                      
            else:
                return
        
               
            print (f"\n!!{ticket_comanda}!!".upper())
            for i, procedimiento in enumerate(nuevo_procedimiento):
                print (i, ".", procedimiento)

if __name__ == "__main__":
    main()
