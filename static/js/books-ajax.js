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

    // $('#suggestion').keyup(function(){
    //     var query;
    //     query = $(this).val();
    //     $.get('/rango/suggest/', {suggestion: query}, function(data){
    //         $('#cats').html(data);
    //     });
    // });
    //
    // $('.rango-add').click(function(){
    //     var catid = $(this).attr("data-catid");
    //     var title = $(this).attr("data-title");
    //     var url = $(this).attr("data-url");
    //     var me = $(this)
    //     $.get("/rango/add/", {category_id: catid, url: url, title: title}, function(data){
    //         $('#pages').html(data);
    //         me.hide();
    //     });
    // });
});