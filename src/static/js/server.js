$("#document").ready(function(){

    //TO get recent operations
    function load() {
        $.ajax({ 
            type: "GET",
            url: "http://127.0.0.1:8080/history",
            ifModified:true,     
            success: function (response) {
                var html = '<h2>Recent Operations</h2>';
                html += '<div>';
                if(response.length > 0) {  
                    html +='<table class="table"><tbody>';
                    for(var i=0;i < response.length; i++) {
                        html +='<tr><td>'+response[i]['operation']+'</td></tr>';
                    }
                    html +='</tbody></table>';
                    }
                    html +='</div>';
                    $('.recent-operations').html(html);
                setTimeout(load, 1000)
            }
        });
    }

    load(); 

    $("#send").click(function(){
        var message = $('#screen').val();
        $.ajax({
            url: "http://127.0.0.1:8080/calculate",
            type: "POST",
            data: {"operation" : message},
            error: function(error) {
                console.log(error)
                $('#screen').val(error.responseText);
             },
        }).done(function(data) {
            $('#screen').val(data);
            load();
        });
    });

   

});