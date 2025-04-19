class Persona:
    def__init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}".
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)
    
    p1=Persona("Rodri",21)
    p2=Persona("Alonso",32)
    resultado = p1+p2
    print(resultado.edad)
    
    
    """
    Aritmeticos:
    __add__(self,other) suma
    __sub__(self,other) resta
    __mul__(self,other) multiplicacion
    __div__(self,other) division
    __mod__(self,other) modulo
    __pow__(self,other) potencia
    comparacion:
    __eq__ ==
    __ne__ !=
    __lt__<
    __gt__>
    __le__<=
    __ge__>=
    Asignacion:
    __iadd__(self,other) suma +=
    __isub__(self,other) resta -=
    __imul__(self,other) multiplicacion
    __idiv__(self,other) division
    __imod__(self,other) modulo
    __ipow__(self,other) potencia
    """