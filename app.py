import streamlit as st

#########################
# Streamlit App Configuration
#########################

st.set_page_config(page_title="👨‍🏫 AI Teaching Agent Team")

#########################
# Response Generator
#########################

def generate_response(topic, agent_type):
    """Generate sample responses based on agent type"""
    responses = {
        "Professor": f"""Here's a knowledge base about {topic}:
        1. Basic concepts and fundamentals
        2. Key principles and theories
        3. Historical development
        4. Modern applications""",
        
        "Academic Advisor": f"""Learning path for {topic}:
        1. Week 1-2: Fundamentals
        2. Week 3-4: Core Concepts
        3. Week 5-6: Advanced Topics
        4. Week 7-8: Practical Applications""",
        
        "Research Librarian": f"""Resources for learning {topic}:
        1. Online courses and tutorials
        2. Recommended textbooks
        3. Video lectures
        4. Practice exercises""",
        
        "Teaching Assistant": f"""Practice exercises for {topic}:
        1. Beginner level tasks
        2. Intermediate challenges
        3. Advanced problems
        4. Real-world projects"""
    }
    return responses.get(agent_type, "Invalid agent type")

#########################
# Streamlit UI Setup
#########################

st.title("AI Teaching Agent Team")
st.write("Enter a topic you want to learn about, and our AI teaching agents will help create a comprehensive learning plan!")

# Text Input for Topic
topic = st.text_input(
    "Enter topic:",
    placeholder="e.g., Machine Learning"
)

# Button to Trigger Agent Runs
if st.button("Start"):
    if not topic:
        st.error("Please enter a topic first!")
    else:
        with st.spinner("Generating Knowledge Base..."):
            professor_response = generate_response(topic, "Professor")
            st.subheader("Professor's Knowledge Base")
            st.write(professor_response)
        
        with st.spinner("Creating Learning Path..."):
            advisor_response = generate_response(topic, "Academic Advisor")
            st.subheader("Academic Advisor's Learning Path")
            st.write(advisor_response)
        
        with st.spinner("Finding Resources..."):
            librarian_response = generate_response(topic, "Research Librarian")
            st.subheader("Research Librarian's Resources")
            st.write(librarian_response)
        
        with st.spinner("Creating Exercises..."):
            ta_response = generate_response(topic, "Teaching Assistant")
            st.subheader("Teaching Assistant's Exercises")
            st.write(ta_response)
