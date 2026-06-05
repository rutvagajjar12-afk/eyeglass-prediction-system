import streamlit as st
from PIL import Image

# Sidebar Navigation
st.sidebar.title("👓 Eye Vision Screening System")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Eye Scan", "Vision Test", "Questionnaire", "Results"]
)

# Session State
if "score" not in st.session_state:
    st.session_state.score = 0

# HOME PAGE
if page == "Home":

    st.title("👓 AI Eye Vision Screening System")

    st.write("""
    Welcome to the AI Eye Vision Screening System.

    Features:
    - Eye Scan
    - Vision Tests
    - Questionnaire
    - Result Analysis
    """)

# EYE SCAN PAGE
elif page == "Eye Scan":

    st.title("📷 Eye Scan")

    uploaded_file = st.file_uploader(
        "Upload Eye or Face Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        st.success("✅ Image Uploaded Successfully")

# VISION TEST PAGE
elif page == "Vision Test":

    st.title("🔍 Vision Test")

    # Test 1
    st.subheader("Test 1 - Large Letters")

    st.markdown("# E F P T O Z")

    test1 = st.radio(
        "Can you read Test 1 clearly?",
        ["Yes", "No"],
        key="test1"
    )

    # Test 2
    st.subheader("Test 2 - Medium Letters")

    st.markdown("### D E F P O T E C")

    test2 = st.radio(
        "Can you read Test 2 clearly?",
        ["Yes", "No"],
        key="test2"
    )

    # Test 3
    st.subheader("Test 3 - Small Letters")

    st.markdown("L P E D F C T O Z")

    test3 = st.radio(
        "Can you read Test 3 clearly?",
        ["Yes", "No"],
        key="test3"
    )

    if st.button("Save Vision Test"):

        vision_score = 0

        if test1 == "No":
            vision_score += 1

        if test2 == "No":
            vision_score += 1

        if test3 == "No":
            vision_score += 1

        st.session_state.score += vision_score

        st.success("✅ Vision Test Saved")

# QUESTIONNAIRE PAGE
elif page == "Questionnaire":

    st.title("📝 Questionnaire")

    q1 = st.radio(
        "Do you experience blurry vision?",
        ["Yes", "No"]
    )

    q2 = st.radio(
        "Do you get headaches while reading?",
        ["Yes", "No"]
    )

    q3 = st.radio(
        "Do you squint while looking at distant objects?",
        ["Yes", "No"]
    )

    q4 = st.radio(
        "Do your eyes feel tired after using screens?",
        ["Yes", "No"]
    )

    if st.button("Save Answers"):

        score = 0

        if q1 == "Yes":
            score += 1

        if q2 == "Yes":
            score += 1

        if q3 == "Yes":
            score += 1

        if q4 == "Yes":
            score += 1

        st.session_state.score += score

        st.success("✅ Answers Saved")

# RESULTS PAGE
elif page == "Results":

    st.title("📊 Screening Result")

    st.write(f"Total Risk Score: {st.session_state.score}")

    if st.session_state.score >= 3:
        st.warning(
            "⚠ Possible vision issue detected. Eye examination is recommended."
        )
    else:
        st.success(
            "✅ No major vision issues detected."
        )

    st.info(
        "This is a screening tool and not a medical diagnosis."
    )
