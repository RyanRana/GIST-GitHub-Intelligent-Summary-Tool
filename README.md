# GIST: GitHub's Intelligent Summary Tool

## Overview

GIST: GitHub's Intelligent Summary Tool provides comprehensive insights into any GitHub repository. By simply inputting a repository URL, users can access information such as repository stars, collaborators, commit histories, and more. Additionally, GIST integrates a chatbox powered by OpenAI's GPT, enabling users to ask questions about the repository and receive intelligent responses. The tool also features graphical and data representations of the repository's details. With GIST, navigating GitHub repositories has never been easier or more insightful.

## Features

- Input GitHub repository URL to retrieve data.
- Display repository stars.
- List repository collaborators.
- Show commit histories.
- Provide a chatbox powered by OpenAI's GPT for user queries.
- Graphical representation of repository details (e.g., stars over time, commit frequency).


## Installation

### Prerequisites
- Python 3.8 or above
- Streamlit
- Flask
- OpenAI API key

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/GIST.git
   cd GIST  
2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Set up the OpenAI API key:**
   ```bash
   export OPENAI_API_KEY='your-openai-api-key'
4. **Run the backend server:**
   ```bash
     python backend.py
5. **Run the Streamlit app:**
   ```bash
     streamlit run streamlit_app.py
6. **Open your browser and go to:** http://localhost:8501

Run the Flask server:
bash
Copy code
python server.py
Open your web browser and navigate to http://127.0.0.1:5000/ to interact with the chatbox and fetch GitHub repository data.
