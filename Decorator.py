"""
Simula un sistema de café, donde puedas añadir decoradores como leche, chocolate, o canela a una bebida base.

Ejemplo esperado:

Pedido: Espresso + Leche + Canela  
Precio: $3.50
"""

from abc import ABC, abstractmethod

class Bebida(ABC):
    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def precio(self):
        pass

class Espresso(Bebida):
    def descripcion(self):
        return "Espresso"

    def precio(self):
        return 2.00
    
class DecoradorBebida(Bebida):
    def __init__(self, bebida):
        self._bebida = bebida

    def descripcion(self):
        return self._bebida.descripcion()
    
    def precio(self):
        return self._bebida.precio()
    
class Leche(DecoradorBebida):
    def descripcion(self):
        return self._bebida.descripcion() + " + Leche"
    
    def precio(self):
        return self._bebida.precio() + 0.50
    
class Chocolate(DecoradorBebida):
    def descripcion(self):
        return self._bebida.descripcion() + " + Chocolate"
    
    def precio(self):
        return self._bebida.precio() + 0.75
    
class Canela(DecoradorBebida):
    def descripcion(self):
        return self._bebida.descripcion() + " + Canela"
    
    def precio(self):
        return self._bebida.precio() + 0.25
    
bebida = Espresso()
bebida = Leche(bebida)
bebida = Canela(bebida)

print(f"Pedido: {bebida.descripcion()}")
print(f"Precio: ${bebida.precio():.2f}")