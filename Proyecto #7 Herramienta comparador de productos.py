precio1=float( input("Precio del primer producto:"))
cantidad1=float( input("Cantidad del primer producto:"))
precio2=float(input("Precio del segundo producto:"))
cantidad2=float(input("Cantidad del segundo producto:"))
#Procesar los datos
factor1=precio1/cantidad1
factor2=precio2/cantidad2
#Detectar si son iguales
if factor1 == factor2:
    print("Los dos son igual de baratos")
#Detectar si conviene comprar el primero
if factor1 < factor2:
    print("Te conviene comprar el primer producto")
#Ver si conviene comprar el segundo
if factor1>factor2:
    print("El segundo producto es mas economico")
print("Gracias por utilizar este programa, Saludos.")