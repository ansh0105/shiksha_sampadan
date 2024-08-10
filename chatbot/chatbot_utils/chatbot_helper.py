import os
from dotenv import load_dotenv
from langchain_community.chat_models import AzureChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain


load_dotenv(override= True)
os.environ["OPENAI_API_TYPE"] = os.getenv("OPENAI_API_TYPE")
os.environ["OPENAI_API_VERSION"] = os.getenv("OPENAI_API_VERSION")
os.environ["OPENAI_API_BASE"] = os.getenv("OPENAI_API_BASE")
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

def get_non_rtr_convo_chain() -> ConversationChain:
    """
    Initialize non-retrieval conversational chain of llm
    """
    llm = AzureChatOpenAI(deployment_name="gpt-4-turbo",
                          model_name="gpt-4-turbo",
                          temperature=0,
                          presence_penalty=0,
                          frequency_penalty = 0)
    memory = ConversationBufferMemory()
    conversation_chain = ConversationChain(
        llm=llm,
        memory=memory
    )
    return conversation_chain


