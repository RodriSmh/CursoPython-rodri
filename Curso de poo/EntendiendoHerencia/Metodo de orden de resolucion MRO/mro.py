class A:
    def hablar(self):
        print("Hola desde A")
class E:
    def hablar(self):
        print("Hola desde E")
class B(A):
    pass
class C(E):
    def hablar(self):
        print("Hola desde C")
class D(B,C):
    pass
d = D()

d.hablar()