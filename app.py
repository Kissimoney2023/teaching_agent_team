import streamlit as st

# Page config
st.set_page_config(
    page_title="Teaching Agent Team",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("Teaching Agent Team")
st.write("Enter a topic you want to learn about, and our AI teaching agents will help create a comprehensive learning plan!")

# Input section
topic = st.text_input("Enter topic:", placeholder="e.g., Machine Learning")

if st.button("Generate Learning Plan"):
    if not topic:
        st.error("Please enter a topic first!")
    else:
        # Professor's Knowledge Base
        with st.expander("Professor's Knowledge Base", expanded=True):
            st.write(f"""
            Here's what you need to know about {topic}:
            1. Core Concepts
            2. Key Principles
            3. Historical Context
            4. Current Applications
            """)
            
        # Academic Advisor's Learning Path
        with st.expander("Academic Advisor's Learning Path", expanded=True):
            st.write(f"""
            Here's your learning path for {topic}:
            1. Week 1-2: Fundamentals
            2. Week 3-4: Intermediate Concepts
            3. Week 5-6: Advanced Topics
            4. Week 7-8: Practical Projects
            """)
            
        # Research Librarian's Resources
        with st.expander("Research Librarian's Resources", expanded=True):
            st.write(f"""
            Recommended resources for {topic}:
            1. Online Courses
            2. Key Textbooks
            3. Video Tutorials
            4. Practice Platforms
            """)
            
        # Teaching Assistant's Exercises
        with st.expander("Teaching Assistant's Exercises", expanded=True):
            st.write(f"""
            Practice exercises for {topic}:
            1. Beginner Exercises
            2. Intermediate Challenges
            3. Advanced Problems
            4. Real-world Projects
            """)
