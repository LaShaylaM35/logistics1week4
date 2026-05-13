from flask import jsonify, request, Blueprint
from psycopg2.extras import RealDictCursor
from database import get_connection

route = Blueprint("route", __name__)

@route.route("/")
def get_route():
    try:
        conn= get_connection()
        cur = conn.cursor(cursor_factory = RealDictCursor)
        cur.execute("""
                        select * from logistics.route
                """)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        
    except Exception as e :
        return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify(rows)
    
@route.route("/", methods=["POST"])
def create_route():
    try:
        conn= get_connection()
        cur = conn.cursor()
        data = request.get_json()
        cur.execute("""
                    insert into logistics.route
                    (order_date, service_zone)
                    values 
                    (%s, %s)
            """, (data["order_date"], data["service_zone"]))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
       return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify({"message": "Object Created"}), 201
    
@route.route("/<int:id>", methods=["PUT"])
def update_route(id):
    try:
        conn= get_connection()
        cur = conn.cursor()
        data = request.get_json()
        print(data)
        cur.execute("""
                    update logistics.route
                    set name = %s ,
                        service_zone = %s
                    where route_id = %s
            """, (data["service_zone"], data["order_date"], id))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"{e}"}), 500
    else:
        return jsonify({"message": "Object Updated"}), 201
    
@route.route("/<int:id>", methods=["DELETE"])
def delete_route(id):
    try:
        conn= get_connection()
        cur = conn.cursor()
        cur.execute("""
                    delete from logistics.route
                    where route_id = %s
            """, (id, ))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e :
        return jsonify({"message": f"An unexpected error occurred: {e}"}), 500
    else:
        return jsonify({"message": "Object Deleted"}), 201
    
   