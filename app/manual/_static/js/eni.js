var eni=function($) {
    var post=function(url) {
        console.log('post to '+url);
        $.ajax({
            url: url,
            type:'post',
            dataType: "jsonp",
            withCredentials: null,
            success:function(result) {
                console.log(JSON.stringify(result));
                $("<div><strong>"+url+"</strong>..."+(result.success===true ? "succeeded":"sended")+"</div>")
                    .appendTo('.eni-post-result');
            }
        });
    }
    var send=function(url) {
        console.log('send to '+url);
        $.ajax({
            url: url,
            type:'get',
            withCredentials: true,
            success:function(result) {
                console.log(JSON.stringify(result));
                $("<div><strong>"+url+"</strong>..."+(result.success===true ? "succeeded":"sended")+"</div>")
                    .appendTo('.eni-post-result');
            }
        });
    }

    function send2(url) {
        console.log('send2 to '+url);
        var s = document.createElement("script");
        s.src = url;
        document.body.appendChild(s);
    }

    return{
        post:post,
        send:send,
        send2:send2
    };
}(jQuery);

$(function(){
    $("a.reference.external").attr('target','_blank');
});