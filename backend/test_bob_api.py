import asyncio
import httpx
import os

async def test_bob_endpoint():
    """Test Bob AI API endpoint"""
    
    # Load API key from .env
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv("BOB_AI_API_KEY")
    api_url = "https://bob.build.cloud.ibm.com/v1/chat/completions"
    
    print(f"Testing Bob AI API...")
    print(f"URL: {api_url}")
    print(f"API Key: {api_key[:20]}..." if api_key else "No API key found")
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "messages": [
            {
                "role": "user",
                "content": "Say hello"
            }
        ],
        "temperature": 0.7,
        "max_tokens": 100
    }
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            print("\nSending test request...")
            response = await client.post(api_url, headers=headers, json=payload)
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text[:200]}")
            
            if response.status_code == 200:
                print("\n✅ Bob AI API is working!")
            else:
                print(f"\n❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"\n❌ Connection Error: {type(e).__name__}: {str(e)}")
            print("\nPossible issues:")
            print("1. Wrong API URL")
            print("2. Network/DNS issue")
            print("3. Invalid API key")

if __name__ == "__main__":
    asyncio.run(test_bob_endpoint())

# Made with Bob
