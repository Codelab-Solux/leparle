//  navbbar dropdown button mechanism ----------------------------------------------
function toggleDropdown(e) {
  e.name === "dropdownBtn"
    ? ((e.name = "close"), dropdownMenu.classList.remove("hidden"))
    : ((e.name = "dropdownBtn"), dropdownMenu.classList.add("hidden"));
}

function toggleMenu(e) {
  e.name === "menu"
    ? ((e.name = "close"), navlinks.classList.remove("hidden"))
    : ((e.name = "menu"), navlinks.classList.add("hidden"));
}
//  back to top button mechanism ---------------------------------------------------
// const to_top_btn = $("#toTopBtn");
// // When the user scrolls down 20px from the top of the document, show the button
// window.onscroll = function () {
//   if (document.body.scrollTop > 40 || document.documentElement.scrollTop > 40) {
//     to_top_btn.removeClass("hidden");
//     to_top_btn.addClass("block");
//   } else {
//     to_top_btn.removeClass("block");
//     to_top_btn.addClass("hidden");
//   }
// };

// // When the user clicks on the button, scroll to the top of the document
// function toTop() {
//   document.body.scrollTop = 0;
//   document.documentElement.scrollTop = 0;
// }
