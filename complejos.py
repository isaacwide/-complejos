import math

class complejos:
 
    def __init__(self,modulo,argumento,parteReal,parteImg):
        self.modulo=modulo
        self.argumeto=argumento
        self.parteReal=parteReal
        self.parteImg=parteImg
        
    #forma trigonometrica de un complejo 
    def forma_trigonometrica(self, parteReal, parteImg):
        #se le asignara uno pa no tener una division pot cero 
        if(parteReal== 0 ):
             parteReal=1
        #inicio de los if para transformar el complejo en su forma trigonnometrica 
        #if del primer cuadrante 
        if(parteReal>=0 and parteImg >=0):

            if(parteReal==0):
                theta=(math.pi/2)
                argumento=math.degrees(theta)
            else:
                theta=math.atan(parteImg/parteReal)
                aux=math.degrees(theta)
                argumento=aux
        #if del segundo cuadrante 
        if(parteReal <= 0 and parteImg>= 0):
             theta=math.atan(parteImg/parteReal)
             argumento=math.degrees(math.pi-(theta*-1))
        
        #if del tercer cuandrate 
        if(parteReal<=0 and parteImg<=0 ):
            theta=math.atan(parteImg/parteReal)
            argumento=math.degrees(math.pi+theta)
        # del tercer cudranrte
        if(parteReal >= 0 and parteImg <= 0):
            if(parteReal== 1 ):
                theta=(math.pi/2)
                argumento=math.degrees((2*math.pi)-theta)
                
            else:
                theta=math.atan(parteImg/parteReal)
                argumento=math.degrees(((2*math.pi)-(theta*-1)))
        return argumento   
  
    def raices_complejos(self, parteReal, parteImg, n):
        #aqui van las raices complejas
        #aqui van los argumentos de cada complejos
        modulo=math.sqrt(parteReal**2+parteImg**2)
        arg=math.radians(self.forma_trigonometrica(parteReal, parteImg))
        lista_argumentos=[]
       #obtenemos el valor de deel agumento interno 
        for i in range(0,n-1):
            argumento_complejo= (arg+ (2*math.pi)*i)/n
            lista_argumentos.append(argumento_complejo)

        raiz_enecima_modulo=pow(modulo,1/n)

        return raiz_enecima_modulo , lista_argumentos

    
num=complejos.forma_trigonometrica(2,2)
num3,ew=complejos.raices_complejos(2,2,5)

print(num)
        