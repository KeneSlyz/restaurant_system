
from comida import procedimientos


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