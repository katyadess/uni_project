const meBtn = document.querySelector("button[name='delivery_to_me']");
const otherBtn = document.querySelector("button[name='delivery_to_other']");
const textarea = document.querySelector("textarea[name='card_message']");
const cardCheckbox = document.querySelector("#card");
const recipientInputs = document.querySelectorAll(".form-box .inputs input");

// --- 1. Початковий стан ---
textarea.style.display = cardCheckbox.checked ? "block" : "none";

// --- 2. Перемикання кнопок ---
const toggleButtons = [meBtn, otherBtn];

toggleButtons.forEach(button => {
    button.addEventListener("click", () => {
        // Снимаем активность с всех кнопок
        toggleButtons.forEach(btn => btn.classList.remove("active"));
        button.classList.add("active");

        // --- Очищаем поля ввода получателя ---
        recipientInputs.forEach(input => input.value = "");
    });
});

// --- 3. Показ / приховування тексту листівки ---
cardCheckbox.addEventListener("change", () => {
    // Скрываем или показываем textarea
    textarea.style.display = cardCheckbox.checked ? "block" : "none";

    // --- Очищаем текст листівки при включении или выключении ---
    textarea.value = "";
});


// Получаем все delivery-box
const deliveryBoxes = document.querySelectorAll('.delivery-box');

deliveryBoxes.forEach(box => {
    const radio = box.querySelector('input[type="radio"]');
    const unknownCheckbox = box.querySelector('input[type="checkbox"]');
    const unknownMessage = box.querySelector('.unknown-message');
    const inputs = box.querySelector('.inputs');

    // При выборе способа доставки
    radio.addEventListener('change', () => {
        deliveryBoxes.forEach(b => {
            b.classList.remove('active');

            const checkbox = b.querySelector('input[type="checkbox"]');
            const message = b.querySelector('.unknown-message');
            const addrInputs = b.querySelector('.inputs');

            if (checkbox && message && addrInputs) {
                // Сбрасываем чекбокс "не знаю адресу"
                checkbox.checked = false;
                message.classList.add('hidden');

                // --- Очищаем абсолютно все input внутри блока ---
                const allInputs = addrInputs.querySelectorAll('input');
                allInputs.forEach(input => {
                    input.value = '';
                    input.style.display = 'flex'; // показываем все поля
                });
            }
        });

        // Делаем активным выбранный блок
        box.classList.add('active');
    });

    // Если есть чекбокс "не знаю адресу"
    if (unknownCheckbox && unknownMessage && inputs) {
        unknownCheckbox.addEventListener('change', () => {
            const street = inputs.querySelector('input[name^="street"]');
            const houseApartmentRow = inputs.querySelector('.row');

            if (unknownCheckbox.checked) {
                unknownMessage.classList.remove('hidden');
                if (street) street.style.display = 'none';
                if (houseApartmentRow) houseApartmentRow.style.display = 'none';
            } else {
                unknownMessage.classList.add('hidden');
                if (street) street.style.display = 'flex';
                if (houseApartmentRow) houseApartmentRow.style.display = 'flex';
            }
        });
    }
});


// Получаем все элементы корзины
const items = document.querySelectorAll('.item');

items.forEach(item => {
    const decreaseBtn = item.querySelector('.minus-btn');
    const increaseBtn = item.querySelector('.plus-btn');
    const quantityInput = item.querySelector('input[name="quantity"]');

    // Кнопка уменьшения
    decreaseBtn.addEventListener('click', () => {
        let currentValue = parseInt(quantityInput.value);
        if (currentValue > 1) { // минимальное значение = 1
            quantityInput.value = currentValue - 1;
        }
    });

    // Кнопка увеличения
    increaseBtn.addEventListener('click', () => {
        let currentValue = parseInt(quantityInput.value);
        quantityInput.value = currentValue + 1;
    });
});
