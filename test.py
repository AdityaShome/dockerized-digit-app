import requests

url = "http://localhost:5000/predict"
files = {"file": open("handwritten3.png", "rb")}
res = requests.post(url, files=files)
print(res.json())
