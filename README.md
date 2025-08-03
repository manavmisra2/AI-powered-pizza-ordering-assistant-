
## Project Type: Web-based Chat Assistant (Python, HTML/CSS/JS)

### Overview
This project is an **AI-powered pizza ordering assistant** that interacts with users via a simple web-based chat interface. It enables users to place customized pizza orders, share dietary preferences, and receive a structured JSON summary for final confirmation. The assistant also supports **voice interaction**, allowing users to speak their orders naturally.

---

### Architecture
The system is composed of the following components:

#### **Frontend**
- `run_gradio.py`: Launches a Gradio web-based interface for interaction.
- `voice_chatbot.py`: Enables voice input/output interaction.
- `index.html`: (Legacy alternative) Provides static HTML structure.
- `styles.css`: Defines the appearance and responsiveness of the UI.

#### **Backend**
- `dialog_agent.py`: **Core logic handler**. This file communicates directly with the Gemini API and manages the full conversation lifecycle.
- `gemini_client.py`: Supports `dialog_agent.py` by sending structured prompts to the Gemini API and receiving structured responses.
- `order_saver.py`: Saves confirmed orders in JSON, CSV, XML, and SQLite formats.

#### **Logic & Utilities**
- `menu.json`: JSON-based data file defining the available menu.
- `utils.py`: Parses input, formats outputs, and supports order validation.
- `request_counter.txt`: Tracks the number of order sessions.

#### **Additional Assets**
- `.env`: Stores the Gemini API Key.
- `requirements.txt`: Lists all required Python dependencies.

#### **Documentation & Screenshots**
- `README.md`: Contains the full project description and setup guide.
- `docs/`: Folder with flowchart (`Mermaidlive.png`) and screenshots from example user interactions.

---

### Technical Architecture
```plaintext
AI_assistant_project/
├── dialog_agent.py           # Core brain handling conversation flow
├── gemini_client.py          # Handles Gemini API interaction
├── order_saver.py            # Saves orders in multiple formats
├── menu.json                 # Defines pizza menu
├── utils.py                  # Processes orders, formats output
├── request_counter.txt       # Tracks number of requests
├── requirements.txt          # Required Python packages
├── README.md                 # Project report
├── .env                      # API key file
├── run_gradio.py             # Gradio Web UI launcher
├── voice_chatbot.py          # Voice input/output interface
├── templates/
│   └── index.html            # Frontend HTML page (optional)
├── static/
│   └── styles.css            # Frontend styling
└── docs/
    ├── Mermaidlive.png
    ├── Convo_start.png
    ├── Convo_response.png
    └── Convo_order_summary.png
```

---

### Features
- ✅ Natural language interaction
- ✅ AI-driven order processing using Gemini API
- ✅ Menu-driven dynamic conversation
- ✅ Support for dietary requirements (e.g., vegan, gluten-free)
- ✅ JSON-based order summary in multiple formats
- ✅ Voice and web chat interface via Gradio
- ✅ **Voice assistance** for hands-free interaction

---

### How It Works
1. The user submits a message via Gradio (or voice input).
2. `dialog_agent.py` receives and logs the input, forming a prompt.
3. `gemini_client.py` sends the prompt to Gemini API and returns the assistant’s reply.
4. The assistant’s response is rendered back in Gradio UI.
5. Final order data is processed and stored via `order_saver.py`.
6. Orders can be exported in JSON, CSV, XML, or SQLite format.

---

### Backend Logic - Breakdown
#### 🔧 Your Backend Includes:
**1. `dialog_agent.py`**
- This is the **core brain** of the app.
- Handles input/output formatting, response parsing, and context maintenance.
- Interfaces directly with Gemini API using `gemini_client.py`.

**2. `gemini_client.py`**
- Manages prompt submission and response fetching from Gemini API.
- Handles retry logic, error handling, and prompt construction.

**3. `order_saver.py`**
- Converts final order data into multiple formats (JSON, CSV, XML, SQLite).
- Designed to ensure order persistence for future use.

---

### Example Conversation (See `docs/`)
- `Convo_start.png`: Assistant greets user.
- `Convo_response.png`: Gemini provides topping options and confirms choices.
- `Convo_order_summary.png`: Final structured JSON order.

---

### Setup Instructions (Run Locally)

1. **Clone the Repository**
```bash
git clone <your_repo_link>
cd AI_assistant_project
```

2. **Set Up Python Environment**
```bash
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Configure Gemini API Key**
Create a `.env` file in the root directory and add:
```env
GEMINI_API_KEY="Insert_Your_API_Key_here"
```

4. **Run the Gradio Interface**
```bash
python run_gradio.py
```

5. **(Optional) Run Voice Assistant**
```bash
python voice_chatbot.py
```

6. **Open in Browser**
Go to: `http://127.0.0.1:7860`

---

### Final Notes
- Ideal for demonstrating conversational AI in a practical e-commerce scenario.
- Easily extensible to support payments or user authentication.
- Lightweight, no database dependency unless added optionally.
- Flexible deployment via Flask or Gradio.
- Includes **voice-enabled interaction** for accessibility and ease of use.
