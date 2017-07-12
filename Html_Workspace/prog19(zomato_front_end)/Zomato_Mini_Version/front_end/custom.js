/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction1() {
    document.getElementById("myDropdown1").classList.toggle("show");
}

function myFunction2() {
    document.getElementById("myDropdown2").classList.toggle("show");
}

function myFunction3() {
    document.getElementById("myDropdown3").classList.toggle("show");
}

function myFunction4() {
    document.getElementById("myDropdown4").classList.toggle("show");
}


// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!(event.target.matches('.dropbtn1') || $(event.target).closest('#myDropdown1').length !=0 )) {
    var dropdowns = document.getElementsByClassName("dropdown-content1");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
 if (!(event.target.matches('.dropbtn2') || $(event.target).closest('#myDropdown2').length !=0 )) {

    var dropdowns = document.getElementsByClassName("dropdown-content2");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
 if (!(event.target.matches('.dropbtn3') || $(event.target).closest('#myDropdown3').length !=0 )) {

    var dropdowns = document.getElementsByClassName("dropdown-content3");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
 if (!(event.target.matches('.dropbtn4') || $(event.target).closest('#myDropdown4').length !=0 )) {

    var dropdowns = document.getElementsByClassName("dropdown-content4");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}

// array for ordered list
var selected = [];

// functions which add the item name (checkbox name attribute value)to array of ordered list from all div
$('.create_order1').click(function(){
    $('#myDropdown1 input:checked').each(function() {
        selected.push($(this).attr('name'));
    });
});
$('.create_order2').click(function(){
    $('#myDropdown2 input:checked').each(function() {
        selected.push($(this).attr('name'));
    });
});
$('.create_order3').click(function(){
    $('#myDropdown3 input:checked').each(function() {
        selected.push($(this).attr('name'));
    });
});
$('.create_order4').click(function(){
    $('#myDropdown4 input:checked').each(function() {
        selected.push($(this).attr('name'));
    });
});

// function to display the message of order registration
$('#order_btn').click(function(){
    if(selected.length==0)
        $('#message').text("Fool First...Order Some Thing!!!") 
    else
        $('#message').text("Thank You for ordering... Your order has been REGISTERED.")
});