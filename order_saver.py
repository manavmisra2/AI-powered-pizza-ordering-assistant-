
import json
import csv
import xml.etree.ElementTree as ET
import sqlite3
import os

def save_order(order_text, base_path="orders"):
    os.makedirs(base_path, exist_ok=True)

    order_data = {"order": order_text}

    with open(os.path.join(base_path, "order.json"), "w") as f:
        json.dump(order_data, f)

    with open(os.path.join(base_path, "order.csv"), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["order"])
        writer.writerow([order_text])

    root = ET.Element("Order")
    ET.SubElement(root, "Text").text = order_text
    tree = ET.ElementTree(root)
    tree.write(os.path.join(base_path, "order.xml"))

    conn = sqlite3.connect(os.path.join(base_path, "order.db"))
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, order_text TEXT)")
    c.execute("INSERT INTO orders (order_text) VALUES (?)", (order_text,))
    conn.commit()
    conn.close()
