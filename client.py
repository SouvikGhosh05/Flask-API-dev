import requests
def send_get():
    return requests.get("http://localhost:5000").text

def send_post(data):
    return requests.post("http://localhost:5000", data=data).text
def send_delete(data):
    return requests.delete("http://localhost:5000", data=data).text
print(send_get())
print(send_post("nice"))
print(send_delete("nice"))

