import openai
import streamlit as st

#Title
st.title("🎬 ScriptBoost - Short Video Script Generator")
#Enter API key
openai.api_key = "your-openai-api-key" #Replace with real API
# Mô tả ngắn gọn cho app
st.write("""
    This app generates video ideas, scripts, and trending hashtags based on a given topic.
    Just type in a topic like "self-development", "travel", or "fitness" to get started!
""")
# Nhập chủ đề
topic = st.text_input("Enter a topic (e.g., 'self-development', 'travel'):")
# Hàm lấy nội dung từ OpenAI
def generate_content(topic):
    prompt_ideas = f"Generate 5 video ideas for the topic '{topic}' in a short, engaging style."
    ideas_response = openai.completions.create(
         engine="text-davinci-003",
         prompt=prompt_ideas,
         max_tokens=150,
         temperature=0.7
    )
    ideas = ideas_response.choices[0].text.strip().split("\n")
    prompt_scripts = f"Write 5 short video scripts (20-40 seconds) based on the topic '{topic}'."
    scripts_response = openai.Completion.create(
        engine="text-davinci-003",
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
# Nút tạo nội dung
if st.button("Generate Content"):
    if topic:
        ideas, scripts, hashtags = generate_content(topic)

        st.subheader("💡 Video Ideas")
        for idea in ideas:
            st.write(f"- {idea}")

        st.subheader("🎬 Video Scripts")
        for script in scripts:
            st.write(f"- {script}")

        st.subheader("🔥 Trending Hashtags")
        for hashtag in hashtags:
            st.write(f"- {hashtag}")
    else:
        st.warning("⚠️ Please enter a topic!")

#         💡 Video Ideas
# - 1. 5-Minute Full Body Workout
# - 2. How to Stay Motivated at the Gym

# 🎬 Video Scripts
# - Script 1: Start your day with this 5-minute full body blast...
# - Script 2: Ever feel lazy to go to the gym? Try this trick...

# 🔥 Trending Hashtags
- #FitnessMotivation
- #QuickWorkout