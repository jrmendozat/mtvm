$ (Document).Ready(function(){

         // Código jQuery que se añade aquí.
         $('#editar').click(function(){
            alert('prueba' + $(this).attr("data-telid"))
            var telid;
            telid = $(this).attr("data-telid");
            $.post('/Telefono/editar_telefono/', {id_telef: telid}, function(data){
                $('.form-group').html(data);
            });
        });

     });
