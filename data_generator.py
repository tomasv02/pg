import numpy as np

# Načtení dříve vytvořeného seznamu dodávek
deliveries_df = pd.read_excel("/mnt/data/dodavky_vygenerovane.xlsx")

# Seznam elektroniky (materiálů)
materials = [
    ("EL1001", "Bezdrátová myš"), ("EL1002", "Klávesnice"), ("EL1003", "USB-C kabel"),
    ("EL1004", "Webkamera"), ("EL1005", "Monitor 24\""), ("EL1006", "Notebook 15.6\""),
    ("EL1007", "Sluchátka s mikrofonem"), ("EL1008", "Externí disk 1TB"),
    ("EL1009", "Grafická karta"), ("EL1010", "Router Wi-Fi 6")
]

# Vygenerování položek pro každou dodávku
items_data = []
for _, row in deliveries_df.iterrows():
    delivery_number = row['Číslo dodávky']
    num_items = random.randint(1, 4)
    used_items = random.sample(materials, num_items)
    for i, (material_code, material_desc) in enumerate(used_items, start=1):
        item_number = random.randint(10, 99)
        quantity = random.randint(1, 20)
        unit_price = round(random.uniform(100, 5000), 2)
        created_time = (datetime.min + timedelta(seconds=random.randint(0, 86399))).time().strftime('%H:%M:%S')
        created_by = random.choice(['VRBAT', 'DVORAKP', 'JANOVECT'])
        items_data.append({
            'Číslo dodávky': delivery_number,
            'položka dodávky': item_number,
            'Materiál': material_code,
            'Text materiálu': material_desc,
            'dodané množství': quantity,
            'dod. Mn. Jednotka': 'ks',
            'Cena za jednotku': unit_price,
            'Vytvořeno': row['Vytvořeno'],
            'Čas': created_time,
            'Založil': created_by
        })

# Uložení do Excelu
items_df = pd.DataFrame(items_data)
items_output_path = "/mnt/data/dodavky_polozky.xlsx"
items_df.to_excel(items_output_path, index=False)

items_output_path