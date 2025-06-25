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
├── main.py                   
├── models.py                
├── nif_client.py             
├── utils.py                
├── requirements.txt          
├── Dockerfile              
├── package.json             
└── .smithery.profile.json    
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

## Claude Desktop Integration

To integrate this MCP with Claude Desktop:

1. **Install Claude Desktop**  
   Download and install from: [https://claude.ai/download](https://claude.ai/download)

2. **Open Configuration**  
   Go to `File > Settings > Developer` and click **Edit Configuration**

3. **Add the MCP server configuration**  
   In the `claude_desktop_config.json`, insert the following configuration:

```json
{
  "mcpServers": {
    "nif-pt-server": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/YOUR/PROJECT/FOLDER",
        "run",
        "main.py"
      ]
    }
  }
}
```

> Replace `/ABSOLUTE/PATH/TO/YOUR/PROJECT/FOLDER` with the actual absolute path where your `main.py` file is located.

4. **Restart Claude Desktop**  
   After saving the configuration, restart Claude Desktop. Your `nif-pt-server` MCP should now be available in the Claude Desktop interface.

---


## One-Click Installation via Smithery

With Claude Desktop open, you can install this MCP directly using the Smithery CLI.  
Just paste the following command into your terminal:

```bash
npx -y @smithery/cli@latest install @ruicarvalho1/mcp_nif --client claude
```

This will automatically install the MCP and register it with Claude Desktop.

---

## Author

Developed by Rui Carvalho.

---

## License

This project is licensed under the MIT License.

