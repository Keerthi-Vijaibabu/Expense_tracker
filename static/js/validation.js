document.addEventListener('DOMContentLoaded', function () {
  const loginForm = document.getElementById('loginForm');
  const registerForm = document.getElementById('registerForm');

  // Login form validation
  if (loginForm) {
    loginForm.addEventListener('submit', function (e) {
      const username = document.getElementById('username').value.trim();
      const password = document.getElementById('password').value.trim();

      clearErrors();

      if (!username) {
        e.preventDefault();
        showError('username', 'Username is required');
        return;
      }

      if (!password) {
        e.preventDefault();
        showError('password', 'Password is required');
        return;
      }

      // Optional: Show loading state
      const submitBtn = loginForm.querySelector('button[type="submit"]');
      submitBtn.innerHTML = 'Signing in...';
      submitBtn.disabled = true;
    });
  }

  // Register form validation
  if (registerForm) {
    registerForm.addEventListener('submit', function (e) {
      const username = document.getElementById('username').value.trim();
      const password = document.getElementById('password').value.trim();
      const confirmPassword = document.getElementById('confirmPassword').value.trim();

      clearErrors();

      if (!username) {
        e.preventDefault();
        showError('username', 'Username is required');
        return;
      }

      if (!password) {
        e.preventDefault();
        showError('password', 'Password is required');
        return;
      }

      if (password.length < 8) {
        e.preventDefault();
        showError('password', 'Password must be at least 8 characters');
        return;
      }

      if (password !== confirmPassword) {
        e.preventDefault();
        showError('confirmPassword', 'Passwords do not match');
        return;
      }

      const submitBtn = registerForm.querySelector('button[type="submit"]');
      submitBtn.innerHTML = 'Creating account...';
      submitBtn.disabled = true;
    });
  }

  // Helper: Remove previous errors
  function clearErrors() {
    document.querySelectorAll('.error-message').forEach(el => el.remove());
    document.querySelectorAll('.form-input').forEach(input => {
      input.style.borderColor = '';
    });
  }

  // Helper: Show inline error
  function showError(inputId, message) {
    const input = document.getElementById(inputId);
    const errorElement = document.createElement('div');
    errorElement.className = 'error-message';
    errorElement.textContent = message;
    errorElement.style.color = 'var(--color-error-600)';
    errorElement.style.fontSize = '0.75rem';
    errorElement.style.marginTop = '4px';

    const existingError = input.parentNode.querySelector('.error-message');
    if (existingError) existingError.remove();

    input.style.borderColor = 'var(--color-error-500)';
    input.parentNode.appendChild(errorElement);

    input.addEventListener('input', function () {
      input.style.borderColor = '';
      const error = input.parentNode.querySelector('.error-message');
      if (error) error.remove();
    }, { once: true });
  }
});
