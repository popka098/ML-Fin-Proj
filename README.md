 ML Project

## About the Project

This project is a full-stack application that combines a machine learning backend with a modern frontend interface.

- **Backend** is built using **FastAPI**, providing a high-performance API for interacting with machine learning models.
- **Frontend** is developed with **Vite + React**, offering a fast and responsive user experience.
- The project integrates trained **machine learning models** that process user input and return predictions/results.

The main idea of the project is to allow users to interact with ML models through a simple web interface, sending text (or other data) to the backend and receiving processed results.

---

## How to Run the Project

### 1. Download Models

Download the required machine learning models from the [provided link](https://drive.google.com/drive/folders/1U-tAaQv6oYfr371B6nvL_BJ53CmMz0EZ?usp=drive_link) and place them into the following directory:

backend/app/models/

> Make sure the directory structure matches what the backend expects.

---

### 2. Run Backend

Navigate to the `backend` directory:

cd backend

Create a virtual environment:

python -m venv venv

Activate it:

- On Linux/macOS:
  source venv/bin/activate
- On Windows:
  venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the backend server:

python app/main.py

---

### 3. Run Frontend

Navigate to the `frontend` directory:

cd frontend

Install dependencies:

npm install

Start the development server:

npm run dev

---

## Notes

- Ensure that the backend is running before starting the frontend.
- Check environment variables or configuration files if required.
