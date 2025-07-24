# 🧠 Python-to-C++ Tutor Chatbot Backend

This is the backend API for the **Python-to-C++ Tutor Chatbot**, a FastAPI-powered application that connects with OpenAI's GPT-4o model to provide educational feedback to students transitioning from Python to C++.

---

## 🚀 Features

- RESTful API with endpoints for both text-based prompts and file uploads
- Uses a structured system prompt to encourage concept-based tutoring
- Performs static analysis on uploaded `.py` and `.cpp` files
- Connects with OpenAI's `chatgpt-4o-latest` model for rich language responses
- Enforces file type validation and handles multipart form data

---

## 📦 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **Uvicorn**
- **OpenAI Python SDK**
- **python-dotenv**

---

## 🔌 API Endpoints

### `POST /ask`
Submits a text prompt to the GPT model.

**Request Body:**
```json
{
  "prompt": "How do you write a for loop in C++ that's similar to Python?"
}
```

**Response:**
```json
{
  "response": "Here's how you would translate a Python for loop to C++..."
}
```

---

### `POST /upload`
Submits a `.py` or `.cpp` file along with a user prompt.

**Content-Type:** `multipart/form-data`

**Form Fields:**
- `file`: The uploaded Python or C++ source file
- `user_prompt`: A custom message or question about the file

**Response:**
```json
{
  "response": "Analyzing your C++ code... Here are a few improvements:"
}
```

---

## 🔐 Environment Variables

Create a `.env` file in the `backend/` directory:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxx
```

---

## ▶️ Running Locally

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the FastAPI server
uvicorn main:app --reload
```

The API will be available at:
📍 `http://localhost:8000`

Swagger docs:
📍 `http://localhost:8000/docs`

---

## 📁 File Upload Notes

- Only `.py` and `.cpp` files are accepted
- Files are read and processed using GPT to provide **feedback, not full solutions**
- If an invalid file is submitted, the API returns a `400` error

---

## 🎯 Intended Use

This backend is part of an AI tutoring assistant created through the **Honors Summer Research Fellowship at Elmhurst University**. It is being piloted in CS courses to support students in learning C++ through guided, concept-focused feedback.

---

## 📄 License

For educational use only. License to be added.

---

## 🤝 Acknowledgments

- OpenAI for API access
- Elmhurst University Honors Program
