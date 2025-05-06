// Theme toggling functionality
document.addEventListener('DOMContentLoaded', function() {
  const themeToggle = document.getElementById('themeToggle');
  
  if (themeToggle) {
    themeToggle.addEventListener('click', function() {
      // Toggle dark mode class on html element
      document.documentElement.classList.toggle('dark');
      
      // Save preference to localStorage
      const isDarkMode = document.documentElement.classList.contains('dark');
      localStorage.setItem('darkMode', isDarkMode);
    });
    
    // Check for saved theme preference or respect OS preference
    const savedTheme = localStorage.getItem('darkMode');
    
    if (savedTheme === 'true') {
      document.documentElement.classList.add('dark');
    } else if (savedTheme === 'false') {
      document.documentElement.classList.remove('dark');
    } else {
      // If no saved preference, check OS preference
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      if (prefersDark) {
        document.documentElement.classList.add('dark');
      }
    }
  }
});