

function updateValue() {
    const width = document.getElementById("width").value;
    const thickness = document.getElementById("thickness").value;

    const widthAmount = document.getElementById("amount-width");
    const thicknessAmount = document.getElementById("amount-thickness");

    widthAmount.textContent = width;
    thicknessAmount.textContent = thickness;
    
    const cost = document.getElementById("totalCost");
    // Total cubic yard = >(Length * Width * (Depth / 12)) / 27
    let calculation = (width * (thickness / 12))/ 27;
    cost.textContent = calculation;
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

