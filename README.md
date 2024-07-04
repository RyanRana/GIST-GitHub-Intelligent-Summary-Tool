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

## Architecture Overview

The architecture of GIST is based on a modular design to ensure scalability and maintainability. The main components are:

1. **Frontend (Streamlit)**
2. **Backend (Python with Flask)**
3. **Chatbot (OpenAI GPT)**
4. **Data Fetching and Processing (GitHub API)**

![architecture](https://www.plantuml.com/plantuml/png/SoWkIImgAStDuU9AoKnEJ4vLqDN8pIbApSmfBZ_0Id0_gXfE9QZc3A5N9H6EujDA7Y2rR9mf4NGm0G00)

## Component Details

### Frontend (Streamlit)
- **Description**: Streamlit is used to build an interactive and user-friendly interface.
- **Responsibilities**:
  - Allow users to input GitHub repository URLs.
  - Display repository stars, collaborators, commit histories.
  - Provide graphical representations of repository data.
  - Integrate with the ChatGPT-powered chatbox.

### Backend (Python with Flask)
- **Description**: The backend is developed using Python and Flask, handling all business logic and data processing.
- **Responsibilities**:
  - Manage API requests from the frontend.
  - Fetch data from GitHub API.
  - Process and format data for display.
  - Communicate with the OpenAI GPT for chat responses.

### Chatbot (OpenAI GPT)
- **Description**: OpenAI's GPT is integrated to provide intelligent responses to user queries.
- **Responsibilities**:
  - Process user questions about the repository.
  - Generate relevant and accurate responses based on repository data.

### Data Fetching and Processing (GitHub API)
- **Description**: Data is fetched from GitHub API and processed to be displayed and analyzed.
- **Responsibilities**:
  - Fetch repository stars, collaborators, commit histories, and other relevant data.
  - Process and format data for display.

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
nstall the dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the OpenAI API key:

bash
Copy code
export OPENAI_API_KEY='your-openai-api-key'
Run the backend server:

bash
Copy code
python backend.py
Run the Streamlit app:

bash
Copy code
streamlit run streamlit_app.py
Open your browser and go to:

arduino
Copy code
http://localhost:8501
Usage
Input the GitHub repository URL in the text box.
View the displayed repository stars, collaborators, and commit histories.
Check the graphical representations of repository data.
Use the chatbox to ask questions about the repository.
Contributing
Contributions are welcome! Please fork the repository and create a pull request.
