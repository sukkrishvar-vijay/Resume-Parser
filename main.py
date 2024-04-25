import re
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Example resumes
# resumes = [
#     "John Doe\nSoftware Engineer\nSkills: Python, Java, JavaScript\nExperience: Software Engineer at ABC Inc.",
#     "Jane Smith\nGraphic Designer\nSkills: Adobe Photoshop, Illustrator, InDesign\nExperience: Graphic Designer at XYZ Corp.",
#     "Michael Johnson\nData Scientist\nSkills: Python, R, SQL\nExperience: Data Scientist at Acme Co."
# ]
resumes = [
    "John Doe\nSoftware Engineer\nSkills: Python, Java, JavaScript\nExperience: Software Engineer at ABC Inc. Led a team of 5 developers and implemented new features. Increased code efficiency by 20%.",
    "Jane Smith\nGraphic Designer\nSkills: Adobe Photoshop, Illustrator, InDesign\nExperience: Graphic Designer at XYZ Corp. Designed marketing materials and led creative projects. Developed brand identity guidelines.",
    "Michael Johnson\nData Scientist\nSkills: Python, R, SQL\nExperience: Data Scientist at Acme Co. Analyzed large datasets and built predictive models. Led data-driven decision-making initiatives."
]



# Resume Parsing
def parse_resume(resume_text):
    """
    Parse a resume and extract relevant information.
    """
    skills = extract_skills(resume_text)
    experiences = extract_experiences(resume_text)
    achievements = extract_achievements(resume_text)
    return {
        "skills": skills,
        "experiences": experiences,
        "achievements": achievements
    }

# Skill Extraction with Synonym Matching
def extract_skills(resume_text):
    """
    Extract skills from the parsed resume.
    """
    skills_list = ["python", "machine learning", "data analysis"]
    
    # Define a regular expression pattern to find skill mentions
    pattern = r'\b(?:' + '|'.join(skills_list) + r')\b'
    
    # Extract skills using the pattern
    skills = re.findall(pattern, resume_text, flags=re.IGNORECASE)
    
    return skills

# Experience Extraction with Pattern Matching
def extract_experiences(resume_text):
    """
    Extract experiences from the parsed resume.
    """
    doc = nlp(resume_text)
    experiences = [ent.text for ent in doc.ents if ent.label_ == "ORG" or ent.label_ == "TITLE"]
    return experiences


# Achievement Extraction with Improved Patterns
def extract_achievements(resume_text):
    """
    Extract quantifiable achievements from the parsed resume.
    """
    achievements = []
    pattern = r'(?:increased|decreased|led|managed|developed|implemented) [a-zA-Z]+(?: by)? \d+%?'
    matches = re.findall(pattern, resume_text, flags=re.IGNORECASE)
    for match in matches:
        achievements.append(match.capitalize())  # Capitalize the achievement
    return achievements


# Additional functionality to handle various resume formats and layouts
def extract_information(resume_text):
    """
    Extract information from resumes including personal details, education history, skills, experiences, and achievements.
    """
    return {
        "personal_details": None,  # No placeholder
        "education_history": None,  # No placeholder
        "skills": parse_resume(resume_text)["skills"],
        "experiences": parse_resume(resume_text)["experiences"],
        "achievements": parse_resume(resume_text)["achievements"]
    }


# Example usage
for resume in resumes:
    extracted_info = extract_information(resume)
    print("Personal Details:", extracted_info["personal_details"])
    print("Education History:", extracted_info["education_history"])
    print("Skills:", extracted_info["skills"])
    print("Experiences:", extracted_info["experiences"])
    print("Achievements:", extracted_info["achievements"])
