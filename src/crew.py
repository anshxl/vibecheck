from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class VibeCheckCrew():
    """Crew for vibe-based venue recommendations"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # --- Agents ---
    @agent
    def vision_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['vision_analyst'],  # type: ignore[index]
            llm=LLM(model="anthropic/claude-sonnet-4-20250514", temperature=0.7),
            verbose=True
        )

    @agent
    def venue_finder(self) -> Agent:
        return Agent(
            config=self.agents_config['venue_finder'],  # type: ignore[index]
            llm=LLM(model="anthropic/claude-sonnet-4-20250514", temperature=0.7),
            verbose=True,
            tools=[SerperDevTool(
                country="us",
                locale="en",
                location="Chicago, Illinois, United States",
                n_results=5,
            )]
        )

    @agent
    def recommender(self) -> Agent:
        return Agent(
            config=self.agents_config['recommender'],  # type: ignore[index]
            llm=LLM(model="anthropic/claude-sonnet-4-20250514", temperature=0.7),
            verbose=True
        )

    # --- Tasks ---
    @task
    def analyze_vibe(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_vibe']  # type: ignore[index]
        )

    @task
    def find_venues(self) -> Task:
        return Task(
            config=self.tasks_config['find_venues']  # type: ignore[index]
        )

    @task
    def package_results(self) -> Task:
        return Task(
            config=self.tasks_config['package_results']  # type: ignore[index]
        )

    # --- Crew ---
    @crew
    def crew(self) -> Crew:
        """Creates the VibeCheck crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,  # run agents in order
            verbose=True,
        )
