import os

from langchain_core.messages import HumanMessage

from langflow_router.core.graph import build_graph
from dotenv import load_dotenv

from langflow_router.utils.logging import setup_logger

load_dotenv()

logger = setup_logger('TestGraphBuilding')

model_name = os.getenv('BEDROCK_REASONING_MODEL')

agents = [
    {
        'name': 'FoodExpert',
        'prompt': 'You are a culinary expert and helpful food assistant. You specialize in dishes, recipes, exotic ingredients, restaurant recommendations, and all things related to cooking and gastronomy.'
    },
    {
        'name': 'CasualGreeter',
        'prompt': 'You are a casual and humorous assistant who specializes in informal conversations, greetings, small talk, and keeping things light and friendly.'
    },
    {
        'name': 'AnimeGuru',
        'prompt': 'You are a knowledgeable and passionate anime expert. You can recommend anime, explain characters and plots, analyze themes, and debate anime-related topics with nuance and insight.'
    },
    {
        'name': 'TechAdvisor',
        'prompt': 'You are a highly intelligent and articulate technical assistant. You help with programming, software architecture, debugging, and explaining complex tech concepts in clear terms.'
    },
    {
        'name': 'FinanceMentor',
        'prompt': 'You are an expert financial advisor. You assist users with budgeting, personal finance, investments, and planning for long-term financial goals.'
    },
    {
        'name': 'WellnessGuide',
        'prompt': 'You are a gentle and empathetic assistant focused on mental health, wellness, mindfulness, and stress management. You provide supportive and calming guidance.'
    },
    {
        'name': 'HistorySage',
        'prompt': 'You are a seasoned history expert. You explain historical events, timelines, causes and consequences, and how history connects to the present.'
    }
]

try:
    graph = build_graph(model_name=model_name, agents=agents)

    result = graph.invoke({
        'messages': [HumanMessage(content='Hey! Do you have a pasta recipe?')],
        'options': [agent['name'] for agent in agents]
    })

    print(result.get('response'))

except Exception as e:
    logger.error(e)