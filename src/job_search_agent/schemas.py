from pydantic import BaseModel, Field
from typing import List, Optional

# -- Create Pydantic models for Resume structured output --
class ContactInfo(BaseModel):
    """
    Represents the contact information of a person.
    """
    name: str = Field(..., description="Full name of the candidate.")
    location: str = Field(..., description="City and country of the candidate.")
    email: str = Field(..., description="Email address of the candidate.")
    linkedin: Optional[str] = Field(None, description="LinkedIn profile URL of the candidate.")
    github: Optional[str] = Field(None, description="GitHub profile URL of the candidate.")

class WorkExperience(BaseModel):
    """
    Represents a single work experience entry in a resume.
    """
    job_title: str = Field(..., description="Job title held by the candidate.")
    company_name: str = Field(..., description="Name of the company where the candidate worked.")
    dates: str = Field(..., description="Dates of employment (e.g., 'Jan 2020 - Dec 2021').")
    responsibilities: List[str] = Field(..., description="List of key responsibilities in the role.")

class Education(BaseModel):
    """
    Represents a single education entry in a resume.
    """
    degree: str = Field(..., description="Degree obtained (e.g., 'Bachelor of Science').")
    university: str = Field(..., description="Name of the university or institution.")
    dates: str = Field(..., description="Dates of attendance (e.g., '2016 - 2020').")

class Certifications(BaseModel):
    """
    Represents a list of certifications in a resume.
    """
    name: str = Field(..., description="Name of the certification.")
    score: Optional[str] = Field(None, description="Score or grade obtained in the certification, if applicable.")

class Skills(BaseModel):
    """
    Represents a list of skills in a resume.
    """
    technical_tools: List[str] = Field(..., description="List of technical skills and tools.")
    domain_knowledge: List[str] = Field(..., description="List of domain-specific knowledge areas.")
    project_management: List[str] = Field(..., description="List of project management skills.")
    languages: List[str] = Field(..., description="List of languages known.")

class Projects(BaseModel):
    """
    Represents a list of projects in a resume.
    """
    project_name: str = Field(..., description="Name of the project.")
    description: str = Field(..., description="Brief description of the project.")
    link: Optional[str] = Field(None, description="Link to the project or its repository, if available.")

class Resume(BaseModel):
    """
    Represents a structured resume with various sections.
    """
    contact_info: ContactInfo
    summary: str = Field(..., description="Professional summary of the candidate.")
    work_experience: List[WorkExperience]
    education: List[Education]
    certifications: List[Certifications]
    skills: Skills
    projects: List[Projects]
    interests: List[str] = Field(..., description="List of personal interests or hobbies.")

# -- Create Pydantic models for Job Postings structured output --
class JobPosting(BaseModel):
    """
    Represents a single job posting found online.
    """
    job_title: str = Field(..., description="The title of the job position.")
    company_name: str = Field(..., description="The name of the company offering the job.")
    location: str = Field(..., description="The geographical location of the job.")
    job_url: str = Field(..., description="The direct URL to the job posting.")
    description: str = Field(..., description="A detailed description of the job responsibilities and requirements.")
    posted_date: Optional[str] = Field(None, description="The date when the job was posted.")

class JobPostings(BaseModel):
    """
    Represets a collection of job postings.
    """
    job_postings: List[JobPosting] = Field(..., description="A list of job postings retrieved from online sources.")

# -- Create Pydantic models for tailored CV structured output --
class TailoredCV(BaseModel):
    """
    Represents a tailored CV with specific sections for job applications.
    """
    company_name: str = Field(..., description="Name of the company the CV is tailored for.")
    job_title: str = Field(..., description="Job title the CV is tailored for.")
    job_url: str = Field(..., description="URL of the job posting the CV is tailored for.")
    tailored_cv_content: Resume = Field(..., description="The structured resume content tailored for the job application.")

class TailoredCVs(BaseModel):
    """
    Represents a collection of tailored CVs for different job applications.
    """
    tailored_cvs: List[TailoredCV] = Field(..., description="A list of tailored CVs for various job applications.")

# -- Create Pydantic models for tailored Cover Letter structured output --
class TailoredCoverLetter(BaseModel):
    """
    Represents a tailored cover letter for a specific job application.
    """
    company_name: str = Field(..., description="Name of the company the cover letter is tailored for.")
    job_title: str = Field(..., description="Job title the cover letter is tailored for.")
    job_url: str = Field(..., description="URL of the job posting the cover letter is tailored for.")
    cover_letter_content: str = Field(..., description="The content of the tailored cover letter.")

class TailoredCoverLetters(BaseModel):
    """
    Represents a collection of tailored cover letters for different job applications.
    """
    tailored_cover_letters: List[TailoredCoverLetter] = Field(..., description="A list of tailored cover letters for various job applications.")