"""
Lesson: Sequential Agent (Google Researcher)
============================================
A SequentialAgent pipeline: 
1. Researcher: Searches the live web using Google Search and saves ALL results.
2. Summarizer: Reads the saved search results and condenses them perfectly.
"""

from google.adk.agents import Agent, SequentialAgent
from google.adk.models import Gemini
from google.adk.tools import google_search  # CORRECT IMPORT: lowercase
from dotenv import load_dotenv

load_dotenv()

# Agent 1: The Researcher
researcher = Agent(
    name="researcher",
    model=Gemini(model="gemini-3-flash-preview"),
    tools=[google_search],  # Using the CORRECT built-in tool instance
    instruction=(
        "You are a professional web researcher. Use the google_search tool to find "
        "detailed and accurate facts about the user's topic. Your final response "
        "must contain all the key facts you discovered so the next agent can see them."
    ),
    output_key="research_raw",
)

# Agent 2: The Summarizer
summarizer = Agent(
    name="summarizer",
    model=Gemini(model="gemini-3-flash-preview"),
    instruction=(
        "You are a summary expert. Your job is to take the raw research findings "
        "provided by the researcher in: {research_raw}. "
        "Create a concise, 2-sentence bulleted summary for a student. "
        "Do not use your own knowledge; only summarize what was provided in the research."
    ),
)

# Root agent orchestrates the two-step flow
root_agent = SequentialAgent(
    name="sequential_pipeline",
    sub_agents=[researcher, summarizer],
    description="A pipeline that researches live topics and then summarizes them.",
)

from google.adk.apps import App
app = App(
    name="sequential",
    root_agent=root_agent,
)
