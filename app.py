import streamlit as st

# Basic page config
st.set_page_config(page_title="Teaching Agent Team")

# Title and description
st.title("Teaching Agent Team")
st.markdown("---")
st.write("Enter a topic you want to learn about!")

# Input section with columns for better layout
col1, col2 = st.columns([3, 1])
with col1:
    topic = st.text_input("Topic:", placeholder="e.g., Machine Learning")
with col2:
    generate = st.button("Generate Plan", use_container_width=True)

# Generate responses
if generate:
    if not topic:
        st.error("Please enter a topic first!")
    else:
        st.success(f"Generating learning plan for: {topic}")
