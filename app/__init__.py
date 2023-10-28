from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # 데이터베이스 설정
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysql@ec2-3-39-126-15.ap-northeast-2.compute.amazonaws.com/mysql'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)

    # 모델 클래스 정의
    class Student(db.Model):
        __tablename__ = 'students'
        student_id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        interest = db.Column(db.String(100))

    class Skill(db.Model):
        __tablename__ = 'skills'
        skill_id = db.Column(db.Integer, primary_key=True)
        skill_name = db.Column(db.String(100), nullable=False)

    class Award(db.Model):
        __tablename__ = 'awards'
        award_id = db.Column(db.Integer, primary_key=True)
        award_name = db.Column(db.String(100), nullable=False)
        award_year = db.Column(db.Integer, nullable=False)

    # 라우트 정의
    @app.route("/", methods=["GET"])
    def home():
        return render_template("index.html")

    @app.route("/students", methods=["GET"])
    def get_students():
        students = Student.query.all()
        students_data = [{"student_id": student.student_id, "name": student.name, "interest": student.interest} for
                         student in students]
        return jsonify(students_data)

    @app.route("/skills", methods=["GET"])
    def get_skills():
        skills = Skill.query.all()
        skills_data = [{"skill_id": skill.skill_id, "skill_name": skill.skill_name} for skill in skills]
        return jsonify(skills_data)

    @app.route("/awards", methods=["GET"])
    def get_awards():
        awards = Award.query.all()
        awards_data = [{"award_id": award.award_id, "award_name": award.award_name, "award_year": award.award_year} for
                       award in awards]
        return jsonify(awards_data)

    return app
