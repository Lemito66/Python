class Vector(object):
    
    def __init__ (self, x, y,z):
        self.x = x
        self.y = y
        self.z=z   
    def __repr__ (self):
        
        return '(%f, %f,%f)' % (self.x, self.y,self.z)

    def __mul__ (self, v):       #sobrecarga de multiplicacion 
        return Vector (self.x *v.x, self.y *v.y, self.z*v.z)
    def productoEscalar(self):
        resultado= self.x+self.y+self.z
        return resultado  
    def segundoTermino(self,A):
        return Vector (self.x *A, self.y *A, self.z*A)
    def __sub__ (self, v): #robrecarga resta
        
        return Vector (self.x - v.x, self.y - v.y,self.z-v.z)


vectorIncidencia = Vector(1, 0,-1)
vectoNormal = Vector(0, 0,1)
# z = Vector(4,5,2)

resultadoProductEs= (vectorIncidencia*vectoNormal)
productoEscalar=Vector.productoEscalar(resultadoProductEs)
#print(productoEscalar)
A=productoEscalar*2
segundoTermino=Vector.segundoTermino(vectoNormal,A)
formula=(vectorIncidencia-segundoTermino)
print("El resultado es "  ,formula)
# print(productoEscalar)