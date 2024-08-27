import math
#hola mundo omo estamos todos
class complejos:
    partReal=0
    parteImg=0


    def __init__(self,modulo,argumento):
        self.modulo=modulo
        self.argumeto=argumento
        
    #forma trigonometrica de un complejo 
    def forma_trigonometrica(parteReal,parteImg):
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
    def raices_complejos():
        #aqui van las raices complejas
        print("hola mundo")