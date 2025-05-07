def suma_numeros():
    #creamos una funcion para llamarla despues
    n1=int(input("ingrese el primer numero: "))
    n2=int(input("ingrese el segundo numero: "))
    n3=int(input("ingrese el tercer numero: "))
    n4=int(input("ingrese el cuarto numero: "))
    n5=int(input("ingrese el quinto numero: "))
    #le pedimos al usuario que añada 5 numeros 
    if n1 %2==0: 
         if n1>0: 
          if n2 %2==0:
            if n2>0:
             if n3 %2==0:
                 if n3>0:
                  if n4 %2==0:
                    if n4>0:
                     if n5 %2==0:
                        if n5>0:   
                         print(n1+n2+n3+n4+n5)
    
suma_numeros()

def clasificacion_edad():
    #creamos una funcion para llamarla despues 
    n=int(input("ingrese su edad: "))
    #le pedimos al usuario que ingrese un numero
    if 0<n<13:
     print("niño")
    if 13<=n<=17:
        print("adolecente")
    if 18<=n<=59:
        print("adulto")
    if 60<=n:
        print("adulto mayor")
        #creamos condicionales para asignar un titulo a tal edad
    elif n<0:
        #verificamos si el numero es negativo
        print("error")
        #si es negativo da error
clasificacion_edad()

def contador_vocales():
    palabra=input("ingrese una palabra (sin espacios): ")

    
    

