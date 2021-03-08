from sympy import Derivative, diff, simplify,Symbol
x=Symbol('x')
y=Symbol('y')

fxy = x*2*y+x*2*y*2+x+y-3
dx=simplify(diff(fxy, x))
dy = Derivative(fxy, y).doit()


simplify(dy)
print (dx)
print (dy)
from sympy import Derivative, diff, simplify,Symbol
x=Symbol('x')
y=Symbol('y')

fxy = x*2*y+x*y*2+x+y-3
dx=simplify(diff(fxy, x))
dy = Derivative(fxy, y).doit()

simplify(dy)
print (dx)
print (dy)

fx1=simplify(diff(dx, x))
fx2=simplify(diff(dy, x))
fy1=simplify(diff(dx, y))
fy2=simplify(diff(dy, y))
print (fx1)
print (fx2)
print (fy1)
print (fy2)

fs1=dx.subs(x, 1)
fs11=fs1.subs(y, 1)
print (fs11)

A=int(input( "ingrese la formula: \n"))
fs1=dx.subs(x, 1)
fs11=fs1.subs(y, 1)
print (fs11)