class Restaurantes():
    def __init__(self,restaurante_elegido, tipo_comida_elegida):
        self.nom_restaurante=restaurante_elegido
        self.tipo_comida=tipo_comida_elegida
    
    def describir_restaurante(self):
        print(self.nom_restaurante)
        print(self.tipo_comida)
    
    def abrir_restaurante(self):
        print("El restaurante esta Abierto")