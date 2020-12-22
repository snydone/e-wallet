import requests
from datetime import date, datetime
from colorama import init,Fore,Back,Style
from io import open

#variable btc
btc_archivo=open("btc.txt")
for v in btc_archivo.readlines():
    valor1=float(v)
btc=valor1

#variable eth
eth_archivo=open("eth.txt")
for v in eth_archivo.readlines():
    valor2=float(v)
eth=valor2

#variable ltc
ltc_archivo=open("ltc.txt")
for v in ltc_archivo.readlines():
    valor3=float(v)
ltc=valor3


#funcion operacion
#enviar
def enviar_btc():
    monto_btc=float(input("monto="))
    while monto_btc>btc:
        print("saldo insuficiente")
        monto_btc=float(input("monto="))
    else:
        print("indique el ID de la Persona a enviar ")
        ID_env=input(":")

        if ID_env in registrados():
            moneda_btc=btc-monto_btc
            btc_archivo=open("btc.txt","w")
            btc_archivo.write(str(moneda_btc))
            btc_archivo.close()
            historial_archivo=open("fecha_env.txt","a")
            historial_archivo.write("ID: ")
            historial_archivo.write(ID_env)
            historial_archivo.write(" ")
            historial_archivo.write(str(monto_btc))
            historial_archivo.write("btc  ")
            historial_archivo.write(fecha())
            historial_archivo.write("\n")
            historial_archivo.close
            print("envio exitoso")
        else:
            print("ID no regregistrado")
            print("por favor vaya al menu (registrar) y registre el ID ")
            pass

def enviar_eth():
    monto_eth=float(input("monto="))
    while monto_eth>eth:
        print("saldo insuficiente")
        monto_eth=float(input("monto="))
    else:
        print("indique el ID de la Persona a enviar ")
        ID_env=input(":")

        if ID_env in registrados():
            moneda_eth=eth-monto_eth
            eth_archivo=open("eth.txt","w")
            eth_archivo.write(str(moneda_eth))
            eth_archivo.close()
            historial_archivo=open("fecha_env.txt","a")
            historial_archivo.write("ID: ")
            historial_archivo.write(ID_env)
            historial_archivo.write(" ")
            historial_archivo.write(str(monto_eth))
            historial_archivo.write("eth  ")
            historial_archivo.write(fecha())
            historial_archivo.write("\n")
            historial_archivo.close
            print("envio exitoso")
        else:
            print("ID no regregistrado")
            print("por favor vaya al menu (registrar) y registre el ID ")
            pass

def enviar_ltc():
    monto_ltc=float(input("monto="))
    while monto_ltc>ltc:
        print("saldo insuficiente")
        monto_ltc=float(input("monto="))
    else:
        print("indique el ID de la Persona a enviar ")
        ID_env=input(":")

        if ID_env in registrados():
            moneda_ltc=ltc-monto_ltc
            ltc_archivo=open("ltc.txt","w")
            ltc_archivo.write(str(moneda_ltc))
            ltc_archivo.close()
            historial_archivo=open("fecha_env.txt","a")
            historial_archivo.write("ID: ")
            historial_archivo.write(ID_env)
            historial_archivo.write(" ")
            historial_archivo.write(str(monto_ltc))
            historial_archivo.write("ltc  ")
            historial_archivo.write(fecha())
            historial_archivo.write("\n")
            historial_archivo.close
            print("envio exitoso")
        else:
            print("ID no regregistrado")
            print("por favor vaya al menu (registrar) y registre el ID ")
            pass

#recibir
def recibir_btc():
    monto_btc=float(input("monto="))
    while monto_btc<=0:
        print("monto invalido")
        monto_btc=float(input("monto="))
    else:
        print("indique el ID de la Persona de quien recibe ")
        ID_env=input(":")

        if ID_env in registrados():
            moneda_btc=btc+monto_btc
            btc_archivo=open("btc.txt","w")
            btc_archivo.write(str(moneda_btc))
            btc_archivo.close()
            historial_arc=open("fecha_rec.txt","a")
            historial_arc.write("ID: ")
            historial_arc.write(ID_env)
            historial_arc.write(" ")
            historial_arc.write(str(monto_btc))
            historial_arc.write("btc  ")
            historial_arc.write(fecha())
            historial_arc.write("\n")
            historial_arc.close
            print("operacion realizada con exito")
        else:
            print("ID no regregistrado")
            print("por favor vaya al menu (registrar) y registre el ID ")
            pass

def recibir_eth():
    monto_eth=float(input("monto="))
    while monto_eth<=0:
            print("monto invalido")
            monto_eth=float(input("monto="))
    else:
        print("indique el ID de la Persona a enviar ")
        ID_env=input(":")

        if ID_env in registrados():
            moneda_eth=eth+monto_eth
            eth_archivo=open("eth.txt","w")
            eth_archivo.write(str(moneda_eth))
            eth_archivo.close()
            historial_arc=open("fecha_rec.txt","a")
            historial_arc.write("ID: ")
            historial_arc.write(ID_env)
            historial_arc.write(" ")
            historial_arc.write(str(monto_eth))
            historial_arc.write("eth  ")
            historial_arc.write(fecha())
            historial_arc.write("\n")
            historial_arc.close
            print("operacion realizada con exito")
        else:
            print("ID no regregistrado")
            print("por favor vaya al menu (registrar) y registre el ID ")
            pass

def recibir_ltc():
    monto_ltc=float(input("monto="))
    while monto_ltc<=0:
        print("monto invalido")
        monto_ltc=float(input("monto="))
    else:
        print("indique el ID de la Persona a enviar ")
        ID_env=input(":")

        if ID_env in registrados():
            moneda_ltc=ltc+monto_ltc
            ltc_archivo=open("ltc.txt","w")
            ltc_archivo.write(str(moneda_ltc))
            ltc_archivo.close()
            historial_arc=open("fecha_rec.txt","a")
            historial_arc.write("ID: ")
            historial_arc.write(ID_env)
            historial_arc.write(" ")
            historial_arc.write(str(monto_ltc))
            historial_arc.write("ltc  ")
            historial_arc.write(fecha())
            historial_arc.write("\n")
            historial_arc.close
            print("operacion realizada con exito")
        else:
            print("ID no regregistrado")
            print("por favor vaya al menu (registrar) y registre el ID ")
            pass

#funcion regi
def registrados():
    registro=open("registro.txt")
    return registro.read()
    registro.close()

def registrar():
    registro=open("registro.txt","a")
    ID_reg=input("ingrese el ID: ")
    print("registro realizado")
    registro.write(ID_reg)
    registro.write("\n")
    registro.close()

def leer_regi():
    registro=open("registro.txt")
    print(registro.read())
    registro.close()


#funcion de cotizacion
def valor_BTC():
    _ENDPOINT = "https://api.binance.com"
    def _url(api):
        return _ENDPOINT+api
    def get_price(cripto):
        return requests.get(_url("/api/v3/ticker/price?symbol="+cripto))
    moneda="BTC"
    data = get_price(moneda+"USDT").json()
    return data.get("price")

def valor_ETH():
    _ENDPOINT = "https://api.binance.com"
    def _url(api):
        return _ENDPOINT+api
    def get_price(cripto):
        return requests.get(_url("/api/v3/ticker/price?symbol="+cripto))
    moneda="ETH"
    data = get_price(moneda+"USDT").json()
    return data.get("price")
    

def valor_LTC():
    _ENDPOINT = "https://api.binance.com"
    def _url(api):
        return _ENDPOINT+api
    def get_price(cripto):
        return requests.get(_url("/api/v3/ticker/price?symbol="+cripto))
    moneda="LTC"
    data = get_price(moneda+"USDT").json()
    return data.get("price")

#funcion   dolar
def dolar_BTC():
    Data=float(valor_BTC())
    btc_usd=btc*Data
    return btc_usd
    
def dolar_ETH():
    Data=float(valor_ETH())
    eth_usd=eth*Data
    return eth_usd

def dolar_LTC():
    Data=float(valor_LTC())
    ltc_usd=ltc*Data
    return ltc_usd

#funcion balance general
def balance_general():
    balance=dolar_BTC()+dolar_ETH()+dolar_LTC()
    return balance

#funcion datetime
def fecha():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

#inicio
init(convert=True)
print(Fore.YELLOW,Back.BLUE,"CRP-Wallet")
print(Style.RESET_ALL)
print(Fore.YELLOW,"Maneje su billetera a placer")
print(Fore.WHITE,"ENVIE  RICIBA  CONSULTE")
print(Style.RESET_ALL)
print(Fore.BLUE,"sea parte de La mejor E-Wallet ")
print(Style.RESET_ALL)
print(fecha())
print()
print("BTC:",valor_BTC(),"usd"," LTC:",valor_LTC(),"usd"," ETH:",valor_ETH(),"usd")
print(Style.RESET_ALL)
print()

#Pedimos que ingrese su ID (python), que sera el encerrado entre parentesis

ID=input("ID:")
while not ID=="python":
    print("ID incorrecto")
    ID=input("ID: ")
    print()
else:
    print("bienvenido")
    print()
    pass

print("Menu")
opcion=0

while opcion!=6:
    print("1)consulta\n2)enviar\n3)recibir\n4)registrar\n5)historial\n6)salir")
    print("elija el numero de la operacion a realiza ejem:1,2,3,4,5 ")
    opcion=input(":")

    if opcion=="1":
        print("Datos Personale")
        print("ID: python  Edad: 27  DNI: 20771730")
        print()
        print("Saldo ")
        print()
        print("BTC="+str(btc)+" --> "+str(dolar_BTC())+" USD")
        print("ETH="+str(eth)+" --> "+str(dolar_ETH())+" USD")
        print("LTC="+str(ltc)+" --> "+str(dolar_LTC())+" USD")
        print()
        print("Total",str(balance_general())+" USD")
        print()

    elif opcion=="2":
        print("1)enviar ")
        print("indique el nombre de la moneda a enviar en mayus: BTC LTC ETH")
        op_moneda=input(":")

        if op_moneda=="BTC":
                print("monto a enviar")
                enviar_btc()
                    
        elif op_moneda=="LTC":
                print("Monto a enviar")
                enviar_ltc()

        elif op_moneda=="ETH":
                print("Monto a enviar")
                enviar_eth()
        else:
            print("opcion invalida")
            print("vuelve a entrar")
            pass
        

    elif opcion=="3":
        print("recibir")
        print("indique el nombre de la moneda que va a recibir en mayus: BTC LTC ETH")
        op_recibir=input(":")

        if op_recibir=="BTC":
            print("monto a Recibir:")
            recibir_btc()
            print()
                    
        elif op_recibir=="LTC":
            print("Monto a Recibir")
            recibir_ltc()
            print()

        elif op_recibir=="ETH":
            print("Monto a Recibir")
            recibir_eth()
            print()
        else:
            print("opcion invalida")
            print("vuelve a entrar")
            pass

    elif opcion=="4":
        print("1)Registrar un ID\n2)Mostrar ID registrados")
        op_reg=input("elija  una opcion: ")

        if op_reg=="1":
            print("registre solo un ID ")
            registrar() 

        elif op_reg=="2":
            leer_regi()

    elif opcion=="5":
        print("1)Mostrar Historial de envio\n2)Mostrar Historial de recibido")
        op_his=input("elija una opcion: ")
        if op_his=="1":
            historial_archivo=open("fecha_env.txt")
            print(historial_archivo.read())
            historial_archivo.close  
        elif op_his=="2":
            historial_arc=open("fecha_rec.txt") 
            print(historial_arc.read())
            historial_arc.close    

    elif opcion=="6":
        print("Gracias por usar nuestra aplicacion")
        break

    else:
        print("opcion invalida")



