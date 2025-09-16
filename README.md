# Healthify : AI-Powered Personal Health & Wellness Assistant

## 🚀 Project Overview
**Healthify** is an interactive web application powered by **Google Gemini AI** that provides personalized health, fitness, and nutrition guidance. Users can enter their personal details, lifestyle habits, and health-related queries, and get structured, actionable advice including fitness recommendations, diet plans, and lifestyle tips — all tailored to their profile.

This project demonstrates the integration of **Streamlit, NLP, Generative AI, and personalized health analytics** in a user-friendly interface.

---

## 🌟 Features
- Collects **personal user details**: name, age, gender, height, weight, lifestyle habits.
- Calculates **BMI** and fitness score.
- Uses **Google Gemini AI** via `generativeai` API to answer health queries.
- Provides **structured advice**:
  - Health assessment
  - Problem analysis
  - Possible causes
  - Lifestyle recommendations
  - Habit modifications
  - Personalized diet plan in **table format**
  - Summary of recommendations
- User-friendly **Streamlit interface** with sidebar input and Markdown-formatted output.
- Fully **interactive and personalized** experience.

---

## 🌐 Technologies & Libraries
- **Python 3.x**
- **Streamlit** – For web interface
- **Google Generative AI (Gemini API)** – For AI-driven responses
- **Pandas** – For BMI calculations and data handling
- **Markdown rendering** in Streamlit for structured output

---

## 💻 Installation

1. **Clone the repository**
```bash
git clone https://github.com/Vikas-B-S/Healthify_Web_App.git
cd Healthify_Web_App
```

2. **Create and activate a virtual environment**
```bash
python -m venv genai_env
# Windows
genai_env\Scripts\activate
# macOS/Linux
source genai_env/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set Google API Key**
```bash
export GOOGLE_API_KEY="your_google_api_key"  # macOS/Linux
setx GOOGLE_API_KEY "your_google_api_key"    # Windows
```

---

## 🖥 Usage
1. Run the app locally:
```bash
streamlit run healthify.py
```
2. Enter your personal details in the sidebar.
3. Enter your health-related question in the input field.
4. Receive **personalized advice** including diet plan, fitness tips, and habit recommendations.

---

## 📂 Project Structure
```
Healthify/
├─ healthify.py        # Main Streamlit app
├─ requirements.txt # Python dependencies
├─ README.md        # Project documentation
└─ ...              # Other supporting files
```

---

## 🌐 App Link :
- https://healthify-ai-health-assistant-vikas-b-s.streamlit.app/

---

## ⚡ How NLP & Generative AI are used
- The app uses **Google Gemini AI** (via `generativeai`) to understand **user queries** in natural language.
- The AI generates **structured, personalized advice** including health analysis, habit recommendations, and diet plans.
- NLP techniques ensure **clarity, personalization, and contextual relevance** in responses.

---

## 📌 Skills & Concepts
- Python programming
- Streamlit web app development
- Natural Language Processing (NLP)
- Generative AI (Google Gemini)
- Personalized health analytics
- UI/UX for interactive web apps
