function crearTabla(){
	var fil = document.getElementById("selectFilas");
	var valor = fil.selectedIndex;
	var filA =  fil.options[valor].text;
	alert(filA);
	var col = document.getElementById("selectColumnas");
	var valorB = col.selectedIndex;
	var colA = col.options[valorB].text;
	var filB = filA;
	var colB = colA;
	c=new String();
  e=document.getElementById('divMatrices');
  c+='<table style="margin-left:40%" name"tblMatrices" id="tblMatrices" border=1>';
  c+='<tr>';

  c+='<td align="center" valing="middle">';
  c+='<table name="tblMtzA">';
  for ( i = 0; i < filA; i++) {
      c+='<tr>';
      for ( j = 0; j < colA; j++) {
          c+='<td><input type="text" size="1" maxlength="2"/></td>';
      }
      c+='</tr>';
  }
  c+='</table>';
  c+='</td>';
	c+='</tr>';
  c+='</table>';
	c+='<br><br>';

	c+='<table style="margin-left:40%" name"tblMatrices2" id="tblMatrices2" border=1>';
  c+='<tr>';
  c+='<td align="center" valign="middle">';
  c+='<table  name="tblMtzB">';
  for ( i = 0; i < filB; i++) {
      c+='<tr>';
      for ( j = 0; j < colB; j++) {
          c+='<td><input type="text" size="1" maxlength="2"/></td>';
      }
      c+='</tr>';
  }
  c+='</table>';
  c+='</td>';

/*  c+='<td align="center" valign="middle">';
  c+='<table name="tblMtzR">';
  for ( i = 0; i < filA; i++) {
      c+='<tr>';
      for ( j = 0; j < colB; j++) {
          c+='<td><input type="text" size="1" maxlength="2"/></td>';
      }
      c+='</tr>';
  }
  c+='</table>';
  c+='</td>';*/

  c+='</tr>';
  c+='</table>';
	alert (c);
  //var matrices = document.getElementById('tblMatrices');
  //document.getElementById('divMatrices').innerHTML = matrices;
  e.innerHTML=c;
}
function limpiarConver() {
  console.log("entreeee");
	document.getElementById('decimal').value = "";
	document.getElementById('binario').value = "";
	document.getElementById('octal').value = "";
	document.getElementById('hexadecimal').value = "";
}
function limpiarieee(){
	document.getElementById('decimal').value = "";
	document.getElementById('signo').value = "";
	document.getElementById('expon').value = "";
	document.getElementById('mantisa').value = "";

}
function borrarTrapecio(){
	document.getElementById('funcion').value = "";
	document.getElementById('intervaloa').value = "";
	document.getElementById('intervalob').value = "";
	document.getElementById('npart').value = "";
	document.getElementById('trapecio').innerHTML = "";
}

function borrarMontecarlo(){
	document.getElementById('funcion').value = "";
	document.getElementById('intervaloa').value = "";
	document.getElementById('intervalob').value = "";
	document.getElementById('npart').value = "";
	document.getElementById('cota').value = "";
	document.getElementById('trapecio').innerHTML = "";
}
