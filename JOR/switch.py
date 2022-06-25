# Un usuario nos da el número del mes y lo pasamos a letra- utilizando diccionarios.

def dameMes(num):
    meses = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio',
             8: 'Agosto', 9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'}
    return meses.get(num, 'Inserte un número del 1 al 12')


numeroMes = int(input('Inserte el número del mes \n'))
print(dameMes(numeroMes))
