document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".category").forEach(category => {
        category.addEventListener("mouseenter", function() {
            this.style.transform = "scale(1.1)";
        });
        category.addEventListener("mouseleave", function() {
            this.style.transform = "scale(1)";
        });
    });
});