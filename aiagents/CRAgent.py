import requests
import json
from langchain.llms import VertexAI
import os
  # You can replace this with your preferred LLM integration (e.g., VertexAI)

# ---------------------------
# Configure GitHub API credentials
# ---------------------------
GITHUB_TOKEN = "token"
REPO_OWNER = "repo_owner"
REPO_NAME = "repo_name"
PULL_REQUEST_NUMBER = 2  # Example PR number

# GitHub API endpoints
GET_PR_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{PULL_REQUEST_NUMBER}"
POST_COMMENT_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues/{PULL_REQUEST_NUMBER}/comments"
GET_DIFF_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{PULL_REQUEST_NUMBER}"

google_credentials_path = "path of google credentials file"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = google_credentials_path

headers_json = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

headers_diff = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3.diff"
}
# Fetch the pull request details
pr_response = requests.get(GET_PR_URL, headers=headers_json)
if pr_response.status_code != 200:
    raise Exception(f"Failed to fetch PR details: {pr_response.content}")

pr_data = pr_response.json()
pr_title = pr_data.get("title", "")
pr_body = pr_data.get("body", "")

# Fetch the diff or file changes
diff_response = requests.get(GET_DIFF_URL, headers=headers_diff)
if diff_response.status_code != 200:
    raise Exception(f"Failed to fetch diff: {diff_response.content}")

pr_diff = diff_response.text  # This is the diff in text format

# ---------------------------
# Step 4: Define the prompt for the LLM using both PR details and the diff
# ---------------------------
prompt = f"""
You are an AI code reviewer specialized in identifying issues, suggesting improvements, and ensuring code quality. 

Here is a pull request for review:

Title: {pr_title}

Description: {pr_body}

The following is the diff (changed code) from the pull request:
------------------------------------------------------------
{pr_diff}
------------------------------------------------------------

Please review the changes in the diff and provide detailed review comments, highlighting any potential bugs, code quality issues, design improvements, and suggestions for better practices.
"""

# ---------------------------
# Step 2: Use LangChain to generate review comments using an LLM
# ---------------------------
# Initialize the LLM (this example uses OpenAI)
llm = VertexAI(
    model_name="model_name",   # specify the Gemini model version
    project="project_name",
    location="project_location",   # or another appropriate region
    temperature=0.2
)

# Generate review comments based on the PR input.
review_comments = llm(prompt)

# For debugging: print the generated review comments
print("Generated Review Comments:")
print(review_comments)

# ---------------------------
# Step 3: Post the review comments to the pull request via GitHub API
# ---------------------------
payload = {
    "body": review_comments
}

post_response = requests.post(POST_COMMENT_URL, headers=headers_json, data=json.dumps(payload))
if post_response.status_code != 201:
    raise Exception(f"Failed to post review comment: {post_response.content}")
else:
    print("Review comment posted successfully!")