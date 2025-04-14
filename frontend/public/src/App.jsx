import React from "react";
import UploadForm from "./components/UploadForm";
function App() {
    return (
        <div>
            <h1>Smart Resume Analyzer</h1>
            <UploadForm />
        </div>
    );
}
export default App;

// firebaseConfig.js
import { initializeApp } from "firebase/app";
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT_ID.appspot.com",
    messagingSenderId: "SENDER_ID",
    appId: "APP_ID"
};
const app = initializeApp(firebaseConfig);
export default app;