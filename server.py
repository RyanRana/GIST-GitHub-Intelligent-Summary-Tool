from flask import Flask, request, jsonify, send_from_directory
import requests
import openai
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Initialize OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Store conversation history
conversation_history = []

# GitHub API headers
headers = {'Authorization': 'token YOUR_GITHUB_TOKEN'}

def fetch_repo_data(repo_url):
    api_url = f"https://api.github.com/repos/{repo_url.strip('https://github.com/')}"
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def fetch_commit_history(repo_url):
    api_url = f"https://api.github.com/repos/{repo_url.strip('https://github.com/')}/commits"
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch commits: {response.status_code}")

def fetch_contributors(repo_url):
    api_url = f"https://api.github.com/repos/{repo_url.strip('https://github.com/')}/contributors"
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch contributors: {response.status_code}")

def process_repo_data(repo_data, commit_history, contributors):
    processed_data = {
        'name': repo_data.get('name'),
        'stars': repo_data.get('stargazers_count'),
        'forks': repo_data.get('forks_count'),
        'open_issues': repo_data.get('open_issues_count'),
        'watchers': repo_data.get('subscribers_count'),
        'description': repo_data.get('description'),
        'owner': repo_data.get('owner', {}).get('login'),
        'commit_history': commit_history,
        'contributors': contributors
    }
    return processed_data

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    global conversation_history

    # Append the user's message to the conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Generate a response using OpenAI's GPT-3
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )

    # Get the reply from the assistant
    assistant_reply = response.choices[0].message['content']

    # Append the assistant's reply to the conversation history
    conversation_history.append({"role": "assistant", "content": assistant_reply})

    return jsonify({"response": assistant_reply})

@app.route('/repo', methods=['POST'])
def get_repo_data():
    repo_url = request.json.get('repo_url')
    repo_data = fetch_repo_data(repo_url)
    commit_history = fetch_commit_history(repo_url)
    contributors = fetch_contributors(repo_url)
    processed_data = process_repo_data(repo_data, commit_history, contributors)
    return jsonify(processed_data)

@app.route('/visualize', methods=['POST'])
def visualize_data():
    data = request.json
    dates = [commit['commit']['author']['date'][:10] for commit in data['commit_history']]
    stars = [commit['commit']['message'].count('star') for commit in data['commit_history']]  # Simplified example

    plt.figure(figsize=(10, 5))
    plt.plot(dates, stars, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Stars')
    plt.title('Stars Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return jsonify({'plot_url': f'data:image/png;base64,{plot_url}'})

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
