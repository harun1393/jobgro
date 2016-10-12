$(function(){
    $('#search').keyup(function() {
    console.log("in keyup");
        $.ajax({
            type : "POST",
            url: "/job/search-job/",
            data: {
                'search_text': $('#search').val(),
                'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });
});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search-results').html(data);
}