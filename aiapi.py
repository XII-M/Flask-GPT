import openai
import config
from langchain.llms import OpenAI
#from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationSummaryBufferMemory

openai.api_key = config.DevelopmentConfig.OPENAI_KEY

def generateChatResponse(messages, prompt):
    
    #messages.append({"role" : "system", "content" : "You are a assistant lawyer/paralegal"})

    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)

    response = openai.ChatCompletion.create(

        model="gpt-3.5-turbo", 
        messages=messages

    )

    try:
        answer = response['choices'][0]['message']['content'].replace('\n', '<br>')
    except:
        answer = 'Oops something went wrong, try a different question. If problem persists contact RM-GPT team (repo202306@gmail.com)'
    return answer

llm = OpenAI()

response = ConversationChain(
        llm=llm,
        memory=ConversationSummaryBufferMemory(llm=llm, max_token_limit=650),
        verbose=True
)

def chatResponse(prompt):

    chat_response = response.predict(input=prompt)
    
    return chat_response

    
