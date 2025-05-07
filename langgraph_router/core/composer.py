from langgraph_router.models.state import State
from langchain_aws import ChatBedrockConverse
from langgraph.prebuilt import create_react_agent

def format_response_factory(model_name: str):
    def format_response(state: State):

        prompt = """
            Remove redundancy, as the text is a merge of two responses. 
            Fix grammar and ensure the message makes sense. 
            Do not add any new information—only include what is in the original message.
        """
        agent = create_react_agent(
            name="answer-composer",
            model=ChatBedrockConverse(model=model_name, temperature=0.3),
            tools=[],
            prompt=prompt,
        )

        execution = agent.invoke({'messages': [state.get('response')]})
        return {
            "response": execution['messages'][-1].content
        }

    return format_response
