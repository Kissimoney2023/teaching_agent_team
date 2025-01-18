import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Teaching Agent Team",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
    }
    .stExpander {
        background-color: #f0f2f6;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    h1 {
        color: #FF4B4B;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("👨‍🏫 Teaching Agent Team")
st.markdown("---")

# Description with better formatting
st.markdown("""
    <div style='background-color: #f0f2f6; padding: 1rem; border-radius: 10px; margin-bottom: 2rem;'>
        <h4>Welcome to your AI Teaching Team! 🎓</h4>
        <p>Enter any topic you want to learn, and our specialized AI agents will create a comprehensive learning plan for you.</p>
    </div>
""", unsafe_allow_html=True)

# Input section with improved layout
col1, col2 = st.columns([3, 1])
with col1:
    topic = st.text_input("Enter topic:", placeholder="e.g., Machine Learning")
with col2:
    st.write("")  # Add some spacing
    generate = st.button("Generate Learning Plan 🚀")

# Generate responses
if generate:
    if not topic:
        st.error("⚠️ Please enter a topic first!")
    else:
        st.success(f"🎯 Generating comprehensive learning plan for: {topic}")
        
        # Professor's Knowledge Base
        with st.expander("🎓 Professor's Knowledge Base", expanded=True):
            st.markdown(f"""
            ### Core Knowledge for {topic}:
            
            1. **Core Concepts**
               - Fundamental principles
               - Basic terminology
               - Key frameworks
            
            2. **Key Principles**
               - Best practices
               - Design patterns
               - Industry standards
            
            3. **Historical Context**
               - Evolution of {topic}
               - Major developments
               - Important milestones
            
            4. **Current Applications**
               - Modern use cases
               - Industry applications
               - Future trends
            """)
        
        # Academic Advisor's Learning Path
        with st.expander("📚 Academic Advisor's Learning Path", expanded=True):
            st.markdown(f"""
            ### Your Learning Journey for {topic}:
            
            1. **Weeks 1-2: Fundamentals**
               - Basic concepts
               - Essential tools
               - Foundation skills
            
            2. **Weeks 3-4: Intermediate Concepts**
               - Advanced topics
               - Practical applications
               - Real-world examples
            
            3. **Weeks 5-6: Advanced Topics**
               - Complex problems
               - System design
               - Performance optimization
            
            4. **Weeks 7-8: Practical Projects**
               - Portfolio projects
               - Team collaboration
               - Industry practices
            """)
        
        # Research Librarian's Resources
        with st.expander("📖 Research Librarian's Resources", expanded=True):
            st.markdown(f"""
            ### Learning Resources for {topic}:
            
            1. **Online Courses**
               - Interactive tutorials
               - Video lectures
               - Hands-on workshops
            
            2. **Key Textbooks**
               - Comprehensive guides
               - Reference materials
               - Practice workbooks
            
            3. **Video Tutorials**
               - Step-by-step guides
               - Expert explanations
               - Live coding sessions
            
            4. **Practice Platforms**
               - Interactive exercises
               - Code challenges
               - Project templates
            """)
        
        # Teaching Assistant's Exercises
        with st.expander("✍️ Teaching Assistant's Exercises", expanded=True):
            st.markdown(f"""
            ### Practice Plan for {topic}:
            
            1. **Beginner Exercises**
               - Basic problems
               - Guided practice
               - Foundational skills
            
            2. **Intermediate Challenges**
               - Complex scenarios
               - Real-world problems
               - Independent work
            
            3. **Advanced Problems**
               - System design
               - Optimization tasks
               - Edge cases
            
            4. **Real-world Projects**
               - Portfolio building
               - Team collaboration
               - Industry standards
            """)
            
# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Made with ❤️ by the Teaching Agent Team</p>
    </div>
""", unsafe_allow_html=True)
