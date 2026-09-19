# AI Resume & Job Description Analyzer

A Python-based tool that analyzes a resume against a job description using rule-based skill matching and a locally hosted Llama 3.2 language model through Ollama.

## Features

- Reads a resume from a text file
- Reads a job description from a text file
- Identifies selected skills and related keywords in the job description
- Compares job requirements with skills listed on the resume
- Calculates a skill match percentage
- Uses a locally hosted Llama 3.2 model to generate an AI-based resume analysis
- Identifies resume strengths
- Identifies important job requirements
- Identifies skills found in the resume
- Identifies missing or weak skills
- Provides evidence for skills found in the resume
- Provides resume improvement suggestions
- Provides an overall analysis of the resume and job description

## Technologies Used

- Python
- Ollama
- Llama 3.2 3B
- Requests
- Git
- GitHub

## How It Works

The project uses two different approaches to analyze the resume.

### 1. Rule-Based Skill Matching

Python reads the resume and job description and searches for predefined skills and related keywords.

The program then:

1. Finds skills mentioned in the job description.
2. Checks whether those skills appear in the resume.
3. Separates matched and missing skills.
4. Calculates a skill match percentage.

### 2. AI Resume Analysis

The resume and job description are then provided to a locally hosted Llama 3.2 model through Ollama.

The AI analyzes the documents and provides:

- Resume strengths
- Important job requirements
- Skills found in the resume
- Missing or weak skills
- Evidence from the resume
- Resume improvement suggestions
- Overall analysis

The prompt instructs the model to use only information provided in the resume and job description and avoid inventing experience or qualifications.

## Example

A sample analysis can produce results such as:

```text
Skill Match Percentage: 77.78%

Matched Skills:
- Python
- Java
- C++
- AI
- Machine Learning
- GitHub
- Data
- Networking

Missing Skills:
- Cybersecurity
- APIs