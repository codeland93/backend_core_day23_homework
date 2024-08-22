from flask import Flask
from config import db
from flask import request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Fitness Center API is running!"

# Add a member
@app.route('/members', methods=['POST'])
def add_member():
    data = request.json
    cursor = db.cursor()
    query = "INSERT INTO Members (name, email, membership_type) VALUES (%s, %s, %s)"
    cursor.execute(query, (data['name'], data['email'], data['membership_type']))
    db.commit()
    return jsonify({"message": "Member added successfully!"}), 201

# Get a member
@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM Members WHERE id = %s"
    cursor.execute(query, (id,))
    member = cursor.fetchone()
    if not member:
        return jsonify({"error": "Member not found"}), 404
    return jsonify(member)

# Update a member
@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.json
    cursor = db.cursor()
    query = "UPDATE Members SET name = %s, email = %s, membership_type = %s WHERE id = %s"
    cursor.execute(query, (data['name'], data['email'], data['membership_type'], id))
    db.commit()
    return jsonify({"message": "Member updated successfully!"})

# Delete a member
@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    cursor = db.cursor()
    query = "DELETE FROM Members WHERE id = %s"
    cursor.execute(query, (id,))
    db.commit()
    return jsonify({"message": "Member deleted successfully!"})

# Schedule a workout session
@app.route('/workout_sessions', methods=['POST'])
def schedule_workout():
    data = request.json
    cursor = db.cursor()
    query = "INSERT INTO WorkoutSessions (member_id, session_date, workout_type, duration) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (data['member_id'], data['session_date'], data['workout_type'], data['duration']))
    db.commit()
    return jsonify({"message": "Workout session scheduled!"}), 201

# Get all workout sessions for a specific member
@app.route('/members/<int:member_id>/workout_sessions', methods=['GET'])
def get_member_workouts(member_id):
    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM WorkoutSessions WHERE member_id = %s"
    cursor.execute(query, (member_id,))
    sessions = cursor.fetchall()
    return jsonify(sessions)

# Update a workout session
@app.route('/workout_sessions/<int:id>', methods=['PUT'])
def update_workout(id):
    data = request.json
    cursor = db.cursor()
    query = "UPDATE WorkoutSessions SET session_date = %s, workout_type = %s, duration = %s WHERE id = %s"
    cursor.execute(query, (data['session_date'], data['workout_type'], data['duration'], id))
    db.commit()
    return jsonify({"message": "Workout session updated!"})

# Delete a workout session
@app.route('/workout_sessions/<int:id>', methods=['DELETE'])
def delete_workout(id):
    cursor = db.cursor()
    query = "DELETE FROM WorkoutSessions WHERE id = %s"
    cursor.execute(query, (id,))
    db.commit()
    return jsonify({"message": "Workout session deleted!"})

if __name__ == '__main__':
    app.run(debug=True)
