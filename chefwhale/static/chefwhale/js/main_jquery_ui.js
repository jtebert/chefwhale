$(document).ready(function () {
    // Style elements with jQuery UI
    $( "#date" ).datepicker();
    $('input[type=button]').button();
    $('button').button();
    $('input[type=submit]').button();
    $("input[type=file]").nicefileinput();

    // Fix select width
    $.each($('select'), function () {
        $(this).selectmenu({ width : $(this).width() + 50})
    });
})