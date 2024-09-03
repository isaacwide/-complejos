import math
from complejos import Complejos
class Operaciones(Complejos):

    def __init__(self, parteReal, parteImg):
        super().__init__(parteReal, parteImg)

    def sumar_complejos(self, a, b, c, d):
        z1 = Complejos(a, b)
        z2 = Complejos(c, d)
        real = z1.parteReal + z2.parteReal
        img = z1.parteImg + z2.parteImg
        return real, img
    
    def restarComplejos(self, a, b, c, d):
        z1 = Complejos(a, b)
        z2 = Complejos(c, d)
        real = z1.parteReal - z2.parteReal
        img = z1.parteImg - z2.parteImg
        return real, img


    #en estas dos secciones usaremos la forma trigonometrica de un complejo
    #dos instancias para poder operar los dos complejos
    def multiplicarComplejos():
        print()
    def DividirComplejos():
        pass

    def raices_complejos(self,a, b, c, d, n):
        #aqui van las raices complejas
        #aqui van los argumentos de cada complejos
        modulo=math.sqrt(self.parteReal**2+self.parteImg**2)
        arg=math.radians(self.forma_trigonometrica())
        lista_argumentos=[]
       #obtenemos el valor de deel agumento interno 
        for i in range(0,n):
            argumento_complejo= (arg+ (2*math.pi)*i)/n
            lista_argumentos.append(argumento_complejo)

        raiz_enecima_modulo=pow(modulo,1/n)

        return raiz_enecima_modulo , lista_argumentos
    def potencia():
        pass
oper = Operaciones(parteReal=0, parteImg=0)
print(oper.sumar_complejos(2, 3, 4, 5))
