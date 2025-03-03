from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def recommend_courses(user_skills, num_recommendations=5):
    
    df = pd.read_csv(r"C:\Users\Asus\Contacts\Desktop\data sci projects\career path recommendation\coursea_data.csv") 

    user_skills = user_skills.lower().strip()

    tfidf = TfidfVectorizer(stop_words='english')
    course_title_matrix = tfidf.fit_transform(df['course_title'].str.lower())
    user_skills_matrix = tfidf.transform([user_skills])

    similarity_scores = cosine_similarity(user_skills_matrix, course_title_matrix)

    course_indices = similarity_scores[0].argsort()[-num_recommendations:][::-1]
    recommended_courses = df.iloc[course_indices].copy()
    recommended_courses['similarity_score'] = similarity_scores[0][course_indices]

    recommended_courses['combined_score'] = (
        0.7 * recommended_courses['similarity_score'] + 
        0.3 * recommended_courses['course_rating']
    )
    recommended_courses = recommended_courses.sort_values('combined_score', ascending=False)

    output_columns = [
        'course_title', 'course_organization', 'course_Certificate_type',
        'course_rating', 'course_difficulty', 'course_students_enrolled'
    ]
    
    return recommended_courses[output_columns]
