use fitness_center_db;

CREATE TABLE Members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    membership_type VARCHAR(50)
);

CREATE TABLE WorkoutSessions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    session_date DATE,
    workout_type VARCHAR(100),
    duration INT,
    FOREIGN KEY (member_id) REFERENCES Members(id)
);
