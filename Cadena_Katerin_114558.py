# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 22:58:16 2020

@author: Katerin
"""

import math
#%%PUNTO 1: PROGRAMA QUE CALCULA EL VALOR ABSOLUTO
'''Sin utilizar el comando abs, escribir un programa que calcule
 e imprima el valor absoluto de cualquier número (sea entero o decimal).'''
 
numero = float(input("Ingrese un numero: ")) #Solicita ingresar un numero, 
                                            #y el float admite  decimal y 
                                            #enteros.''' 
if numero >= 0 :
   print('su numero en valor absoluto es :',numero) #si el número ingresado 
                                                    #cumple la condición, 
                                                    #entonces imprime el valor 
                                                    #que se le halla ingresado
else:
   numero=numero*-1 # y si ya no cumpiio la primera condición,
                    #pasa a multiplica la variable numero por -1
   print('su numero en valor absoluto es :',numero)
#%%PUNTO 2:PROGRAMA QUE PIDE INGRESAR DOS NUMEROS Y COMPRUEBA SI LA DIFERENCIA 
#ENTRE ELLOS DA UN NUMERO PRIMO
   
'''Leer dos números enteros y determinar si la magnitud de 
la diferencia entre los dos es un número primo'''
import math
num1 = int(input('ingrese un número entero: '))
num2 = int(input('ingrese un segundo numero: '))
diferencia = num1-num2
diferencia = int(math.sqrt(diferencia*diferencia))
print(diferencia)
contador = 0
for i in range(1,diferencia+1):
    if (diferencia% i)==0:
        contador =contador +1
if contador ==2:
    print('la diferencia entre los dos nuneros arroja un numero primo')
else:
    print('la diferencia entre los dos nuneros no arroja un numero primo')

#%% PUNTO 3: PROGRAMA PARA ITERAR
'''Iterar a través de los primeros cien enteros positivos, buscando los 
múltiplos de 3 e imprimiendo y almacenándolos en una lista hasta encontrar 
los primeros 15 de ellos. Una vez encontrados, continuar iterando en busca 
de los múltiplos de 4 y almacenarlos en otra lista.'''

def multiple(valor, multiple):
    """
    Funcion para calcular si el numero es multiplo
    utilizando el modulo de la division
    """
    resto = valor % multiple
    if resto == 0:
        return True
    else:
        return False
 
# lista que contendra los valores multiples
multiples_3=[]
multiples_4=[]
 
# bucle del 1 al 100
for i in range(1,101):
 
    if multiple(i,3) and len(multiples_3)<16:
        multiples_3.append(i)
        x =i

for j in range(x,101):
    if multiple(j,4):
        multiples_4.append(j)
    
 
print ("Los multiples de 3 son: " , multiples_3)

print ("Los multiples de 4 son: ", multiples_4)

#%% PUNTO 4: PROGRAMA DEL CIRCULO

import math
print("Ingrese las cordenadas de origen y el radio del circulo 1")
numeros1=input()
arreglo1=numeros1.split()
print(arreglo1)
print("ingrese las cordenadas de origen y el radio del circulo 2")
numeros2=input()
arreglo2=numeros2.split()
print(arreglo2)
print("digite el punto que sea ver si esta dentro de los circulos")
numeros3=input()
arreglo3=numeros3.split()
print(arreglo3)
print(arreglo3[1])
d1=math.sqrt(math.pow(((int)(arreglo3[0])-((int)(arreglo1[0]))),2)+math.pow((((int)(arreglo3[1]))-((int)(arreglo1[1]))),2))
d2=math.sqrt(math.pow(((int)(arreglo3[0])-((int)(arreglo2[0]))),2)+math.pow((((int)(arreglo3[1]))-((int)(arreglo2[1]))),2))
if(d1<(((int)(arreglo1[2])) and d2<((int)(arreglo2[2])))) :
       print("el punto está entre ambos circulos")
else:
       if(d1<((int)(arreglo1[2]))):
          print("el punto está dentro del circulo 1")
       if(d2<((int)(arreglo2[2]))):
            print("el punto está dentro del circulo 1")
       else:
            print("el punto no está dentro de ningun circulo")
            
#
#%% CADENAS. PUNTO 5
'''Escribir un programa que reciba una cadena de texto y reporte
a) cuántas letras vocales en mayúscula se entraron;
b) cuántas letras con tilde se entraron (minúsculas y mayúsculas);
c) cuántos dígitos se entraron, 
d) cuántos espacios se entraron;
e) cuántas palabras reservadas se entraron.'''
    
import keyword
texto= input("Ingrese un texto") # PIDE QUE SE INTRODUZCA UN TEXTO
M="AEIOUÁÉÍÓÚ"                      # Vocales mayusculas con y sin tilde
S1=[]                               # Espacios
for i in range(0, len(texto)): 
   if texto[i] in M:
       S1.append(texto[i])      #Append Permite agregar un elemento a la lista
print ("El texto ingresado tiene", len(S1),"vocales mayusculas")

MT="ÁÉÍÓÚáéíóú"
S2=[]
for i in range(0, len(texto)):
   if texto[i] in MT:
       S2.append(texto[i])
print ("El texto ingresado tiene", len(S2),"vocales con tilde")

num="0123456789"
S3=[]
for i in range(0, len(texto)):
   if texto[i] in num:
       S3.append(texto[i])
print ("El texto ingreado tiene", len(S3),"digitos")


espacio= " "
S4=[]
for i in range(0, len(texto)):
   if texto[i] in espacio:
       S4.append(texto[i])
print ("El texto ingreasdo tiene", len(S4),"espacios")

S5=texto.split()
S6=[]
for i in range(0, len(S5)):
   if [i] in keyword.kwlist:
       S6.append(S5[i])
print (S6,"son keywords contenidas en la palabra digitada")

#%%% Punto 6
''' Leer una cadena de texto y organizar alfabéticamente cada una de las 
letras que la componen, repitiendo cada una tantas veces como se encuentra. 
Por ejemplo, la cadena ‘tarea importante’ será ‘aaaeeimnoprrttt’. 
(Note que no se incluyen los espacios). '''

print("Ingrese la cadena") #imprime en pantalla el mensaje de ingresar texto
cadena = input( )  #aqui se guarda el texto ingrsado
cadena=cadena.replace(' ', '') #aqui se esta quitando los espacios
lista=[]
for i in cadena:
    lista.append(i) #con append se esta agregando elemntos a la lista
    lista.sort()
cadena2=''
for i in lista:
    cadena2 +=i
print(cadena2)

#%% lISTAS. PUNTO 7

'''Leer una lista de números ya ordenados de forma ascendente y verificar 
que dicha lista está ordenada. Luego, leer un número e insertarlo en la lista 
en la posición que le corresponde a dicho número.'''
   
print("digite el arreglo")
cadena=input()
cadena=cadena.replace(' ', '')
lista=[]
for i in cadena:
    lista.append(i)
    lista.sort()
cadena2=''
for i in lista:
    cadena2 +=i
if(cadena != cadena2):
    print("la lista no está ordenada")
else:
    print("digite el valor a ingresar a la lista")
    num=input()
    lista.append(num)
    lista.sort()
print(lista)

#%% PUNTO 8

print("digite el arreglo")             
cadena=[]                              
cadena=input().split()                 
cadena1=[]                             
for i in cadena:                       
    cadena1.append(int(i))             
lista_nueva = []                       
for i in cadena1:                      
    if i not in lista_nueva:           
        lista_nueva.append(i)          
lista_nueva.remove(max(lista_nueva))   
print(max(lista_nueva))
            

#%% PUNTO 9. 
'''Escribir un programa que calcule términos de la sucesión 
#Un+1 = 3 Un + 1 si Un es impar y U n+1 = Un / 2 si Un es par. El
#programa tiene que pedir el término U0 y el número de términos a calcular'''                                                      
                                                                                                                                
numero = int(input("Ingresa un numero: "))                                                                                      
pausa = int(input("Ingresa la cantidad de numeros: "))                                                                          
nume=0                                                                                                                          
while numero != 1:                                                                                                              
    nume=nume+1                                                                                                                 
    if numero % 2 == 0:                                                                                                         
        print("%d," % (numero), end = "")                                                                                       
        numero = numero / 2                                                                                                     
    else:                                                                                                                       
        print("%d," % (numero), end = "")                                                                                       
        numero = (numero * 3) + 1                                                                                               
                                                                                                                                
    if numero == 1:                                                                                                             
        print("1")                                                                                                              
    if(nume == pausa):                                                                                                          
        break                                                                                                                   
            
 #%% PUNTO 10: 
'''Leer una matriz e imprimir el vector que aparece cuando 
la matriz se desenreda en forma de espiral que gira en el            
sentido horario a partir de la esquina inferior derecha'''                                                                             
                                                                                                                                     
import random                                                                                                                        
n = int(5)                                                                                                                           
matriz=[None]*n                                                                                                                      
for i in range(0,n):                                                                                                                 
    matriz[i] = [None]*n                                                                                                             
for i in range(0,n):                                                                                                                 
    for j in range(0,n):                                                                                                             
        matriz[i][j] = (int)(random.randint(1,1001))                                                                                 
print(matriz)                                                                                                                        
for i in range(n-1,-1,-1):                                                                                                           
    if(i%2==0):                                                                                                                      
        for j in range(n-1,-1,-1):                                                                                                   
            print (matriz[j][i])                                                                                                     
    else:                                                                                                                            
        for j in range(0,n):                                                                                                         
            print (matriz[j][i])                                                                                                     
                                                                                                                                     
                                                                                                                                     
#%% PUNTO 11. 
'''Diseñar una función de tres parámetros que pida la altura y anchura de
un rectángulo, y el carácter a utilizar para          
dibujarlO.'''                                                                                                                  
# PROGRAMA QUE PIDE B Y H DE UN RECTÁNGULO Y LO GRAFICA
anchura = int(input("Anchura del rectángulo: ")) #solicita el ancho
altura = int(input("Altura del rectángulo: ")) #solicita la altura
caracter =(input('Caracter: ')) #solita el caracter que se dibujara

for i in range(altura):
    for j in range(anchura):
        print(caracter, end="  ")
    print()                                                                                           
                                                                                                                                     
#%%PUNTO 12: 
'''Pide anchura de un triángulo y lo dibuje con caracteres producto (*).'''

a = int(input("ingrese el ancho ancho del triangulo:  "))

for k in range(a+1):
    print("* "*k)
    
for d in range(1, a):
    for j in range(a - d):
        print("* ", end="")
    print()                                                                                                          
                                                                                                                                     

#%%PUNTO 13: Calculador de años bisiestos
'''Función evalua_int, garantiza que el valor ingresado sea entero,
 de no ser asi, la función volvera a pedir los datos, hasta hallar el correcto.
 valor'''
  
def evalua_int():                  #la función no tiene parametros de entrada
    while True:                    # mientras sea verdad el ciclo se va 
                                   #a repetir:  
        try:                       #1) evaluar la variable num
            num=int(input('--> ')) #2) si el valor ingresado es un int el ciclo
            break                  #se finalizara con un break
        except ValueError:         #3) sino muestra error
                                   #en este caso es el mensaje al usario
            print('no es un número entero, intentalo otra vez')
                                   # esto se repite hasta que se ingrese un int          
            
    return(num)                    #retorno valor de la variable num
    


def añosbisiesto():            # funcion sin parametros 
    print('Escriba un año')    # informacion dada por el usuario
    num1=evalua_int()          #verifca el número ingresado
    while True:                #ciclo de repeticion para garantizar que el num2
                               #sea mayor que el num1
         print('Por favor escriba otro año, posterior al año ',num1)
         num2=evalua_int()     #evalua y valida el num2 mediante la 
                               #función evalua_int 
         if num1>num2:         #compara los valores ingresados si num1>num2
                               #el programa arroja el mesaje al usuario para 
                               #que se modifique 
             print(num2, 'No es mayor que ',num1,'intentelo de nuevo --> ')
         else:                 #de lo contrario los valores ingresados son los 
             break             #solicitados y el ciclo se cierra con un break
            
    cont=0                       #inicialización del contador para años
                                 #bisiestos 
    for i in range(num1,num2+1): #evaluación de todos los años en el rango 
        if i%4==0:               #si es múltiplo de 4 significa que es bisiesto
            cont+=1              #y se agrega una unidad al contador 
    
    #resultado listo para imprimir 
    R='Entre los años',num1,'y',num2,'hay',num2-num1+1,'años,',cont,'de ellos son bisiestos'
    return(R)    
    
                          
print(*añosbisiesto())               #se llama a la función año bisiesto                                                                                                     
                                                                                                                                     
#%% PUNTO 14: 
'''Diseñar una función que proponga sumas de números positivos (dos 
#números entre 1 y 100) al usuario y compruebe la respuesta. El programa 
#continuará hasta que se acierten cinco sumas. (Tip: para generar los números 
#enteros aleatorios, existe la función random.randint(a,b) de la librería 
#random).'''                                                       
                                                                                                                                     
import random                                                                                                                        
aciertos=0                                                                                                                           
while(True):                                                                                                                         
    num1=random.randint(0, 100)                                                                                                      
    num2=random.randint(0, 100)                                                                                                      
    print("adivine la suma de los numeros " + str(num1) + " y "+str(num2))                                                           
    respueta_in=int(input())                                                                                                         
    respuesta_real=num1+num2                                                                                                         
    if(respueta_in==respuesta_real):                                                                                                 
        aciertos=aciertos+1                                                                                                          
    else:                                                                                                                            
        aciertos=0                                                                                                                   
    if(aciertos==5):                                                                                                                 
        break                                                                                                                        
    print("sus aciertos son: " + str(aciertos))                                                                                      
print("usted acerto 5 veces :D")

#%% PUNTO 15
import random

# simbolos validos en el codigo
digitos = ('0','1','2','3','4','5','6','7','8','9')

# "elegimos" el codigo
codigo = ''
for i in range(4):
    candidato = random.choice(digitos)
    # vamos eligiendo digitos no repetidos*
    while candidato in codigo:
        candidato = random.choice(digitos)
    codigo = codigo + candidato

print ("Bienvenido/a, Tienes que adivinar un numero de", 4, "cifras distintas")
propuesta =input("Propon un código: ") #solicita ingresar un código

intentos = 1 # empieza a mirar propuestas e indica  aciertos y coincidencias
while propuesta != codigo:
    intentos = intentos + 1
    aciertos = 0
    coincidencias = 0

    for i in range(4): # procesa la propuesta y verifica en el codigo
        if propuesta[i] == codigo[i]:
            aciertos = aciertos + 1
        elif propuesta[i] in codigo:
            coincidencias = coincidencias + 1
    print ("Tu propuesta (", propuesta, ") tiene", aciertos, \
          "aciertos y ", coincidencias, "coincidencias.")
    
    propuesta =input("Propon otro codigo: ") # pedimos siguiente propuesta*

print ("Genial! Adivinaste el codigo en", intentos, "intentos.")






























