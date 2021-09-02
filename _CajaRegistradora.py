import unittest

# Producto:
class Producto():
    def __init__(self,codigo,nombre):
        self.codigo=codigo
        self.nombre=nombre
    def carga(self,codigo,nombre):
        detalle[nombre] = codigo
    def mostrar(self,codigo,nombre):
        print("\nLos detalles de sus artículos son: ")
        for i in detalle:
            print("Producto '", i, "' con el código => ", detalle[nombre])
        return detalle


# Precio:
class Precio():
    def __init__(self,codigo,precio):
        self.codigo=codigo
        self.precio=precio
    def valor(self,codigo,precio):
        articulos[codigo] = precio
    def mostrar(self,codigo,nombre):
        print("\nSus articulos existentes son: ")
        for i in articulos:
            print("\nCódigo de producto: '", i, "' => $ ", articulos[codigo],"\n")
        return articulos

# Compra:
class Compra():
    def __init__(self):
        pass

    def compras(self,lista):
        if len(lista) > 0:
            caja_2 = True
            total = 0
            while caja_2 == True:
                for clave in lista:
                    print("\nCódigo del producto '", clave, "' Precio es :", lista[clave])
                codigo = input("\nIngrese el código del producto que desea llevar:\n")
                for elemento in lista:
                    if elemento == codigo:
                        print("Usted escogio el código:",  elemento)
                        subtotal = int(lista[elemento])
                        total = total + subtotal
                        print("\nEl arículo: ", elemento, " con un subtotal de $", total)
                        volver = True
                        while volver == True:
                            seguir = input("\nDesea elegir otro articulo SI/NO: ")
                            if seguir.lower() == "si":
                                caja_2 = True
                                volver = False
                            elif seguir.lower() == "no":
                                caja_2 = False
                                volver = False
                                return total
                            else:
                                print("opcion invalida")
                                volver = True
        else:
            print("No hay productos existentes")

# Registradora:
class Registradora():
    def __init__(self):
        pass

    def factura(self,fulltotal):
        caja_2 = True
        while caja_2 == True:
            print("\n Usted puede abonar:")
            print("1)Tarjeta")
            print("2)Efetivo")
            print("\nSeleccione el método de pago:")
            tarjeta = input()
            try:
                if tarjeta.isalpha() == False:
                    if tarjeta == "1":
                        print("\nEl cliente tiene un descuento del 5%")
                        print("El subtotal de la factura es $", fulltotal)
                        des=Registradora()
                        descuento=des.descuento(fulltotal)
                        totaltotal = fulltotal - descuento
                        tot=Registradora()
                        totaltotal = tot.totfin(fulltotal, descuento)
                        #  aqui comienza facturación
                        print("Debe: $ %s" % (fulltotal))
                        print("______________________")
                        nombre_del_cliente = input("Nombre Del Cliente: ")

                        efectivo = int(input("Va abonar con:  "))
                        cam=Registradora()
                        cambio = cam.cambio(efectivo, fulltotal)

                        print("__________________________")
                        print("Precio $\t", fulltotal)
                        print("Total $\t", totaltotal)
                        print("Abono $\t", efectivo)
                        print("__________________________")
                        print("Cambio $", cambio)
                        break

                    elif tarjeta == "2":
                        totaltotal = fulltotal
                        #  aqui comienza facturación
                        print("Debe: $", totaltotal)
                        print("______________________")
                        nombre_del_cliente = input("Nombre Del Cliente: ")
                        efectivo = int(input("Efectivo :  "))
                        cambio = efectivo - totaltotal
                        print("__________________________")
                        print("Precio $\t", fulltotal)
                        print("Total $\t", totaltotal)
                        print("Efectivo $\t", efectivo)
                        print("__________________________")
                        print("Cambio  $ ", cambio)
                        caja_2 = False
                    else:
                        print("Opción no valida")
                else:
                    print("Solo se aceptan numeros")
            except:
                opcion3 = True
            print("Gracias por su compra, Regrese Pronto.")



    def cambio(self, efectivo, fulltotal):
        cambio=efectivo - fulltotal
        return cambio

    def descuento(self, fulltotal):
        des = (fulltotal * 0.05)
        return des

    def totfin(self, fulltotal, descuento):
        tot=fulltotal - descuento
        return tot


def ingreso_productos():
    caja = True
    while caja == True:
        opcion = input("\nDesea ingresar un producto SI/NO: ")
        try:
            if opcion.isalpha() == True:
                if opcion.lower() == "si":
                    producto = input("Ingrese el producto: ")
                    codigo= input("Ingrese el código del producto:")
                    precio= input ("Ingrese el precio del producto:")
                    prod = Producto(codigo,producto)
                    prod.carga(codigo,producto)
                    prec= Precio(codigo, precio)
                    prec.valor(codigo,precio)
                elif opcion.lower() == "no":
                    caja = False
                else:
                    print("Dato erroneo")
            else:
                print("No se reconocen datos numericos")
        except:
            caja = True

    detalle=prod.mostrar(codigo,producto)
    articulos=prec.mostrar(codigo,producto)
    return articulos


def pre_compra(articulos):
    com=Compra()
    subtotal=com.compras(articulos)
    return subtotal

class ProductoDoesNotExist(Exception):
    pass

articulos = {}
fulltotal = 0
detalle = {}


#Test:
class Test(unittest.TestCase):

    def test1_add_product(self):
        prod = Producto('12', 'Pera')
        prod.carga('12', 'Pera')
        prec = Precio('12', '22')
        prec.valor('12', '22')
        self.codigo1= '12'
        self.precio1 = '22'
        articulos[self.codigo1] = self.precio1


    def test2_subtotal(self):
        print(articulos['12'])
        self.assertEqual('22', articulos['12'])

    def test3_cambio(self):
        reg=Registradora()
        reg_2=reg.cambio(100, 90)
        self.assertEqual(10, reg_2)

    def test4_descuento(self):
        reg=Registradora()
        reg_3=reg.descuento(100)
        self.assertEqual(5, reg_3)

    def test5_total(self):
        reg=Registradora()
        reg_4=reg.totfin(100, 5)
        self.assertEqual(95, reg_4)




print("Seleccione")
print("1.) Para cargar los datos y las compras")
print("2.) Para correr test, previo haber corrido la registradora:\n")
test=input()
if test=='2':
    if __name__ == '__main__':
        unittest.main()
else:
    # Inicio Registradora:
    salir = False
    while salir == False:
        print("\nBienvenido a la Caja Registradora")
        print("¿Qué desea realizar?")
        print("1.) Ingresar productos")
        print("2.) Registrar compra")
        print("3.) Abonar compra")
        opmenu = (input("Ingrese el número de Menu: "))
        try:
            if opmenu.isalpha() == False:
                if opmenu == "1":
                    articulos=ingreso_productos()
                    opcionmenu = input("Desea volver al menu SI/NO: ")
                    if opcionmenu.lower() == "si":
                        salir = False
                    else:
                        break
                elif opmenu == "2":
                    fulltotal = pre_compra(articulos)
                    opcionmenu = input("Desea volver al menu SI/NO: ")
                    if opcionmenu.lower() == "si":
                        salir = False
                    else:
                        break
                elif opmenu == "3":
                    facturacion=Registradora()
                    print(facturacion.factura(fulltotal))
                    opcionmenu = input("Desea vover al menu SI/NO: ")
                    if opcionmenu.lower() == "si":
                        salir = False
                    else:
                        break
        except:
            print("Error\n")


