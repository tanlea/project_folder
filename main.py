import streamlit as st
import random

# Placeholder CrewAI query function (can be replaced with your actual logic)
def crewai_query(query):
    # Simulate response from website query
    knowledge_base = {
        "Python": "Python is a powerful programming language known for its ease of use and versatility.",
        "Streamlit": "Streamlit is an open-source app framework for Machine Learning and Data Science teams.",
        "AI": "Artificial Intelligence is a field of study focused on creating smart machines."
    }
    return knowledge_base.get(query, "I'm sorry, I couldn't find information on that topic.")

# Detailed information for each follow-up topic
def follow_up_info(topic):
    topic_details = {
        "AI in Healthcare": "AI is revolutionizing healthcare with predictive analytics, personalized medicine, and AI-driven diagnostics.",
        "Python for Data Science": "Python is widely used in data science for data manipulation, visualization, and machine learning using libraries like Pandas, Matplotlib, and Scikit-learn.",
        "Streamlit Best Practices": "Best practices in Streamlit include optimizing performance, structuring apps, and managing session state effectively."
    }
    return topic_details.get(topic, "I don't have more information on that topic.")

# Generate follow-up topics
def suggest_topics():
    topics = ["AI in Healthcare", "Python for Data Science", "Streamlit Best Practices"]
    return random.sample(topics, 3)  # Randomize the topics

# Streamlit app
st.title("AI Chatbot with Topic Suggestions")

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'follow_up_topic' not in st.session_state:
    st.session_state.follow_up_topic = None

# User input section
#user_input = st.text_input("Ask me anything:")
user_input = st.chat_input("Ask me anything:")

if user_input:
    # Store user input
    st.session_state.chat_history.append({"message": user_input, "is_user": True})

    # Generate AI response
    ai_response = crewai_query(user_input)
    st.session_state.chat_history.append({"message": ai_response, "is_user": False})

    # Suggest follow-up topics
    suggested_topics = suggest_topics()
    st.session_state.chat_history.append({
        "message": f"Would you like to know more about:", 
        "is_user": False,
        "topics": suggested_topics
    })

# Display the chat history using Streamlit elements
for index, chat in enumerate(st.session_state.chat_history):
    if chat["is_user"]:
        st.markdown(f"**You:** {chat['message']}")
    else:
        st.markdown(f"**Bot:** {chat['message']}")
        if "topics" in chat:
            # Display follow-up topic buttons with unique keys
            topic_a, topic_b, topic_c = chat["topics"]
            if st.button(topic_a, key=f"topic_a_{index}"):
                st.session_state.follow_up_topic = topic_a
            if st.button(topic_b, key=f"topic_b_{index}"):
                st.session_state.follow_up_topic = topic_b
            if st.button(topic_c, key=f"topic_c_{index}"):
                st.session_state.follow_up_topic = topic_c

# Show detailed information if a topic is selected
if st.session_state.follow_up_topic:
    detailed_info = follow_up_info(st.session_state.follow_up_topic)
    st.markdown(f"**Bot:** {detailed_info}")

# Option to restart conversation
if st.button("Restart Conversation", key="restart"):
    # Clear the session state
    for key in st.session_state.keys():
        del st.session_state[key]
    
    # Set a query parameter to force the app to rerun and reset the session state
    st.experimental_set_query_params(reset="true")
