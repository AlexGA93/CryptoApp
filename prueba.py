# https://www.geeksforgeeks.org/modulo-2-binary-division/


def polynomial(d):  # pasando cadena de numeros(indices del polinomio)---> d="  10"
    # interpreta la base del poliniomio
    base = int(d[0])  # 4-->base = 5
    # print(base)
    # cadena vacia
    binario = ""
    i = 0
    for j in range(base, -1, -1):  # para tantas iteraciones como indices del poliniomio
        # print(j)
        if j == int(d[i]):
            binario += "1"
            i += 1
        else:
            binario += "0"
    #print('binario: '+binario)
    return binario


def xorFunc(trama, pol):
    # inicializamos el resultado
    resul = []

    # recorremos cada elemento de la longitud de pol
    # print(trama)
    # print(pol)
    for i in range(0, len(pol)-1):
        print(i)

        # si los elementos coinciden metemos en el resultado un  0. En caso contrario un 1
        if trama[i] == pol[i]:
            resul.append('0')
        else:
            resul.append('1')
    # devolvemos la lista convertida en cadena
    return ''.join(resul)


def modDivFunc(dividendo, divisor):  # Habiendo juntado la trama con el residuo
    # extraemos las longitudes de los argumentos
    long_trama = len(dividendo)
    long_pol = len(divisor)
    # cojemos la primera parte de tantos bits de dividendo como tantos forman divisor

    tmp = dividendo[0: long_pol]
    # print(tmp)

    # mientreas que [longitud de divisor] < [longitud del dividendo]
    while long_pol < long_trama:
        # si el primer elemento de tmp es 0 o 1
        if tmp[0] == '1':
            # reemplazamos el numero del dividendo por el proceso XOR y la ultima parte para la proxima iteracion
            # a;adimos el bit siguiente
            tmp = xorFunc(tmp, divisor) + dividendo[long_pol]

        else:  # si es 0
            tmp = xorFunc(tmp, '0'*long_pol)+dividendo[long_pol]

        long_pol += 1

    # Pra los ultimos bits
    if tmp[0] == '1':
        tmp = xorFunc(tmp, divisor)
    else:
        tmp = xorFunc('0'*long_pol, tmp)

    return tmp


def CRC(trama, pol):
    # longitud del polinomio
    long = len(pol)
    # a;adimos a la derecha de la trama tantos 0 como longitud tiene el polinomio
    adjunto = trama + '0'*(long-1)

    datoFinal = modDivFunc(adjunto, pol)
    return datoFinal


d = "320"
trama = "Hola"  # queremos pasar esto a binario

#trama_bin = ''.join(format(ord(x), 'b')for x in trama)
trama_bin = "111101"
polinomio = polynomial(d)

final_data = CRC(trama_bin, polinomio)
