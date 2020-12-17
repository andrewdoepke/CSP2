function showDownload(id_choice) {
    var display = document.getElementById("option-selected");
    var mobile_list = document.getElementById("moblist");
    var computer_list = document.getElementById("comlist");
    var console_list = document.getElementById("conlist");
    var idVal = id_choice;

    if (display.style.display === "none") {
        display.style.display = "flex";

        if (idVal === "computer") {
            computer_list.style.display = "block";
            mobile_list.style.display = "none";
            console_list.style.display = "none";
        } else if (idVal === "mobile") {
            mobile_list.style.display = "block";
            computer_list.style.display = "none";
            console_list.style.display = "none";
        } else if (idVal === "console") {
            console_list.style.display = "block";
            mobile_list.style.display = "none";
            computer_list.style.display = "none";
        }
    } else if (display.style.display === "flex") {
        if (idVal === "computer") {
            computer_list.style.display = "block";
            mobile_list.style.display = "none";
            console_list.style.display = "none";
        } else if (idVal === "mobile") {
            mobile_list.style.display = "block";
            computer_list.style.display = "none";
            console_list.style.display = "none";
        } else if (idVal === "console") {
            console_list.style.display = "block";
            mobile_list.style.display = "none";
            computer_list.style.display = "none";
        }
    }
}

function showLinks() {
    var selection = document.getElementById("option-selected");
}

// Hide the div on load
document.getElementById("option-selected").style.display = "none";

document.getElementById("option-selected").onclick = function() {
    showDownload(this.id);
};
