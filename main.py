from fastmcp import FastMCP
from models import Company
from nif_client import fetch_company_by_nif, fetch_companies_by_term
from utils import is_valid_nif, format_company

mcp = FastMCP(name="NIF.PT Server")

async def get_company_data(nif: str, api_key: str) -> Company | None:
    if not is_valid_nif(nif):
        return None
    data = await fetch_company_by_nif(nif, api_key)
    record = data.get("records", {}).get(nif)
    if not record:
        return None
    cae_value = record.get("cae")
    if isinstance(cae_value, str):
        cae_value = [cae_value]
    return Company(
        nif=nif,
        name=record.get("title", ""),
        city=record.get("city", ""),
        activity=record.get("activity", ""),
        status=record.get("status", ""),
        address=record.get("address", ""),
        phone=record.get("contacts", {}).get("phone"),
        email=record.get("contacts", {}).get("email"),
        website=record.get("contacts", {}).get("website"),
        cae=cae_value or [],
        racius=record.get("racius"),
        portugalio=record.get("portugalio")
    )

@mcp.tool()
async def get_company(nif: str, api_key: str) -> str:
    company = await get_company_data(nif, api_key)
    if not company:
        return "Invalid NIF or company not found."
    return format_company(company)

@mcp.tool()
async def is_accounting_company(nif: str, api_key: str) -> str:
    company = await get_company_data(nif, api_key)
    if not company:
        return "Company not found or invalid NIF."
    keywords = ["accounting", "accountant", "tax consulting", "financial management"]
    if any(p in company.activity.lower() for p in keywords):
        return f"The company with NIF {nif} is related to accounting."
    return f"The company with NIF {nif} does not appear to be related to accounting."

@mcp.tool()
async def is_active(nif: str, api_key: str) -> str:
    company = await get_company_data(nif, api_key)
    if not company:
        return "Company not found or invalid NIF."
    if "active" in company.status.lower():
        return f"The company with NIF {nif} is active."
    return f"The company with NIF {nif} is inactive or closed."

@mcp.tool()
async def search_companies_by_name_and_city(name: str, city: str, api_key: str) -> str:
    term = f"{name} {city}"
    data = await fetch_companies_by_term(term, api_key)
    if not data or "records" not in data or not data["records"]:
        return f"No companies found for '{term}'."
    results = []
    for nif, record in data["records"].items():
        cae_value = record.get("cae")
        if isinstance(cae_value, str):
            cae_value = [cae_value]
        company = Company(
            nif=nif,
            name=record.get("title", ""),
            city=record.get("city", ""),
            activity=record.get("activity", ""),
            status=record.get("status", ""),
            address=record.get("address", ""),
            cae=cae_value or []
        )
        results.append(format_company(company))
    return "\n\n---\n\n".join(results[:5])

@mcp.tool()
async def find_nif_by_name(name: str, api_key: str) -> str:
    data = await fetch_companies_by_term(name, api_key)
    if not data or "records" not in data or not data["records"]:
        return f"No companies found for '{name}'."
    for nif, record in data["records"].items():
        if record.get("title", "").lower() == name.lower():
            return f"The NIF of the company '{name}' is {nif}."
    return f"NIF not found based on exact name match '{name}'."


if __name__ == "__main__":
    import os
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        base_path="/mcp"
    )