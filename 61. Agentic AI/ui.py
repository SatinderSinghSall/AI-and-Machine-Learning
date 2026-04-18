import streamlit as st
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title = "🎥 Youtube Video Analyzer",
    layout = "centered"
)

st.title("🎥 AI Youtube Video Analyzer")

@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

# Input Box / Text:
video_url = st.text_input("Enter Youtube Video URL/Link: ")

# Submit Button:
button = st.button("Analyse Video")

if video_url and button:
    with st.spinner("Analyzing Video..."):
        response = agent.run(
            f"Analyse this Video: {video_url}"
        )
        
    st.markdown("Analysis Report of the Video:")
    st.markdown(response.content)

# To run app: python -m streamlit run ui.py
