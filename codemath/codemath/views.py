from django.shortcuts import render
from codemath.forms import convertform
from django.http import HttpResponse
from static.programas.conversion import *
from static.programas.ieee import *
from static.programas.bisreg import *
from static.programas.rectangulos import *
from static.programas.trapecios import *

from math import*
# Create your views here.

def index(request):
    return render(request, 'pages/index.html', {})

def tipomatrices(request):
    return render(request, 'pages/matrices.html', {})

def tipomatricesdoc(request):
    return render(request, 'pages/matricesdoc.html', {})

def ejemploPagina(request):
    return render(request, 'pages/ejemplo.html', {})

def conversorNumerico(request):
    if (request.method=='POST'):
        decimal=request.POST['decimal']
        binaria=request.POST['binario']
        octall=request.POST['octal']
        hexadeci=request.POST['hexadecimal']
        if(decimal !=""):
            deci=decimal
            mostrar=Decimalotras()
            enviar=mostrar.decimalToOthers(float(decimal))
            todos=enviar.split("-")
            ant=todos[0].split("b")
            bina=float(ant[1])
            ant1=todos[1].split("o")
            octa=float(ant1[1])
            ant2=todos[2].split("x")
            hexa=ant2[1]
            return render(request,'pages/conversorNumerico.html',{"deci":deci,"bina":bina,"octa":octa,"hexa":hexa} )
        if(binaria !=""):
            bina=binaria
            mostrar=Binariootras()
            enviar=mostrar.binarioToOthers(float(binaria))
            todos=enviar.split("-")
            deci=float(todos[0])
            ant1=todos[1].split("o")
            octa=float(ant1[1])
            ant2=todos[2].split("x")
            hexa=ant2[1]
            return render(request,'pages/conversorNumerico.html',{"deci":deci,"bina":bina,"octa":octa,"hexa":hexa} )
        if(octall !=""):
            octa=octall
            mostrar=Octalotras()
            enviar=mostrar.octalToOthers(float(octall))
            todos=enviar.split("-")
            deci=float(todos[0])
            ant=todos[1].split("b")
            bina=float(ant[1])
            ant2=todos[2].split("x")
            hexa=ant2[1]
            return render(request,'pages/conversorNumerico.html',{"bina":bina,"deci":deci,"octa":octa,"hexa":hexa} )
        if(hexadeci !=""):
            hexa=hexadeci
            mostrar=Hexadecimalotras()
            enviar=mostrar.hexadecimalToOthers(str(hexadeci))
            todos=enviar.split("-")
            deci=float(todos[0])
            ant1=todos[1].split("b")
            bina=float(ant1[1])
            ant2=todos[2].split("o")
            octa=float(ant2[1])
            return render(request,'pages/conversorNumerico.html',{"bina":bina,"octa":octa,"deci":deci,"hexa":hexa} )
    else:
        bina=""
        octa=""
        hexa=""
    return render(request,'pages/conversorNumerico.html',{"bina":bina,"octa":octa,"hexa":hexa} )

def Ieeetd(request):
        if (request.method=='POST'):
            funcion=request.POST['decimal']
            signo=request.POST['signo']
            expon=request.POST['expon']
            mantisa=request.POST['mantisa']
            if(funcion!=""):
                mostrar=Tdbits()
                enviar=mostrar.paso2NormalizarExpDos(float(funcion))
                todos=enviar.split("-")
                sign=float(todos[0])
                exponen=float(todos[1])
                mantis=float(todos[2])
                return render(request,'pages/Ieeetd.html',{"sign":sign,"exponen":exponen,"mantis":mantis} )
            if(signo!="" and expon!="" and mantisa!=""):
                mostrar=Invtdieee()
                enviar=mostrar.convertirElNumerotd(signo,expon,mantisa)
                decima=float(enviar)
                if(signo==1):
                    decima=float(enviar)*-1
                return render(request,'pages/Ieeetd.html',{"dec":decima} )
        else:
            dec=""
            sign=""
            exponen=""
            mantis=""
        return render(request,'pages/Ieeetd.html',{"dec":dec,"sign":sign,"exponen":exponen,"mantis":mantis} )


def Ieeesc(request):
        if (request.method=='POST'):
            funcion=request.POST['decimal']
            signo=request.POST['signo']
            expon=request.POST['expon']
            mantisa=request.POST['mantisa']
            if(funcion!=""):
                mostrar=Scbits()
                enviar=mostrar.paso2NormalizarExpDos(float(funcion))
                todos=enviar.split("-")
                sign=todos[0]
                exponen=todos[1]
                mantis=todos[2]
                return render(request,'pages/Ieeesc.html',{"sign":sign,"exponen":exponen,"mantis":mantis} )
            if(signo!="" and expon!="" and mantisa!=""):
                mostrar=Invscieee()
                enviar=mostrar.convertirElNumerosc(signo,expon,mantisa)
                return render(request,'pages/Ieeesc.html',{"dec":enviar} )
        else:
            dec=""
            sign=""
            exponen=""
            mantis=""
        return render(request,'pages/Ieeesc.html',{"dec":dec,"sign":sign,"exponen":exponen,"mantis":mantis} )

def biseccion(request):
    if (request.method=='POST'):
        recibir=[3]
        cont=0
        final=[]
        funcion=request.POST['funcion']
        a=request.POST['intervaloa']
        b=request.POST['intervalob']
        error=request.POST['Errorr']
        mostrar=Bisec()
        recibir=mostrar.biseccionraiz(funcion,float(a),float(b),float(error))
        for i in recibir:
            tablam=i.split("|")
            final.append(tablam)
        return render(request,'pages/biseccion.html',{"final":final} )
    else:
        enviar=""
    return render(request,'pages/biseccion.html',{"enviar":enviar} )

def reglaFalsa(request):
    if (request.method=='POST'):
        final=[]
        funcion=request.POST['funcion']
        a=request.POST['intervaloa']
        b=request.POST['intervalob']
        error=request.POST['Errorr']
        mostrar=Regla_falsa()
        recibir=mostrar.regla_falsaraiz(funcion,float(a),float(b),float(error))
        for i in recibir:
            tablam=i.split("|")
            final.append(tablam)
        return render(request,'pages/reglafalsa.html',{"final":final} )
    else:
        enviar=""
    return render(request,'pages/reglaFalsa.html',{"enviar":enviar} )

def secante(request):
    if (request.method=='POST'):
        final=[]
        funcion=request.POST['funcion']
        a=request.POST['intervaloa']
        b=request.POST['intervalob']
        error=request.POST['Errorr']
        mostrar=Secantec()
        recibir=mostrar.secantef(funcion,float(a),float(b),float(error))
        for i in recibir:
            tablam=i.split("|")
            final.append(tablam)
        return render(request,'pages/secante.html',{"final":final} )
    else:
        enviar=""
    return render(request,'pages/secante.html',{"enviar":enviar} )

def newtonRaphson(request):
    if (request.method=='POST'):
        funcion=request.POST['funcion']
        a=request.POST['intervaloa']
        error=request.POST['Errorr']
        mostrar=Regla_falsa()
        enviar=mostrar.regla_falsaraiz(funcion,float(a),float(error))
        return render(request,'pages/newtonRaphson.html',{"enviar":enviar} )
    else:
        enviar=""
    return render(request,'pages/newtonRaphson.html',{"enviar":enviar} )

def raicesPolinomio(request):

        if (request.method=='POST'):
            funcion=request.POST['funcion']
            mostrar=Polin()
            enviar=mostrar.raizPolinomios(funcion)
            return render(request,'pages/raicesPolinomio.html',{"enviar":enviar} )
        else:
            enviar=""
        return render(request,'pages/raicesPolinomio.html',{"enviar":enviar} )

def evaluadorf(request):
    if (request.method=='POST'):
        funcion=request.POST['funcion']
        x=request.POST['valorx']
        mostra=Evalu()
        enviar=mostra.evalua(float(x),funcion)
        return render(request,'pages/evaluador.html',{"enviar":enviar} )
    else:
        enviar=""
    return render(request,'pages/evaluador.html',{"enviar":enviar} )

def derivacion(request):
    if (request.method=='POST'):
        funcion=request.POST['funcion']
        x=request.POST['valorx']
        mostra=Deriv()
        enviar=mostra.derivando(float(x),funcion)
        todos=enviar.split("|")
        primera=todos[0]
        print("la primera: "+primera)
        primeraNum=todos[1]
        print("la primera num: "+primeraNum)
        segunda=todos[2]
        print("la segunda: "+segunda)
        segundaNum=todos[3]
        print("la segunda num: "+segundaNum)
        return render(request,'pages/derivacion.html',{"primera":primera,"primeraNum":primeraNum,"segunda":segunda,"segundaNum":segundaNum} )
    else:
        primera=""
        primeraNum=""
        segunda=""
        segundaNum=""
    return render(request,'pages/derivacion.html',{"primera":primera,"primeraNum":primeraNum,"segunda":segunda,"segundaNum":segundaNum} )


def rectangulos(request):
    if (request.method=='POST'):
        funcion=request.POST['funcion']
        a=request.POST['intervaloa']
        b=request.POST['intervalob']
        particiones=request.POST['npart']
        mostrar=Rectangulos()
        enviarIz=mostrar.recIzquierda(funcion,float(a),float(b),int(particiones))
        enviarDe=mostrar.recDerecha(funcion,float(a),float(b),int(particiones))
        enviarMe=mostrar.recMedios(funcion,float(a),float(b),int(particiones))
        return render(request,'pages/rectangulos.html',{"enviarIz":enviarIz,"enviarDe":enviarDe,"enviarMe":enviarMe} )
    else:
        enviarIz=""
        enviarDe=""
        enviarMe=""
    return render(request,'pages/rectangulos.html',{"enviarIz":enviarIz,"enviarDe":enviarDe,"enviarMe":enviarMe} )

def trapecios(request):
    if (request.method=='POST'):
        funcion=request.POST['funcion']
        a=request.POST['intervaloa']
        b=request.POST['intervalob']
        particiones=request.POST['npart']
        mostrar=Trapecios()
        enviar=mostrar.trap(funcion,float(a),float(b),int(particiones))
        return render(request,'pages/trapecios.html',{"enviar":enviar} )
    else:
        enviar=""
    return render(request,'pages/trapecios.html',{"enviar":enviar} )


def simpson13(request):
    if (request.method=='POST'):
        funcion=request.POST['funcion']
        a=request.POST['intervaloa']
        b=request.POST['intervalob']
        particiones=request.POST['npart']
        mostrar=Simp13()
        enviar=mostrar.simpin13(int(particiones),float(a),float(b),funcion)
        return render(request,'pages/simpson13.html',{"enviar":enviar} )
    else:
        enviar=""
    return render(request,'pages/simpson13.html',{"enviar":enviar} )

def simpson38(request):
    if (request.method=='POST'):
        funcion=request.POST['funcion']
        a=request.POST['intervaloa']
        b=request.POST['intervalob']
        particiones=request.POST['npart']
        mostrar=Simp13()
        enviar=mostrar.simpin13(int(particiones),float(a),float(b),funcion)
        return render(request,'pages/simpson38.html',{"enviar":enviar} )
    else:
        enviar=""
    return render(request,'pages/simpson38.html',{"enviar":enviar} )

def montecarlo(request):
    return render(request, 'pages/montecarlo.html',{})

def ecuaciones(request):
    return render(request,'pages/ecuaciones.html',{} )
    #return HttpResponse("donde estoy")
def integrales(request):
    return render(request,'pages/integrales.html',{} )

def matricessuma(request):
    return render(request,'pages/matricessuma.html',{} )

def productomatrices(request):
    return render(request,'pages/productomatrices.html',{} )

def productoescalar(request):
    return render(request,'pages/productoescalar.html',{} )

def matrizinversa(request):
    return render(request,'pages/matrizinversa.html',{} )

def matrizdeter(request):
    return render(request,'pages/matrizdeter.html',{} )

def matriztrans(request):
    return render(request,'pages/matriztrans.html',{} )

def gaussjordan(request):
    return render(request,'pages/gaussjordan.html',{} )
