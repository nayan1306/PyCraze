// static/js/scripts.js
document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.recipe-card');

    cards.forEach(card => {
        const header = card.querySelector('.recipe-header');
        header.addEventListener('click', () => {
            const content = card.querySelector('.recipe-content');
            content.style.display = content.style.display === 'block' ? 'none' : 'block';
        });
    });
});

function toggleRecipeContent(header) {
    const content = header.nextElementSibling;
    content.style.display = content.style.display === 'block' ? 'none' : 'block';
}
