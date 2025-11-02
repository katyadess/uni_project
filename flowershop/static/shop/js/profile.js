const passwordInput = document.getElementById('password');
const toggleIcon = document.getElementById('togglePassword');

toggleIcon.addEventListener('click', function () {
    const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordInput.setAttribute('type', type);
    
    this.classList.toggle('bi-eye');
    this.classList.toggle('bi-eye-slash');
});