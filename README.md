# 🎯 Job Search Automation Crew

This project automates the job application process using an agent-based architecture powered by [CrewAI](https://github.com/joaomdmoura/crewAI). It parses a user's resume, finds matching job listings online, generates tailored CVs and personalized cover letters, and organizes the output in a structured folder format.

## ⚠️ Disclaimer

This tool **does not fabricate or generate** your resume from scratch. It only **rewrites your existing CV** to better align with specific job descriptions and improve **ATS (Applicant Tracking System)** compatibility.

You must supply your real, valid resume in the `input/` folder. The system enhances it based on real job postings, but **does not invent experience, skills, or credentials**.

## 🚀 Features

- ✅ **CV Parsing** from `.pdf`, `.docx`, `.txt`, or `.md`
- 🌍 **Job Search** using Serper.dev and website scraping tools
- ✍️ **Tailored CV and Cover Letter Generator** aligned with job descriptions
- 📂 **Organized Output** in per-company/job-title folders
- 🤖 Fully modular agents and task definitions via YAML

## 📁 Project Structure

```bash
. 
├── input/ # Place your CV file here (.pdf, .docx, .txt, .md) 
├── output/ # Generated output files and organized folders 
├── src/ 
│ └── job_search_agent/ 
│ ├── crew.py # Main crewAI agent/task definitions 
│ ├── main.py # Entrypoint for running/training/testing the crew 
│ ├── schemas.py # Pydantic models for structured data 
│ ├── config/ 
│ │ ├── agents.yaml 
│ │ └── tasks.yaml 
│ └── tools/ 
│     └── custom_tool.py # Custom tools for agents
├── pyproject.toml # Project metadata and dependencies 
├── .env # Environment variables (API keys, model names) 
├── README.md # Project documentation 

```

## 🧠 Workflow Overview

```text
[ Resume File ]
      │
      ▼
[ CV Parser Agent ]
      │
      ▼
[ Search Jobs Agent ] ← Web scraping and search APIs
      │
      ▼
 ┌─────────────────────────────┐
 │                             │
 │ [ Tailor CV Agent ]         │
 │ [ Cover Letter Agent ]      │
 │   (run in parallel)         │
 └─────────────────────────────┘
      │
      ▼
[ Output Organizer ] → Structured folders + Word documents
```

## 🧪 Supported Input Formats

Place your resume inside the `input/` directory. Supported file types:

- `.pdf`
- `.docx`
- `.txt`
- `.md`

## 📦 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/abcxyz91/job_search_agent
   cd job_search_agent
   ```

2. **Install dependencies:**
   ```bash
   # Install Python >= 3.10
    https://www.python.org/downloads/

    # Install uv package manager
    https://docs.astral.sh/uv/getting-started/installation/

    # Install crewai
    uv tool install crewai

    # Refer to crewai installation guide if you encounter errors
    https://docs.crewai.com/installation

    # Install dependencies
    crewai install
   ```

3. **Set up environment variables:**

   Create a `.env` file in the root directory:

   ```env
   MODEL=generation-model-name
   GEMINI_API_KEY=your-gemini-api-key
   SERPER_API_KEY=your-serper-api-key
   ```

- Google Gemini API key (register free from [Google AI Studio](https://aistudio.google.com/apikey))
- Serper.dev API key (register free from [serper.dev](https://serper.dev/api-key))

4. **Add your resume:**

   Place your resume inside the `input/` folder using one of the supported formats.

## ⚙️ Configuration

### 🔹 Agent Config (`agents.yaml`)
Defines each agent's personality, goals, and tools.

### 🔹 Task Config (`tasks.yaml`)
Defines each task’s description, expected output schema, and execution behavior.

## 🛠️ How to Run

From the main script or interactive session:

```bash
# Use the following command to run the program
crewai run
```

The agents will parse your resume, find job postings, generate tailored CVs and cover letters, and save them to `output/`.

## 🧾 Output Example

For a job at **Google** as a **Data Scientist**, this folder will be created:

```
output/Google-Data_Scientist/
├── cv.docx
└── cover_letter.docx
```

## 🧰 Tools Used

- `crewAI` for orchestrating agents and tasks
- `Google Gemini API` for LLM tasks
- `pdfplumber`, `python-docx` for parsing and writing documents
- `Serper.dev API`, `BeautifulSoup4` for job search and scrape
- `pydantic` for strict schema validation
- `dotenv` for environment variable management

## 📌 Notes

- Ensure your API keys are valid before execution.
- The first valid resume file in the `input/` directory will be used.
- Outputs are structured to match each job application.

## 📄 License

MIT License. See `LICENSE` file for details.

## 🤝 Contributing

Contributions, issue reports, and feature suggestions are welcome.
