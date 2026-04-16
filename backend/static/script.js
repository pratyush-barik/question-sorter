let syllabusFile = null;
let questionFile = null;

const syllabusInput = document.getElementById("syllabus");
const questionInput = document.getElementById("questions");
const button = document.getElementById("generateBtn");
const status = document.getElementById("status");

// Handle syllabus upload
syllabusInput.addEventListener("change", (e) => {
  syllabusFile = e.target.files[0];
});

// Handle question upload
questionInput.addEventListener("change", (e) => {
  questionFile = e.target.files[0];
});

// Handle button click
button.addEventListener("click", async () => {

  if (!syllabusFile || !questionFile) {
    alert("Please upload both files!");
    return;
  }

  button.innerText = "Processing...";
  status.innerText = "⏳ Reading files...";

  try {
    // Read files
    const syllabus = await syllabusFile.text();
    const questions = await questionFile.text();

    status.innerText = "📡 Sending data to server...";

    // Send request
    const res = await fetch("/process", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        syllabus: syllabus,
        questions: questions
      })
    });

    if (!res.ok) {
      const errText = await res.text();
      throw new Error(errText);
    }

    status.innerText = "⚙️ Processing data...";

    const data = await res.json();

    if (data.error) {
      throw new Error(data.error);
    }

    status.innerText = "📄 Generating PDF...";

    // Download PDF
    const link = document.createElement("a");
    link.href = "data:application/pdf;base64," + data.file;
    link.download = "output.pdf";
    link.click();

    status.innerText = "✅ PDF generated and downloaded successfully!";

  } catch (err) {
    console.error(err);
    status.innerText = "❌ Error: " + err.message;
    alert("Error: " + err.message);
  }

  button.innerText = "Generate Mapping";
});
