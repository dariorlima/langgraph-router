
from langgraph.graph import StateGraph, START, END

from langflow_router.core.agents import query_agent_factory
from langflow_router.core.composer import format_response_factory
from langflow_router.core.router import route_query_factory
from langflow_router.models.state import State
from langflow_router.utils.logging import setup_logger

logger = setup_logger('graph')

def build_graph(
    model_name: str,
    agents: list[dict],
):
    logger.info("Starting Graph")

    graph_builder = StateGraph(State)

    # router
    route_query = route_query_factory(model_name)

    # agent
    query_agent = query_agent_factory(model_name, agents)

    # Composer
    composer_agent = format_response_factory(model_name)

    graph_builder.add_node("Router", route_query)
    graph_builder.add_node("Agent", query_agent)
    graph_builder.add_node("Composer", composer_agent)

    # Connect the nodes
    graph_builder.add_edge(START, "Router")
    graph_builder.add_edge("Router", "Agent")
    graph_builder.add_edge("Agent", "Composer")
    graph_builder.add_edge("Composer", END)

    graph_builder.set_entry_point("Router")

    logger.info("Compiling Graph")


    return graph_builder.compile()
