import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


def load_system_prompt():
    with open("Prompts/system_prompt.md", "r", encoding="utf-8") as file:
        return file.read()


system_prompt = load_system_prompt()

st.set_page_config(
    page_title="Tanglarity - Stability AI",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #0f1722 0%, #16202d 45%, #1d2a36 100%);
    color: white;
}

.block-container {
    max-width: 1000px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3, h4, h5, h6, p, div, span, label {
    text-align: left !important;
}

.hero-title {
    color: white !important;
    font-size: 48px !important;
    font-weight: 900 !important;
    line-height: 1.15 !important;
    margin-bottom: 16px !important;
}

.hero-subtitle {
    color: white !important;
    font-size: 40px !important;
    font-weight: 750 !important;
    line-height: 1.2 !important;
    margin-bottom: 18px !important;
}

.hero-description {
    color: white !important;
    font-size: 35px !important;
    font-weight: 600 !important;
    line-height: 1.35 !important;
    margin-bottom: 36px !important;
}

.section-title {
    color: white !important;
    font-size: 35px !important;
    font-weight: 800 !important;
    line-height: 1.25 !important;
    margin-top: 28px !important;
    margin-bottom: 18px !important;
}

.subsection-title {
    color: white !important;
    font-size: 30px !important;
    font-weight: 750 !important;
    line-height: 1.25 !important;
    margin-top: 24px !important;
    margin-bottom: 16px !important;
}

.body-text {
    color: white !important;
    font-size: 25px !important;
    line-height: 1.6 !important;
}

p, li {
    color: white !important;
    font-size: 20px !important;
    line-height: 1.6 !important;
}

label,
[data-testid="stWidgetLabel"] p {
    color: white !important;
    font-size: 20px !important;
    font-weight: 600 !important;
}

.stSelectbox label p {
    font-size: 15px !important;
    color: white !important;
}

.stSelectbox div[data-baseweb="select"] {
    background-color: #243241 !important;
    border-radius: 15px !important;
    color: white !important;
    font-size: 20px !important;
    border: 1px solid #5da6bd !important;
}

.stTextArea textarea {
    background-color: #243241 !important;
    color: white !important;
    border-radius: 15px !important;
    font-size: 20px !important;
    border: 1px solid #5da6bd !important;
}

.stSlider label p,
.stSlider p,
.stSlider span {
    color: white !important;
    font-size: 20px !important;
}

.stInfo,
.stInfo div,
.stInfo p {
    color: white !important;
    font-size: 15px !important;
}

.streamlit-expanderHeader {
    color: white !important;
    font-size: 30px !important;
    font-weight: 800 !important;
}

[data-testid="stExpander"] p {
    color: white !important;
    font-size: 20px !important;
    line-height: 1.6 !important;
}

.stButton button {
    background-color: #4f8ea3 !important;
    color: white !important;
    border-radius: 20px !important;
    border: none !important;
    padding: 1rem 1.6rem !important;
    font-size: 20px !important;
    font-weight: 700 !important;
}

.stButton button:hover {
    background-color: #5da6bd !important;
}

.progress-text {
    color: white !important;
    font-size: 20px !important;
    font-weight: 700 !important;
    margin-top: 18px !important;
    margin-bottom: 24px !important;
}

.stSuccess,
.stSuccess div,
.stSuccess p,
.stWarning,
.stWarning div,
.stWarning p,
.stError,
.stError div,
.stError p {
    color: white !important;
    font-size: 20px !important;
}

h1 {
    font-size: 48px !important;
    color: white !important;
}

h2 {
    font-size: 40px !important;
    color: white !important;
}

h3 {
    font-size: 30px !important;
    color: white !important;
}

hr {
    margin-top: 2rem !important;
    margin-bottom: 2rem !important;
}
</style>
""", unsafe_allow_html=True)

if "intro_done" not in st.session_state:
    st.session_state.intro_done = False

if not st.session_state.intro_done:
    st.video("tanglarity-demo_2.mp4")

    st.markdown("""
    <div class="hero-title">Welcome to Tanglarity</div>
    <div class="hero-subtitle">Stability AI</div>
    <div class="hero-description">
    Close the gap between knowing what to do and actually being able to do it.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Empowering You</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="body-text">
    A calm AI assisted space for reducing overwhelm, regaining clarity, and finding one manageable next step.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    if st.button("Enter Stability AI"):
        st.session_state.intro_done = True
        st.rerun()

else:
    st.markdown("""
    <div class="hero-title">Tanglarity</div>
    <div class="hero-subtitle">Stability AI</div>
    <div class="hero-description">
    Close the gap between knowing what to do and actually being able to do it.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    with st.expander("🧭 Quick Phase Guide", expanded=True):
        st.write("Survival: overwhelmed, frozen, reactive, or emotionally flooded.")
        st.write("Stabilization: able to do small actions but still needs structure.")
        st.write("Organization: ready to sort tasks, schedules, and priorities.")
        st.write("Growth: stable enough to build habits, reflect, and plan forward.")

    st.video("tanglarity-demo_1.mp4")

    st.markdown("---")

    st.markdown(
        '<div class="subsection-title">Quick Stabilization Quiz</div>',
        unsafe_allow_html=True
    )

    stress_level = st.slider(
        "How overloaded do things feel right now?",
        0,
        10,
        5
    )

    clarity_level = st.slider(
        "How clear does the next step feel?",
        0,
        10,
        5
    )

    energy_level = st.slider(
        "How much energy do you have to take action?",
        0,
        10,
        5
    )

    if stress_level >= 8 or energy_level <= 2:
        suggested_phase = "Survival"
    elif stress_level >= 6 or clarity_level <= 4:
        suggested_phase = "Stabilization"
    elif clarity_level >= 5 and energy_level >= 4:
        suggested_phase = "Organization"
    else:
        suggested_phase = "Growth"

    st.info(f"Suggested phase based on quiz: {suggested_phase}")

    st.markdown("---")

    st.markdown(
        '<div class="subsection-title">What phase feels closest right now?</div>',
        unsafe_allow_html=True
    )

    phase = st.selectbox(
        "Select Stabilization Phase",
        ["Survival", "Stabilization", "Organization", "Growth"],
        index=["Survival", "Stabilization", "Organization", "Growth"].index(suggested_phase)
    )

    st.markdown(
        '<div class="subsection-title">What feels hardest right now?</div>',
        unsafe_allow_html=True
    )

    pressure_point = st.text_area(
        "Describe one current pressure point or situation",
        height=150
    )

    uploaded_file = st.file_uploader(
        "Optional: Upload a document for added context",
        type=["txt", "md"]
    )

    uploaded_context = ""

    if uploaded_file is not None:
        uploaded_context = uploaded_file.read().decode("utf-8")
        st.success("Document uploaded and added as context.")

    support_type = st.selectbox(
        "What kind of support would help most?",
        [
            "Next step",
            "Organization help",
            "Grounding",
            "Clarity",
            "Planning",
            "Reflection"
        ]
    )

    st.markdown("---")

    st.markdown(
        '<div class="subsection-title">Progress Tracking</div>',
        unsafe_allow_html=True
    )

    overload_score = st.slider(
        "Overload level",
        0,
        10,
        stress_level
    )

    clarity_score = st.slider(
        "Clarity level",
        0,
        10,
        clarity_level
    )

    readiness_score = st.slider(
        "Readiness for action",
        0,
        10,
        energy_level
    )

    progress_average = int(
        (clarity_score + readiness_score + (10 - overload_score)) / 3 * 10
    )

    st.progress(progress_average)

    st.markdown(
        f'<div class="progress-text">Stabilization progress estimate: {progress_average}%</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    if st.button("✨ Generate Stability Plan"):
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            st.error(
                "Missing OPENAI_API_KEY. Add it to your local .env file or Streamlit secrets."
            )

        elif not pressure_point.strip():
            st.warning("Please describe one current pressure point.")

        else:
            client = OpenAI(api_key=api_key)

            user_message = f"""
Uploaded document context:
{uploaded_context[:3000]}

Current stabilization phase:
{phase}

Pressure point:
{pressure_point}

Support type requested:
{support_type}

Overload score:
{overload_score}/10

Clarity score:
{clarity_score}/10

Readiness score:
{readiness_score}/10

Generate a custom response that clearly references the user's actual pressure point.

Return these exact sections:
- Current Phase Summary
- Current Pressure Point
- One Priority Lane
- One or Two Next Actions
- What To Pause
- Grounding Reminder
- Optional Reflection Question

Rules:
- Make the response specific to the pressure point.
- Use the uploaded document only as additional context if it is relevant.
- Do not use generic placeholder wording.
- Keep the response calm, concise, stabilizing, non overwhelming, structured, and realistic.
- Avoid therapy, diagnosis, legal advice, or crisis language.
- If the pressure point is unusual or fictional, still respond to the actual details calmly.
"""

            with st.spinner("Generating Stability Plan with OpenAI..."):
                try:
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": user_message}
                        ],
                        temperature=0.7
                    )

                    ai_output = response.choices[0].message.content

                    st.success("Live AI response generated from OpenAI.")
                    st.markdown("## Stability AI Response")
                    st.markdown(ai_output)

                except Exception as e:
                    st.error("The AI response could not be generated.")
                    st.write(e)