import requests
querry=input("What news do you want to see:")    

url= f"https://newsapi.org/v2/everything?q={querry}&from=2024-11-15&sortBy=popularity&apiKey=98b98361096c42ea88462a15b1b6d9c2"
r = requests.get(url)
print(r.text)
