from langgraph_router.models.state import State
from langchain_aws import ChatBedrockConverse
from langgraph.prebuilt import create_react_agent

from langgraph_router.utils.logging import setup_logger

logger = setup_logger('Agents')

def query_agent_factory(model_name: str, agents: list[dict]):
    """
    agents: list of agent dicts with keys: name, prompt (required).
    """
    agent_map = {a["name"]: a for a in agents}

    def query_agent(state: State):
        route = state.get("route")
        messages = state.get("messages")
        logger.info(f"Defining Routes: {route}")


        routes = [r.strip() for r in route.split("|")] if "|" in route else [route.strip()]
        results = []

        if len(state['messages']) <= 1 and '#' in routes[-1]:
            deleted_route = routes.pop()
            routes.append(deleted_route.split('#')[1])
        elif len(state['messages']) > 1 and '#' in state['messages'][-1].content:
            routes.pop()

        logger.info(f"Defining Routes Final: {routes} {state['messages'][-1]}")

        for r in routes:
            agent_data = agent_map.get(r)
            if not agent_data:
                continue

            prompt = f"""
                You are limited to the scope below. Do not mention or agree with anything outside of it.
                {agent_data["prompt"]}
            """

            logger.info(prompt)

            agent = create_react_agent(
                name=r,
                model=ChatBedrockConverse(model=model_name, temperature=0),
                tools=[],
                prompt=prompt,
            )

            response = agent.invoke({"messages": messages}).get("messages")[-1]
            results.append(response.content)

        return {"response": "\n".join(results)}

    return query_agent
