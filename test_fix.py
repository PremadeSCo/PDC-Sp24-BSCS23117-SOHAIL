import asyncio
import httpx

async def test():
    url = "http://127.0.0.1:8000/api/generate-challenge"
    headers = {"X-Student-ID": "BSCS23117"}
    payload = {"difficulty": "easy"}

    # send both reqs at ze same time
    async with httpx.AsyncClient() as client:
        responses = await asyncio.gather(
            client.post(url, json=payload, headers=headers, timeout=60),
            client.post(url, json=payload, headers=headers, timeout=60)
        )
        
        for i, r in enumerate(responses):
            print(f"Request {i+1} Status: {r.status_code}")

if __name__ == "__main__":
    asyncio.run(test())
