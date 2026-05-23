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

/* Main Headers */
h1 {
    color: white !important;
    font-weight: 700 !important;
}

/* Secondary Headers */
h2, h3 {
    color: white !important;
    font-weight: 600 !important;
}

.hero-title {
    font-size: 64px !important;
    line-height: 1.0 !important;
    margin-bottom: 0.2rem !important;
}

.hero-subtitle {
    font-size: 40px !important;
    color: #dbeafe !important;
    margin-top: 0.2rem !important;
    margin-bottom: 1.1rem !important;
}

.hero-description,
.body-text,
.caption-text,
.stInfo,
.stCaption,
[data-testid="stCaptionContainer"] p {
    color: white !important;
    font-size: 20px !important;
    line-height: 1.6 !important;
}

.hero-description {
    font-size: 26px !important;
    font-weight: 500 !important;
    margin-bottom: 2rem !important;
}

.section-title {
    color: white !important;
    font-size: 28px !important;
    font-weight: 700 !important;
    margin-top: 1.5rem !important;
    margin-bottom: 0.75rem !important;
}

.subtle-text {
    color: #dbeafe !important;
    font-size: 18px !important;
    line-height: 1.6 !important;
}

.stButton button {
    background-color: #4f8ea3 !important;
    color: white !important;
    border-radius: 12px !important;
    border: none !important;
    padding: 0.8rem 1.2rem !important;
    font-size: 18px !important;
    font-weight: 600 !important;
}

.stButton button:hover {
    background-color: #5da6bd !important;
}

.stSlider label,
.slider-label {
    color: white !important;
    font-size: 18px !important;
}

.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] {
    background-color: #243241 !important;
    color: white !important;
    border-radius: 12px !important;
    font-size: 18px !important;
    border: 1px solid #5da6bd !important;
}

.streamlit-expanderHeader {
    font-size: 22px !important;
    color: white !important;
    font-weight: 600 !important;
}

.stSuccess,
.success-text {
    font-size: 20px !important;
    color: #d1fae5 !important;
}

.stProgress > div > div > div > div {
    background-color: #5da6bd !important;
}

.progress-text {
    font-size: 24px !important;
    color: white !important;
    font-weight: 700 !important;
}

</style>

""", unsafe_allow_html=True)

if "intro_done" not in st.session_state:
    st.session_state.intro_done = False

if not st.session_state.intro_done:
    st.video("tanglarity-demo_2.mp4")

    st.markdown("""

<h1 style='
    text-align: center;
    color: white;
    font-size: 72px;
    font-weight: 900;
    margin-bottom: 0;
    letter-spacing: 1px;
'>
Welcome to Tanglarity
</h1>

<h2 style='
    text-align: center;
    color: #dbeafe;
    font-size: 46px;
    font-weight: 600;
    margin-top: 5px;
'>
Stability AI
</h2>
""", unsafe_allow_html=True)

    st.markdown("""

<p style='
    text-align: center;
    color: white;
    font-size: 26px;
    font-weight: 500;
    margin-bottom: 30px;
'>
Close the gap between knowing what to do and actually being able to do it.
</p>
""", unsafe_allow_html=True)

    st.markdown("### Empowering You")

    st.write(
        "A calm AI assisted space for reducing overwhelm, regaining clarity, and finding one manageable next step."
    )

    st.markdown("---")

    if st.button("Enter Stability AI"):
        st.session_state.intro_done = True
        st.rerun()

else:
    st.markdown("""

<h1 class='hero-title'>
Tanglarity
</h1>

<h2 class='hero-subtitle'>
Stability AI
</h2>

<p class='hero-description'>
Close the gap between knowing what to do and actually being able to do it.
</p>
""", unsafe_allow_html=True)

    st.markdown("---")

    with st.expander("🧭 Quick Phase Guide", expanded=True):
        st.write("Survival: overwhelmed, frozen, reactive, or emotionally flooded.")
        st.write("Stabilization: able to do small actions but still needs structure.")
        st.write("Organization: ready to sort tasks, schedules, and priorities.")
        st.write("Growth: stable enough to build habits, reflect, and plan forward.")

    st.video("tanglarity-demo_1.mp4")

    st.markdown("---")

    st.markdown("### Quick Stabilization Quiz")

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

    st.markdown("### What phase feels closest right now?")

    phase = st.selectbox(
        "Select Stabilization Phase",
        ["Survival", "Stabilization", "Organization", "Growth"],
        index=["Survival", "Stabilization", "Organization", "Growth"].index(suggested_phase)
    )

    st.markdown("### What feels hardest right now?")

    pressure_point = st.text_area(
        "Describe one current pressure point or situation",
        height=150
    )

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

    st.markdown("### Progress Tracking")

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

    st.markdown(f"""

<p style='
    text-align: center;
    color: white;
    font-size: 28px;
    font-weight: 700;
    margin-top: 15px;
    margin-bottom: 25px;
'>
Stabilization progress estimate: {progress_average}%
</p>
""", unsafe_allow_html=True)

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
