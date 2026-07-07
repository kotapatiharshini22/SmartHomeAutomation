import sqlite3

DATABASE = "smart_home.db"

def create_database():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS devices(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT,

            status TEXT

        )
    """)

    cursor.execute("DELETE FROM devices")

    devices = [

        ("Light","OFF"),

        ("Fan","OFF"),

        ("Door","LOCKED"),

        ("AC","OFF")

    ]

    cursor.executemany(

        "INSERT INTO devices(name,status) VALUES(?,?)",

        devices

    )

    conn.commit()

    conn.close()


def get_devices():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM devices")

    rows = cursor.fetchall()

    conn.close()

    return rows


def update_device(device_id,status):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(

        "UPDATE devices SET status=? WHERE id=?",

        (status,device_id)

    )

    conn.commit()

    conn.close()