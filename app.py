# -*- coding: utf-8 -*-
import streamlit as st
from collections import Counter

st.set_page_config(page_title="Career Matcher v2", page_icon="🧠", layout="centered")

# עיצוב רקע ותצוגה
st.markdown("""
    <style>
        .stApp {
            background-image: url("nigers.avif");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }

        .title {
            font-size: 50px;
            font-weight: 900;
            color: white;
            text-align: center;
            text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.7);
            margin-bottom: 10px;
        }

        .subtitle {
            font-size: 24px;
            color: white;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.6);
            margin-bottom: 40px;
        }

        .box {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 0 15px rgba(0,0,0,0.2);
            margin-top: 20px;
        }

        .stButton>button {
            background-color: #2ecc71;
            color: white;
            border-radius: 12px;
            padding: 0.6em 1.5em;
            font-size: 16px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #27ae60;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">Career Matcher v2 🔍</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">ענה על כמה שאלות ונגלה יחד מה בול המקצוע שלך!</div>', unsafe_allow_html=True)

# כפתור מדריך
with st.expander("📘 מדריך שימוש"):
    st.markdown("""
    1. בחר את כל האפשרויות שמדברות אליך בכל שאלה.
    2. לחץ על כפתור "מצא לי מקצוע!" בסוף.
    3. תוכל לשמור את התוצאה כ-PDF, לשתף או לנסות שוב.
    """)

with st.form("career_form"):
    q1 = st.multiselect("מה מלהיב אותך?", ["טכנולוגיה", "אמנות", "עבודה עם אנשים", "טבע ובעלי חיים", "אוכל ובישול", "עסקים", "משהו שקט ונעים"])
    q2 = st.multiselect("איפה אתה מדמיין את עצמך עובד?", ["משרד הייטק", "אולפן", "בית ספר", "מסעדת שף", "חווה או שטח פתוח", "מהבית", "מעבדה"])
    q3 = st.multiselect("מה הכי מאפיין אותך?", ["יצירתיות", "אכפתיות", "דיוק", "חברותיות", "סקרנות", "משמעת עצמית", "אהבת טכנולוגיה"])
    q4 = st.multiselect("איך אתה אוהב לעבוד?", ["בצוות", "לבד", "עם ילדים", "עם מחשבים", "עם אוכל", "עם בעלי חיים", "עם קהל"])
    q5 = st.radio("כמה אתה אוהב ללמוד דברים חדשים?", ["מאוד", "בינוני", "פחות"])
    submitted = st.form_submit_button("מצא לי מקצוע!")

if submitted:
    interests = q1 + q2 + q3 + q4

    job_scores = {
        "מתכנת / סייבר / מפתח תוכנה": ["טכנולוגיה", "אהבת טכנולוגיה", "דיוק", "עם מחשבים", "משרד הייטק", "סקרנות"],
        "שחקן / מוזיקאי / במאי": ["אמנות", "אולפן", "יצירתיות", "עם קהל"],
        "מורה / מדריך / מרצה": ["עבודה עם אנשים", "בית ספר", "אכפתיות", "עם ילדים", "חברותיות"],
        "וטרינר / מאלף / מטפל בבעלי חיים": ["טבע ובעלי חיים", "חווה או שטח פתוח", "עם בעלי חיים", "דיוק"],
        "שף / קונדיטור / בלוגר אוכל": ["אוכל ובישול", "מסעדת שף", "עם אוכל", "יצירתיות"],
        "יזם / מנהל שיווק / כלכלן": ["עסקים", "מהבית", "דיוק", "סקרנות", "עם קהל"],
        "ספרן / כותב / מתרגם": ["משהו שקט ונעים", "לבד", "דיוק", "מהבית"]
    }

    score_counter = {}

    for job, keywords in job_scores.items():
        matches = len(set(keywords) & set(interests))
        score_counter[job] = matches

    best_match = max(score_counter, key=score_counter.get)

    # תצוגה עם נתונים מדומים לדוגמה
    job_data = {
        "מתכנת / סייבר / מפתח תוכנה": "93% ביקוש בתעשייה • ממוצע שכר: 24,000 ש""ח",
        "שחקן / מוזיקאי / במאי": "60% השתלבות בפועל • ממוצע שכר: 8,000 ש""ח",
        "מורה / מדריך / מרצה": "85% צורך ארצי • ממוצע שכר: 10,500 ש""ח",
        "וטרינר / מאלף / מטפל בבעלי חיים": "70% סיפוק אישי • ממוצע שכר: 9,000 ש""ח",
        "שף / קונדיטור / בלוגר אוכל": "65% גיוון יצירתי • ממוצע שכר: 10,000 ש""ח",
        "יזם / מנהל שיווק / כלכלן": "80% גמישות תעסוקתית • ממוצע שכר: 15,000 ש""ח",
        "ספרן / כותב / מתרגם": "55% עבודה מהבית • ממוצע שכר: 7,500 ש""ח"
    }

    st.markdown(f'<div class="box"><h3>המקצוע שהכי מתאים לך הוא:</h3><p><strong>{best_match}</strong><br>{job_data.get(best_match)}</p></div>', unsafe_allow_html=True)

    # אפשרות לשיתוף או שמירה
    st.download_button("📄 שמור תוצאה כ-PDF", data=f"המקצוע שהכי מתאים לך: {best_match}\n{job_data.get(best_match)}", file_name="career_result.pdf")
    st.button("🔄 נקה הכל ונסה שוב")
