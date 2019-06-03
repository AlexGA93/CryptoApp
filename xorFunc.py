def merchecojonesnoayudas(trama, pol):
    # recorro pol
    i = 0
    trama_nueva = ""
    for g in pol:
        if g == trama[i]:
            trama_nueva += "0"
        else:
            trama_nueva += "1"
    # 0010
    lista = [" "]*len(trama_nueva)
    if len(trama_nueva) == len(pol):  # siempre y cuando las dimensiones sean iguales
        for i in range(len(trama_nueva)):  # recorro CADENA
            print(i)  # indice
            if trama_nueva[i] == '1':  # si el elemento es 1
                # lo insertamos en el primer elemento de la lista
                lista.insert(0, trama_nueva[i])

                # COMO COJONES HAG PARA METER EL RESTO DE LA CADENA EN LA LISTA A PARTIR DE AQUI????


trama = "111101000"
pol = "1101"
data = merchecojonesnoayudas(trama, pol)
#print("data: ", data)

# print(data)
