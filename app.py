import streamlit as st
from transformers import pipeline

#########################
# Streamlit App Configuration
#########################

st.set_page_config(page_title="👨‍🏫 AI Teaching Agent Team")

#########################
# Model Setup
#########################

@st.cache_resource
def load_model():
    try:
        return pipeline('text-generation', model='distilgpt2')
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def generate_response(prompt, agent_type):
    """Generate responses using the model"""
    try:
        model = load_model()
        if model is None:
            return f"Sample response for {agent_type} about {prompt} (Model loading failed)"
            
        response = model(f"{agent_type} explanation about {prompt}", 
                        max_length=100, 
                        num_return_sequences=1)[0]['generated_text']
        return response
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")
        return f"Could not generate response for {prompt}"

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
