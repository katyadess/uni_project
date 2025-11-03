document.querySelectorAll('.filters select').forEach(select => {
    select.addEventListener('change', () => {
        select.form.submit();
    });
});

if (window.location.search) {
        window.history.replaceState({}, document.title, window.location.pathname);
}