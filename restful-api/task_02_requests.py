#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    # URL-e GET sorgusu gonderirik
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Status kodunu cap edirik
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        # Melumati JSON formatinda parse edirik
        posts = response.json()

        #  Her bir postun basligini (title) ekrana cap edirik
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Melumati id, title ve body acarlari olan lugetler siyahisina yigiriq
        structured_data = []
        for post in posts:
            structured_data.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })

        # Melumati posts.csv faylina yaziriq
        filename = "posts.csv"
        keys = ['id', 'title', 'body']

        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(structured_data)
