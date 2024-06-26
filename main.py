import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('ResumeDataSet.csv')

data.head()

data.shape

"""# Exploring Categories"""

data['Category'].value_counts()

plt.figure(figsize=(15,5))
sns.countplot(data['Category'])
plt.xticks(rotation=90)
plt.show()

data['Category'].unique()

counts = data['Category'].value_counts()
labels = data['Category'].unique()
plt.figure(figsize=(15,10))

plt.pie(counts,labels=labels,autopct='%1.1f%%',shadow=True, colors=plt.cm.plasma(np.linspace(0,1,3)))
plt.show()

"""# Exploring Resume"""

data['Category'][0]

data['Resume'][0]

# Cleaning Data:

import re
def cleanResume(txt):
    clean_text = re.sub('http\S+\s', ' ', txt)
    clean_text = re.sub('RT|cc', ' ', clean_text)
    clean_text = re.sub('#\S+\s', ' ', clean_text)
    clean_text = re.sub('@\S+', '  ', clean_text)
    clean_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', clean_text)
    clean_text = re.sub(r'[^\x00-\x7f]', ' ', clean_text)
    clean_text = re.sub('\s+', ' ', clean_text)
    return clean_text

data['Resume'] = data['Resume'].apply(lambda x: cleanResume(x))

data['Resume'][0]

"""# words into categorical values"""

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

le.fit(data['Category'])
data['Category'] = le.transform(data['Category'])

data.Category.unique()

# ['Data Science', 'HR', 'Advocate', 'Arts', 'Web Designing',
#        'Mechanical Engineer', 'Sales', 'Health and fitness',
#        'Civil Engineer', 'Java Developer', 'Business Analyst',
#        'SAP Developer', 'Automation Testing', 'Electrical Engineering',
#        'Operations Manager', 'Python Developer', 'DevOps Engineer',
#        'Network Security Engineer', 'PMO', 'Database', 'Hadoop',
#        'ETL Developer', 'DotNet Developer', 'Blockchain', 'Testing'],
#       dtype=object)

"""# Vactorization"""

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')

tfidf.fit(data['Resume'])
requredText  = tfidf.transform(data['Resume'])

"""# Splitting"""

from sklearn.model_selection import train_test_split

x_train, x_train, y_train, y_test = train_test_split(requredText, data['Category'], test_size=0.2, random_state=42)

x_train.shape

x_train.shape

"""# Now let’s train the model and print the classification report:"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score

clf = OneVsRestClassifier(KNeighborsClassifier())
clf.fit(x_train,y_train)
ypred = clf.predict(x_train)
print(accuracy_score(y_test,ypred))

ypred

"""# Prediction System"""

import pickle
pickle.dump(tfidf,open('tfidf.pkl','wb'))
pickle.dump(clf, open('clf.pkl', 'wb'))

!pip install PyPDF2
!pip install docx2txt

import PyPDF2

def pdftotext(file_name):
  with open('Resume.pdf', 'rb') as f:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(f)

    # Get the number of pages in the PDF file
    num_pages = len(pdf_reader.pages)

    # Extract text from each page
    text = []
    for page_num in range(num_pages):
      page = pdf_reader.pages[page_num]
      text.append(page.extract_text())

    # Combine the extracted text into a single string
    text = ''.join(text)

    return text

import docx2txt

def docxtotext(file_name):
  docx_file_path = file_name

  # Extract text from the docx file
  text = docx2txt.process(docx_file_path)

  return text

def txttotext(file_name):
  with open(file_name, 'r') as file:
    text = file.read()
  return text

import pickle

def predict_resume(resume):
  # Load the trained classifier
  clf = pickle.load(open('clf.pkl', 'rb'))

  # Clean the input resume
  cleaned_resume = cleanResume(resume)

  # Transform the cleaned resume using the trained TfidfVectorizer
  input_features = tfidf.transform([cleaned_resume])

  # Make the prediction using the loaded classifier
  prediction_id = clf.predict(input_features)[0]

  # Map category ID to category name
  category_mapping = {
      15: "Java Developer",
      23: "Testing",
      8: "DevOps Engineer",
      20: "Python Developer",
      24: "Web Designing",
      12: "HR",
      13: "Hadoop",
      3: "Blockchain",
      10: "ETL Developer",
      18: "Operations Manager",
      6: "Data Science",
      22: "Sales",
      16: "Mechanical Engineer",
      1: "Arts",
      7: "Database",
      11: "Electrical Engineering",
      14: "Health and fitness",
      19: "PMO",
      4: "Business Analyst",
      9: "DotNet Developer",
      2: "Automation Testing",
      17: "Network Security Engineer",
      21: "SAP Developer",
      5: "Civil Engineer",
      0: "Advocate",
  }

  category_name = category_mapping.get(prediction_id, "Unknown")

  # print("Predicted Category:", category_name)
  # print(prediction_id)
  return category_name

inputtext = input("Enter the File Name: ")
inputtextsplit = inputtext.split(".")
# print(inputtext)
if(inputtextsplit[-1]=='docx'):
  resume = docxtotext(inputtext)
if(inputtextsplit[-1]=='pdf'):
  resume = pdftotext(inputtext)
if(inputtextsplit[-1]=='txt'):
  resume = txttotext(inputtext)

resume_cat = predict_resume(resume)
print("This candidate is suitable for the role "+resume_cat)
# print(resume)
# resume = cleanResume(resume)
# print(resume)
info = extract_candidate_details(resume)
for key, value in info.items():
      print(f"{key}: {value}")
      print("\n")

# Install pytesseract
!pip install pytesseract
!apt install tesseract-ocr

# Import necessary libraries
import cv2
import pytesseract
import spacy
import re

def extract_candidate_details(resume):
  # Load English language model for spaCy
  nlp = spacy.load('en_core_web_sm')

  # Set the path to the Tesseract-OCR executable
  pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

  # Function to extract text from images using Tesseract OCR
  def extract_text_from_image(image_path):
      # Read the image using OpenCV
      image = cv2.imread(image_path)
      # Convert the image to grayscale
      gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      # Use pytesseract to perform OCR on the preprocessed image
      text = pytesseract.image_to_string(gray_image)
      return text

  # Function to extract relevant information from the extracted text using spaCy
  def extract_information_from_text(text):
      # Use spaCy for named entity recognition (NER)
      doc = nlp(text)
      # Initialize variables to store extracted information
      personal_details = {}
      education_history = []
      work_experience = []
      skills = []
      certifications = []

      # Extract information from spaCy document
      for ent in doc.ents:
          if ent.label_ == 'PERSON':
              personal_details['Name'] = ent.text
          elif ent.label_ == 'EMAIL':
              personal_details['Email'] = ent.text
          elif ent.label_ == 'PHONE':
              personal_details['Phone'] = ent.text
          elif ent.label_ == 'ORG':
              if 'University' in ent.text or 'College' in ent.text:
                  education_history.append(ent.text)
              elif 'Company' in ent.text or 'Organization' in ent.text:
                  work_experience.append(ent.text)
          elif ent.label_ == 'DATE':
              if '202' in ent.text:  # Assuming dates containing '202' are related to years
                  if ' - ' in ent.text:  # Education or Work experience duration
                      if 'Bachelor' in ent.text or 'Master' in ent.text:  # Education history
                          education_history.append(ent.text)
                      else:  # Work experience duration
                          work_experience.append(ent.text)
              elif 'Skill' in ent.text:  # Skills section
                  skills.append(ent.text)
              elif 'Certification' in ent.text:  # Certifications section
                  certifications.append(ent.text)

      # Construct dictionary with extracted information
      extracted_information = {
          'Personal Details': personal_details,
          'Education History': education_history,
          'Work Experience': work_experience,
          'Skills': skills,
          'Certifications': certifications
      }
      return extracted_information

  # Function to extract name using regex pattern
  def extract_name(text):
      # Define regex pattern for extracting names
      name_pattern = r'[A-Z][a-z]+(?: [A-Z][a-z]+)*'  # Example pattern for names with capitalization

      # Find all matches of the pattern in the text
      matches = re.findall(name_pattern, text)

      # Return the first match as the name
      if matches:
          return matches[0]
      else:
          return None

  # Function to extract personal details using regex
  def extract_personal_details(text):
      # Define regular expressions for extracting personal details
      name_pattern = r'([A-Z][a-z]+(?: [A-Z][a-z]+)*)'
      email_pattern = r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
      phone_pattern = r'(\(\d{3}\) \d{3} - \d{4})'

      # Extract personal details using regular expressions
      name = re.search(name_pattern, text).group(1)
      email = re.search(email_pattern, text).group(1)
      phone = re.search(phone_pattern, text).group(1)

      return {'Name': name, 'Email': email, 'Phone': phone}

  # Function to extract education history using regex
  def extract_education_history(text):
      # Define regular expressions for extracting education history
      education_pattern = r'EDUCATION\n(.+?)(?:INTERNSHIP EXPERIENCE|VOLUNTEER WORK|PROJECT|$)'

      # Extract education history using regular expressions
      education_matches = re.search(education_pattern, text, re.DOTALL)
      if education_matches:
          education = education_matches.group(1).strip()
      else:
          education = ""

      return {'Education': education}

  # Function to extract work experience using regex
  def extract_work_experience(text):
      # Define regular expressions for extracting work experience
      work_pattern = r'INTERNSHIP EXPERIENCE\n(.+?)(?:VOLUNTEER WORK|PROJECT|$)'

      # Extract work experience using regular expressions
      work_matches = re.search(work_pattern, text, re.DOTALL)
      if work_matches:
          work_experience = work_matches.group(1).strip()
      else:
          work_experience = ""

      return {'Work Experience': work_experience}

  # Function to extract skills using regex
  def extract_skills(text):
      # Define regular expressions for extracting skills
      skills_pattern = r'Languages: (.+?)\n'

      # Extract skills using regular expressions
      skills_matches = re.search(skills_pattern, text)
      if skills_matches:
          skills = skills_matches.group(1).strip()
      else:
          skills = ""

      return {'Skills': skills}

  # Function to extract certifications using regex
  def extract_certifications(text):
      # Define regular expressions for extracting certifications
      certifications_pattern = r'Certifications: (.+?)\n'

      # Extract certifications using regular expressions
      certifications_matches = re.search(certifications_pattern, text)
      if certifications_matches:
          certifications = certifications_matches.group(1).strip()
      else:
          certifications = ""

      return {'Certifications': certifications}

  def extract_information_from_resume(resume_text):
      # Extract information using defined functions
      personal_details = extract_personal_details(resume_text)
      education_history = extract_education_history(resume_text)
      work_experience = extract_work_experience(resume_text)
      skills = extract_skills(resume_text)
      certifications = extract_certifications(resume_text)

      # Combine all extracted information
      extracted_information = {
          **personal_details,
          **education_history,
          **work_experience,
          **skills,
          **certifications
      }

      return extracted_information

  # Provided resume text
  resume_text = resume

  # resume_text = """
  """S*********r V***y S******a K******n
  v***y@gmail.com  | (476) 424 - 5555  | www.linkedin.com/in/s**y  | Website
  SUMMARY
  * Dedicated Computer Science graduate student knowledgeable in Cybersecurit y, Networks,  Software Development.
  Possesses excellent client management skills and the ability to multitask effectively.
  * Familiar with Languages: Python, Java, C, C++ , SQL , HTML, CSS, JavaScript.
  * Familiar with Tools: Git Hub, Visual Studio Code, Burp Suite, Nessus, Nmap , MS Word, MS Excel, MS PowerPoint .
  * Knowledgeable in Operating Systems: Windows, LINUX.

  EDUCATION
  University of New Haven          West Haven, CT
  Master  of Science , Computer Science  | CGPA:4/4       May 2025

  Vellore Institute of Technology         Chennai, India
  Bachelor of Technology, Electronics and Communication  | CGPA:8.57/10    May 2023

  INTERNSHIP EXPERIENCE
  SecureITSSLab            Remote
  Consultant          Oct 2022 – Jun 2023
  * Developed and implemented data protection policies and procedures to ensure the confidentiality, integrity, and
  availability of sensitive information,  specifically PII information.
  * Assisted in the development and implementation of data protection strategies for identified data elements.
  * Conducted regular audits of data protection processes and recommended improvements to ensure compliance with
  industry best practices.
  * Conducted business impact assessment exercises and developed Business Continuity Plans for various clients in the
  Philippines and  Kingdom of Bahrain.
  * Assisted in ISO Compliance project for various clients where the goal was to identify control weaknesses and provide
  ideas  to strengthen the current control environment based on controls defined in ISO 27001 , 27701 , 22301.
  Research          Jul 2022 – Sep 2022
  * Researched different domains in cybersecurity  and application of cybersecurity in various Industries, especially
  Banking , Financial Services  and NIST Framework .
  * Performed External and Internal Vulnerability Assessment, External and Internal Penetration Testing , and Brand
  Assessment  to test the integrity of company’s website and networks .
  VOLUNTEER  WORK
  Vellore Institute of Technology , Rotary Club       Chennai, India
  Club Service Member          Jul 2021 – May 2022
  * Effectively contributed to activities like event management, and resource management of all related events,
  especially the blood donation camp conducted in the academic year.
  PROJECT
  Blog Site  – (Python , HTML, CSS, JavaScript )
  * Created a blog post site using HTML, CSS and JavaScript for frontend and Flask for backend to make the website
  dynamic.
  Rain Alert via SMS  – (Python)
  * Created a rain alert project in python which collects weather data from Open weather using API and sends SMS to
  your mobile using Twilio API by analyzing the weather data.
  Stock Trading News alert – (Python)
  * Created a stock trading alert project in python which collects data from Alpha vantage API and sends alerts via SMS to
  your mobile using Twilio API by analyzing the stock price data .
  """

  # Extract information from resume text
  extracted_info = extract_information_from_resume(resume_text)
  return extracted_info
  # print(extracted_info)
  # for key, value in extracted_info.items():
  #     print(f"{key}: {value}")
  #     print("\n\n")
