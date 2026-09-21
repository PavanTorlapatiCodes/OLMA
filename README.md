# 🤖 OLMA — Ollama Local AI Assistant

OLMA is a simple AI assistant application built with **Python, Streamlit, and Ollama**. It allows users to enter a prompt and receive an AI-generated response using a locally running **Gemma 3** language model.

The project demonstrates how to connect a Python application with a local Large Language Model (LLM) through the Ollama Python client.

---

## 🚀 Features

- 🤖 AI-powered chat interface
- 🧠 Uses the **Gemma 3** local language model
- 🖥️ Simple and interactive Streamlit UI
- 🔒 Runs the AI model locally through Ollama
- ⚡ Generates responses directly from user prompts
- 🐍 Built using Python
- 🔌 Uses the Ollama Python client

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Ollama**
- **Gemma 3 LLM**

---

## 🏗️ Project Architecture

```text
User
  ↓
Streamlit Web Interface
  ↓
Python Application
  ↓
Ollama Python Client
  ↓
Ollama Local Server
  ↓
Gemma 3 Model
  ↓
AI Generated Response
```

---

## 📁 Project Structure

```text
OLMA/
│
├── olm.py
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

| File | Description |
|---|---|
| `olm.py` | Main Streamlit application |
| `requirements.txt` | Required Python packages |
| `README.md` | Project documentation |
| `.gitignore` | Files excluded from Git |

---

## ⚙️ Requirements

Before running this project, install:

1. Python
2. Ollama
3. Required Python packages
4. Gemma 3 model

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/PavanTorlapatiCodes/OLMA.git
```

Go inside the project folder:

```bash
cd OLMA
```

---

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Install Ollama

Download and install Ollama from the official Ollama website.

After installation, verify it:

```bash
ollama --version
```

---

### 4. Download the Gemma Model

Pull the model used by the project:

```bash
ollama pull gemma3:270m
```

Make sure Ollama is running locally.

The application connects to:

```text
http://localhost:11434
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run olm.py
```

After running the command, Streamlit will provide a local URL.

Open the URL in your browser and enter your prompt.

---

## 💡 How It Works

The application follows a simple workflow:

1. User enters a prompt in the Streamlit interface.
2. The Python application receives the prompt.
3. The Ollama Python client sends the prompt to the local Ollama server.
4. Ollama processes the request using the Gemma 3 model.
5. The generated response is returned to the Python application.
6. Streamlit displays the response to the user.

---

## 🎯 Project Objective

The main objective of OLMA is to understand how a Python application can interact with a locally running Large Language Model.

This project provides practical experience with:

- Local LLM integration
- Ollama
- Python AI application development
- Streamlit
- Prompt-based interaction
- API/client communication

---

## 🔐 Local AI

OLMA uses Ollama to run the language model locally.

The application communicates with the local Ollama server rather than directly depending on a cloud-based LLM API.

---

## 👨‍💻 Author

**Pavan Kumar Torlapati**

GitHub:  
https://github.com/PavanTorlapatiCodes

LinkedIn:  
https://linkedin.com/in/pavan-torlapati-7543732ba

---

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.
