import math
from complejos import Complejos
class Operaciones(Complejos):

    def __init__(self, parteReal, parteImg):
        super().__init__(parteReal, parteImg)
    #ingresa 4 datos que se combierten 

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
    def multiplicarComplejos(self, a, b, c, d):
        z1 = Complejos(a, b)
        z2 = Complejos(c, d)

        #calculamos los argumentos de los numeros complejos
        arg1=math.radians(z1.forma_trigonometrica())#asociado con z1
        arg2=math.radians(z2.forma_trigonometrica())#asociado con z2
        
        #calculamos los modulos de cada complejo 
        modulo_1=math.sqrt(z1.parteReal**2+z1.parteImg**2)#asociado con z1
        modulo_2=math.sqrt(z2.parteReal**2+z2.parteImg**2)

        modulo_resultado=modulo_1*modulo_2
        arg_resultante=arg1+arg2

        return modulo_resultado , arg_resultante
        

    def DividirComplejos():
        pass


    def raices_complejos(self,a, b, n):
        #aqui van las raices complejas
        #aqui van los argumentos de cada complejos
        z1 = Complejos(a, b)
        modulo=math.sqrt(z1.parteReal**2+z1.parteImg**2)
        arg=math.radians(z1.forma_trigonometrica())
        lista_argumentos=[]
       #obtenemos el valor de deel agumento interno 
        for i in range(0,n):
            argumento_complejo= (arg+ (2*math.pi)*i)/n
            lista_argumentos.append(argumento_complejo)

        raiz_enecima_modulo=pow(modulo,1/n)

        return raiz_enecima_modulo , lista_argumentos
    
    
    def potencia(self,a,b,e):
        z1=Complejos(a,b)
        modulo_z1=math.sqrt(z1.parteReal**2+z1.parteImg**2)
        argument_z1=math.radians(z1.forma_trigonometrica())
        exp_z1_mod=e*modulo_z1
        exp_z1_arg=e*argument_z1

        return exp_z1_mod, exp_z1_arg

      
oper = Operaciones(parteReal=0, parteImg=0)
print(oper.sumar_complejos(2, 3, 4, 5))
