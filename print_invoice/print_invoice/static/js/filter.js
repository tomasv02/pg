function filterTable() {
    // Získání hodnot filtrů
    let deliveryNumber = document.getElementById("filterDeliveryNumber").value.toLowerCase();
    let customer = document.getElementById("filterCustomer").value.toLowerCase();
    let rows = document.querySelectorAll("table tbody tr");

    // Procházení všech řádků
    rows.forEach(function(row) {
        let deliveryNumberCell = row.cells[0].textContent.toLowerCase();
        let customerCell = row.cells[5].textContent.toLowerCase();

        // Zobrazení nebo skrytí řádku na základě kritérií filtru
        if (
            (deliveryNumberCell.includes(deliveryNumber) || deliveryNumber === "") &&
            (customerCell.includes(customer) || customer === "")
        ) {
            row.style.display = "";  // Zobrazit řádek
        } else {
            row.style.display = "none";  // Skrýt řádek
        }
    });
}