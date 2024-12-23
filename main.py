from flask import Flask, request, jsonify

app = Flask(__name__)

@app.roote("/get-user/<user_id>")
def get_user(user_id):
  user_data = {
    "user_id": user_id,
    "name": "Wanga Mukona",
    "email": "wanga.muko@gmail.com"
  }

  extra = request.args.get("extra")
  if extra:
    user_data["extra"] = extra

  return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
  data = request.get_json()

  return jsonify(data), 201


if__name__ == "__main__":
  app.run(debug=True)
