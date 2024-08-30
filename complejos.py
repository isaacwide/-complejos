import math

class complejos:
 
    def __init__(self,parteReal,parteImg):
        super().__init__()
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
  
    def raices_complejos(self, n):
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

    

numer=complejos(parteReal=2, parteImg=2)

print(numer.forma_trigonometrica())

# Obtener las raíces complejas
print(numer.raices_complejos(3))
