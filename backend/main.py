from recommender import recommend_jobs, format_recommendations
from course import recommend_courses

user_skills = ["Python", "Machine Learning", "SQL"]
recommendations = recommend_jobs(user_skills, top_n=5)

print(format_recommendations(recommendations))

skills="Git, Linux"
print(recommend_courses(skills,num_recommendations=5))