function darkLight() {
    var element = document.body;
    element.dataset.bsTheme =
        element.dataset.bsTheme == "light" ? "dark" : "light";
}