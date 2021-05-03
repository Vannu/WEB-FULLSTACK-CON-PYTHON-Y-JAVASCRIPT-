'''
2. Crea una clase Minibus que herede de la clase Vehiculo . Debes poder tener
un método capacidad() que defina por defecto la capacidad de 6 asientos.
Luego crea una clase Pasajero que puedas ir agregando a una instancia de
Minibus . Esa instancia no deberá permitir mas de 50 pasajeros únicos (no
se permiten pasajeros repetidos).
'''

from ast import Index

# CLASE 01
class Vehiculo:

    def __init__(self, patente, color, modelo):
        self.patente = patente
        self.color = color
        self.modelo = modelo
    
    def imprimir(self):
        return f"El numero de matricula es : {self.patente}\nEl color del vehiculo es:{self.color}\nEl modelos es: {self.modelo}"
    
# CLASE 02
class Minibus (Vehiculo):

    def __init__ (self, patente, color, modelo):
        super().__init__(patente, color, modelo)# llama al constructor del padre
        self.setCapacidad()#llama al metodo para cargar la capacidad
        self.capacidad
        self.listaPasajeros = [] # crea lista vacia de pasajeros
        self.limitePasajero = 50 # determina el limite de elementos que tendra de lista de pasajero
        
        
    # metodo que asigna el valor al atributo capacidad
    def setCapacidad(self):
        self.capacidad = 6
    
    # metodo devuelve la cantidad de lugares disponible(valor entero)
    def getLugarDisponible(self):
       return self.limitePasajero - len(self.listaPasajeros)
         
        
    # metodo para cargar pasajeros, en cuanto cumpla las dos condiciones
    def setCargarPasajero(self, pasajero):
        if self.getLugarDisponible() and self.repetido(pasajero):
            self.listaPasajeros.append(pasajero)
           
    #Metodo busca si hay repetido devolviendo un Booleano
    def repetido(self, pasajero):
        for x in self.listaPasajeros:
            if(x.dni == pasajero.dni):   
                return False
        return True
    # Imprime la lista de pasajeros cargados
    def imprimirLista(self):
        for pers in self.listaPasajeros:
            print(pers.getDni())
# CLASE 03    
class Persona():
    # metodo constructor
    def __init__(self, dni):
        self.dni = dni

    #metodo devuelve el valor dni
    def getDni(self):
        return self.dni
    
    #metodo retorno un string con el dni
    def __str__(self):
        return f"el dni de esta persona es {self.getDni}"
       

