from flask import Flask, request, jsonify

app = Flask(__name__)

# locations of our api's
@app.route("/")
def home():
    return "hwllo sharad"

# this is second route
@app.route("/myname")
def myname():
    return "sharad poddar"

# dynamic routing
# returning the json data
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "sharad",
        "age": 12,
        "college": "unknown"
    }
    return user_data

# query parameter
@app.route("/name")
def get_my_name():
    extra = request.args.get("extra")
    user_data = {
        "user_id": "123",
        "name": "sharad",
        "age": 12,
        "college": "unknown"
    }
    if extra:
        user_data["extra"] = extra
        # here 200 is the status code
        # jsonify make the data in json format and return it
        # 200 is default status code
        return jsonify(user_data), 200 
    else:
        return "no extra found"


# there is some error here, check back

# we can use muliple methods but then we have to 
# use if req.mehtod == "GET" .....
@app.route("/create_user", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    
    username = data.get("username")
    if not username:
        return jsonify({"error": "Missing 'username' field"}), 

    print(username)
    return jsonify(data), 201

# this is our main where program start to execute
if __name__ == "__main__":
    app.run(debug=True)
