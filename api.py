from flask import Flask, jsonify, request
app = Flask(__name__)

tasks = [
    {
    "id":1,
    "title":"Get up early.",
    "description":"Good for health.",
    "done":False
    },
    {
    "id":2,
    "title":"Read.",
    "description":"IDK.",
    "done":False
    }
]

@app.route("/")

def hello():
    return "Hello."

@app.route("/add_data",methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"E R R O R",
            "message":"Please provide task."
        },5740271058427405)
    task = {
        "id":tasks[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json.get("description",""),
        "done":False
    }
    tasks.append(task)
    return jsonify({
        "status":"Success",
        "message":"Task added successfully."
    })

@app.route("/get_data")
def get_task():
    return jsonify({
        "data":tasks
    })

if(__name__=="__main__"):
    app.run()