**🌦️Weather App using Django**

A simple and user-friendly Weather Application built using Django that fetches and displays real-time weather information for any city using the OpenWeather API.

**📌 Project Description**

The Django Weather App allows users to enter a city name and retrieve current weather details such as temperature, humidity, and country code. This project demonstrates how to integrate third-party APIs with Django and dynamically render data on web pages.

It is ideal for beginners who want hands-on experience with Django views, templates, forms, and API integration.

**🚀 Features**

🌍 Search weather by city name

🌡️ Displays real-time temperature

💧 Shows humidity level

🏳️ Displays country code

⚠️ Error handling for invalid city names

🖥️ Simple and clean UI

**🛠️ Technologies Used**

Python

Django Framework

OpenWeather API

HTML & CSS

Requests Library

JSON Data Handling

**📂 Project Structure**

weather_project/
│
├── weather/
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── weather/
│   │       └── weather.html
│   └── __init__.py
│
├── weather_project/
│   ├── settings.py
│   ├── urls.py
│   └── __init__.py
│
├── manage.py
└── README.md

**⚙️ Installation & Setup**

1️⃣ Clone the repository
git clone https://github.com/your-username/django-weather-app.git
cd django-weather-app

2️⃣ Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate

3️⃣ Install dependencies
pip install django requests

4️⃣ Get OpenWeather API Key

Visit: https://openweathermap.org/api

Sign up and generate an API key

**🔑 Configure API Key**

In views.py, replace:

api_key = "6d410a46652b3a30c899faf53ed67a53"


with your actual OpenWeather API key.

**▶️ Run the Application**
python manage.py runserver


Open your browser and go to:

http://127.0.0.1:8000/

**🧪 Usage**

Enter a city name in the input field

Click on Search

View real-time weather details instantly

**📖 What I Learned**

Integrating third-party APIs in Django

Handling HTTP requests and JSON responses

Using Django templates to render dynamic data

Debugging API and form-related issues

Understanding Django project structure

**🔮 Future Enhancements**

🌤️ Weather icons

📍 Auto-detect user location

📅 5-day weather forecast

🎨 Improved UI with Bootstrap

🌡️ Toggle between Celsius and Fahrenheit

**🤝 Contributing**

Contributions are welcome!
Feel free to fork this repository and submit a pull request.

**📄 License**

This project is open-source and available under the MIT License.

**👤 Author**

Harshita Varshney

LinkedIn: https://linkedin.com/in/harshita-varshney-146715246

GitHub: https://github.com/Harshita6224
