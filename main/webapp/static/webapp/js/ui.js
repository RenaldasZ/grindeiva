function handleImage(selectedImage) {
    const galleryItems = document.querySelectorAll('.job-image');
    const overlay = document.querySelector('.overlay');

    if (selectedImage.classList.contains("active")) {
        selectedImage.classList.remove("active");
        document.body.style.overflow = 'auto';
        overlay.style.display = 'none';
    } else {
        galleryItems.forEach(item => item.classList.remove('active'));
        selectedImage.classList.add("active");

        document.body.style.overflow = 'hidden';
        overlay.style.display = 'block';
    }
}

function updateValue() {
    const base_price_per_m2 = 4.5;
    const extra_charge_per_cm = 0.20;

    const area_m2 = parseFloat(document.getElementById("area_m2").value);
    const thickness = parseFloat(document.getElementById("thickness").value);

    if (isNaN(area_m2) || isNaN(thickness)) {
        // Handle invalid input, e.g., show an error message
        return;
    }

    const widthAmount = document.getElementById("amount-width");
    const thicknessAmount = document.getElementById("amount-thickness");

    widthAmount.textContent = area_m2;
    thicknessAmount.textContent = thickness;

    const cost = document.getElementById("totalCost");

    if (thickness > 5) {
        const excess_thickness = thickness - 5;
        let total_price = area_m2 * (base_price_per_m2 + excess_thickness * extra_charge_per_cm);
        cost.textContent = total_price.toFixed(2); // Rounds to 2 decimal places
    } else {
        let total_price = area_m2 * base_price_per_m2;
        cost.textContent = total_price.toFixed(2); // Rounds to 2 decimal places
    }
}

const uncollapsible = document.querySelector("#top-level-menu");
const burgerBtn = document.querySelector("#burger-button");
const wholePage = document;

burgerBtn.addEventListener("click", active_button);

function active_button() {
    if (uncollapsible.classList.contains("active")) {
        uncollapsible.classList.remove("active");
    } else {
        uncollapsible.classList.add("active");
    }
}

wholePage.addEventListener("click", (event) => {
    const isInsideBurger = uncollapsible.contains(event.target) || burgerBtn.contains(event.target);

    if (!isInsideBurger && uncollapsible.classList.contains("active")) {
        uncollapsible.classList.remove("active");
    }
});

