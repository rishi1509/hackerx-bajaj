import requests
import json

# Test data
test_data = {
    "documents": "https://hackrx.blob.core.windows.net/assets/policy.pdf?sv=2023-01-03&st=2025-07-04T09%3A11%3A24Z&se=2027-07-05T09%3A11%3A00Z&sr=b&sp=r&sig=N4a9OU0w0QXO6AOIBiu4bpl7AXvEZogeT%2FjUHNO7HzQ%3D",
    "questions": [
        "What is the grace period for premium payment under the National Parivar Mediclaim Plus Policy?",
        "What is the waiting period for pre-existing diseases (PED) to be covered?",
        "Does this policy cover maternity expenses, and what are the conditions?"
    ]
}

# Test the /api/v1/hackrx/run endpoint
print("Testing /api/v1/hackrx/run endpoint...")
response = requests.post(
    "http://localhost:8001/api/v1/hackrx/run",
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer 4bdd6eb81f04fa54d3aa5df27c94189a3d87e08a412eb143d2aca614da591b4b"
    },
    data=json.dumps(test_data)
)

print(f"Status Code: {response.status_code}")
if response.status_code == 200:
    result = response.json()
    print("Answers:")
    for i, answer in enumerate(result["answers"]):
        print(f"{i+1}. {answer}")
else:
    print(f"Error: {response.text}")

# Test the /api/v1/hackrx/run_detailed endpoint
print("\nTesting /api/v1/hackrx/run_detailed endpoint...")
response = requests.post(
    "http://localhost:8001/api/v1/hackrx/run_detailed",
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer 4bdd6eb81f04fa54d3aa5df27c94189a3d87e08a412eb143d2aca614da591b4b"
    },
    data=json.dumps(test_data)
)

print(f"Status Code: {response.status_code}")
if response.status_code == 200:
    result = response.json()
    print("Detailed Answers:")
    for i, item in enumerate(result):
        print(f"\n{i+1}. Question: {item['question']}")
        print(f"   Answer: {item['answer']}")
        print(f"   Confidence: {item['confidence']}")
        print(f"   Evidence: {len(item['evidence'])} chunks")
else:
    print(f"Error: {response.text}")
