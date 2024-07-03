import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


def fetch_daily_menu():
    iframe_url = 'https://www.prazskejrej.cz/menu-na-web/bistro-nekazanka-11'
    response = requests.get(iframe_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    with open('debug_iframe.html', 'w', encoding='utf-8') as file:
        file.write(response.text)

    food_sub_section = soup.find('div', class_='food-sub-section')
    if not food_sub_section:
        return "Daily menu not found. Check debug_iframe.html for the page's HTML structure."

    with open('debug_food_sub_section.html', 'w', encoding='utf-8') as file:
        file.write(str(food_sub_section))

    menu_items = []
    for section in food_sub_section.find_all('div', class_='section-food'):
        for div in section.find_all('div', recursive=False):
            text = div.get_text(" ", strip=True)  
            if text:  
                menu_items.append(text)

    daily_menu = "\n".join(menu_items)
    return daily_menu


@app.route('/')
def home():
    daily_menu = fetch_daily_menu()
    return render_template('menu.html', daily_menu=daily_menu)


if __name__ == '__main__':
    app.run(debug=True)
