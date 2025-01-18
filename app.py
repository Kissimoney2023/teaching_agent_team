import streamlit as st

#########################
# Streamlit App Configuration
#########################

st.set_page_config(page_title="👨‍🏫 AI Teaching Agent Team")

#########################
# Simple Response Generator
#########################

def generate_response(prompt, agent_type):
    """Simple function to generate responses based on agent type"""
    if agent_type == "professor":
        return f"Here's a comprehensive knowledge base about {prompt}..."
    elif agent_type == "advisor":
        return f"Here's a learning roadmap for {prompt}..."
    elif agent_type == "librarian":
        return f"Here are some learning resources for {prompt}..."
    elif agent_type == "assistant":
        return f"Here are some practice exercises for {prompt}..."
    return "Please provide a topic to learn about."

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
            professor_response = generate_response(topic, "professor")
            st.subheader("Professor's Knowledge Base")
            st.write(professor_response)
        
        with st.spinner("Creating Learning Path..."):
            advisor_response = generate_response(topic, "advisor")
            st.subheader("Academic Advisor's Learning Path")
            st.write(advisor_response)
        
        with st.spinner("Finding Resources..."):
            librarian_response = generate_response(topic, "librarian")
            st.subheader("Research Librarian's Resources")
            st.write(librarian_response)
        
        with st.spinner("Creating Exercises..."):
            ta_response = generate_response(topic, "assistant")
            st.subheader("Teaching Assistant's Exercises")
            st.write(ta_response)
