from langchain_core.prompts import ChatPromptTemplate
from pathlib import Path
from langgraph_router.models.state import State
from langchain_aws import ChatBedrockConverse
from pydantic import BaseModel, Field

from langgraph_router.utils.logging import setup_logger

logger = setup_logger('Router')

def load_classifier_prompt() -> ChatPromptTemplate:
    prompt_path = Path(__file__).resolve().parent.parent / "core" / "prompts" / "classifier_prompt.txt"
    template = prompt_path.read_text(encoding="utf-8")

    logger.debug(f"Checking Route Template: {template}")
    return ChatPromptTemplate.from_messages([
        ("system", template),
        ("human", "{input}")
    ])

def route_query_factory(model_name: str):
    logger.info("Entering Router Query Factory")

    classifier_llm = ChatBedrockConverse(model=model_name, temperature=0)
    prompt = load_classifier_prompt()

    def route_query(state: State):
        class RouteQuery(BaseModel):
            route: str = Field(
                description="Given a provided message choose to route to one or more available options"
            )

        logger.info("Entering Router Query System")

        structured_llm_router = classifier_llm.with_structured_output(RouteQuery)
        router = prompt | structured_llm_router

        logger.info("Router has been created")

        last_message = state['messages'][-1]
        response = router.invoke({'input': last_message.content, 'options': state['options']})
        return {'route': response.route}

    return route_query