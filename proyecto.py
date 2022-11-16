#Ejercicio 2

def notas():

    NHI=float(input("Nota en el hito individual: "))
    NHG=float(input("Nota en el hito grupal: "))
    NE=float(input("Nota en el examen: "))

    NT=(NHI*0.3+NHG*0.2+NE*0.5)
    print(f"La nota es {round(NT)}")

#Ejercicio 3

def notaNashe():
    ntotal=0
    aciertos=float(input("Cuantas has acertado?: "))
    errores=float(input("Cuantas preguntas has fallado?: "))
    nulos=float(input("Cuantas preguntas no has contestado?: "))

    
    total=ntotal+(aciertos*0.5)-(errores*0.25)+(nulos*0)
    print(f"La nota es {total}")
notaNashe()

#Ejercicio 4

def rectangulo():
    base=float(input("Pon la base del rectangulo: "))
    altura=float(input("Pon la altura del rectangulo: "))

    perimetroR=(base*2+altura*2)
    areaR=(base*altura)

    print(f"El perimetro es {perimetroR}m y el area es {areaR}m2.")
