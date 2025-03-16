window.addEventListener('beforeunload', function (event) {
    event.preventDefault();
    event.returnValue = 'Are you sure you want to leave this page? Plenty of books await.'; 
});

    document.querySelectorAll(".book-card").forEach(card => {
        card.addEventListener("mouseenter", function () {
            this.style.transform = "scale(1.05)";
            this.style.transition = "transform 0.3s ease-in-out";
        });
        card.addEventListener("mouseleave", function () {
            this.style.transform = "scale(1)";
        });
    });
