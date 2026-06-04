
import streamlit as st
from PIL import Image

st.title("👓 AI Eye Vision Screening System")

# Upload image
st.header("Eye Scan")
uploaded_file = st.file_uploader(
    "Upload your eye or face image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    st.success("✅ Image uploaded successfully!")

# Vision Questions
st.header("Vision Screening Questions")

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

# Eye Chart Test
st.header("Simple Eye Chart Test")

st.markdown("## E F P T O Z")

vision_test = st.selectbox(
    "Can you read the letters clearly?",
    ["Yes", "No"]
)

# Analyze Button
if st.button("Analyze Result"):

    score = 0

    if q1 == "Yes":
        score += 1

    if q2 == "Yes":
        score += 1

    if q3 == "Yes":
        score += 1

    if q4 == "Yes":
        score += 1

    if vision_test == "No":
        score += 1

    st.subheader("Result")

    if score >= 3:
        st.warning(
            "⚠ Possible vision issue detected. An eye examination is recommended."
        )
    else:
        st.success(
            "✅ No major vision issues detected in this screening."
        )
