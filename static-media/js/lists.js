function send_ajax($url, $data){

    $data['csrfmiddlewaretoken'] = $("input[name='csrfmiddlewaretoken']").val();

    $.ajax({
        url: $url,
        data: $data,
        type: "POST",
        dataType: "json",
        success: function(response){
            if(response['id']){
                prepend_row(response['id'], response['text']);
            }else{
                console.log(response);
            }
        },
        error: function(response){
            console.log(response);
        }
    });
}

function prepend_row(id, text){
    row = "<li> \
        <div class='row-container'> \
            <input class='task-check' type='checkbox' task='"+id+"'/> \
            <textarea class='task' wrap='off' rows='1' task= '" + id + "' url='{% url update_task %}' >"+
                text + "</textarea></div> </li>";
    $(".tasks-container").prepend(row);
}

$("#add-task").on("click", function(){
    $("#new-task-form").removeClass("invisible");
});

$("#new-task-form textarea").keydown(function(e){
    if((e.keyCode || e.which) == 13){
        e.preventDefault();
        $("#new-task-form").addClass("invisible");
        $form = $("#new-data form");
        $text = $("#id_text").val();
        $("#id_text").val("");
        $data = {
            'text': $text
        }
        console.log($data);
        $url = $form.attr("url");
        send_ajax($url, $data);
    }
});


$(".task").keydown(function(e){
    if((e.keyCode || e.which) == 13){
        e.preventDefault();
        $text = $(this).val();
        $id = $(this).attr("task");
        $url = $(this).attr("url");
        $data = {
            'id': $id,
            'text': $text
        }
        console.log($data);
        send_ajax($url, $data);
    }
});

$(".tasks-container").on("change",'.task-check', function(){
    $id = $(this).attr("task");
    console.log("In task check");
    console.log($id);
    qr = "textarea[task="+$id+"]";
    $textarea = $(qr);
    $url = $textarea.attr("url");
    if($(this).is(":checked")){
        $textarea.prop("disabled", true);
        $textarea.addClass("completed");
        $completed = "true";
    }else{
        $textarea.prop("disabled", false);
        $textarea.removeClass("completed");
        $completed = "false";
    }
    $data = {
        'completed': $completed,
        'id': $id
    }

    send_ajax($url, $data);

});

$(".tasks-select").on("change", function(){
    $val = $(this).val();
    if($val == "all"){
        $("textarea.completed").parent().fadeIn();
    }else if($val == "incomplete"){
        $("textarea.completed").parent().fadeOut();
    }
});