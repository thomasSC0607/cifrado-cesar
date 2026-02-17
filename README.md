# Algoritmo cifrado Cesar implementado con Pyhton 

El archivo `cesar.py` contiene el programa que simula el proceso de cifrado y descifrado Cesar, consiste en 2 funciones:

* **cesar_encriptar()**: Esta recibe 2 parámetros, un texto tipo sstring y una clave tipo entero, y devuelve un string del mensaje cifrado pasado por parámetro.

El "core" de esta función es una operación matemática que desplaza cada caracter del alfabeto n posiciones para convertirlo en otro, siendo n la llave. Teniendo en cuenta que los caracteres especiales y espacios no se ven afectados por el algoritmo. 

`result.append(chr(ord(ch) - base + key) % 26 + base)`


* **cesar_descifrar**: Recibe al igual que la función anterior 2 parámteros iguales y devuelve la cadena de texto descifrada. 

La lógica matemática de esta función es deshacer lo que se hizo anteriormente al cifrar, es decir, si a cada posición del caracter se le suma la llave, para volver al caracter original basta con restar la clave al caracter cifrado, por esta razón usamos la llave negativa con la misma función de cifrar, pero en este caso no se va a sumar la llave sino que se va a restar.