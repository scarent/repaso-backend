class Equipo:
    def __init__(self,nombre:str,ciudad:str,campeonatos:float,sponsor:str):
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__campeonatos = campeonatos
        self.__sponsor = sponsor
        self.__jugadores = []  #cuando un equipo se crea aparece sin jugadores, el listado es para hacer el append
    #get para obtener, set para asignar
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def get_nombre(self):
        return self.__nombre
    
    def set_ciudad(self,ciudad):
        self.__ciudad = ciudad
    def get_ciudad(self):
        return self.__ciudad
    
    def set_campeonatos(self,campeonatos):
        self.__campeonatos = campeonatos
    def get_campeonatos(self):
        return self.__campeonatos

    def set_sponsor(self,sponsor):
        self.__sponsor = sponsor
    def get_sponsor(self):
        return self.__sponsor
    
    def set_jugadores(self,jugadores):  #carga masiva inicial
        self.__jugadores = jugadores
    def get_jugadores(self):
        return self.__jugadores
    
    def contratar_jugador(self,jugador):
        if jugador in self.__jugadores:
            print("EL jugador ya esta contratado")
        else:
            self.__jugadores.append(jugador)
    def despedir_jugador(self,jugador):
        if jugador not in self.__jugadores:
            print("El jugador no esta en el equipo")
        else:
            self.__jugadores.remove(jugador)

