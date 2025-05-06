// Form validation
document.addEventListener('DOMContentLoaded', function() {
  const loginForm = document.getElementById('loginForm');
  const registerForm = document.getElementById('registerForm');
  
  // Login form validation and submission
  if (loginForm) {
    loginForm.addEventListener('submit', function(e) {
      e.preventDefault();
      
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
      
      // Validate inputs
      if (!email) {
        showError('email', 'Email is required');
        return;
      }
      
      if (!isValidEmail(email)) {
        showError('email', 'Please enter a valid email address');
        return;
      }
      
      if (!password) {
        showError('password', 'Password is required');
        return;
      }
      
      // Show loading state
      const submitBtn = loginForm.querySelector('button[type="submit"]');
      submitBtn.innerHTML = 'Signing in...';
      submitBtn.disabled = true;
      
      // Simulate API call with setTimeout
      setTimeout(function() {
        // Redirect to dashboard
        window.location.href = 'dashboard.html';
      }, 1000);
    });
  }
  
  // Registration form validation and submission
  if (registerForm) {
    registerForm.addEventListener('submit', function(e) {
      e.preventDefault();
      
      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
      const confirmPassword = document.getElementById('confirmPassword').value;
      
      // Validate inputs
      if (!name) {
        showError('name', 'Name is required');
        return;
      }
      
      if (!email) {
        showError('email', 'Email is required');
        return;
      }
      
      if (!isValidEmail(email)) {
        showError('email', 'Please enter a valid email address');
        return;
      }
      
      if (!password) {
        showError('password', 'Password is required');
        return;
      }
      
      if (password.length < 8) {
        showError('password', 'Password must be at least 8 characters');
        return;
      }
      
      if (password !== confirmPassword) {
        showError('confirmPassword', 'Passwords do not match');
        return;
      }
      
      // Show loading state
      const submitBtn = registerForm.querySelector('button[type="submit"]');
      submitBtn.innerHTML = 'Creating account...';
      submitBtn.disabled = true;
      
      // Simulate API call with setTimeout
      setTimeout(function() {
        // Redirect to dashboard
        window.location.href = 'dashboard.html';
      }, 1000);
    });
  }
  
  // Helper functions
  function showError(inputId, message) {
    const input = document.getElementById(inputId);
    const errorElement = document.createElement('div');
    errorElement.className = 'error-message';
    errorElement.textContent = message;
    errorElement.style.color = 'var(--color-error-600)';
    errorElement.style.fontSize = '0.75rem';
    errorElement.style.marginTop = '4px';
    
    // Remove any existing error
    const existingError = input.parentNode.querySelector('.error-message');
    if (existingError) {
      existingError.remove();
    }
    
    // Add error class to input
    input.style.borderColor = 'var(--color-error-500)';
    
    // Add error message
    input.parentNode.appendChild(errorElement);
    
    // Focus the input
    input.focus();
    
    // Remove error when input changes
    input.addEventListener('input', function() {
      input.style.borderColor = '';
      const error = input.parentNode.querySelector('.error-message');
      if (error) {
        error.remove();
      }
    }, { once: true });
  }
  
  function isValidEmail(email) {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
  }
});