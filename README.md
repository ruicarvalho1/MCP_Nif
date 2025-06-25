# MCP NIF.PT

This project implements an intelligent server based on [FastMCP](https://github.com/antero-ferreira/fastmcp), allowing you to query and analyze information about Portuguese companies using the [NIF.PT](https://www.nif.pt/) public API. It supports multiple useful tools such as search by NIF, company name or city, checking company status, and identifying accounting-related businesses.

---

## Features

- Retrieve complete company data by NIF
- Check if a company is active or closed
- Identify if a company is related to accounting
- Search companies by name and city
- Get the NIF based on the exact company name
- Access external links (Google Maps, Racius, Portugalio)

---

## Project Structure

```
.
├── main.py                   # Entrypoint and MCP tool definitions
├── models.py                 # Pydantic model for the Company entity
├── nif_client.py             # HTTP client for consuming the NIF.PT API
├── utils.py                  # Utility functions (validation, formatting)
├── requirements.txt          # Project dependencies
├── Dockerfile                # Docker configuration
├── package.json              # Optional, used by Smithery
└── .smithery.profile.json    # Smithery integration profile
```

---

## Technologies Used

- FastMCP
- FastAPI
- httpx
- Pydantic
- Docker
- Python 3.10+

---

## How to Run

### Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

The application uses `transport="stdio"` by default, making it compatible with Claude Desktop or terminal-based environments.

### Using Docker

```bash
docker build -t nif-mcp .
docker run -it nif-mcp
```

---

## Usage Examples

- Qual é a empresa com o NIF 504426744?
- A empresa com o NIF 504426744 está ativa?
- A empresa com o NIF 504426744 é de contabilidade?
- Procurar empresas com o nome "contabilidade" em Lisboa
- Qual é o NIF da empresa "XPTO LDA"?

---

## Output Format

The responses include details such as:

- Nome, cidade, atividade e estado
- Morada com link para Google Maps
- Contactos (telefone, email, website)
- CAE (Código de Atividade Económica)
- Ligações externas (Racius, Portugalio)


---

## Author

Developed by Rui Carvalho.

---

## License

This project is licensed under the MIT License.
