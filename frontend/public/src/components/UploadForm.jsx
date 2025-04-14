import React, { useState } from "react";
function UploadForm() {
    const [result, setResult] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("resume", e.target.resume.files[0]);
        formData.append("jobdesc", e.target.jobdesc.files[0]);

        const res = await fetch("http://127.0.0.1:8000/analyze", {
            method: "POST",
            body: formData
        });
        const data = await res.json();
        setResult(data);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="file" name="resume" required />
            <input type="file" name="jobdesc" required />
            <button type="submit">Analyze</button>
            {result && (
                <div>
                    <p>Grammar Issues: {result.grammar_issues.length}</p>
                    <p>Match Score: {result.match_score}</p>
                </div>
            )}
        </form>
    );
}
export default UploadForm;
