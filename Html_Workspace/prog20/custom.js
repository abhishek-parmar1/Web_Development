$('.play_btn').click(function(){
    arr = $('.song_play');
    if(arr[0].paused == true)
        {
            arr[0].play();
            $('#icon_toggle').removeClass('fa-pause');
            $('#icon_toggle').addClass('fa-play');
            
        }
    else
        {
            arr[0].pause();
            $('#icon_toggle').removeClass('fa-play');
            $('#icon_toggle').addClass('fa-pause');
        }    
});