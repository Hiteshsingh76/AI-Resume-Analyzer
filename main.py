# Read the resume
with open("resume.txt", "r") as file:
    resume = file.read()

# Read the job description
with open("job_description.txt", "r") as file:
    job_description = file.read()

# Display the information
print("===== RESUME =====")
print(resume)

print("\n===== JOB DESCRIPTION =====")
print(job_description)

skills = [
    "Python",
    "Java",
    "C++",
    "AI",
    "machine learning",
    "GitHub",
    "data",
    "cybersecurity",
    "networking",
    "APIs"

]
skill_keywords = {
    "cybersecurity": ["cybersecurity", "network security", "information security"],
    "networking": ["networking", "computer networks", "network"],
    "APIs": ["apis", "api", "rest api", "restful api"],
    "machine learning": ["machine learning", "ml"]
}

print("\n===== SKILLS FOUND IN JOB DESCRIPTION =====")

job_skills = []

for skill in skills:
    keywords = skill_keywords.get(skill, [skill])

    for keyword in keywords:
        if keyword.lower() in job_description.lower():
            job_skills.append(skill)
            print(skill)
            break


print("\n===== SKILL MATCH =====")

matched_skills = []
missing_skills = []

for skill in skills:
    keywords = skill_keywords.get(skill, [skill])

    found = False

    for keyword in keywords:
        if keyword.lower() in resume.lower():
            found = True
            break

    if found:
        print(skill + " → Resume: YES")
        matched_skills.append(skill)
    else:
        print(skill + " → Resume: NO")
        missing_skills.append(skill)

job_matched_skills = []

for skill in job_skills:
    if skill in matched_skills:
        job_matched_skills.append(skill)

match_percentage = (len(job_matched_skills) / len(job_skills)) * 100

print("\n===== MATCHED SKILLS =====")
print(matched_skills)

print("\n===== MISSING SKILLS =====")
for skill in missing_skills:
    print("- " + skill)

print("\nSkill Match Percentage:", round(match_percentage, 2), "%")

import requests

prompt = f"""
You are a resume analysis assistant.

Your job is to compare the resume with the job description using ONLY information explicitly provided in the two documents.

IMPORTANT RULES:
- Do not invent, assume, or infer experience that is not explicitly stated.
- Do not claim the candidate has a technology, skill, internship, certification, or experience unless it appears in the resume.
- Do not treat coursework as professional work experience.
- Do not treat a programming language being listed as proof of experience with a specific framework or platform.
- If information is not present in the resume, say "Not found in resume."
- Base every conclusion on evidence from the provided resume or job description.

RESUME:
{resume}

JOB DESCRIPTION:
{job_description}

Analyze the documents using these sections:

1. Resume Strengths
List strengths that are directly supported by the resume and relevant to the job.

2. Important Job Requirements
List the important skills, qualifications, technologies, and responsibilities explicitly mentioned in the job description.

3. Skills Found in Resume
List job-related skills that are explicitly present in the resume.

4. Missing or Weak Skills
List important job requirements that are not explicitly demonstrated in the resume.
Do not assume the candidate has them.

5. Evidence
For each important skill found in the resume, briefly explain where it appears in the resume.

6. Resume Improvement Suggestions
Give specific suggestions for improving the resume.
Do not tell the candidate to claim experience they do not have.
Suggestions may include building projects, gaining experience, or better describing existing experience.

7. Overall Analysis
Give a short, factual explanation of how the resume relates to the job description.
Do not invent qualifications or experience.
"""

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream": False
    }
)

result = response.json()

print("\n===== AI RESUME ANALYSIS =====")
print(result["response"])