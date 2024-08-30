import complejos

class operaciones(complejos):
    def __init___(self,suma,resta,mult,divi,parteReal,parteImg):
        super().__init__(parteReal)
        super().__init__(parteImg)
        self.suma=suma
        self.resta=resta
        self.mult=mult
        self.divi=divi
    
    def sumarcomplejos(self,a,b,c,d):
        z1=complejos(parteReal=a, parteImg=b)
        z2=complejos(parteReal=c, parteImg=d)

        real=z1.parteReal+z2.parteReal
        img=z1.parteImg+z2.parteImg

        return real, img

    def restarComplejos():
        print()


    #en estas dos secciones usaremos la forma trigonometrica de un complejo
    #dos instancias para poder operar los dos complejos
    def multiplicarComplejos():
        print()
    def DividirComplejos():
        print()
    

