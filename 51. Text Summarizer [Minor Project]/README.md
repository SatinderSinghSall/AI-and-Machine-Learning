# 📄 Text Summarizer App (HuggingFace Transformer)

# AI / ML: Deep Learning – Reinforcement Learning

A full-stack **Text Summarization Web Application** built using **Transformer models (T5)** from HuggingFace, deployed with **FastAPI** and a simple **HTML/CSS/JavaScript frontend**.

This project demonstrates end-to-end implementation of:

- NLP model fine-tuning
- Model serving via API
- Frontend-backend integration
- Deployment-ready architecture

---

## 🚀 Project Overview

This application takes user-input text (dialogue or paragraph) and generates a concise summary using a fine-tuned **T5 Transformer model**.

The system includes:

- 🧠 Transformer-based summarization model
- ⚡ FastAPI backend for inference
- 🌐 Interactive web UI for user input/output

---

## 🧱 Tech Stack

### 🔹 Machine Learning

- HuggingFace Transformers (T5)
- PyTorch

### 🔹 Backend

- FastAPI
- Pydantic
- Jinja2 Templates

### 🔹 Frontend

- HTML5
- CSS3
- JavaScript (Fetch API)

---

## 📂 Project Structure

```
├── app.py                # FastAPI backend (model inference)
├── index.html           # Frontend UI
├── saved_summary_model/ # Fine-tuned T5 model
├── README.md            # Project documentation
└── notebook.ipynb       # Training & preprocessing pipeline
```

---

## ⚙️ How It Works

### 1. Input Processing

User enters text in the UI → sent to backend via POST request.

### 2. Data Cleaning

Text is cleaned before processing:

- Removes extra spaces
- Removes HTML tags
- Converts to lowercase
  (Implemented in backend)

### 3. Tokenization

- Uses T5 tokenizer
- Max length: 512 tokens
- Applies padding & truncation

### 4. Model Inference

- Fine-tuned T5 model generates summary
- Beam search used for better output quality:
  - `num_beams=4`
  - `max_length=150`

### 5. Output

- Decoded summary returned as JSON
- Displayed dynamically on frontend

---

## 🧠 Backend Details (FastAPI)

The backend is implemented using FastAPI :

### Key Features:

- Loads trained T5 model from local directory
- Device selection:
  - Apple MPS / CUDA / CPU

- REST API endpoint:
  - `POST /summarize/`

- Web route:
  - `GET /` → serves UI

### API Example

```json
POST /summarize/

{
  "dialogue": "Your input text here"
}
```

Response:

```json
{
  "summary": "Generated summary text"
}
```

---

## 🎨 Frontend Details

The frontend UI is built using HTML, CSS, and JavaScript .

### Features:

- Clean and responsive UI
- Text input area for content
- Real-time API interaction
- Loading & error handling
- Dynamic summary display

### Workflow:

1. User submits text
2. JS sends request via Fetch API
3. Backend processes input
4. Summary is displayed instantly

---

## 🧪 Model Details

- Model: **T5 (Text-to-Text Transfer Transformer)**
- Fine-tuned for **text summarization task**
- Stored locally: `./saved_summary_model`

### Generation Parameters:

- `max_length=150`
- `num_beams=4`
- `early_stopping=True`

---

## ▶️ Running the Project

### 1. Install Dependencies

```bash
pip install fastapi uvicorn transformers torch jinja2
```

---

### 2. Start the Server

```bash
uvicorn app:app --reload
```

---

### 3. Open in Browser

```
http://127.0.0.1:8000/
```

---

## 📸 Features Demonstrated

- End-to-end NLP pipeline
- Transformer fine-tuning
- API deployment
- Frontend-backend integration
- Real-time inference system

---

## 📌 Learning Outcomes

From this project, the following concepts were implemented:

- Data preprocessing for NLP
- Tokenization using T5 tokenizer
- Fine-tuning transformer models
- Model saving & loading
- FastAPI-based deployment
- REST API design
- Frontend integration using JavaScript

---

## ⚠️ Known Issues / Improvements

- Minor typo in CUDA check:

  ```python
  torch.cuda.is_availanle()
  ```

  → should be `is_available()`

- Add:
  - Input validation limits
  - Streaming responses for long text
  - Docker deployment
  - Better UI/UX enhancements

---

## 🔮 Future Enhancements

- Support for multiple languages
- Upload files (PDF, DOCX)
- Summarization modes (short / detailed)
- Deploy on cloud (AWS / GCP / Render)
- Add authentication

---

## 👨‍💻 Author

**Satinder Singh Sall**
AI/ML Practitioner

---

## 📄 License

This project is for academic and educational purposes.

---

## ⭐ Acknowledgements

- HuggingFace Transformers
- PyTorch
- FastAPI Framework
- Apna College AI/ML Program

---
