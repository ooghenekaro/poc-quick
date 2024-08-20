document.addEventListener('DOMContentLoaded', function() {
    const glideInElements = document.querySelectorAll('.glide-in');
    const dishes = document.querySelectorAll('.dish img');

    function checkPosition() {
        glideInElements.forEach(element => {
            const position = element.getBoundingClientRect();
            if (position.top < window.innerHeight && position.bottom >= 0) {
                element.classList.add('show');
            }
        });

        dishes.forEach((dish, index) => {
            setTimeout(() => {
                dish.classList.add('fade-in');
            }, index * 300); // Delay each image's fade-in effect
        });
    }

    window.addEventListener('scroll', checkPosition);
    checkPosition(); // Initial check on page load
});
