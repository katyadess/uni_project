const paymentOptions = document.querySelectorAll('input[name="payment_method"]');
const continueBtn = document.getElementById('continueBtn');

paymentOptions.forEach(option => {
    option.addEventListener('change', () => {
        if (option.value === 'cash') {
            continueBtn.href = 'zamovlenya_usp.html';
        } else {
            continueBtn.href = 'oplata.html';
        }
    });
});