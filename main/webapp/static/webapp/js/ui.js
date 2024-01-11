

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

async function active_button(obj_id) {
    const uncollapsible = document.getElementById(obj_id);
    if (uncollapsible.classList.contains("active")) {
        uncollapsible.classList.remove("active");
    } else {
        uncollapsible.classList.add("active");
    };
};