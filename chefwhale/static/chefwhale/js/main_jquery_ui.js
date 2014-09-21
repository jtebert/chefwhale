$(document).ready(function () {
    // Style elements with jQuery UI
    $( "#date" ).datepicker();
    $('input[type=button]').button();
    $('button').button();
    $('input[type=submit]').button();
    $("input[type=file]").nicefileinput();

    // Fix select width
    $.each($('select'), function () {
        $(this).selectmenu({ width: $(this).width() + 50}).selectmenu("menuWidget").addClass('overflow');
    });

    // Dynamic formsets
    $(function() {
       $('#ingredient-form-table tr').formset({
           prefix: '{{ ingredient_form.prefix }}',
           formCssClass: 'dynamic-ingredient-formset'
       });

       $('#instruction-form-table tbody tr').formset({
           prefix: '{{ instruction_form.prefix }}',
           formCssClass: 'dynamic-instruction-formset'
       });
    });
})