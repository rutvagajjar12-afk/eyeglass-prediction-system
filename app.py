
import streamlit as st
from PIL import Image

# Page Navigation

st.sidebar.title("👓 Eye Vision Screening System")

page = st.sidebar.radio(
"Navigation",
["Home", "Eye Scan", "Vision Test", "Questionnaire", "Results"]
)

# Session State

if "score" not in st.session_state:
st.session_state.score = 0

# Home Page

if page == "Home":

```
st.title("👓 AI Eye Vision Screening System")

st.write("""
Welcome to the AI Eye Vision Screening System.

Features:
- Eye Image Upload
- Vision Test
- Eye Health Questionnaire
- Result Analysis
""")
```

# Eye Scan Page

elif page == "Eye Scan":

```
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
```

# Vision Test Page

elif page == "Vision Test":

```
st.title("🔍 Vision Test")

st.subheader("Can you read these letters?")

st.markdown("## E F P T O Z")

vision_test = st.radio(
    "Select your answer:",
    ["Yes", "No"]
)

if vision_test == "No":
    st.session_state.score += 1
```

# Questionnaire Page

elif page == "Questionnaire":

```
st.title("📝 Vision Questionnaire")

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
    "Do your eyes feel tired after using a mobile or computer?",
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

    st.success("Answers Saved")
```

# Results Page

elif page == "Results":

```
st.title("📊 Screening Result")

st.write(
    f"Total Risk Score: {st.session_state.score}"
)

if st.session_state.score >= 3:

    st.warning(
        "⚠ Possible vision issue detected. Eye examination is recommended."
    )

else:

    st.success(
        "✅ No major vision issues detected during screening."
    )

st.info(
    "This is only a preliminary screening and not a medical diagnosis."
)
```
