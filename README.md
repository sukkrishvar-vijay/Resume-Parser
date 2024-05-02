# Resume-Parser

1. Setup and Installation:

• Ensure you have Python installed on your system.

2. Data Preparation:

• Prepare your resume dataset in CSV format similar to 'ResumeDataSet.csv' provided in the project.
• Ensure it contains columns for 'Category' (job categories) and 'Resume' (textual content of resumes).

3. Training the Model:

• Run the provided code to preprocess the data, train the model, and serialize the trained components (TF-IDF vectorizer and classifier).
• This step involves executing the Python script or notebook containing the code snippets provided in the project.

4. Utilizing the Trained Model:
• Once the model is trained and saved, you can use it to classify new resumes and extract candidate information.
• For classifying a new resume, provide the resume file (PDF, DOCX or TXT format) to the provided functions (pdftotext(), docxtotext(), txttotext(), predict_resume()).
• The predict_resume() function will return the predicted job category for the candidate based on their resume content.

5. Extracting Candidate Information:
• Similarly, you can use the extract_candidate_details() function to extract relevant details from a resume text.
• Provide the resume text to this function, and it will return a dictionary containing extracted personal details, education history, work experience, skills, and certifications.

6. Interpreting Results:
• Once you have classified a resume or extracted candidate information, interpret the results to make informed decisions in the recruitment process.
• The predicted job category can guide you in matching candidates to suitable roles, while the extracted information can provide insights into a candidate's qualifications and experience.

7. Integration:
• Integrate the provided functionalities into your recruitment pipeline or application as needed.
• You can automate the processing of resumes, classification of candidates, and extraction of relevant information to streamline your hiring process.
• By following these steps one can effectively utilize the provided project for resume classification and candidate information extraction in recruitment workflow.
