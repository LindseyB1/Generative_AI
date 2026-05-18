import streamlit as st

st.set_page_config(
    page_title="Tanglarity - Stability AI",
    page_icon="🧠",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #0f1722 0%, #16202d 45%, #1d2a36 100%);
    color: #f1f5f9;
}

h1, h2, h3 {
    color: #e2e8f0;
}

.stTextArea textarea {
    background-color: #243241;
    color: white;
    border-radius: 12px;
}

.stSelectbox div[data-baseweb="select"] {
    background-color: #243241;
    border-radius: 12px;
}

.stButton button {
    background-color: #4f8ea3;
    color: white;
    border-radius: 12px;
    border: none;
    padding: 0.6rem 1rem;
}

.stButton button:hover {
    background-color: #5da6bd;
}

.stSlider {
    padding-top: 10px;
    padding-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

if "intro_done" not in st.session_state:
    st.session_state.intro_done = False

# INTRO SCREEN
if not st.session_state.intro_done:

    st.video("tanglarity-demo_2.mp4")

    st.title("Welcome to Tanglarity")
    st.subheader("Stability AI")

    st.caption(
        "Close the gap between knowing what to do and actually being able to do it."
    )

    st.markdown("### Empowering You")

    st.write(
        "A calm AI assisted space for reducing overwhelm, regaining clarity, and finding one manageable next step."
    )

    st.markdown("---")

    if st.button("Enter Stability AI"):
        st.session_state.intro_done = True
        st.rerun()

# MAIN APP
else:

    st.title("Tanglarity")
    st.subheader("Stability AI")

    st.caption(
        "Close the gap between knowing what to do and actually being able to do it."
    )

    st.markdown("---")

    with st.expander("🧭 Quick Phase Guide", expanded=True):
        st.write(
            "Survival: overwhelmed, frozen, reactive, or emotionally flooded."
        )

        st.write(
            "Stabilization: able to do small actions but still needs structure."
        )

        st.write(
            "Organization: ready to sort tasks, schedules, and priorities."
        )

        st.write(
            "Growth: stable enough to build habits, reflect, and plan forward."
        )

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

    # PHASE SUGGESTION LOGIC
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
        index=[
            "Survival",
            "Stabilization",
            "Organization",
            "Growth"
        ].index(suggested_phase)
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
        (
            clarity_score
            + readiness_score
            + (10 - overload_score)
        ) / 3 * 10
    )

    st.progress(progress_average)

    st.caption(
        f"Stabilization progress estimate: {progress_average}%"
    )

    st.markdown("---")

    if st.button("✨ Generate Stability Plan"):

        st.markdown("## Stability AI Response")

        st.markdown("### Current Phase")
        st.write(phase)

        st.markdown("### Current Pressure Point")

        st.write(
            pressure_point
            if pressure_point
            else "No pressure point entered yet."
        )

        st.markdown("### Support Type")
        st.write(support_type)

        st.markdown("### Priority Lane")

        if phase == "Survival":

            st.write(
                "Reduce input, lower pressure, and focus only on the safest next step."
            )

        elif phase == "Stabilization":

            st.write(
                "Create a small rhythm and complete one manageable action."
            )

        elif phase == "Organization":

            st.write(
                "Sort the pressure points into categories before trying to solve all of them."
            )

        else:

            st.write(
                "Use current stability to build consistency and long term systems."
            )

        st.markdown("### One or Two Next Actions")

        if phase == "Survival":

            st.write(
                "1. Pause noncritical decisions for now."
            )

            st.write(
                "2. Identify one task that would reduce the most pressure today."
            )

        elif phase == "Stabilization":

            st.write(
                "1. Choose one small task that can be completed in under 15 minutes."
            )

            st.write(
                "2. Remove one competing input or distraction."
            )

        elif phase == "Organization":

            st.write(
                "1. List the top three pressure points."
            )

            st.write(
                "2. Sort them into urgent, important, and can wait."
            )

        else:

            st.write(
                "1. Identify one habit or system to strengthen."
            )

            st.write(
                "2. Track one small win today."
            )

        st.markdown("### What To Pause")

        st.write(
            "Pause anything that adds pressure without helping the current priority."
        )

        st.markdown("### Grounding Reminder")

        st.write(
            "Clarity often improves after reducing chaos, not increasing pressure."
        )

        st.markdown("### Optional Reflection")

        st.write(
            "What would make today feel 10% more manageable?"
        )
