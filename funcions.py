# -*- coding: utf-8 -*-
# DEFINIR
def saludar():
    print("Hola Andrea")
#EJECUTAR
saludar()    


# DEFINIR + PARÁMETRO 
def saludar(name):
    print("Hola " + name)
#EJECUTAR
saludar("Sergi") 
saludar("Andre") 
saludar("JM") 


# DEFINIR 
def saludar(name):
    print("Hola " + name)
#EJECUTAR
saludar("Sergi") 
saludar("Andre") 
saludar("JM") 
saludar("")


# DEFINIR 
def saludar(name):
    return "Hola " + name
#EJECUTAR
saludo = "voy a visitar: " + saludar("María")
print(saludo)


# DATOS
names = ["Andre", "Sergi", "Rosana"]
#DEFINIR
def saludar(name):
    return "Hola " +  name
#EJECUTAR
