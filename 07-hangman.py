import random
import os

def verificar(letra, acertadas, letras):
    cont=0
    if letra in acertadas:
        return -1
    else:
        for i in letras:
            if letra == i:
                cont+=1
        return cont

def dibujar(cont_errores):

    print("\t  +---+")
    print("\t  |   |")
    print("\t  ", end="")
    if cont_errores>0:
        print("O", end="")
    else:
        print(" ", end="")
    print("   |")
    print("\t ", end="")
    if cont_errores>2:
        print("/", end="")
    else:
        print(" ", end="")
    if cont_errores>1:
        print("|", end="")
    else:
        print(" ", end="")
    if cont_errores>3:
        print("\\", end="")
    else:
        print(" ", end="")
    print("  |")
    print("\t ", end="")
    if cont_errores>4:
        print("/", end="")
    else:
        print(" ", end="")
    print(" ", end="")
    if cont_errores>5:
        print("\\", end="")
    else:
        print(" ", end="")
    print("  |")
    print("\t      |")
    print("\t=========\n\n")

def volver():
    while True:
        os.system("cls")
        print('''
         _                                             
        | |                                            
        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
        | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        | | | | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            _/  |                      
                           |___/     

            ''')
        print("Volver a jugar?: \n1-Si\n2-No")
        try:
            respuesta=int(input("=> "))
            if respuesta==1:
                return True
            elif respuesta==0:
                return False
            else:
                print("Su respuesta no pudo ser procesada...")
                input("\npresione cualquier tecla para continuar") 
        except ValueError:
            print("Su respuesta no pudo ser procesada...")
            input("\npresione cualquier tecla para continuar")

    

palabras = ["abracadabrante", "papahuevos", "papichulo", "conflictuar", 
"euroescepticismo", "amigovio", "culamen", "descambiar","angeltequieromucho",
"toballa", "vagamundo", "espanglish", "friki", "paralelepipedo", "euler",
"aracnido", "provocar", "gabiota", "extinto", "canto", "deshielo", "tristeza",
"declamar", "morder", "postizo", "cicatriz", "estudios", "desnudo", "estanciero",
"lastre", "acariciar", "detenerse", "copiar", "azulejo", "barrer", "microondas"
"piloto", "aspiradora", "renacuajos", "platillo", "revoluciones", "plumero", 
"grasa", "mejor", "dureza", "cinco", "carnicero", "rociar", "calzado", "pitagoras",
"bach", "mozart", "maquiavelo", "tesla", "babosa", "aniversario", "vestir", "patata"
"italiano", "ahorcar", "venezuela", "retrofuturismopsicotropical", "etapas", "karate",
"anciano", "mundo", "crudo", "acceso", "calentar", "papel", "ponerse", "pulpo", "pueblo",
"manejar", "protesta", "profesor", "memoria", "lastimadura", "lavarropas", "tendedero",
"golosina", "hormiguero", "verdura", "numerar", "cardinales", "ornitorrinco", "otorrino"]

rejugar=True
while rejugar==True:

    os.system("cls")

    palabra=random.choice(palabras)

    letras=[]
    acertadas=[]
    cont_aciertos=0
    cont_errores=0
    terminar=False

    for i in palabra:
        letras+=i

    print('''
         _                                             
        | |                                            
        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
        | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        | | | | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            _/  |                      
                           |___/     

    ''')
    letra=input("Adivina una letra: ").lower()

    resultado=verificar(letra, acertadas, letras)

    if resultado==0:
        cont_errores+=1
    else:
        acertadas+=letra
        cont_aciertos+=resultado

    while terminar!=True:

        os.system("cls")

        for i in range(len(palabra)):
            if letras[i] in acertadas:
                print(letras[i], end=" ")
            else:
                print("_", end=" ")

        print("\n\n")
        
        dibujar(cont_errores)

        if letra in letras:
            print(f'Excelente, has acertado: "{letra}" si forma parte de la palabra')
        else:
            print(f'Vaya, "{letra}" no forma parte de la palabra...')

        if cont_aciertos==len(palabra):
            print("Has ganado!")
            terminar=True
        elif cont_errores==6:
            print("Has perdido...")
            terminar=True
        else:
            letra=input("Adivina una letra: ").lower()

            resultado=verificar(letra, acertadas, letras)
            if resultado==0:
                cont_errores+=1
            elif resultado!=-1:
                cont_aciertos+=resultado
                acertadas+=letra 

    input("\npresione cualquier tecla para continuar")
    rejugar=volver()