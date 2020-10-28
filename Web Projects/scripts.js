console.log("DOM READY");


var countdownDate = new Date("Feb 20, 2098 15:00:00").getTime();
//console.log(countdownDate);

var countdown = setInterval(() => {
    var now = new Date().getTime();
    var distance = countdownDate - now;

    //console.log(distance);

    if(distance < 0) {
        clearInterval(countdown);
        document.getElementById("demo").innerHTML = "EXPIRED";

    } else {
        var day = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hour = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minute = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var second = Math.floor((distance % (1000 * 60)) / 1000);
    
        document.getElementById("demo").innerHTML = "<p>" + day + " days, " + hour + "h " + minute + "m " + second + "s</p>";
    }
}, 1000);