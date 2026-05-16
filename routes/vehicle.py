from flask import jsonify, request, Blueprint
from psycopg2.extras import RealDictCursor
from database import get_connection

vehicle = Blueprint("vehicle", __name__)

@vehicle.route("/")
def get_driver():
    try:
        conn= get_connection()
        cur = conn.cursor(cursor_factory = RealDictCursor)
        cur.execute("""
                        select * from logistics.vehicle
                """)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        
    except Exception as e :
        return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify(rows)
    
@vehicle.route("/", methods=["POST"])
def create_vehicle():
    try:
        conn= get_connection()
        cur = conn.cursor()
        data = request.get_json()
        cur.execute("""
                    insert into logistics.vehicle
                    (model, license_plate, driver_id)
                    values 
                    (%s, %s, %s)
            """, (data["model"], data["license_plate"], data["driver_id"]))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
       return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify({"message": "Object Created"}), 201
    
@vehicle.route("/<int:id>", methods=["PUT"])
def update_driver(id):
    try:
        conn= get_connection()
        cur = conn.cursor()
        data = request.get_json()
        print(data)
        cur.execute("""
                    update logistics.vehicle
                    set model = %s ,
                        license_plate = %s,
                        driver_id = %s
                    where vehicle_id = %s
            """, (data["model"], data["license_plate"], data["driver_id"], id))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"{e}"}), 500
    else:
        return jsonify({"message": "Object Updated"}), 201
    
@vehicle.route("/<int:id>", methods=["DELETE"])
def delete_vehicle(id):
    try:
        conn= get_connection()
        cur = conn.cursor()
        cur.execute("""
                    delete from logistics.vehicle
                    where vehicle_id = %s
            """, (id, ))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify({"message": "Object Deleted"}), 201