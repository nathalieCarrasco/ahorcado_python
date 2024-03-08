# JUEGO DEL AHORCADO EN ¨PYTHON 
#1- definir una palabra 
#2-Numero definido de intentos 
#3-pedir al usuario que ingrese una letra a vez 
#resultado de acierto o de perdida 


def ahorcado():
    #definimos palabra secreta
    palabra_secreta="sirius"
    letras_adivinadas=[]
    #lista es para almacenar las letras que concuerden con mi palabra
    intentos=5 #numero de intentos 
    
    while intentos> 0:
        palabra_mostrada= ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_mostrada += letra
            else:
                palabra_mostrada +="_ "
                
        print(palabra_mostrada)
            
        if palabra_mostrada == palabra_secreta:
                print("haz adivinado la palabra")
                break
            #pedir al usuaro una letra 
        letra_usuario=input("Ingrese una letra: ")
            
            #verificar si la letra ah sido adivinada en letras adivinadas 
        if letra_usuario in letras_adivinadas:
                print("ya has adivinado esa letra ")
                continue
        if letra_usuario in palabra_secreta:
                print(" bien tu letra esta en la palabra")
                letras_adivinadas.append(letra_usuario)
        else:
                intentos -= 1 
                print("Incorrecto , pierdes un intento")
                
        if intentos == 0:
                print(" Lo siento , has agotado todos los intentos , La palabra era "+ palabra_secreta)
                
            
# llamar a la funcion 
ahorcado()
