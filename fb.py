
import requests

# Set your GitHub username, repository name, and access token
username = 'ankit848'
repository = 'cloner'
token = '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'

# Define file path
file_path = '/sdcard/old.txt'

# Read file contents
with open(file_path, 'rb') as file:
    file_contents = file.read()

# Set upload URL
url = f'https://api.github.com/repos/{username}/{repository}/contents/{file_path}'

# Set commit message
commit_message = 'Add photo'

# Set request headers
headers = {
    'Authorization': f'token {token}',
    'Content-Type': 'application/json',
}

# Create payload
payload = {
    'message': commit_message,
    'content': file_contents.decode('utf-8'),  # Encode file contents as base64
}

# Make request to upload file
response = requests.put(url, json=payload, headers=headers)

# Check if upload was successful
if response.status_code == 200:
    print('File uploaded successfully.')
else:
    print('Failed to upload file:', response.text)
