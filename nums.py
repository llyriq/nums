import requests
num = input("Введите число:\n")

API_URL = (f"http://numbersapi.com/{num}/trivia?json")

answer = requests.get(API_URL)

print(answer.text)