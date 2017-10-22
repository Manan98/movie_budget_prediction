
$(function() {
  $('#parameters').change(function() {
    if ($(this).val() === "1") {
      $('#parameter1Type').slideDown("slow");
      $('#parameter2Type').slideUp("slow");
      $('#parameter3Type').slideUp("slow");
    }
    if ($(this).val() === "2") {
      $('#parameter1Type').slideDown("slow");
      $('#parameter2Type').slideDown("slow");
      $('#parameter3Type').slideUp("slow");
    }
    if ($(this).val() === "3") {
      $('#parameter1Type').slideDown("slow");
      $('#parameter2Type').slideDown("slow");
      $('#parameter3Type').slideDown("slow");
    }
  });
});


$(function(){
  $('#parameter1Type').change(function(){
  if ($('#type1').val() === "genre") {
  $('#genreType').slideDown("slow");
  }
  if ($('#type1').val() === "score") {
  $('#predictedScore').slideDown("slow");
  }
  if ($('#type1').val() === "time") {
  $('#runtime').slideDown("slow");
  }
});
});

$(function(){
  $('#parameter2Type').change(function(){
  if ($('#type2').val() === "genre") {
  $('#genreType').slideDown("slow");
  }
  if ($('#type2').val() === "score") {
  $('#predictedScore').slideDown("slow");
  }
  if ($('#type2').val() === "time") {
  $('#runtime').slideDown("slow");
  }
});
});

$(function(){
  $('#parameter3Type').change(function(){
  if ($('#type3').val() === "genre") {
  $('#genreType').slideDown("slow");
  }
  if ($('#type3').val() === "score") {
  $('#predictedScore').slideDown("slow");
  }
  if ($('#type3').val() === "time") {
  $('#runtime').slideDown("slow");
  }
});
});

// $.ajax({
//     type: "POST",
//     dataType: 'json',
//     url: "http://127.0.0.1:5010/get_data",
//     success: function(data){console.log(data);},
//    contentType: formdata,
// });

function loadDoc() {

console.log("meow");
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("parameters").innerHTML = this.responseText;
      document.getElementById("parameter1Type").innerHTML = this.responseText;
    }
  };
  xhttp.open("POST", "http://127.0.0.1:5010/get_data", true);
  xhttp.send();
}
//
// function loadDoc() {
//   var xhttp = new XMLHttpRequest();
//   xhttp.onreadystatechange = function() {
//     if (this.readyState == 4 && this.status == 200) {
//       document.getElementById("demo").innerHTML = this.responseText;
//     }
//   };
//   xhttp.open("POST", "demo_post.asp", true);
//   xhttp.send();
// }
