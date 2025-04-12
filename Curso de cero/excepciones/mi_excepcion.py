class MiExcepcion(Exception):
    def __init__(self, *args,e):
        super().__init__(*args)
        print(f"Definiste el error como {e}")
        

#raise ZeroDivisionError ("Diviste entre 0")
try:
    raise MiExcepcion("Generaste una excepcion")
except:
    print("Como vas a cometer ese error")