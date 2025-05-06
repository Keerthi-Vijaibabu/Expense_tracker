// Sidebar functionality
document.addEventListener('DOMContentLoaded', function() {
  const sidebar = document.getElementById('sidebar');
  const sidebarToggle = document.getElementById('sidebarToggle');
  
  if (sidebar && sidebarToggle) {
    // Toggle sidebar collapsed state
    sidebarToggle.addEventListener('click', function() {
      sidebar.classList.toggle('collapsed');
      
      // Change toggle icon direction
      const toggleIcon = sidebarToggle.querySelector('svg');
      if (sidebar.classList.contains('collapsed')) {
        toggleIcon.innerHTML = '<path d="m9 18 6-6-6-6"></path>';
      } else {
        toggleIcon.innerHTML = '<path d="m15 18-6-6 6-6"></path>';
      }
      
      // Save preference to localStorage
      const isCollapsed = sidebar.classList.contains('collapsed');
      localStorage.setItem('sidebarCollapsed', isCollapsed);
    });
    
    // Check for saved sidebar state
    const savedState = localStorage.getItem('sidebarCollapsed');
    
    if (savedState === 'true') {
      sidebar.classList.add('collapsed');
      const toggleIcon = sidebarToggle.querySelector('svg');
      toggleIcon.innerHTML = '<path d="m9 18 6-6-6-6"></path>';
    }
    
    // Mobile sidebar toggle
    const mobileToggle = document.createElement('button');
    mobileToggle.classList.add('mobile-sidebar-toggle');
    mobileToggle.innerHTML = `
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <line x1="3" y1="12" x2="21" y2="12"></line>
        <line x1="3" y1="6" x2="21" y2="6"></line>
        <line x1="3" y1="18" x2="21" y2="18"></line>
      </svg>
    `;
    
    document.querySelector('.main-header .header-start').prepend(mobileToggle);
    
    mobileToggle.addEventListener('click', function() {
      sidebar.classList.toggle('open');
    });
    
    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', function(e) {
      if (window.innerWidth <= 768 && 
          sidebar.classList.contains('open') && 
          !sidebar.contains(e.target) && 
          e.target !== mobileToggle) {
        sidebar.classList.remove('open');
      }
    });
  }
});