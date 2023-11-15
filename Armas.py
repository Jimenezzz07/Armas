class armas:
    def __init__(self, sonido, nombre, color):
        self.sonido = sonido 
        self.nombre = nombre
        self.color = color

class pistola (armas):
    def __init__(self, sonido, nombre, color, daño):
        super().__init__(sonido, nombre, color)
        self.daño = daño
    def mostrar_informacion(self):
        print(f"sonido: {self.sonido}, nombre: {self.nombre}, color: {self.color}, daño: {self.daño}")


armap = pistola ("RATATATA RATATATA", "MP30", "azul", "30")


armap.mostrar_informacion()


    
        