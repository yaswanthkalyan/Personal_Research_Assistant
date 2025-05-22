import streamlit as st
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool

# Load environment variables
load_dotenv()

# Define structured response model
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# Set up LLM and parser
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# Create prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use necessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Function to run the research
def run_research(query: str) -> ResearchResponse:
    raw_response = agent_executor.invoke({"query": query})
    return parser.parse(raw_response.get("output")[0]["text"])

# Streamlit UI
st.set_page_config(page_title="Research Assistant", layout="centered")
st.title("🧠 AI-Powered Research Assistant")

query = st.text_input("What can I help you research?", placeholder="Enter a research question...")

if st.button("Run Research") and query:
    with st.spinner("Researching..."):
        try:
            result = run_research(query)

            st.success("✅ Research Completed")
            st.subheader("📌 Topic")
            st.markdown(result.topic)

            st.subheader("🧠 Summary")
            st.markdown(result.summary)

            st.subheader("📚 Sources")
            for src in result.sources:
                st.markdown(f"- {src}")

            st.subheader("🛠️ Tools Used")
            st.markdown(", ".join(result.tools_used))

            report_text = f"""Research Report

            📌 Topic:
            {result.topic}

            🧠 Summary:
            {result.summary}

            📚 Sources:
            {chr(10).join(f"- {src}" for src in result.sources)}

            🛠️ Tools Used:
            {', '.join(result.tools_used)}
            """

            st.download_button(
                label="📄 Download Report (.txt)",
                data=report_text,
                file_name="research_report.txt",
                mime="text/plain"
            )

        except Exception as e:
            st.error(f"❌ Error: {e}")


