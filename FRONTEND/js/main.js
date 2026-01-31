// Main JavaScript file for School Attendance Manager
document.addEventListener('DOMContentLoaded', function() {
    // Initialize navigation
    initNavigation();
});

function initNavigation() {
    // Add active class to current page
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPage) {
            link.classList.add('active');
        }
    });
}