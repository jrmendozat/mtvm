$(document).ready(main);

var contador = 1;

function main () {
$('.menu2').click(function(){
if (contador == 1) {
$('.menu').animate({
left: '0'
});
contador = 0;
} else {
contador = 1;
$('.menu').animate({
left: '-110%'
});
}
});

// Mostramos y ocultamos submenus
$('.menu').click(function(){
$(this).children('.menu').slideToggle();
});
}

$('.comercialClick').click(function(){
    var comercial = $('.comercialLink');
    var operaciones = $('.operacionesLink');
    var administracion = $('.administracionLink');
    var sistemas = $('.sistemasLink');
    var divider = $('.divider');
    divider.css('display','block');
    comercial.addClass('block');
    operaciones.removeClass('block');
    administracion.removeClass('block');
    sistemas.removeClass('block');
    $('.comercialClick').css('background','rgba(0,0,0,.1)');
    $('.operacionesClick').css('background','rgba(0,0,0,.0)');
    $('.administracionClick').css('background','rgba(0,0,0,.0)');
    $('.sistemasClick').css('background','rgba(0,0,0,.0)');
})

$('.operacionesClick').click(function(){
    var comercial = $('.comercialLink');
    var operaciones = $('.operacionesLink');
    var administracion = $('.administracionLink');
    var sistemas = $('.sistemasLink');
    var divider = $('.divider');
    divider.css('display','none');
    comercial.removeClass('block');
    operaciones.addClass('block');
    administracion.removeClass('block');
    sistemas.removeClass('block');
    $('.comercialClick').css('background','rgba(0,0,0,.0)');
    $('.operacionesClick').css('background','rgba(0,0,0,.1)');
    $('.administracionClick').css('background','rgba(0,0,0,.0)');
    $('.sistemasClick').css('background','rgba(0,0,0,.0)');

})

$('.administracionClick').click(function(){
    var comercial = $('.comercialLink');
    var operaciones = $('.operacionesLink');
    var administracion = $('.administracionLink');
    var sistemas = $('.sistemasLink');
    var divider = $('.divider');
    divider.css('display','none');
    comercial.removeClass('block');
    operaciones.removeClass('block');
    administracion.addClass('block');
    sistemas.removeClass('block');
    $('.comercialClick').css('background','rgba(0,0,0,.0)');
    $('.operacionesClick').css('background','rgba(0,0,0,.0)');
    $('.administracionClick').css('background','rgba(0,0,0,.1)');
    $('.sistemasClick').css('background','rgba(0,0,0,.0)');
})

$('.sistemasClick').click(function(){
    var comercial = $('.comercialLink');
    var operaciones = $('.operacionesLink');
    var administracion = $('.administracionLink');
    var sistemas = $('.sistemasLink');
    var divider = $('.divider');
    divider.css('display','none');
    sistemas.addClass('block');
    comercial.removeClass('block');
    operaciones.removeClass('block');
    administracion.removeClass('block');
    $('.comercialClick').css('background','rgba(0,0,0,.0)');
    $('.operacionesClick').css('background','rgba(0,0,0,.0)');
    $('.administracionClick').css('background','rgba(0,0,0,.0)');
    $('.sistemasClick').css('background','rgba(0,0,0,.1)');
})
$(function () {
  $('[data-toggle="popover"]').popover()
})

//focus para los input

var focuNombre = $('#id_nombre');
focuNombre.focus();

var focuCondicion = $('#id_condicion');
    focuCondicion.focus();

var focuSegmento = $('#id_segmento');
focuSegmento.focus();

var focuDescripcion = $('#id_descripcion');
    focuDescripcion.focus();

var focuNP = $('#id_nombre_principal');
    focuNP.focus();

var focuNumero = $('#id_tipo_telefono');
    focuNumero.focus();

var focuDireccion = $('#id_direccion');
    focuDireccion.focus();

//var focuTipoDireccion = $('#id_direccion');
  //  focuTipoDireccion.focus();

var focuEmail = $('#id_email');
    focuEmail.focus();

$('.eliminar1').click(function(){
    var mensaje = $('.mensaje')
    var eliminar = $('.eliminar2');
    eliminar.addClass('block');
    mensaje.addClass('block');

})
