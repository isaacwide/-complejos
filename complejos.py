import math

class Complejos:
 
    def __init__(self,parteReal,parteImg):
        self.parteReal=parteReal
        self.parteImg=parteImg
        
    #forma trigonometrica de un complejo 
    def forma_trigonometrica(self):
        #inicio de los if para transformar el complejo en su forma trigonnometrica 
        #if del primer cuadrante 
        if(self.parteReal>0 and self.parteImg >=0):
            theta=math.atan(self.parteImg/self.parteReal)
            aux=math.degrees(theta)
            argumento=aux
        #if del segundo cuadrante 
        elif(self.parteReal < 0 and self.parteImg >= 0):
             theta=math.atan(self.parteImg/self.parteReal)
             argumento=math.degrees(math.pi-(theta*-1)) 
        #if del tercer cuandrate 
        elif(self.parteReal < 0 and self.parteImg <=0 ):
            theta=math.atan(self.parteImg/self.parteReal)
            argumento=math.degrees(math.pi+theta)
        # if cuarto cudranrte
        elif(self.parteReal> 0 and self.parteImg <= 0):
                theta=math.atan(self.parteImg/self.parteReal)
                argumento=math.degrees(((2*math.pi)-(theta*-1)))
        #een caso de que la parte real sea cero
        elif(self.parteReal==0):
                  if(self.parteImg>0):
                       argumento=math.degrees((math.pi)/2)
                  else:
                       argumento=math.degrees(math.pi)
        elif(self.parteReal==0 and self.parteImg==0):
             print("retorno al inicio")               
        return argumento   

    def forma_polar(self):
         pass
  
    
numer=Complejos(parteReal=2, parteImg=2)
print(numer.parteReal)
#argumento del complejo
print(numer.forma_trigonometrica())
