import requests
import json

# The n8n Webhook URL
url = "http://localhost:5678/webhook-test/process-lead"

# The Lead Data
data = {
    "name": "Adarsh",
    "email": "adarsh@example.com",
    "company": "AI Innovators",
    "message": "This is a successful end-to-end test!"
}

print(f"--- Sending Lead to n8n ---")
try:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    print(f"---------------------------")
    if response.status_code == 200:
        print("SUCCESS! Now check your n8n screen for green checkmarks.")
    else:
        print("FAILED! Make sure you clicked 'Execute Workflow' in n8n first.")
except Exception as e:
    print(f"ERROR: Could not connect to n8n. Is Docker running? {str(e)}")
