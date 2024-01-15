def calculate_preliminary_price(area_m2, thickness_cm):
    base_price_per_m2 = 4.5  # Base price per square meter in EUR
    extra_charge_per_cm = 0.20  # Extra charge per square meter if thickness is over 5 cm

    # Check if thickness is greater than 5 cm and apply extra charge
    if thickness_cm > 5:
        total_price = area_m2 * (base_price_per_m2 + extra_charge_per_cm)
    else:
        total_price = area_m2 * base_price_per_m2

    return total_price

if __name__ == "__main__":
    # Input from the user
    plotas = float(input("Įveskite plotą (m2): "))
    storis = float(input("Įveskite storį (cm): "))

    # Calculate the price
    kaina = calculate_preliminary_price(plotas, storis)

    # Output the preliminary price
    print(f"Preliminari kaina: {kaina:.2f} EUR + medžiagos")