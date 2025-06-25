from flask import Flask,render_template,request,jsonify

## WSGI application
app = Flask(__name__)

@app.route("/")
def home():
    return "welcome to homepage of ToDo List"

items = [
    {"id":1,"name":"apple","description":"apple is fruit"},
    {"id":2,"name":"orange","description":"orange fruit"},
    {"id":3,"name":"apple","description":"orange fruit"},
]

# get : retireve all the item
@app.route("/items",methods=["GET"])
def get_items():
    return jsonify(items)

# get the item by its id
@app.route("/items/<int:id>",methods=["GET"])
def get_item(id):
    item = next((item for item in items if item["id"] == id),None)
    if item is None:
        return  jsonify({"error":"item not found"})
    return jsonify(item)

# Post : for creating a new task
@app.route("/items",methods=["POST"])
def create_item():
    if (not request.json or not "name" in request.json):
        return jsonify({"error":"missing name"})

    newItem = {
        "id":items[-1]["id"] +1 if items else 1,
        "name":request.json["name"],
        "description":request.json["description"],
    }

    items.append(newItem)
    return jsonify(newItem)

# Put : updating the existig item
@app.route("/items/<int:id>",methods=["PUT"])
def update_item(id):
    item = next((item for item in items if item["id"]==id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    item["name"] = request.json.get("name",item["name"])
    item["description"] = request.json.get("description",item["description"])
    return jsonify(item)

# Delete : Delete an item
@app.route("/items/<int:id>",methods=["DELETE"])
def delete_item(id):
    global items
    items = [item for item in items if item["id"] != id]
    return jsonify({"items":items})



if __name__ == "__main__":
    app.run(debug=True)
