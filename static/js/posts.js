var hi = document.getElementById("list").innerHTML;
hi = (hi.trim) ? hi.trim() : hi.replace(/^\s+/,'');
if(hi == '') {
    document.getElementById("list").outerHTML = "<h2 id='nothing'>No Posts Available</h2>";
}