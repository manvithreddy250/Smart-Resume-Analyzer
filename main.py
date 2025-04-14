from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from utils.extract_text import extract_text_from_pdf
from utils.grammar_check import check_grammar
from utils.match_score import get_similarity_score

import firebase_admin
from firebase_admin import credentials, firestore, storage
import os

# Debug: Print current working directory
print("Current working directory:", os.getcwd())

# Initialize FastAPI app
app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Firebase
cred = credentials.Certificate("backend/firebase_key.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'smart-resume-analyzer.appspot.com'
})

# Firestore client
db = firestore.client()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Resume Analyzer API!"}

# Resume analysis endpoint
@app.post("/analyze")
async def analyze_resume(resume: UploadFile = File(...), jobdesc: UploadFile = File(...)):
    resume_text = await resume.read()
    job_text = await jobdesc.read()

    resume_content = extract_text_from_pdf(resume_text)
    job_content = extract_text_from_pdf(job_text)

    grammar_issues = check_grammar(resume_content)
    score = get_similarity_score(resume_content, job_content)

    return {
        "grammar_issues": grammar_issues,
        "match_score": score
    }

# Firebase test endpoint
@app.get("/test-firebase")
async def test_firebase():
    try:
        # Replace 'users' and 'test_user' with your actual Firestore collection and document ID
        doc_ref = db.collection('users').document('test_user')
        doc = doc_ref.get()

        if doc.exists:
            return {"firebase_data": doc.to_dict()}
        else:
            return {"message": "No such document found in Firestore!"}
    except Exception as e:
        return {"error": str(e)}
