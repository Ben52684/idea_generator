🚀 Hackathon Idea Generator

A web application designed to spark creativity by generating hackathon ideas using OpenAI's ChatGPT API. This project was developed as part of a challenge, combining Django (backend) and Vue.js (frontend).

📖 Table of Contents
Overview
Features
Tech Stack
Setup and Installation
Usage
Acknowledgments
🔍 Overview
The Hackathon Idea Generator is a tool designed to help developers, designers, and enthusiasts brainstorm innovative ideas for hackathons. It provides a chat-like interface where users can interact with OpenAI's ChatGPT API to generate personalized suggestions.

Key Highlights:
💬 Interactive Chat Interface: Engage with the AI for tailored suggestions.
📱 Responsive UI: Optimized for all screen sizes.
🔗 Integrated Deployment: The frontend's dist files are served by the Django backend.
✨ Features
Generate unique and creative hackathon ideas.
Save and retrieve previously generated ideas.
User-friendly chat interface.
Offline support for viewing saved ideas.
🛠️ Tech Stack
Frontend: Vue.js, Shadcn-vue
Backend: Django, Django REST Framework
Database: SQLite
API Integration: OpenAI ChatGPT API
Deployment: Frontend dist files served by Django backend
⚙️ Setup and Installation
Prerequisites
Python 3.10+
Node.js 18+
npm or yarn
OpenAI API Key
Backend and Frontend Setup
Clone the repository:


git clone https://github.com/Ben52684/idea_generator
cd hackathon-idea-generator
Set up the backend:
Navigate to the backend directory:

cd backend
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Build the frontend:
Navigate to the frontend directory:

cd ../frontend
Install dependencies:

npm install
Build the project:

npm run build
Copy the dist folder to the backend's static directory:

cp -r dist ../backend/static/
Run migrations and start the server:
Navigate back to the backend directory:

cd ../backend
Run migrations and start the development server:

python manage.py migrate
python manage.py runserver

💡 Usage
Open your browser and navigate to:
http://127.0.0.1:8000

Interact with the chat interface to generate ideas.

Ideas are automatically stored for future use.

🙌 Acknowledgments
OpenAI for their amazing ChatGPT API.
The open-source community for their contributions to tools and libraries.
