from flask import Flask , jsonify , request 

app =  Flask(__name__)

countries = [
    { "id":1 , "name":"Thailand" ,  "Capital": "Bangkok", "Area" : 513120},
    { "id":2 , "name":"India" ,  "Capital": "Delhi" , "Area" : 7617930},
    { "id":3 , "name":"Egypt" , "Capital": "Cairo" , "Area" : 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) +1  

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.post("/countries") 
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country , 201
    return { " error": "request must be JSON"} , 415

@app.get("/country")
def get_country():
    return countries[1]