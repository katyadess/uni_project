const paymentOptions = document.querySelectorAll('input[name="payment_method"]');
const continueBtn = document.getElementById('continueBtn');
const cashUrl = continueBtn.dataset.cashUrl;
const cardUrl = continueBtn.dataset.cardUrl;


function updateButtonHref() {
  const selected = document.querySelector('input[name="payment_method"]:checked');
  
  if (!selected) return;

  if (selected.value === 'cash') {
    continueBtn.setAttribute('href', cashUrl);
  } else {
    continueBtn.setAttribute('href', cardUrl);
  }
}

updateButtonHref();

paymentOptions.forEach(option => {
  option.addEventListener('change', updateButtonHref);
});

