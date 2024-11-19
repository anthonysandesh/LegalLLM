import os
import json
import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))
GROQ_API_KEY = config_data["GROQ_API_KEY"]
os.environ["GROQ_API_KEY"] = GROQ_API_KEY


@st.cache_resource
def setup_vectorstore():
    persist_directory = f"{working_dir}/vector_db_dir"
    embeddings = HuggingFaceEmbeddings()
    vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
    return vectorstore


@st.cache_resource
def create_chain(_vectorstore):
    llm = ChatGroq(model="llama-3.1-70b-versatile", temperature=0)
    retriever = _vectorstore.as_retriever()

    custom_prompt = """
    You are a legal assistant specialized in the US legal domain. Your goal is to help the user by providing detailed and relevant legal information for their query.
    The user will ask questions related to legal cases, and you should respond by:
    
    1. Retrieving and listing 2 similar cases from the database.
    2. Recommending the most applicable precedent case and explaining why it is relevant.
    3. Predicting the likely judgment of the case based on historical case outcomes and precedents.

    Your response should be clear, concise, and based on historical legal data to ensure accuracy. Please ensure that you provide:
    - Two relevant similar cases with their basic details (e.g., case title, year, parties involved).
    - One relevant precedent case with an explanation of why it applies.
    - A reasoned prediction of the likely judgment outcome.

    User's Question: {question}
    """
    prompt_template = PromptTemplate(input_variables=["question"], template=custom_prompt)

    # Set up memory to explicitly save only the "answer" key
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        output_key="answer",  # Specify which key to save in memory
        return_messages=True
    )

    # Create the conversational retrieval chain
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        memory=memory,
        return_source_documents=True
    )
    return conversation_chain



st.set_page_config(page_title="Chatbot", page_icon="📚", layout="centered")
st.title("📚 LegalLLM Chatbot: California Legal Analytics")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

vectorstore = setup_vectorstore()
conversation_chain = create_chain(vectorstore)

if st.button("New Chat"):
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input for new messages
user_input = st.chat_input("Ask AI...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        response = conversation_chain({"question": user_input})
        assistant_response = response["answer"]
        st.markdown(assistant_response)
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
