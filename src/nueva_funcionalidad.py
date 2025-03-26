def es_par(numero):
    """ Devuelve True si el número es par, False si es impar. """
    return numero % 2 == 0

def contar_vocales(cadena):
    """ Cuenta la cantidad de vocales en una cadena. """
    return sum(1 for letra in cadena.lower() if letra in "aeiou")

def invertir_lista(lista):
    """ Invierte el orden de los elementos en una lista. """
    return lista[::-1]
