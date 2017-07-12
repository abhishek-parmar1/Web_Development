$('.play_btn').click(function(){
    arr = $('.song_play');
    if(arr[0].paused == true)
        {
            arr[0].play();
            $('#icon_toggle').removeClass('fa-play');
            $('#icon_toggle').addClass('fa-pause');
            
        }
    else
        {
            arr[0].pause();
            $('#icon_toggle').removeClass('fa-pause');
            $('#icon_toggle').addClass('fa-play');
        }    
});
$('body').on('keypress',function(event){
    if(event.keyCode == 32)
        {
            arr = $('.song_play');
            if(arr[0].paused == true)
                {
                    arr[0].play();
                    $('#icon_toggle').removeClass('fa-play');
                    $('#icon_toggle').addClass('fa-pause');

                }
            else
                {
                    arr[0].pause();
                    $('#icon_toggle').removeClass('fa-pause');
                    $('#icon_toggle').addClass('fa-play');
                }        
        }
        
});
/*$('.duration-button').on('click',function(){
    arr = $('.song_play');
    $('.duration').text("Total duration : " + Math.round(arr[0].duration*100)/100 + "seconds");
});
$('.current-time-button').on('click',function(){
    arr = $('.song_play');
    $('.current-time').text("Current duration : " + Math.round(arr[0].currentTime*100)/100 + "seconds");
});
*/
function fancyTimeFormat(time)
{   
    // Hours, minutes and seconds
    var hrs = ~~(time / 3600);
    var mins = ~~((time % 3600) / 60);
    var secs = time % 60;

    // Output like "1:01" or "4:03:59" or "123:03:59"
    var ret = "";

    if (hrs > 0) {
        ret += "" + hrs + ":" + (mins < 10 ? "0" : "");
    }

    ret += "" + mins + ":" + (secs < 10 ? "0" : "");
    ret += "" + secs;
    return ret;
}
function updateCurrentTime(){
    arr = $('.song_play');
    time1 = arr[0].duration;
    time1 = fancyTimeFormat(time1);
    time2 = arr[0].currentTime;
    time2 = fancyTimeFormat(time2);
    $('.duration').text("Total duration : " + time1 + "seconds");
    $('.current-time').text("Current duration : " + time2 + "seconds");
}
window.onload = function(){
    updateCurrentTime();
}
$('.play_btn').on('click',function(){
    setInterval(function(){
        updateCurrentTime(); 
    }, 1000);
});

