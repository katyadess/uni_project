const paymentOptions = document.querySelectorAll('input[name="payment_method"]');
const continueBtn = document.getElementById('continueBtn');

paymentOptions.forEach(option => {
    option.addEventListener('change', () => {
        if (option.value === 'cash') {
            // continueBtn.setAttribute('href', '{% url "shop:zamovlenya_usp" %}');
          return;  
        } else {
            continueBtn.setAttribute('href', '{% url "shop:oplata" %}');
        }
    });
});