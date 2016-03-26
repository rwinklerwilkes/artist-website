function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
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

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).ready(function () {
   $('.like-button').click(function () {
        var art_id = $(this).attr('id');
        $.ajax({
            type:'POST',
            url:'/comments/like/',
            data:{'artwork_id':art_id},
            success: function(dataFromServer) {
                var btn = $('#'+art_id);
                var html_str = '<span class="glyphicon glyphicon-thumbs-up" aria-hidden="true"></span> ' + dataFromServer.likes;
                btn.html(html_str);
            }
        });
   });
});