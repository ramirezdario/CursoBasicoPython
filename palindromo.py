def palindromo(palabra):
    palabra = palabra.replace(' ', '') #eliminar espacios
    palabra = palabra.lower() #pasar a minusculas
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra) #recupera verdadero o falso
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()