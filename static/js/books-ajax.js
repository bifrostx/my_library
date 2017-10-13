/**
 * Created by HanXin on 2017-10-11.
 */
$(document).ready(function() {

    $('ul.navbar-nav > li > a[href="' + document.location.pathname + '"]').parent().addClass('active');

    $('ul.nav > li > a[href="' + document.location.pathname + '"]').addClass('active');

    $('#likes').click(function(){
        var bookid;
        bookid = $(this).attr("data-bookid");
        $.get("/like/", {book_id: bookid}, function(data){
            $('#like_count').html(data);
            $('#likes').hide();
        });
    });

//    $('#result').click(function(){
//        var bookid;
//        bookid = $(this).attr("data-bookid");
//        $.get("/like/", {book_id: bookid}, function(data){
//            $('#like_count').html(data);
//            $('#likes').hide();
//        });
//    });
});