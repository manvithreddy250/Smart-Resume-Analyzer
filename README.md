Smart Resume Analyzer
Overview:

The Smart Resume Analyzer is an advanced AI tool designed to help job seekers optimize their resumes and match them with job descriptions. Using a combination of FastAPI, spaCy, Sentence-BERT, and Firebase, this tool automatically extracts text from resumes and job descriptions, checks for grammar issues, and calculates a match score to assist with job matching.

Features:
Resume Analysis: Upload a resume and a job description in PDF format to receive a detailed analysis.

Grammar Checking: The AI-powered tool checks for grammar mistakes in resumes.

Job Matching: Calculate a similarity score between your resume and a job description to determine how well the resume fits the job.

Technologies Used:
Backend: FastAPI (for API development)

AI & NLP Tools:

spaCy (for text extraction and processing)

Sentence-BERT (for computing similarity scores)

Cloud Integration:

Firebase (for Firestore database and storage)

Firebase Hosting (for deploying the application)

Frontend: React (for building the web UI)

How to Use:
1. Clone the Repository:

git clone https://github.com/your-username/smart-resume-analyzer.git
cd smart-resume-analyzer
2. Set Up Backend:
Navigate to the backend directory:

cd backend
Install required dependencies:


pip install -r requirements.txt
3. Firebase Setup:
Create a Firebase project on the Firebase Console.

Enable Firestore and Firebase Storage.

Download your firebase_key.json file from the Firebase project settings and place it in the backend folder.

4. Run the Backend API:
Start the FastAPI server:



uvicorn main:app --reload
This will start the backend API at http://127.0.0.1:8000/.

5. Set Up Frontend:
Navigate to the frontend directory.

Install the frontend dependencies:


npm install
Start the frontend server:



npm start
This will start the frontend at http://localhost:3000/.

API Endpoints:
GET /: Welcome message indicating that the API is running.

POST /analyze: Upload your resume and job description in PDF format to analyze grammar and match the job description.

GET /test-firebase: Fetch a sample document from Firebase Firestore for testing purposes.

To Do (Future Enhancements):
UI Improvements: Improve the frontend user interface for better user interaction.

Additional Features: Add more features to enhance job matching and resume analysis.

Cloud Deployment: Deploy the application on a cloud platform for easier access.

License:
This project is licensed under the MIT License.



