import httpx
from urllib.parse import quote

NIFPT_API_URL = "https://www.nif.pt/?json=1&q="
API_KEY = "98eda15d86624a3b57223c7dde7dba50"

async def fetch_company_by_nif(nif: str):
    url = f"{NIFPT_API_URL}{nif}&key={API_KEY}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        return resp.json()

async def fetch_companies_by_term(term: str):
    formatted_term = quote(term)
    url = f"{NIFPT_API_URL}{formatted_term}&key={API_KEY}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        return resp.json()
