const backButton = document.getElementById("go-back");
const photoDisplay = document.getElementById("feature-img");
const featureDesc = document.getElementById("new-feature-title");
const nextButton = document.getElementById("go-next");


var imgArr = ["<img src=" + "/static/images/new-characters.png" + ' alt="Feature" id = "feature">',
    "<img src=" + "/static/images/honey-block.png" + ' alt="Feature" id = "feature">',
    "<img src=" + "/static/images/beep.png" + ' alt="Feature" id = "feature">'];

var imgDesc = ["New Characters", "New Blocks", "New Animals"];

var i = 0;
function display(clickIndex) {
    i = (i + clickIndex + imgArr.length) % imgArr.length;
    var img = imgArr[i];
    photoDisplay.innerHTML = img;
}

var k = 0;
function displayDesc(clickIndex) {
    k = (k + clickIndex + imgDesc.length) % imgDesc.length;
    featureDesc.innerHTML = imgDesc[k];
}

function next() {
    display(1);
    displayDesc(1);
}

function back() {
    display(-1);
    displayDesc(-1);
}

display(0);
displayDesc(0);