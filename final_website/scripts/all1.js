

function loadDoc() {

var xhttp = new XMLHttpRequest();
xhttp.open("POST", "http://127.0.0.1:5100/get_data", true);

xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {

        var json = JSON.parse(xhr.responseText);
        var data={"genre":document.getElementById("genre").value
        "predictedScore":document.getElementById("predictedScore").value,
        "runtime":document.getElementById("runtime").value,
        "revenue":document.getElementById("revenue").value}"}
        xhttp.send(data);
        function(){window.open("file///Users/mananchugh/Desktop/movie_budget_predictor/final_website/index2.html");}
      }
  };
}

