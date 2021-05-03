from vehiculo import Vehiculo, Minibus, Persona

        #Prueba Actividad 02
print("\n------ ACTIVIDAD VEHICULO MINIBUS------")

#genero una instancia de Minibus
mini01 = Minibus(754, "Rojo", "Kangoo")

#Imprimo caracteristicas del minibus
print(mini01.imprimir())

# genero instancias de personas
persona01 = Persona(1)
persona02 = Persona(22)
persona03 = Persona(33)
persona04 = Persona(44)
persona05 = Persona(55)
persona06 = Persona(22)#dni repetido
persona07 = Persona(7)

# Procedo a la carga de pasajeros
mini01.setCargarPasajero(persona01)
mini01.setCargarPasajero(persona02)
mini01.setCargarPasajero(persona03)
mini01.setCargarPasajero(persona04)
mini01.setCargarPasajero(persona05)
mini01.setCargarPasajero(persona06)#carga dni repetido
mini01.setCargarPasajero(persona07)

#Imprimo la cantidad de lugares disponibles de la lista
print(f"\nDisponiblidad de lugares en la lista: {mini01.getLugarDisponible()}")

print("\nListado de Pasajeros x DNI")
mini01.imprimirLista()