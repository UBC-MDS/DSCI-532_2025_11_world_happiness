// assets/scroll.js
window.addEventListener('DOMContentLoaded', function() {
    const dropdowns = document.querySelectorAll('select');
    dropdowns.forEach(function(dropdown) {
        dropdown.addEventListener('change', function() {
            const chartContainer = document.getElementById('radar-chart-container');
            if (chartContainer) {
                chartContainer.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});
