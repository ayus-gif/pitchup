/* =========================================
   DISABLE RIGHT CLICK
========================================= */

document.addEventListener("contextmenu", function (e) {
    e.preventDefault();
});

/* =========================================
   DISABLE F12
========================================= */

document.addEventListener("keydown", function (e) {

    if (e.key === "F12") {
        e.preventDefault();
    }

});