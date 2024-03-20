import random
import os
import time

def read():
    palabra=""
    with open("data.txt","r",encoding="utf-8") as f:
        iterables = f.readlines()
        palabra = random.choice(iterables).strip()
    return palabra

def palabra_aleatoria():
    palabra_a = read()
    palabra_oculta = ["_"]*len(palabra_a)
    letras_usadas = []
    vidas = 5
    acierto = False
    mega_acierto = False
    
    try:
        while vidas > 0:
            os.system("cls")
            acierto = False
            if vidas == 1:
                print("Ultima vida")
            else:
                print("Vida número #",vidas)
            print("letras ya adivinadas: ",letras_usadas)
            print("".join(palabra_oculta))
            letra = input("Ingresa una letra para adivinar que palabra es: ")
        
            if len(letra)>1:
                for i in range(len(palabra_oculta)):
                    try:
                        if letra[i] == palabra_a[i]:
                            palabra_oculta[i] = letra[i]
                            acierto = True
                    except:
                        print("Solo se permite ingresar una letra o la palabra entera")
                        time.sleep(2)
                        print("Intentalo de nuevo :)")
                        time.sleep(2)
                        break
            if "".join(palabra_oculta) == palabra_a:
                mega_acierto = True  
                break        
            else:
                for i in range(len(palabra_oculta)):
                    if letra == palabra_a[i]:
                        palabra_oculta[i] = letra
                        acierto = True
                letras_usadas.append(letra)
            if "".join(palabra_oculta) == palabra_a:
                mega_acierto = True  
                break    
            if not acierto:
                vidas -=1 
        if mega_acierto:
            print("Ganaste felicidades")
            print("La palabra era: " + palabra_a)
            time.sleep(2)
        else:        
            print("Perdiste")
            print("La palabra era: " + palabra_a) 
            time.sleep(2)            
    except:
        print("Error en palabra_aleatoria llame al admin")
    

def palabra_usuario():
    palabra_a = input("Ingresa una palabra a adivinar: ")
    palabra_oculta = ["_"]*len(palabra_a) 
    letras_usadas = []
    vidas = 5
    acierto = False
    mega_acierto = False
    
    try:
        while vidas > 0:
            os.system("cls")
            acierto = False
            if vidas == 1:
                print("Ultima vida")
            else:
                print("Vida número #",vidas)
            
            print("letras usadas: ",letras_usadas)
            print("".join(palabra_oculta))
            letra = input("Ingresa una letra para adivinar que palabra es: ")
        
            if len(letra)>1:
                for i in range(len(palabra_oculta)):
                    try:
                        if letra[i] == palabra_a[i]:
                            palabra_oculta[i] = letra[i]
                            acierto = True
                    except:
                        print("Solo se permite ingresar una letra o la palabra entera")
                        time.sleep(2)
                        print("Intentalo de nuevo :)")
                        time.sleep(2)
                        break
            if "".join(palabra_oculta) == palabra_a:
                mega_acierto = True
                break           
            else:
                for i in range(len(palabra_oculta)):
                    if letra == palabra_a[i]:
                        palabra_oculta[i] = letra
                        acierto = True
                letras_usadas.append(letra)
            if "".join(palabra_oculta) == palabra_a:
                mega_acierto = True  
                break    
                
            if not acierto:
                vidas -=1 
        if mega_acierto:
            print("Ganaste felicidades")
            print("La palabra era: " + palabra_a)
            time.sleep(2)
        else:    
            print("Perdiste")
            print("La palabra era: " + palabra_a) 
            time.sleep(2)            
    except:
        print("Error en palabra_usuario llame al admin")


 

def run():
    
    inicio = """
    __  __   ___       _   __   ______   __  ___   ___       _   __
   / / / /  /   |     / | / /  / ____/  /  |/  /  /   |     / | / /
  / /_/ /  / /| |    /  |/ /  / / __   / /|_/ /  / /| |    /  |/ / 
 / __  /  / ___ |   / /|  /  / /_/ /  / /  / /  / ___ |   / /|  /  
/_/ /_/  /_/  |_|  /_/ |_/   \____/  /_/  /_/  /_/  |_|  /_/ |_/                                                                 
"""
    inicio2= """
   ______   ___       __  ___   ______
  / ____/  /   |     /  |/  /  / ____/
 / / __   / /| |    / /|_/ /  / __/   
/ /_/ /  / ___ |   / /  / /  / /___   
\____/  /_/  |_|  /_/  /_/  /_____/   
"""
    menu = '''
HORA DE JUGAR AL AHORCADO
Menú:
1. Jugar con palabra aleatoria
2. Jugar con palabra ingresada por el usuario
3. Salir
'''
    
    
    while True:
        os.system("cls")
        print(inicio)
        print(inicio2)
        try:
            respuesta = int(input(menu))
            if respuesta == 3:
                break
            elif respuesta == 1:
                palabra_aleatoria()
            elif respuesta == 2:
                palabra_usuario()
            else:
                print("¡Ingrese una opción valida!")
        except:
            print("Ingrese un número")

if __name__ == '__main__':
    run()