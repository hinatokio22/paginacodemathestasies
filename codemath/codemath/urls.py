from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ejemplo/', views.ejemploPagina, name ="ejemplo"),
    url(r'^ejemplo', views.ejemploPagina, name ="ejemplo"),
    url(r'^matricesdoc/', views.tipomatricesdoc, name ="tipomatricesdoc"),
    url(r'^tipomatrices', views.tipomatrices, name ="tipomatrices"),
    url(r'^conversorNumerico/', views.conversorNumerico, name ="conversorNumerico"),
    url(r'^Ieeetd/', views.Ieeetd, name="Ieeetd"),
    url(r'^Ieeesc/', views.Ieeesc, name="Ieeesc"),
    url(r'^biseccion/', views.biseccion, name="biseccion"),
    url(r'^reglaFalsa/', views.reglaFalsa, name="reglaFalsa"),
    url(r'^secante/', views.secante, name="secante"),
    url(r'^newtonRaphson/', views.newtonRaphson, name="newtonRaphson"),
    url(r'^raicesPolinomio/', views.raicesPolinomio, name="raicesPolinomio"),
    url(r'^evaluadorf/', views.evaluadorf, name="evaluadorf"),
    url(r'^derivacion/', views.derivacion, name="derivacion"),
    url(r'^rectangulos/', views.rectangulos, name="rectangulos"),
    url(r'^trapecios/', views.trapecios, name="trapecios"),
    url(r'^simpson13/', views.simpson13, name="simpson13"),
    url(r'^simpson38/', views.simpson38, name="simpson38"),
    url(r'^montecarlo/', views.montecarlo, name="montecarlo"),
    url(r'^matricessuma/', views.matricessuma, name="matricessuma"),
    url(r'^productomatrices/', views.productomatrices, name="productomatrices"),
    url(r'^productoescalar/', views.productoescalar, name="productoescalar"),
    url(r'^matrizinversa/', views.matrizinversa, name="matrizinversa"),
    url(r'^matriztrans/', views.matriztrans, name="matriztrans"),
    url(r'^matrizdeter/', views.matrizdeter, name="matrizdeter"),
    url(r'^gaussjordan/', views.gaussjordan, name="gaussjordan"),
    url(r'', views.index, name="index"),
]
