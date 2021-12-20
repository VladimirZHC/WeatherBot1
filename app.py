from flask import Flask, request
import requests

app = Flask(__name__)


def get_weather():
    params = {"access_key": "36df53649b6a793772017a459a3c1885", "query": "New York"}
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    return f"Сейчас в Нью-Йорке {api_response['current']['temperature']} градусов"


def send_message(chat_id, text):
    method = "sendMessage"
    token = "5055856840:AAHuzZKACd6rGCVKy6PKn16L6dZ3kggbYdY"
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)


@app.route("/", methods=["GET", "POST"])
def receive_update():
    if request.method == "POST":
        print(request.json)
        chat_id = request.json["message"]["chat"]["id"]
        weather = get_weather()
        send_message(chat_id, weather)
    return {"ok": True}
