async function loadPartial(id, url) {
  const response = await fetch(url);
  const html = await response.text();
  document.getElementById(id).innerHTML = html;
}

window.addEventListener("DOMContentLoaded", () => {
  loadPartial("header", "/static/partials/header.html");
  loadPartial("footer", "/static/partials/footer.html");
});
