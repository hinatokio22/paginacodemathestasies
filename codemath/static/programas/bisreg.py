from math import*
#from sympy.solvers import solve
from sympy import *
#from pylab import *
#from numpy import *


class Bisec:

    def __init__(self):
        return

    def funcion_evaluada(self,x,funcion):
        return eval(funcion)

    def biseccionraiz(self,funcion,a,b,errort):
        arregloEnviar=[]
        m=Bisec()
        if (m.funcion_evaluada(float(a),funcion)>0 and m.funcion_evaluada(float(b),funcion) <0) or (m.funcion_evaluada(float(a),funcion)<0 and m.funcion_evaluada(float(b),funcion)>0):
            raiz=a
            cont=0
            merr=[]
            merr.insert(0,0)
            error=1
            i=0
            numeroItEnviar=""
            raizEnviar=""
            errorEnviar=""
            while abs(error)>errort and cont<=100:
                raiz=(a+b)/2

                merr.append(raiz)
                if m.funcion_evaluada(float(a),funcion)*m.funcion_evaluada(float(raiz),funcion)<0:
                    b=raiz
                else:
                    a=raiz
                cont=cont+1
                i=i+1
                error=(merr[i]-merr[i-1])/merr[i]
                print(str(cont)+","+str(raiz))
                print("Error: ",abs(error))
                lineaa=(str(cont)+"|"+str(raiz)+"|"+str(error))
                arregloEnviar.append(lineaa)
            return arregloEnviar
        else:
            return 'no es menor que 0 no toca el eje x no hay raiz '


        """     numeroItEnviar=numeroItEnviar+str(cont)+"|"
                raizEnviar=raizEnviar+str(raiz)+"|"
                errorEnviar=errorEnviar+str(error)+"|"
            arregloEnviar.append(numeroItEnviar)
            arregloEnviar.append(raizEnviar)
            arregloEnviar.append(errorEnviar)"""
class Regla_falsa:

    def __init__(self):
        return

    def funcion_evaluada(self,x,funcion):
        return eval(funcion)

    def regla_falsaraiz(self,funcion,lim1,lim2,errort):
        arregloEnviar=[]
        cont=0
        raiz=0
        merr=[]
        merr.insert(0,0)
        error=1
        i=0
        m=Bisec()
        while cont<=100 and abs(error)>errort:
            if m.funcion_evaluada(float(lim1),funcion) * m.funcion_evaluada(float(lim2),funcion) < 0 :
                raiz = lim2 - (m.funcion_evaluada(float(lim2),funcion) * (lim2-lim1)) / (m.funcion_evaluada(float(lim2),funcion) - m.funcion_evaluada(float(lim1),funcion))
                merr.append(raiz)
                if m.funcion_evaluada(float(lim1),funcion) * m.funcion_evaluada(float(raiz),funcion) < 0:
                    lim2 = raiz
                else:
                    lim1 = raiz
                cont=cont+1
                i=i+1
                error=(merr[i]-merr[i-1])/merr[i]
                lineaa=(str(cont)+"|"+str(raiz)+"|"+str(error))
                arregloEnviar.append(lineaa)
            else:
                return 'no es menor que 0 no toca el eje x no hay raiz'
        return arregloEnviar

class Secantec:

    def __init__(self):
        return

    def f(self,x,funcion):
        return eval(funcion)


    def secantef(self,funcion,x1,x0,error):
         arregloEnviar=[]
         itera=0
         i=0
         raiz=[]
         raiz.insert(0,0)
         erro=1
         m=Secantec()
         while(i<=100 and abs(erro)>error):
             x2=x1-(m.f(x1,funcion)*(x1-x0))/(m.f(x1,funcion)-m.f(x0,funcion))
             raiz.append(x2)
             x0=x1
             x1=x2
             itera=itera+1
             i=i+1
             erro=(raiz[i]-raiz[i-1])/raiz[i]
             lineaa=(str(itera)+"|"+str(x2)+"|"+str(abs(erro)))
             arregloEnviar.append(lineaa)
         return arregloEnviar

class Polin:

    def __init__(self):
        return

    def raizPolinomios(self,funcion):
        x=Symbol('x')
        raices=solve(funcion,x)
        return raices

class Evalu:
    def __init__(self):
        return

    def funcion_evaluada(self,x,funcion):
        return eval(funcion)

    def evalua(self,x,funcion):
        m=Evalu()
        res=m.funcion_evaluada(x,funcion)
        return res

class Deriv:
    def __init__(self):
        return

    def funcion_evaluada(self,x,funcion):
        return eval(funcion)

    def derivada(self,fun):
        return diff(fun)

    def derivando(self,x,funcion):
        m=Deriv()
        primera=str(m.derivada(funcion))
        acumulado=primera
        res=m.funcion_evaluada(x,primera)
        acumulado=str(acumulado+"|"+str(res))
        segunda=str(m.derivada(primera))
        acumulado=str(acumulado+"|"+segunda)
        resdos=m.funcion_evaluada(x,segunda)
        acumulado=str(acumulado+"|"+str(resdos))
        return acumulado

class Simp13:

    def __init__(self):
        return

    def fx(self,x, f):
        return eval(f)

    def simpin13(self,n, a, b, f):
        m=Simp13()
        h = (b - a) / n
        suma = 0.0
        for i in range(1, n):
            x = a + i * h
            if(i % 2 == 0):
                suma = suma + 2 * m.fx(x, f)
            else:
                suma = suma + 4 * m.fx(x, f)
        suma = suma + m.fx(a, f) + m.fx(b, f)
        rest = suma * (h / 3)
        return (rest)
