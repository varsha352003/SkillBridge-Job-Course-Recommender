from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

mod = pd.read_csv(r"C:\Users\Asus\Contacts\Desktop\data sci projects\career path recommendation\processed_naukri.csv")  

def clean_skills(skills):
    cleaned_skills = set()
    try:
        if isinstance(skills, str):
            if skills.strip().startswith('[') and skills.strip().endswith(']'):
                try:
                    skills_list = eval(skills)
                    if isinstance(skills_list, list):
                        skills = skills_list
                    else:
                        skills = skills.strip('[]').split(',')
                except:
                    skills = skills.strip('[]').split(',')
            else:
                skills = skills.split(',')
        
        if isinstance(skills, set):
            skills = list(skills)
        
        if not isinstance(skills, list):
            skills = [str(skills)]
        
        for skill in skills:
            if isinstance(skill, (str, int, float)):
                cleaned_skill = str(skill).strip().strip("'").strip('"').lower()
                if cleaned_skill:
                    cleaned_skills.add(cleaned_skill)
                    
        return cleaned_skills
    except Exception as e:
        print(f"Error in cleaning skills: {str(e)}")
        return set()

def calculate_skill_gap(job_skills, user_skills):
    missing_skills = set()
    matched_skills = set()
    
    job_skills = {skill.lower() for skill in job_skills}
    user_skills = {skill.lower() for skill in user_skills}
    
    for job_skill in job_skills:
        skill_found = False
        
        if job_skill in user_skills:
            matched_skills.add(job_skill)
            skill_found = True
            continue
        
        for user_skill in user_skills:
            if (job_skill in user_skill) or (user_skill in job_skill):
                matched_skills.add(job_skill)
                skill_found = True
                break
                
            job_words = set(job_skill.split())
            user_words = set(user_skill.split())
            common_words = job_words.intersection(user_words)
            
            if len(common_words) / max(len(job_words), len(user_words)) > 0.5:
                matched_skills.add(job_skill)
                skill_found = True
                break
        
        if not skill_found:
            missing_skills.add(job_skill)
    
    return missing_skills

def recommend_jobs(user_skills, top_n=10):
    try:
        user_skills_set = clean_skills(user_skills)
        if not user_skills_set:
            raise ValueError("No valid user skills found after cleaning")
        
        mod_copy = mod.copy()
        mod_copy["Clean_Skills"] = mod_copy["Skills"].apply(clean_skills)
        
        skills_list = [" ".join(sorted(list(skills))) for skills in mod_copy["Clean_Skills"]]
        skills_list.append(" ".join(sorted(list(user_skills_set))))
        
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(skills_list)
        
        similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])[0]
        
        top_indices = similarity_scores.argsort()[-top_n:][::-1]
        
        top_jobs = []
        for idx in top_indices:
            job_skills = mod_copy.iloc[idx]["Clean_Skills"]
            missing_skills = calculate_skill_gap(job_skills, user_skills_set)
            
            total_required = len(job_skills)
            match_percentage = round(((total_required - len(missing_skills)) / total_required) * 100, 1) if total_required > 0 else 0.0
            
            job_info = {
                "Job Title": mod_copy.iloc[idx]["Job Title"],
                "Role": mod_copy.iloc[idx]["Role"],
                "Industry": mod_copy.iloc[idx]["Industry"],
                "Missing Skills": sorted(list(missing_skills)),
                "Match Percentage": match_percentage,
                "Similarity Score": round(similarity_scores[idx], 3)
            }
            top_jobs.append(job_info)
        
        return top_jobs
    except Exception as e:
        print(f"Error in job recommendation: {str(e)}")
        return []

def format_recommendations(recommendations):
    if not recommendations:
        return "No matching jobs found."
        
    output = []
    for i, job in enumerate(recommendations, 1):
        output.extend([
            f"\n{i}. Job Details:",
            f"   Title           : {job['Job Title']}",
            f"   Role            : {job['Role']}",
            f"   Industry        : {job['Industry']}",
            f"   Match           : {job['Match Percentage']}%",
            f"   Missing Skills  : {', '.join(job['Missing Skills']) if job['Missing Skills'] else 'None'}",
            "-" * 80
        ])
    
    return "\n".join(output)
