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

song_arr = ["song1.mp3","song2.mp3","song3.mp3","song4.mp3"];
song_status = [-1,-1,-1,-1];


window.onload = function(){
    
    $('.first').text(song_arr[0]);
    $('.second').text(song_arr[1]);
    $('.third').text(song_arr[2]);
    $('.fourth').text(song_arr[3]);
    updateCurrentTime();
}

/* 1st method */
/*$('.first').on('click',function(){
    
    var s = $('audio');
    
    var flag1 = $('.second').hasClass("toggle_play");
    var flag2 = $('.third').hasClass("toggle_play");
    var flag3 = $('.fourth').hasClass("toggle_play");
    
    if(flag1 || flag2 || flag3) 
    {
         $('.second').removeClass("toggle_play");
         $('.third').removeClass("toggle_play");
         $('.fourth').removeClass("toggle_play");
    }
    
    if($('.first').hasClass("toggle_play"))
        {
            if(s[1].paused)
                {
                    s[1].play();
                }
            else{
                s[1].pause();    
            }
        }
    
    else
    {
        $('#play_selected').attr('src',"song1.mp3");
        $('.first').addClass("toggle_play");
        s[1].play();
    }
    
});

$('.second').on('click',function(){
    
    var s = $('audio');
    
    var flag1 = $('.first').hasClass("toggle_play");
    var flag2 = $('.third').hasClass("toggle_play");
    var flag3 = $('.fourth').hasClass("toggle_play");
    
    if(flag1 || flag2 || flag3)
    {
         $('.first').removeClass("toggle_play");
         $('.third').removeClass("toggle_play");
         $('.fourth').removeClass("toggle_play");
    }
    
   if($('.second').hasClass("toggle_play"))
        {
            if(s[1].paused)
                {
                    s[1].play();
                }
            else{
                s[1].pause();    
            }
        }
    
    else
    {
        $('#play_selected').attr('src',"song2.mp3");
        $('.second').addClass("toggle_play");
        s[1].play();
    }
    
});

$('.third').on('click',function(){
   var s = $('audio');
    
    var flag1 = $('.first').hasClass("toggle_play");
    var flag2 = $('.second').hasClass("toggle_play");
    var flag3 = $('.fourth').hasClass("toggle_play");
    
    if(flag1 || flag2 || flag3)
    {
         $('.first').removeClass("toggle_play");
         $('.second').removeClass("toggle_play");
         $('.fourth').removeClass("toggle_play");
    }
    
   if($('.third').hasClass("toggle_play"))
        {
            if(s[1].paused)
                {
                    s[1].play();
                }
            else{
                s[1].pause();    
            }
        }
    
    else
    {
        $('#play_selected').attr('src',"song3.mp3");
        $('.third').addClass("toggle_play");
        s[1].play();
    }
});

$('.fourth').on('click',function(){
    var s = $('audio');
    
    var flag1 = $('.first').hasClass("toggle_play");
    var flag2 = $('.second').hasClass("toggle_play");
    var flag3 = $('.third').hasClass("toggle_play");
    
    if(flag1 || flag2 || flag3)
    {
         $('.first').removeClass("toggle_play");
         $('.second').removeClass("toggle_play");
         $('.third').removeClass("toggle_play");
    }
    
   if($('.fourth').hasClass("toggle_play"))
        {
            if(s[1].paused)
                {
                    s[1].play();
                }
            else{
                s[1].pause();    
            }
        }
    
    else
    {
        $('#play_selected').attr('src',"song4.mp3");
        $('.fourth').addClass("toggle_play");
        s[1].play();
    }
});
*/

/* 2nd method */
/*
$('.first').on('click',function(){
    var s = $('audio');
    
   song_status[1]=song_status[2]=song_status[3]=-1;
    
   if(song_status[0]!=-1)
        {
            if(s[1].paused)
                {
                    s[1].play();
                    song_status[0]=1;
                }
            else{
                s[1].pause(); 
                song_status[0]=0;
            }
        }
    
    else
    {
        $('#play_selected').attr('src',"song1.mp3");
        s[1].play();
        song_status[0]=1;
    }
});


$('.second').on('click',function(){
    var s = $('audio');
    
   song_status[0]=song_status[2]=song_status[3]=-1;
    
   if(song_status[1]!=-1)
        {
            if(s[1].paused)
                {
                    s[1].play();
                    song_status[1]=1;
                }
            else{
                s[1].pause(); 
                song_status[1]=0;
            }
        }
    
    else
    {
        $('#play_selected').attr('src',"song2.mp3");
        s[1].play();
        song_status[1]=1;
    }
});

$('.third').on('click',function(){
    var s = $('audio');
    
   song_status[0]=song_status[1]=song_status[3]=-1;
    
   if(song_status[2]!=-1)
        {
            if(s[1].paused)
                {
                    s[1].play();
                    song_status[2]=1;
                }
            else{
                s[1].pause(); 
                song_status[2]=0;
            }
        }
    
    else
    {
        $('#play_selected').attr('src',"song3.mp3");
        s[1].play();
        song_status[2]=1;
    }
});

$('.fourth').on('click',function(){
    var s = $('audio');
    
   song_status[0]=song_status[1]=song_status[2]=-1;
    
   if(song_status[3]!=-1)
        {
            if(s[1].paused)
                {
                    s[1].play();
                    song_status[3]=1;
                }
            else{
                s[1].pause(); 
                song_status[3]=0;
            }
        }
    
    else
    {
        $('#play_selected').attr('src',"song4.mp3");
        s[1].play();
        song_status[3]=1;
    }
});
*/

/* 3rd method */
function toggleSong(){
    var s = $('audio');
    if(s[1].paused)
        {
            s[1].play();
        }
    else
    {
        s[1].pause();
    }
}

$('.first').on('click',function(){
    var s = $('audio');
    var currentSong = s[1].src;
    
   if(currentSong.search(song_arr[0]) != -1)
        {
            toggleSong();
        }
    else
    {
        $('#play_selected').attr('src',"song1.mp3");
        s[1].play();
    }
});

$('.second').on('click',function(){
    var s = $('audio');
    var currentSong = s[1].src;
    
   if(currentSong.search(song_arr[1]) != -1)
        {
            toggleSong();
        }
    else
    {
        $('#play_selected').attr('src',"song2.mp3");
        s[1].play();
    }
});

$('.third').on('click',function(){
    var s = $('audio');
    var currentSong = s[1].src;
    
   if(currentSong.search(song_arr[2]) != -1)
        {
            toggleSong();
        }
    else
    {
        $('#play_selected').attr('src',"song3.mp3");
        s[1].play();
    }
});

$('.fourth').on('click',function(){
    var s = $('audio');
    var currentSong = s[1].src;
    
   if(currentSong.search(song_arr[3]) != -1)
        {
            toggleSong();
        }
    else
    {
        $('#play_selected').attr('src',"song4.mp3");
        s[1].play();
    }
});

$('.play_btn').on('click',function(){
    setInterval(function(){
        updateCurrentTime(); 
    }, 1000);
});

