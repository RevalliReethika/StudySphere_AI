import streamlit as st

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="StudySphere AI",
    page_icon="🎓",
    layout="wide"
)

# ============================================================
# MAIN HEADER
# ============================================================

st.title("🎓 StudySphere AI")

st.subheader("Your Personalized AI Learning Assistant")

st.write(
    "StudySphere AI is an intelligent learning platform that helps "
    "students learn, practice, analyze their performance, and improve "
    "their academic skills using Artificial Intelligence and Data Science."
)

st.markdown("---")

# ============================================================
# WELCOME SECTION
# ============================================================

st.header("🌟 Welcome to Your Learning Space")

st.write(
    "StudySphere AI provides personalized learning support based on "
    "your subjects, quiz performance, learning goals, and study progress."
)

# ============================================================
# MAIN FEATURES
# ============================================================

st.header("🚀 Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        "### 👤 Student Profile\n"
        "Create your personalized learning profile with your subjects, "
        "learning goals, and preferred difficulty level."
    )

with col2:
    st.info(
        "### 🤖 AI Tutor\n"
        "Ask questions and receive simple, personalized explanations "
        "using Artificial Intelligence."
    )

with col3:
    st.info(
        "### 📄 PDF Summarizer\n"
        "Upload study materials and get useful summaries to understand "
        "important concepts quickly."
    )

col4, col5, col6 = st.columns(3)

with col4:
    st.info(
        "### 📝 Quiz Generator\n"
        "Take subject-based quizzes and instantly analyze your score, "
        "mistakes, and performance."
    )

with col5:
    st.info(
        "### 📅 Study Plan\n"
        "Generate a personalized study plan based on your learning goals "
        "and quiz performance."
    )

with col6:
    st.info(
        "### 📊 Performance Analytics\n"
        "Track your scores, mistakes, subject performance, and learning "
        "progress using data-driven analytics."
    )

st.markdown("---")

# ============================================================
# HOW IT WORKS
# ============================================================

st.header("⚙️ How StudySphere AI Works")

steps = [
    ("1️⃣", "Create Profile", "Enter your subjects and learning goals."),
    ("2️⃣", "Learn with AI", "Ask questions and get personalized explanations."),
    ("3️⃣", "Study Materials", "Upload PDFs and generate summaries."),
    ("4️⃣", "Take Quizzes", "Test your knowledge with personalized quizzes."),
    ("5️⃣", "Analyze Performance", "View scores, mistakes, and weak subjects."),
    ("6️⃣", "Improve", "Get recommendations and personalized study plans.")
]

for icon, title, description in steps:
    st.write(f"### {icon} {title}")
    st.write(description)

st.markdown("---")

# ============================================================
# DATA SCIENCE & MACHINE LEARNING
# ============================================================

st.header("🧠 Data Science & Machine Learning")

st.write(
    "StudySphere AI uses Data Science techniques to analyze quiz scores, "
    "mistakes, subject performance, and learning patterns."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.success(
        "📈 **Performance Analysis**\n\n"
        "Analyze quiz scores and identify weak and strong subjects."
    )

with col2:
    st.success(
        "🎯 **Personalized Recommendations**\n\n"
        "Recommend subjects and difficulty levels based on performance."
    )

with col3:
    st.success(
        "🤖 **ML Prediction**\n\n"
        "Use Machine Learning to classify overall student performance."
    )

st.markdown("---")

# ============================================================
# TECHNOLOGIES
# ============================================================

st.header("🛠️ Technologies Used")

tech_col1, tech_col2, tech_col3, tech_col4 = st.columns(4)

with tech_col1:
    st.write("🐍 **Python**")

with tech_col2:
    st.write("🌐 **Streamlit**")

with tech_col3:
    st.write("📊 **Pandas & Scikit-learn**")

with tech_col4:
    st.write("🤖 **Gemini AI**")

st.markdown("---")

# ============================================================
# FOOTER
# ============================================================

st.success(
    "🎉 Start your personalized learning journey with StudySphere AI!"
)

st.caption(
    "StudySphere AI – Personalized AI Learning Assistant"
)