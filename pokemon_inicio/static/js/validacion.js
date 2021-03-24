


function buscarpokemonapi() {
    let nombre_pokemon = $("#nombre_pokemon").val();
    $("#resultado").empty();

    if (nombre_pokemon=="" ) {
        $("#resultado").empty();
        
    }else{
        let data = { nombre: nombre_pokemon};
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            headers: { 'X-CSRFToken': csrftoken },
    
            url: 'buscar_pokemon_api',
            method: "POST",
            data: data,
        }).done(function (data) {
            if (data=='400'){
                $("#resultado").empty();

                $("#resultado").append('<p style="color:red">Sin registros de pokemon</p>');

            }else{
                $("#resultado").empty();

$("#resultado").append('<table class="default"><tr><td>Nombre&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td>Foto&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>   <td>Accion</td>  </tr>  <tr>    <td>'+data['nombre']+'</td>    <td><img src="'+data['img']+'" alt="Girl in a jacket" width="50" height="50"></img></td>    <td><a href="" class="active agregar_pokemon" ui-toggle-class="" data-id="'+data['idpokemon']+'"><i class="fa fa-check text-success text-active" title="agregar"></i></a></td>  </tr></table><br>');
            }
        });
    }
}




function validFormDatosCreditos() { 
    $("#mensaje").empty();
   
    //let nombre = document.getElementById('nombre').value();
    let nombre = $("#nombre").val();
    if (nombre=="" ) {
        $("#mensaje").append('<p style="color:red">Ingresa un usuario</p>');

        $("#btn_submit").attr("disabled", true);
        document.getElementById("btn_submit").style.backgroundColor = "gray";

    }
   
            else{
                

            
    let data = { nombre: nombre, 
    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
};
$.ajax({
    url: 'validar_usuario',
    method: "POST",
    data: data,
}).done(function (data) {
    if (data=='True'){
        $("#btn_submit").attr("disabled", true);
        document.getElementById("btn_submit").style.backgroundColor = "gray";

        $("#mensaje").append('<p style="color:red">Usuario existente</p>');
    }
    else{

        $("#mensaje").append('<p >Usuario Disponible</p>');
        $("#btn_submit").attr("disabled", false);
        document.getElementById("btn_submit").style.backgroundColor = "red";

    }
});
}
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


$(document).on('click', '.agregar_pokemon', function(e) {
    event.preventDefault()
    var csrftoken = getCookie('csrftoken');

    let id_pokemon = $(this).attr("data-id");
    var result = confirm('Realmente desea Agregar?')

    if (result == true) {
        let data = {
            id_pokemon: id_pokemon
            
        }
    
        $.ajax({
            headers: { 'X-CSRFToken': csrftoken },
    
            url: 'agregar_pokemon',
            method: "POST",
            data: data,
        }).done(function (data) {
            location.reload();
        });
    }
});

$(document).on('click', '.eliminar', function(e) {
event.preventDefault()
var csrftoken = getCookie('csrftoken');

let id = $(this).attr("data-id");
var result = confirm('Realmente desea eliminar?')
if (result == true) {
    let data = {
        id: id
        
    }

    $.ajax({
        headers: { 'X-CSRFToken': csrftoken },

        url: 'eliminar_pokemon',
        method: "POST",
        data: data,
    }).done(function (data) {
        location.reload();
    });
}
});

