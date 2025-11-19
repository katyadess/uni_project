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


const box = document.querySelector('.delivery-box.active');
const deliverySelect = box.querySelector('select[name="delivery_method"]');
const unknownCheckbox = box.querySelector('input[name="unknown_address"]');
const unknownMessage = box.querySelector('.unknown-message');
const streetInput = box.querySelector('input[name="street"]');
const houseApartmentRow = box.querySelector('.inputs .row');
const pickupBlock = document.querySelector('.pickup-address');
const timeInput = box.querySelector('input[name="time"]');
const checkboxRow = unknownCheckbox ? unknownCheckbox.closest('label.checkbox') : null;
const emptyAddress = document.querySelector('.empty-address');

const toggleFields = () => {
    if (!deliverySelect) return;

    const value = deliverySelect.value;

    // Показываем/скрываем поле времени
    if (value === 'exact' || value === 'pickup') {
        timeInput.style.display = 'flex';
    } else {
        timeInput.style.display = 'none';
    }

    if (unknownCheckbox) {
        unknownCheckbox.checked = false;
        if (unknownMessage) unknownMessage.classList.add('hidden');
        if (streetInput) streetInput.style.display = 'block';
        if (houseApartmentRow) houseApartmentRow.style.display = 'flex';
        if (emptyAddress) emptyAddress.style.display = 'none';
    }

    // Показываем/скрываем адресные поля
    if (value === 'pickup') {
        if (streetInput) streetInput.style.display = 'none';
        if (houseApartmentRow) houseApartmentRow.style.display = 'none';
        if (checkboxRow) checkboxRow.style.display = 'none';
        if (unknownMessage) unknownMessage.classList.add('hidden'); // скрываем сообщение на всякий случай
        pickupBlock.classList.remove('hidden');
    } else {
        if (streetInput) streetInput.style.display = 'block';
        if (houseApartmentRow) houseApartmentRow.style.display = 'flex';
        if (checkboxRow) checkboxRow.style.display = 'flex';
        if (emptyAddress) emptyAddress.style.display = 'block';
        pickupBlock.classList.add('hidden');
    }
};

// Слушаем изменения метода доставки
if (deliverySelect) {
    deliverySelect.addEventListener('change', toggleFields);
    toggleFields(); // применяем сразу при загрузке страницы
}

// Чекбокс "Я не знаю адресу" работает только для остальных вариантов (не pickup)
if (unknownCheckbox && unknownMessage && streetInput && houseApartmentRow) {
    unknownCheckbox.addEventListener('change', () => {
        if (unknownCheckbox.checked) {
            unknownMessage.classList.remove('hidden');
            streetInput.style.display = 'none';
            houseApartmentRow.style.display = 'none';
            emptyAddress.style.display = 'none';
        } else {
            unknownMessage.classList.add('hidden');
            streetInput.style.display = 'block';
            houseApartmentRow.style.display = 'flex';
            emptyAddress.style.display = 'block';
        }
    });
}
