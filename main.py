#Resume Parser
import spacy
from spacy.matcher import PhraseMatcher
from collections import defaultdict
nlp = spacy.load("en_core_web_sm")
resumes = [
    "Creative resume text here...",
    "Visual resume text here...",
    "Standard resume text here..."
]

# Resume Parsing
def parse_resume(resume_text):
    """
    Parse a resume and extract relevant information.
    """
    doc = nlp(resume_text)
    skills = extract_skills(doc)
    experiences = extract_experiences(doc)
    achievements = extract_achievements(doc)
    return {
        "skills": skills,
        "experiences": experiences,
        "achievements": achievements
    }

# Skill and Experience Extraction
def extract_skills(doc):
    """
    Extract skills from the parsed resume.
    """
    matcher = PhraseMatcher(nlp.vocab)
    skills_list = ["python", "machine learning", "data analysis"]  
patterns = [nlp(skill) for skill in skills_list]
    matcher.add("Skills", None, *patterns)
    matches = matcher(doc)
    return [doc[start:end].text for match_id, start, end in matches]

def extract_experiences(doc):
    """
    Extract experiences from the parsed resume.
    """
    experiences = []  
    return experiences

# Quantifiable Achievement Identification
def extract_achievements(doc):
   
    achievements = []  
    return achievements

# Example usage
for resume in resumes:
    parsed_resume = parse_resume(resume)
    print("Skills:", parsed_resume["skills"])
    print("Experiences:", parsed_resume["experiences"])
    print("Achievements:", parsed_resume["achievements"])

