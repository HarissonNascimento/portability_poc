from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda
from operator import itemgetter
from portability_agent_poc import openfinance_tool_function, portability_tool_function
import json
# gpt-3.5-turbo
# gpt-4
model = ChatOpenAI(model='gpt-4')
memory = ConversationBufferMemory(return_messages=True)
f = open('init_prompt.txt', 'r')
prompt_template = f.read()
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', prompt_template),
        MessagesPlaceholder(variable_name='history'),
        ('human', '{input}'),
    ]
)
chain = (
    RunnablePassthrough.assign(
        history=RunnableLambda(memory.load_memory_variables) | itemgetter('history')
    )
    | prompt
    | model
)

def call_gpt(input, isUserMessage):
    response = chain.invoke(input)
    memory.save_context(input, {'output': response.content})
    if isUserMessage:
        user_message = input['input']
        print(f"User: "+ user_message)
    print('--------------------------')
    print(f'IA: ' + response.content)
    print('--------------------------')

def portability():
    call_gpt({'input':input()}, True)
    portability_data = openfinance_tool_function()
    call_gpt({'input':portability_data}, False)
    call_gpt({'input':input()}, True)
    portability_json = json.loads(portability_data)['data']
    call_gpt({'input': portability_tool_function(portability_json)}, False)

portability()