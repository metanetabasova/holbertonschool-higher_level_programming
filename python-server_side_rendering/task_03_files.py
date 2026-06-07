#!/usr/bin/python3
import os
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json():
    if not os.path.exists('products.json'):
        return []
    with open('products.json', 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def read_csv():
    if not os.path.exists('products.csv'):
        return []
    products = []
    with open('products.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Tiplərin json formatı ilə eyni olması üçün konvertasiya edirik
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

@app.route('/products')
def show_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # 1. Şərt: source parametrinin doğruluğu
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # Məlumat mənbəyinin seçilməsi
    if source == 'json':
        data = read_json()
    else:
        data = read_csv()

    # 2. Şərt: Əgər id parametri verilibsə filtrləmə aparırıq
    if product_id is not None:
        try:
            target_id = int(product_id)
            filtered_data = [p for p in data if p["id"] == target_id]
            
            # id tapılmadıqda verilən xəta
            if not filtered_data:
                return render_template('product_display.html', error="Product not found")
            
            data = filtered_data
        except ValueError:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
