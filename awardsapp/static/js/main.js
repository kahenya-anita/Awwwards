const sideNav = document.getElementById("side-nav");

const overlay = document.getElementById("overlay");

const banner = document.getElementById("banner");

function openNav() {
  sideNav.style.width = "250px";
  overlay.style.display = "block";
  banner.style.marginLeft = "250px";
}

function closeNav() {
  sideNav.style.width = "0";
  overlay.style.display = "none";
  banner.style.marginLeft = "0";
}

