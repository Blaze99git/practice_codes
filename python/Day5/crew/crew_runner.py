from crewai import Agent, Crew, Task
from crew.agents import preanalysis, diagnostics, action

def run_agent(step, state):

    if step == "preanalysis":
        return preanalysis(state["data"])

    if step == "diagnostics":
        return diagnostics(state["data"])

    if step == "action":
        return action(state["results"]["diagnostics"])


    return {}
