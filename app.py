import openai
import streamlit as st
st.title("🎬 ScriptBoost - Short Video Script Generator")

openai.api_key = "your-openai-api-key"  # Replace with your OpenAI API key
st.title("Video Script Generator")


st.write("""
    This app generates video ideas, scripts, and trending hashtags based on a given topic.
    Just type in a topic like "self-development", "travel", or "fitness" to get started!
""")

topic = st.text_input("Enter your topic")

def generate_content(topic):
    #Request OpenAi to generate ideas
    prompt_ideas = f"Generate 5 video ideas for the topic '{topic}' in a short, engaging style."
    ideas_response = openai.Completion.create(
        engine="text-davinci-003",  # Or GPT-4 if you have access
        prompt=prompt_ideas,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    ideas = ideas_response.choices[0].text.strip().split("\n")
    prompt_scripts = f"Write 5 short video scripts (20-40 seconds) based on the topic '{topic}'."
    scripts_response = openai.Completion.create(
        engine="text-davinci-003", # Or GPT-4   
        prompt=prompt_scripts,
        max_tokens=300,
        temperature=0.7
    )
    scripts = scripts_response.choices[0].text.strip().split("\n")
    
    prompt_hashtags = f"Generate 5 trending hashtags for the topic '{topic}'."
    hashtags_response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_hashtags,
        max_tokens=50,
        temperature=0.7
    )
    hashtags = hashtags_response.choices[0].text.strip().split("\n")

    return ideas, scripts, hashtags
    st.title("SparkShort: Video Idea Generator")
    st.write("Easily create ideas, scripts, and hashtags for your TikTok/Reels videos.")
