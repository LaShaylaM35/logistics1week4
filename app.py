from flask import Flask , jsonify, request
from psycopg2.extras import RealDictCursor
from database import init_db
from routes.driver import driver
from routes.vehicle import vehicle
from routes.route import route



app = Flask(__name__)

init_db()
app.register_blueprint(driver, url_prefix="/driver")
app.register_blueprint(vehicle, url_prefix="/vehicle")
app.register_blueprint(route, url_prefix="/route")

@app.route("/")
def home():
    return jsonify({"message": "Server Online"})


if __name__ == "__main__":
    app.run(debug=True)