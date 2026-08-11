# Python Model Context Protocol (MCP) Server & Client

A simple implementation of a Model Context Protocol (MCP) server and client in Python using the official `mcp` SDK.

This repository demonstrates how to expose tools, resources, and prompts from an MCP server using standard I/O (stdio) transport, and how an MCP client can connect, list tools, and invoke tool calls programmatically.
## 📁 Repository Structure
```text
.
├── server.py         
├── client.py         
├── requirements.txt  
├── .gitignore        
└── README.md         
```

## ✨ Features

### MCP Server (`server.py`)
- **Tools**:
  - `add(a, b)`: Adds two integers.
  - `multiply(a, b)`: Multiplies two integers.
  - `greet(name)`: Returns a personalized greeting string.
- **Resources**:
  - `queue://{facility}/status`: Dynamic resource exposing queue status for a given facility.
- **Prompts**:
  - `analyze_queue(facility)`: Pre-defined prompt template for evaluating facility bottlenecks and waiting times.

### MCP Client (`client.py`)
- Spawns the MCP server sub-process over `stdio`.
- Establishes a `ClientSession`.
- Automatically retrieves and prints registered server tools and schemas.
- Demonstrates executing a tool call (`add`) and printing the result.

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher installed.

### Installation
1. **Create and activate a virtual environment**:
   - **Windows**:
     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```
   - **macOS / Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Running the Code

Execute the client script to automatically launch the MCP server in a subprocess and execute sample tool calls:

```bash
python client.py
```