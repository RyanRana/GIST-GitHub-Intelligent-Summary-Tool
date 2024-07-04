# GIST: GitHub's Intelligent Summary Tool

## Overview

GIST: GitHub's Intelligent Summary Tool provides comprehensive insights into any GitHub repository. By simply inputting a repository URL, users can access information such as repository stars, collaborators, commit histories, and more. Additionally, GIST integrates a chatbox powered by OpenAI's GPT, enabling users to ask questions about the repository and receive intelligent responses. The tool also features graphical and data representations of the repository's details.

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
   Copy code
   pip install -r requirements.txt
   
3. **Set up the OpenAI API key:**

   ```bash
   Copy code
   export OPENAI_API_KEY='your-openai-api-key'

4. **Run the backend server:**
  ```bash
   Copy code
   python backend.py

5. **Run the Streamlit app:**
  ```bash
   Copy code
   streamlit run streamlit_app.py

Open your browser and go to: http://localhost:8501
