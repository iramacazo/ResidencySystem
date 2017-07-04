/**
 * Created by Ira Macazo on 05/07/2017.
 */

$(document).ready(function(){
    /** CSRF FOR AJAX **/

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

    /** CSRF FOR AJAX **/

    $("#submitTeam").click(function()
    {
        var teamName = $("#teamNameInput").val();
        var teamDescription = $("#teamDescriptionInput").val();
        var teamTypeInput = $("input[name='teamType']:checked").val();
        $.ajax
        (
            {
                type: 'POST',
                url: 'ajax/validateteamname',
                data:{
                    teamName: teamName,
                    teamDescription: teamDescription,
                    teamTypeInput: teamTypeInput
                },
                success:[ function(data)
                {
                    if(data !== 'WRONG')
                        window.location.reload()
                }]
            }
        )
    })
});