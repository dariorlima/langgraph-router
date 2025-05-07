# Langflow Router

This project demonstrates how to dynamically build and invoke an agent-routing graph using `LangGraph` and LangChain components. It simulates a multi-agent system where each agent specializes in a unique domain (e.g., cooking, tech, anime, wellness).

## 🔧 Features

* Defines multiple domain-specific AI agents.
* Dynamically constructs a reasoning graph using `build_graph()`.
* Routes user input to the most relevant agent using Bedrock's reasoning model.
* Uses environment configuration with `.env`.
* Includes logging for debugging and tracing.


## 📦 Requirements

* Python 3.8+
* `python-dotenv`
* `langgraph`
* `langchain`
* `langchain-aws`
* `pydantic`
* AWS credentials (for Bedrock)

## 📁 Environment Setup

Create a `.env` file based on `.env.example`

```env
# === AWS Bedrock ===
AWS_PROFILE=default

# === Bedrock Model ===
BEDROCK_REASONING_MODEL=anthropic.claude-3-sonnet-20240229-v1:0

# === Logging Setup ===
LOG_LEVEL=INFO

# === Langsmith Setup (Optional) ===
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT="https://api.smith.langchain.com"
LANGSMITH_API_KEY="*******"
LANGSMITH_PROJECT="*******"
```
## How to install
Go to the project root and run:
```bash
pip install -e .
```


## 🧠 Examples of Agents

| Name            | Description                                                       |
| --------------- | ----------------------------------------------------------------- |
| `FoodExpert`    | Culinary specialist for recipes, ingredients, and cooking advice. |
| `CasualGreeter` | Friendly, humorous assistant for light conversation.              |
| `AnimeGuru`     | Passionate anime expert for recommendations and discussions.      |
| `TechAdvisor`   | Technical expert for programming and debugging help.              |
| `FinanceMentor` | Financial advisor for budgeting and investment advice.            |
| `WellnessGuide` | Empathetic guide focused on mental health and wellness.           |
| `HistorySage`   | Knowledgeable historian explaining historical contexts.           |

## 📬 Example Query
```python 
HumanMessage(content='Hey! Do you have a pasta recipe?')
```

## 🚀 Running the Example
```bash 
python test/test_graph.py
```

## 📓 Expected results
This message would typically be routed to the FoodExpert agent.

```md
I'd be happy to share a pasta recipe with you! Here's a simple and delicious one:

**Classic Spaghetti Aglio e Olio**

**Ingredients:**
- 1 pound (450g) spaghetti
- 4-6 cloves garlic, thinly sliced
- 1/2 cup extra virgin olive oil
- 1/2 teaspoon red pepper flakes (adjust to taste)
- 1/4 cup fresh parsley, chopped
- Salt to taste
- Grated Parmesan cheese (optional)

**Instructions:**
1. Bring a large pot of salted water to boil and cook spaghetti according to package directions until al dente
2. While pasta cooks, gently heat olive oil in a large pan and add sliced garlic, cooking until just golden (be careful not to burn it)
3. Add red pepper flakes to the oil and remove from heat
4. Drain pasta, reserving 1/4 cup of pasta water
5. Add pasta to the pan with the garlic oil, toss well
6. Add reserved pasta water if needed for moisture
7. Stir in fresh parsley and season with salt
8. Serve immediately with grated Parmesan if desired

Would you like me to suggest any variations or a different pasta recipe instead?
```


