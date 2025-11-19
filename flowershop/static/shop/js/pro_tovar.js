const tabLinks = document.querySelectorAll('.tab-link');
const tabPanes = document.querySelectorAll('.tab-pane');

tabLinks.forEach(link => {
    link.addEventListener('click', () => {
        // Знімаємо 'active' з усіх
        tabLinks.forEach(l => l.classList.remove('active'));
        tabPanes.forEach(p => p.classList.remove('active'));

        // Додаємо 'active' до натиснутої кнопки
        link.classList.add('active');
        
        // Додаємо 'active' до відповідного контенту
        const tabId = link.getAttribute('data-tab');
        document.getElementById(tabId).classList.add('active');
    });
});

