document.querySelectorAll('.filters select').forEach(select => {
    select.addEventListener('change', () => {
        select.form.submit();
    });
});