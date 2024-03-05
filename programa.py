# 1 Escribe un programa en Python que imprima tu nombre en la pantalla.
def imprimir_nombre():
    print('Daniel Noboa')

if __name__ == "__main__":
    # Se llama a la función imprimir_nombre() para ejecutarla
    imprimir_nombre()
    
# 2 Escribe un programa que calcule la suma de los números del 1 al 10.
def suma_1_al_10():
    suma = sum(range(1, 11))  # Se utiliza la función sum() para calcular la suma del rango del 1 al 10
    # Se devuelve el resultado de la suma
    return suma

if __name__ == "__main__":
    resultado = suma_1_al_10()  # Se llama a la función suma_1_al_10() para obtener el resultado
    # Se imprime el resultado de la suma
    print(resultado)

# 3 Crea variables para almacenar tu edad, nombre y estatura, e imprímelas en pantalla.
def imprimir_datos_personales(nombre, edad, estatura):
    print(f'Nombre: {nombre}\nEdad: {edad}\nEstatura: {estatura}')
        

if __name__ == "__main__":
    # Se definen las variables con los datos personales
    nombre = "Daniel Noboa"
    edad = 30
    estatura = 1.75
    # Se llama a la función imprimir_datos_personales() para mostrar los datos
    imprimir_datos_personales(nombre, edad, estatura)
    
# 4 Escribe un programa que determine si un número ingresado por el usuario es par o impar.
def par_o_impar(numero):
    try:
        if numero % 2 == 0:
            return 'par'
        else:
            return 'impar'
    except ValueError:
        print('Error: Tipo de dato no válido, ingrese un número')

if __name__ == "__main__":
    num = float(input("Ingrese un número: "))  # Se solicita al usuario que ingrese un número
    print(par_o_impar(num))  # Se imprime si el número ingresado es par o impar

# 5 Crea una función que calcule el área de un círculo dado su radio.
import math

def area_circulo(radio):
    area = math.pi * radio ** 2  # Se calcula el área del círculo utilizando la fórmula matemática
    return area

if __name__ == "__main__":
    radio = float(input("Ingrese el radio del círculo: "))  # Se solicita al usuario que ingrese el radio del círculo
    print("El área del círculo es:", area_circulo(radio))  # Se imprime el área calculada del círculo

# 6 Define una función que reciba dos números como argumentos y devuelva su suma.
def suma(a, b):
    return sum((a, b))
    
if __name__ == "__main__":
    num1 = int(input("Ingrese el primer número: "))  # Se solicita al usuario que ingrese el primer número
    num2 = int(input("Ingrese el segundo número: "))  # Se solicita al usuario que ingrese el segundo número
    print("La suma es:", suma(num1, num2))  # Se imprime la suma de los dos números ingresados

# 7 Modifica la función que calcula el área del círculo para que reciba el radio como parámetro.
import math

def area_circulo(radio):
    area = math.pi * radio ** 2  # Se calcula el área del círculo utilizando la fórmula matemática
    return area

if __name__ == "__main__":
    radio = float(input("Ingrese el radio del círculo: "))  # Se solicita al usuario que ingrese el radio del círculo
    print("El área del círculo es:", area_circulo(radio))  # Se imprime el área calculada del círculo

# 8 Diseña un programa que convierta grados Celsius a Fahrenheit y viceversa, utilizando funciones para realizar los cálculos.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32  # Se aplica la fórmula de conversión de Celsius a Fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit-32)*5/9

if __name__ == "__main__":
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))  # Se solicita al usuario que ingrese la temperatura en grados Celsius
    print("Temperatura en Fahrenheit:", celsius_a_fahrenheit(celsius))  # Se imprime la temperatura convertida a grados Fahrenheit
    # Se solicita al usuario que ingrese la temperatura en grados Fahrenheit
    fahrenheit = float(input('Ingrese la temperatura en grados Fahrenheit: '))
    print("Temperatura en Celsius:", fahrenheit_a_celsius(fahrenheit))  # Se imprime la temperatura convertida a grados Celsius
