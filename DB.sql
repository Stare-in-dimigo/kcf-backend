CREATE TABLE students (
  student_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  interest VARCHAR(100)
);

CREATE TABLE skills (
  skill_id INT AUTO_INCREMENT PRIMARY KEY,
  skill_name VARCHAR(100) NOT NULL
);

CREATE TABLE awards (
  award_id INT AUTO_INCREMENT PRIMARY KEY,
  award_name VARCHAR(100) NOT NULL,
  award_year YEAR NOT NULL
);

CREATE TABLE student_skills (
  student_id INT,
  skill_id INT,
  PRIMARY KEY (student_id, skill_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (skill_id) REFERENCES skills(skill_id)
);

CREATE TABLE student_awards (
  student_id INT,
  award_id INT,
  PRIMARY KEY (student_id, award_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (award_id) REFERENCES awards(award_id)
);

CREATE TABLE clubs (
  club_id INT AUTO_INCREMENT PRIMARY KEY,
  club_name VARCHAR(100) NOT NULL,
  club_type VARCHAR(100) NOT NULL
);

CREATE TABLE project_teams (
  team_id INT AUTO_INCREMENT PRIMARY KEY,
  team_name VARCHAR(100) NOT NULL,
  project_type VARCHAR(100) NOT NULL,
  project_topic VARCHAR(100) NOT NULL
);

CREATE TABLE student_clubs (
  student_id INT,
  club_id INT,
  PRIMARY KEY (student_id, club_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (club_id) REFERENCES clubs(club_id)
);

CREATE TABLE student_project_teams (
  student_id INT,
  team_id INT,
  PRIMARY KEY (student_id, team_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (team_id) REFERENCES project_teams(team_id)
);

