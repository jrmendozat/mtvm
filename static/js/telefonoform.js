var telefono = $('.telefono');
var select = $('select');
var input = $('input')
var area = $('.area');
var buscador = $('.buscador');
var seleccion =$('#seleccionM');

input.focusin(function(){
    telefono.css('display','none');
    select.css('display','inline-block');
    seleccion.css('display','none');
});
input.focusout(function(){
    telefono.css('display','none');
    seleccion.css('border','none');
    seleccion.css('display','inline-block');
    input.css('border','1px solid #ccc')

});
telefono.hover(function(){
    telefono.css('display','none');
    select.css('display','inline-block');
});

    function borrarCampo() {
    docu|t.getElementById("formulario").reset();
}

function cargarNumero() {
  var numero = document.getElementById("casilla").value;


  var casilla = $('#casilla');
  var telefono = $('.telefono');
  var lista = $('.lista');
  var select = $('select');
  var seleccion = $('#seleccionM')


    telefono.css('display','none');

    seleccion.css('display','inline-block');



  document.getElementById("casilla").value = numero;
  }

$('select').on('change',function(){
    var valor = $(this).val();
    var tipo;
switch (valor) {
    case "0":
        tipo = "Seleccione un tipo";
        break;
    case "1":
        tipo = "Movil";
        break;
    case "2":
        tipo = "Trabajo";
        break;
    case "3":
        tipo = "Hogar";
        break;
    case "4":
        tipo = "Principal";
        break;
    case "5":
        tipo = "Fax Trabajo";
        break;
    case "6":
        tipo = "Fax Hogar";
        break;
    case "7":
        tipo = "Fax Hogar";
        break;
    default:
        tipo = "Seleccione un tipo de telefono";
        break;
}
   document.getElementById("seleccionM").innerHTML = null;


});



    $(document).ready(function(){




  $("#id_numero").keydown(function(event) {
     if(event.shiftKey)
     {
          event.preventDefault();
     }

     if (event.keyCode == 46 || event.keyCode == 8)    {
     }
     else {
          if (event.keyCode < 95) {
            if (event.keyCode < 48 || event.keyCode > 57) {
                  event.preventDefault();
            }
          }
          else {
                if (event.keyCode < 96 || event.keyCode > 105) {
                    event.preventDefault();
                }
          }
        }
     });
  });
