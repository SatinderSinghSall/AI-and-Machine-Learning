const sidebar = document.getElementById("sidebar");
const menuBtn = document.getElementById("menuBtn");

menuBtn.addEventListener("click", () => {
  if (window.innerWidth < 900) {
    sidebar.classList.toggle("active");
  } else {
    sidebar.classList.toggle("collapsed");
  }
});
