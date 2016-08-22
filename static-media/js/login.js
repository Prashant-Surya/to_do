$(document).ready(function(){
    $(".tab").hover(function(){
    $(this).css("cursor", "pointer");
    $(this).addClass("border-bottom");
    }, function(){
        $(this).removeClass("border-bottom");
    });

    $("#login").on('click', function(){
        $("#signup").removeClass("border-bottom");
        $(this).addClass("border-bottom");
        $("#for-login").removeClass("invisible");
        $("#for-signup").addClass("invisible");
    });

    $("#signup").on('click', function(){
        $("#login").removeClass("border-bottom");
        $(this).addClass("border-bottom");
        $("#for-login").addClass("invisible");
        $("#for-signup").removeClass("invisible");
    });

});