document.addEventListener('DOMContentLoaded', function() {
  const sidebar = document.getElementById('sidebar');
  const sidebarToggle = document.getElementById('sidebarToggle');
  
  if (!sidebar || !sidebarToggle) {
    console.error('Sidebar or toggle button not found!');
    return;
  }

  function toggleSidebar() {
    sidebar.classList.toggle('collapsed');
    
    // Update toggle icon
    const toggleIcon = sidebarToggle.querySelector('svg');
    if (toggleIcon) {
      toggleIcon.innerHTML = sidebar.classList.contains('collapsed') 
        ? '<path d="m9 18 6-6-6-6"></path>' 
        : '<path d="m15 18-6-6 6-6"></path>';
    }
    
    // Save state
    localStorage.setItem('sidebarCollapsed', sidebar.classList.contains('collapsed'));
  }

  // Initialize from saved state
  const savedState = localStorage.getItem('sidebarCollapsed'); // Note: Typo here was fixed
  if (savedState === 'true') {
    sidebar.classList.add('collapsed');
    const toggleIcon = sidebarToggle.querySelector('svg');
    if (toggleIcon) {
      toggleIcon.innerHTML = '<path d="m9 18 6-6-6-6"></path>';
    }
  }

  // Toggle on click
  sidebarToggle.addEventListener('click', toggleSidebar);

  // Mobile toggle (unchanged)
  const mobileToggle = document.createElement('button');
  mobileToggle.classList.add('mobile-sidebar-toggle');
  mobileToggle.innerHTML = `
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <line x1="3" y1="12" x2="21" y2="12"></line>
      <line x1="3" y1="6" x2="21" y2="6"></line>
      <line x1="3" y1="18" x2="21" y2="18"></line>
    </svg>
  `;
  
  document.querySelector('.main-header .header-start')?.prepend(mobileToggle);
  
  mobileToggle.addEventListener('click', function() {
    sidebar.classList.toggle('open');
  });
  
  document.addEventListener('click', function(e) {
    if (window.innerWidth <= 768 && 
        sidebar.classList.contains('open') && 
        !sidebar.contains(e.target) && 
        e.target !== mobileToggle) {
      sidebar.classList.remove('open');
    }
  });
});