# daily-menu-checker
# 📋 Menu App

Welcome to the **Menu App**! This Flask application fetches and displays the daily menu from [Bistro Nekázanka](https://www.bistronekazanka.cz/). 🍽️

## 🚀 Features

- Fetches daily menu automatically from an external website.
- Displays the menu in a clean, centered, and aesthetically pleasing format.
- Uses Flexbox for centering and responsive design.
- Simple and easy to set up!

## 🛠️ Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/menu_app.git
    cd menu_app
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the app**:
    ```bash
    export FLASK_APP=app.py
    export FLASK_ENV=development
    flask run
    ```

    Visit `http://127.0.0.1:5000/` in your browser to see the app in action!

## 📝 Usage

The app fetches the daily menu from the iframe on the [Bistro Nekázanka](https://www.bistronekazanka.cz/) website and displays it in a user-friendly format.

## 🖥️ Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **Requests**: Simple HTTP library for Python.
- **BeautifulSoup**: Library for parsing HTML and XML documents.
- **Bootstrap**: CSS framework for creating responsive and modern web pages.

## 👏 Contributing

Feel free to fork this repository and make improvements! Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- Thanks to [Bistro Nekázanka](https://www.bistronekazanka.cz/)

