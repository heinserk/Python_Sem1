edad = 29
estatura = 1.71
peso = 70.5
complejo = 1 + 4j


print("impresion de un numero complejo:"),complejo


#Transformando un entero a real
print("Transformando un valor entero a real:",float(edad))

#Transformando un valor real a entero
print("Transformando un valor real a entero:",int(peso))

#OPERACION ARITMETICA BÁSICA
imc = peso / (estatura==2)
print("Mi IMC es de:{imc}")
print ("Mi imc es de: {:.5f}",format(imc))#formateamos imc

#Valores booleanos

ampolleta = False 
interruptor = True

print(ampolleta,interruptor)
print("La variable ampolleta es de tipo: ",type(interruptor))

#Podemos transformar cualquier valor a un booleano 

print(bool(0))
print(bool(""))
print(bool(None))
print(bool("False"))
print(bool(1))

#Inicializando listas de 2 maneras
nueva_lista = list()
otra_lista = []
print("Esta es una lista vacia:",nueva_lista)
print("Esta es otra lista vacia:",otra_lista)
print(type(otra_lista))

#¿Como accedo  a un elemento especifico de la lista?

print(estudiantes[0])#Elemento 1 de la lista
print(estudiantes[1])#Elemento 2 de la lista
print("Posicion -2",estudiantes[-2])

#Inicializando otra lista de datos mixtos
data_asig = [10023,"Porgramacion",1,True]

cod,ramo,semestre,estado = data_asig   

#Se pueden sumar listas?

print("Suma de listas",estudiantes +  num) 

#Que hacen estas funciones?
print(list("python"))
print(list(range(10)))

# TUPLAS (NO MUTABLES)

newtupla = tuple()
grupo1 = ("Daniel","Cristian","Felipe",200,100,"Daniel")
print(type(grupo1))

#Accediendo al primer elemento de la tupla
print(grupo1[0])

#Consultando el elemento "Daniel" cuantas veces se encuentra en la tupla
print("El elemtno se repite:",grupo1.count("Daniel"))
#Muestra el indice del primer elemento buscado
print("Indice del elemento:",grupo1.index("Daniel"))

#Obteniendo un trozo de la tupla
grupo2 = ("Pedro",100,"Felipe","Diego",2020,"Alejandra")
print("Trozo de la tabla",grupo2[0:3])

#Entonces como no puedo modificar una tulpa, que puedo hacer?
grupo1 = list(grupo1)
print("La tupla ahora es de tipo:",type(grupo1))


# SETS [CONJUNTOS] ESTRUCTURA FIJA
# FORMAS DE INICIALIZAR UN SET
print("-------SETS-------")
conjunto_vacio = set()
conjunto_vacio1 = {} #¿diccionario o set?
print(type(conjunto_vacio1))
conjunto_colores = set({"Azul","Rojo","Verde"})
conjunto_animales = {"Gato","Perro","Loro"}


print(type(conjunto_colores))