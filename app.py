from flask import Flask, jsonify, request
from database import get_connection, create_table

app = Flask(__name__)
create_table()

@app.route("/")
def home():
    return "Hello, Job Tracker!"

@app.route("/applications", methods=["GET"])
def list_applications():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM applications").fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])

@app.route("/applications", methods=["POST"])
def add_application():
    data = request.get_json()
    conn = get_connection()
    cursor = conn.execute(
        "INSERT INTO applications (company, role, date_applied, status) VALUES (?, ?, ?, ?)",
        (data["company"], data["role"], data.get("date_applied"), data.get("status", "applied"))
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": new_id, "message": "Job added"}), 201

@app.route("/applications/<int:app_id>", methods=["PUT"])
def update_application(app_id):
    data = request.get_json()
    conn = get_connection()
    conn.execute(
        "UPDATE applications SET status = ? WHERE id = ?",
        (data["status"], app_id)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Status updated"})

@app.route("/applications/<int:app_id>", methods=["DELETE"])
def delete_application(app_id):
    conn = get_connection()
    conn.execute("DELETE FROM applications WHERE id = ?", (app_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Job deleted"})

if __name__ == "__main__":
    app.run(debug=True)