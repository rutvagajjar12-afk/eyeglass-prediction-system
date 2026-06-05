
elif page == "Vision Test":

    st.title("🔍 Vision Test")

    st.subheader("Test 1: Large Letters")

    st.markdown(
        "<h1 style='text-align:center;'>E F P T O Z</h1>",
        unsafe_allow_html=True
    )

    test1 = st.radio(
        "Can you read Test 1 clearly?",
        ["Yes", "No"],
        key="test1"
    )

    st.divider()

    st.subheader("Test 2: Medium Letters")

    st.markdown(
        "<h3 style='text-align:center;'>D E F P O T E C</h3>",
        unsafe_allow_html=True
    )

    test2 = st.radio(
        "Can you read Test 2 clearly?",
        ["Yes", "No"],
        key="test2"
    )

    st.divider()

    st.subheader("Test 3: Small Letters")

    st.markdown(
        "<p style='font-size:18px;text-align:center;'>L P E D F C T O Z</p>",
        unsafe_allow_html=True
    )

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
