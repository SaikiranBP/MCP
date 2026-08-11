# Python Model Context Protocol (MCP) Server & Client

A simple implementation of a Model Context Protocol (MCP) server and client in Python using the official `mcp` SDK.

This repository demonstrates how to expose tools, resources, and prompts from an MCP server using standard I/O (stdio) transport, and how an MCP client can connect, list tools, and invoke tool calls programmatically.
## 📁 Repository Structure
```text
.
├── server.py         # MCP server defining tools, resources, and prompts
├── requirements.txt  # Python package dependencies
```

## ✨ Features

### MCP Server (`server.py`)
- **Tools**:
  - `add(a, b)`: Adds two integers.
  - `multiply(a, b)`: Multiplies two integers.
  - `greet(name)`: Returns a personalized greeting string.

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
```bash
uv run mcp dev server.py
```