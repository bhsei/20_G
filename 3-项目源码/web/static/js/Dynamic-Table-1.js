$(document).ready(function(){
    $('.dynamic-table').each(function(){
        div = $(this);
        div.data('rows', 0);
         div.find(".dynamic-table-add_row").click(function(){
          var i = div.data('rows');
             i++;
             row = div.find('.dynamic-table-addr'+i)
          row.html("<td>"+ (i) +"</td>"+div.find('.dynamic-table-addr0').html());
            row.find('.datetimepicker').datetimepicker();
          div.find('.dynamic-table-tab_logic').append('<tr class="dynamic-table-addr'+(i+1)+'"></tr>');
             
        div.data('rows', i);
      });
         div.find('.dynamic-table-delete_row').click(function(){
             var i = div.data('rows');
             if(i>0){
                 div.find('.dynamic-table-addr'+(i)).html('');
                 i--;
        div.data('rows', i);
             }
         });
        div.find('.dynamic-table-add_row').trigger('click');
        
    });

});