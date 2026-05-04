import psycopg2 , os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        sslmode=os.getenv("DB_SSLMODE"),
    )

    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(""" 
                

                create table if not exists driver 
                (
                    driver_id serial primary key,
                    name varchar(250),
                    license_type varchar(100)
                );

                 create table if not exists vehicle
                (
                    vehicle_id serial primary key,
                    license_plate varchar,
                    model varchar(100),
                    driver_id int references driver(driver_id)
                );

                create table if not exists route
                (
                    route_id serial primary key,
                    service_zone varchar,
                    order_date TIMESTAMP,
                    driver_id int references driver(driver_id)

                );

                create table if not exists package
                (
                    package_id serial primary key,
                    description varchar(500),
                    weight numeric,
                    route_id int references route(route_id),
                    driver_id int references driver(driver_id)
                );


        """)

    conn.commit()
    cur.close()
    conn.close()
    print("Database Ready!✅")
