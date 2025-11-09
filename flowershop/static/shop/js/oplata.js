(function() {
  const cardNumberEl = document.getElementById('card-number');
  const expiryEl = document.getElementById('card-expiry');
  const cvvEl = document.getElementById('card-cvv');
  const holderEl = document.getElementById('card-holder');
  
  // helper
  const onlyDigits = (s) => s.replace(/\D/g, '');

  // format card number as #### #### #### #### (max 16 digits)
  cardNumberEl.addEventListener('input', (e) => {
    let v = onlyDigits(e.target.value).slice(0,16);
    let parts = [];
    for (let i=0; i<v.length; i+=4) parts.push(v.slice(i, i+4));
    e.target.value = parts.join(' ');
    document.getElementById('card-number-error').textContent = '';
  });

  // expiry: auto slash, enforce MM/YY format
  expiryEl.addEventListener('input', (e) => {
    let v = onlyDigits(e.target.value).slice(0,4);
    if (v.length >= 3) v = v.slice(0,2) + '/' + v.slice(2);
    e.target.value = v;
    document.getElementById('card-expiry-error').textContent = '';
  });


  // CVV: only digits, max 3
  cvvEl.addEventListener('input', (e) => {
    e.target.value = onlyDigits(e.target.value).slice(0,3);
});

  // card holder: uppercase, letters + spaces, allow Cyrillic + Latin
  holderEl.addEventListener('input', (e) => {
    // keep letters (A-Z, а-я, А-Я, ёЁ) and spaces
    const cleaned = e.target.value.replace(/[^A-Za-z\u0400-\u04FF\s]/g, '');
    e.target.value = cleaned.toUpperCase();
});

})();