#question_data=[
    #{"text" : "the slug blood is green", "answer":"true"},
    #{"text" : "the rainbow has 7 color", "answer":"true"},
    #{"text": "Soccer player Cristiano Ronaldo opened a museum dedicated to himself.","answer": "True"}
#]
import requests

parameter={
    "amount":10,
    "type":"boolean"

}
response = requests.get(url="https://opentdb.com/api.php",params=parameter)
response.raise_for_status()
data = response.json()
print(data)
question_data=data["results"]
print(question_data)
