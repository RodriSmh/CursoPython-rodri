nombres= ["Juan", "Pedro", "Maria", "Ana", "Luis"]
apellidos= ["Gomez", "Lopez", "Martinez", "Hernandez", "Garcia"]

with open("Nombres_apellidos.txt","w", encoding="utf-8") as archivo:
    archivo.writelines("los datos son:\n")
    [archivo.writelines(f"nombre: {n}\napellido: {a}\n--------------\n") for n,a in zip(nombres,apellidos) ]
    