from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from recommender import recommend_jobs, format_recommendations
from course import recommend_courses

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)

CORS(app)  

# Load datasets
jobs_df = pd.read_csv(r"C:\Users\Asus\Contacts\Desktop\data sci projects\career path recommendation\processed_naukri.csv")
courses_df = pd.read_csv(r"C:\Users\Asus\Contacts\Desktop\data sci projects\career path recommendation\coursea_data.csv")

@app.route('/')
def home():
    return "Welcome to the Career Path Recommendation API!"

@app.route('/recommend_jobs', methods=['POST'])
def job_recommendation():
    try:
        data = request.get_json()
        user_skills = data.get('skills', [])
        top_n = data.get('top_n', 10)

        if not user_skills:
            return jsonify({"error": "No skills provided"}), 400

        recommended_jobs = recommend_jobs(user_skills, top_n)
        formatted_jobs = format_recommendations(recommended_jobs)

        return jsonify({"recommended_jobs": formatted_jobs})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/recommend_courses', methods=['POST'])
def course_recommendation():
    try:
        data = request.get_json()
        missing_skills = data.get('missing_skills', [])

        if not missing_skills:
            return jsonify({"error": "No missing skills provided"}), 400

   
        missing_skills_str = ', '.join(missing_skills) 

        recommended_courses = recommend_courses(missing_skills_str)
        recommended_courses_json = recommended_courses.to_dict(orient='records')
        return jsonify({"recommended_courses": recommended_courses_json})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
