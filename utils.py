def is_valid_nif(nif: str) -> bool:
    return nif.isdigit() and len(nif) == 9

def format_company(company) -> str:
    address_query = company.address.replace(" ", "+") if company.address else company.city.replace(" ", "+")
    maps_url = f"https://www.google.com/maps/search/?api=1&query={address_query}"

    phone = getattr(company, "phone", "N/A")
    email = getattr(company, "email", "N/A")
    website = getattr(company, "website", "N/A")
    cae = getattr(company, "cae", [])
    racius = getattr(company, "racius", "")
    portugalio = getattr(company, "portugalio", "")

    cae_str = ", ".join(cae) if isinstance(cae, list) else cae

    external_links = ""
    if racius:
        external_links += f"Racius: {racius}\n"
    if portugalio:
        external_links += f"Portugalio: {portugalio}\n"

    return (
        f"Name: {company.name}\n"
        f"City: {company.city}\n"
        f"Activity: {company.activity}\n"
        f"Status: {company.status}\n"
        f"Address: {company.address}\n"
        f"CAE: {cae_str}\n"
        f"Phone: {phone}\n"
        f"Email: {email}\n"
        f"Website: {website}\n"
        f"{external_links}"
        f"Map: {maps_url}"
    )

