import requests
from langchain import hub
from langchain.tools import tool
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.runnable import RunnablePassthrough, RunnableLambda
from operator import itemgetter
from langchain.utilities import SerpAPIWrapper
# from portability_agent_poc import openfinance_tool, portability_tool
import json
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.agents import AgentExecutor
from langchain.agents.format_scratchpad import format_log_to_messages
from langchain.agents.output_parsers import JSONAgentOutputParser
from langchain.tools.render import render_text_description

# @tool
def openfinance_tool_function():
    """Api responsável por buscar dados no OpenFinance"""
    try:
        response = requests.get("http://127.0.0.1:8080/account_data")
        return response.content.decode('UTF-8')
    except:
        response = 'Não foi possível chamar a API do OpenFinance.'
        return response
    
# @tool
def portability_tool_function(json_data: str):
    """Api resonsável por cadastrar a solicitação de portabilidade"""
    try:
        response = requests.post(url="http://127.0.0.1:8081/effect_portability", json=json_data)
        return response.content.decode('UTF-8')
    except:
        response = 'Não foi possível chamar a API de portabilidade.'
        return response

# tools = [openfinance_tool_function, portability_tool_function]

# f = open('init_prompt.txt', 'r')
# prompt_template = f.read()

# prompt = hub.pull('hwchase17/react-chat-json')
# prompt = prompt.partial(
#     tools = render_text_description(tools),
#     tool_names=', '.join([t.name for t in tools])
# ) | ChatPromptTemplate.from_messages(
#     [
#         ('system', prompt_template),
#         MessagesPlaceholder(variable_name='chat_history'),
#         ('human', '{input}'),
#     ]
# )

# llm = ChatOpenAI(model='gpt-3.5-turbo')

# # agent = initialize_agent(tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

# memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

# # chain = (
# #     RunnablePassthrough.assign(
# #         history=RunnableLambda(memory.load_memory_variables) | itemgetter('history')
# #     )
# #     | prompt
# #     | llm
# # )

# agent = (
#     {
#         'input': lambda x: x['input'],
#         'agent_scratchpad': lambda x: format_log_to_messages(
#             x['intermediate_steps'], template_tool_response='{observation}'
#         ),
#         'chat_history': lambda x: x['chat_history'],
#     }
#     | prompt
#     | llm
#     | JSONAgentOutputParser()
# )

# agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory)

# agent_executor.invoke({"input": "Gostária de fazer a portabilidade do meu salário"})['output']

# agent = initialize_agent()

# def interaction_agent_mock():
#     call_gpt({'input':"Olá, gostaria de fazer a portabilidade do meu salário para o banco XPTO"}, True)
#     portability_agent()

# def call_gpt(input, isUserMessage):
#     response = chain.invoke(input)
#     memory.save_context(input, {'output': response.content})
#     if isUserMessage:
#         user_message = input['input']
#         print(f"User: "+ user_message)
#     print('--------------------------')
#     print(f'IA: ' + response.content)
#     print('--------------------------')

# def portability_agent():
#     portability_data = openfinance_tool()
#     call_gpt({'input':portability_data}, False)
#     call_gpt({'input':"Isso, todas as informações estão corretas!"}, True)
#     portability_json = json.loads(portability_data)['data']
#     call_gpt({'input': portability_tool(portability_json)}, False)

# portability_agent()



