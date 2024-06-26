import json

def AgregarCategoria():

    with open("biblioteca.json", mode = "r") as agregarCat:
        agregar = json.load(agregarCat)
        
        
        for i in agregarCat:
            Categoria = {
                
                "CategoriaID":13,
                "Nombre":""
            }
             

        agregarCat["Categoria"].append[i]

                
    with open("biblioteca.json", mode = "W") as agregarCat:

            json.dump(agregar,agregarCat,indent = 4)

def EditarCategoria():
     with open("biblioteca.json", mode = "w") as editarArhivo:
        
        contadorE = 0

        #