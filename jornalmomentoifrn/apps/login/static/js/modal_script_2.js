function loadModal(url, title) {
    fetch(url)
        .then(response => response.text())
        .then(html => {
            document.getElementById("modalContent").innerHTML = html;
            document.getElementById("categoriaModalLabel").innerText = title; 

        });
}
