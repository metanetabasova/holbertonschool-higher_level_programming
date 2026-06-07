#!/usr/bin/python3
import os
import json
import csv
import sqlite3
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
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

def read_sql(product_id=None):
    if not os.path.exists('products.db'):
        return []
    
    products = []
    try:
        conn = sqlite3.connect('products.db')
        # Sətirləri dictionary formatına yaxın oxumaq üçün row_factory təyin edirik
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if product_id is not None:
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id = ?", (product_id,))
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")
            
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row["id"],
                "name": row["name"],
                "category": row["category"],
                "price": row["price"]
            })
        conn.close()
    except sqlite3.Error:
        # Verilənlər bazası xətası baş verərsə boş siyahı qaytarırıq
        return []
    return products

@app.route('/products')
def show_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # 1. Şərt: Source parametrinin düzgünlüyü yoxlanılır (json, csv, sql)
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # SQL mənbəyi olduqda sorğunu birbaşa verilənlər bazası daxilində filtrləmək daha optimaldır
    if source == 'sql':
        if product_id is not None:
            try:
                target_id = int(product_id)
                data = read_sql(product_id=target_id)
            except ValueError:
                return render_template('product_display.html', error="Product not found")
        else:
            data = read_sql()
            
        # Əgər id verilibsə və sql daxilindən heç bir data qayıtmayıbsa
        if product_id is not None and not data:
            return render_template('product_display.html', error="Product not found")

    # JSON və ya CSV mənbələri üçün mövcud məntiq işləyir
    else:
        if source == 'json':
            data = read_json()
        else:
            data = read_csv()

        if product_id is not None:
            try:
                target_id = int(product_id)
                filtered_data = [p for p in data if p["id"] == target_id]
                
                if not filtered_data:
                    return render_template('product_display.html', error="Product not found")
                
                data = filtered_data
            except ValueError:
                return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
