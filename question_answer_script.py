import requests
import json

# List of 10 questions as per the sample upload request
questions = [
    "What is the grace period for premium payment under the National Parivar Mediclaim Plus Policy?",
    "What is the waiting period for pre-existing diseases (PED) to be covered?",
    "Does this policy cover maternity expenses, and what are the conditions?",
    "What is the waiting period for cataract surgery?",
    "Are the medical expenses for an organ donor covered under this policy?",
    "What is the No Claim Discount (NCD) offered in this policy?",
    "Is there a benefit for preventive health check-ups?",
    "How does the policy define a 'Hospital'?",
    "What is the extent of coverage for AYUSH treatments?",
    "Are there any sub-limits on room rent and ICU charges for Plan A?"
]

# API endpoint URL
url = "http://localhost:8001/api/v1/hackrx/run"

# Authorization token
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": "Bearer 4bdd6eb81f04fa54d3aa5df27c94189a3d87e08a412eb143d2aca614da591b4b"
}

# Prepare the request payload
payload = {
    "documents": "https://hackrx.blob.core.windows.net/assets/policy.pdf?sv=2023-01-03&st=2025-07-04T09%3A11%3A24Z&se=2027-07-05T09%3A11%3A00Z&sr=b&sp=r&sig=N4a9OU0w0QXO6AOIBiu4bpl7AXvEZogeT%2FjUHNO7HzQ%3D",
    "questions": questions
}

def get_answers():
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        result = response.json()
        print("Answers:")
        for i, answer in enumerate(result["answers"]):
            print(f"{i+1}. {answer}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    get_answers()
