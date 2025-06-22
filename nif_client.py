import httpx
from urllib.parse import quote

NIFPT_API_URL = "https://www.nif.pt/?json=1&q="

async def fetch_company_by_nif(nif: str, api_key: str):
    url = f"{NIFPT_API_URL}{nif}&key={api_key}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        return resp.json()

async def fetch_companies_by_term(term: str, api_key: str):
    formatted_term = quote(term)
    url = f"{NIFPT_API_URL}{formatted_term}&key={api_key}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        return resp.json()
