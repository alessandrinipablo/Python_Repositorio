class FiguraGeometrica:
    
    def __init__(self, ancho, alto):
        # encapsulamos
        # validaciones
        if self._validar_valor(ancho):
            self._ancho=ancho
        else:
            print(f"Valor erroneo, fuera de rango permitido {ancho}")
            
        # encapsulamos
        # validaciones
        if self._validar_valor(alto):
            self._alto=alto
        else:
            self._alto=0
            print(f"Valor erroneo, fuera de rango permitido {alto}")    
    
    def _validar_valor(self, valor):
        return True if 0<valor<10 else False
    
    
    # metodo get para acceder
    @property
    def ancho(self):
        return self._ancho
    
    # metodos set, para nuevo valor
    @ancho.setter
    def ancho(self, ancho):
        self._ancho=ancho
        
    # metodo get para acceder    
    @property
    def alto(self):
        return self._alto
    # metodos set, para nuevo valor
    @alto.setter
    def alto(self, alto):
        self._alto=alto
        
    def __str__(self):
        return f"Figura Geometrica [Ancho: {self._ancho}, Alto: {self._ancho}.]"