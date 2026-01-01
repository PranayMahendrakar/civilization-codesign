"""
Human-Machine Civilization Co-Design Platform
Exploring optimal arrangements of human and AI capabilities for future societies
Author: Pranay M
"""

import ollama
import json
from datetime import datetime
from pathlib import Path
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.progress import Progress, SpinnerColumn, TextColumn
import sys

console = Console()
MODEL = "llama3.2"
DATA_DIR = Path("civilization_data")
DATA_DIR.mkdir(exist_ok=True)


@dataclass
class SocietalDomain:
    """A domain of societal function"""
    name: str
    human_strengths: List[str]
    ai_strengths: List[str]
    current_arrangement: str
    transition_challenges: List[str]


SOCIETAL_DOMAINS = [
    SocietalDomain("Governance", ["Value judgments", "Legitimacy", "Accountability"], 
                   ["Data analysis", "Consistency", "Prediction"], "Humans decide with AI assistance",
                   ["Legitimacy", "Power concentration"]),
    SocietalDomain("Healthcare", ["Empathy", "Complex judgment", "Patient relationship"],
                   ["Diagnosis", "Drug discovery", "Monitoring"], "Human practitioners with AI tools",
                   ["Trust", "Liability"]),
    SocietalDomain("Education", ["Mentorship", "Inspiration", "Character development"],
                   ["Personalization", "Assessment", "Accessibility"], "Human teachers with AI supplements",
                   ["Human development", "Social skills"]),
    SocietalDomain("Creative Arts", ["Meaning", "Emotion", "Authenticity"],
                   ["Generation", "Variation", "Collaboration"], "Human creators with AI tools",
                   ["Authenticity", "Value"]),
    SocietalDomain("Scientific Research", ["Intuition", "Questions", "Ethics"],
                   ["Computation", "Pattern finding", "Simulation"], "Human scientists with AI assistance",
                   ["Understanding", "Credit"])
]


class CapabilityMapper:
    """Map human and AI capabilities"""
    
    def analyze_domain(self, domain: str) -> str:
        """Analyze human vs AI capabilities in a domain"""
        prompt = f"""Analyze human and AI capabilities in: {domain}

Provide:
1. **Human Advantages**: Where humans excel and why
2. **AI Advantages**: Where AI excels and why
3. **Complementarities**: Where human+AI > either alone
4. **Current Division**: How work is currently divided
5. **Optimal Division**: Ideal capability allocation
6. **Transition Path**: How to get from current to optimal
7. **Safeguards**: How to protect human interests"""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']
    
    def identify_complementarities(self, task: str) -> str:
        """Find human-AI complementarities for a task"""
        prompt = f"""Identify human-AI complementarities for: {task}

Analyze:
1. **Subtasks**: Break down the task
2. **Assignment**: Which subtasks best for human, AI, or together
3. **Integration Points**: Where handoffs occur
4. **Synergies**: Where collaboration multiplies value
5. **Workflow Design**: Optimal human-AI workflow"""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']


class ScenarioGenerator:
    """Generate and analyze civilization scenarios"""
    
    def generate_scenario(self, parameters: Dict) -> str:
        """Generate a detailed civilization scenario"""
        prompt = f"""Generate a human-AI civilization scenario:

PARAMETERS: {json.dumps(parameters, indent=2)}

Include:
1. **Overview**: What this civilization looks like
2. **Daily Life**: How people live day-to-day
3. **Work & Economy**: How value is created/distributed
4. **Governance**: How decisions are made
5. **Education**: How people learn
6. **Human Flourishing**: How humans find meaning
7. **AI Role**: Exact role of AI systems
8. **Risks & Mitigations**: What could go wrong"""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']
    
    def compare_scenarios(self, scenario1: str, scenario2: str) -> str:
        """Compare two civilization scenarios"""
        prompt = f"""Compare civilization scenarios:

SCENARIO 1: {scenario1[:1200]}

SCENARIO 2: {scenario2[:1200]}

Compare on: Human Flourishing, Efficiency, Equity, Freedom, Safety, Feasibility"""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']


class GovernanceDesigner:
    """Design human-AI governance systems"""
    
    def design_governance(self, context: str) -> str:
        """Design governance structure"""
        prompt = f"""Design human-AI governance for: {context}

Include:
1. **Decision Rights**: Who/what decides what
2. **Accountability**: How responsibility is assigned
3. **Oversight**: How AI is monitored
4. **Human Control**: How human override works
5. **Adaptation**: How the system evolves
6. **Fail-safes**: What happens when things go wrong"""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']
    
    def analyze_power_dynamics(self, arrangement: str) -> str:
        """Analyze power dynamics"""
        prompt = f"""Analyze power dynamics in: {arrangement}

Examine: Power Distribution, Dependencies, Concentration Risks, Human Agency, 
Checks & Balances, Vulnerable Groups"""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']


class EconomicDesigner:
    """Design human-AI economic systems"""
    
    def design_economy(self, parameters: Dict) -> str:
        """Design economic system"""
        prompt = f"""Design human-AI economic system:

PARAMETERS: {json.dumps(parameters, indent=2)}

Include: Value Creation, Distribution, Work roles, Meaning/Purpose, 
Incentives, Ownership, Safety Net, Transition path"""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']


class FlourishingAnalyzer:
    """Analyze human flourishing"""
    
    def analyze_flourishing(self, scenario: str) -> str:
        """Analyze human flourishing potential"""
        prompt = f"""Analyze human flourishing in: {scenario[:1500]}

Evaluate: Physical Health, Mental Health, Social Connection, Autonomy, 
Competence, Purpose, Creativity, Spirituality

Provide overall flourishing score and key insights."""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']
    
    def identify_risks(self, arrangement: str) -> str:
        """Identify risks to human flourishing"""
        prompt = f"""Identify risks in: {arrangement}

Analyze: Dependency Risks, Skill Atrophy, Meaning Crisis, Social Fragmentation,
Autonomy Erosion, Inequality, Control Loss, Existential risks

For each: Likelihood, Severity, Mitigations"""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']


class ParticipatoryDesign:
    """Tools for inclusive civilization design"""
    
    def generate_discussion_guide(self, topic: str) -> str:
        """Generate guide for public deliberation"""
        prompt = f"""Create public deliberation guide for: {topic}

Include: Introduction, Key Questions, Different Perspectives, Trade-offs,
Concrete Scenarios, Values Clarification, Discussion Prompts, Decision Framework"""

        response = ollama.generate(model=MODEL, prompt=prompt)
        return response['response']


def show_banner():
    banner = """
╔══════════════════════════════════════════════════════════════╗
║     🌐 Human-Machine Civilization Co-Design Platform 🌐      ║
║          Designing Our Shared Future Together                ║
║                    Author: Pranay M                          ║
╚══════════════════════════════════════════════════════════════╝
    """
    console.print(Panel(banner, style="bold green"))


def show_menu():
    table = Table(title="Civilization Co-Design", show_header=False, box=None)
    table.add_column("Option", style="cyan")
    table.add_column("Description")
    
    table.add_row("1", "🔍 Analyze Domain Capabilities")
    table.add_row("2", "🤝 Find Complementarities")
    table.add_row("3", "🌆 Generate Civilization Scenario")
    table.add_row("4", "🏛️ Design Governance")
    table.add_row("5", "💰 Design Economy")
    table.add_row("6", "🌱 Analyze Flourishing")
    table.add_row("7", "⚠️  Identify Risks")
    table.add_row("8", "👥 Public Deliberation Guide")
    table.add_row("0", "🚪 Exit")
    
    console.print(table)


scenarios = []


def analyze_domain():
    console.print("\n[cyan]Domains:[/cyan]", ", ".join(d.name for d in SOCIETAL_DOMAINS))
    domain = Prompt.ask("Domain", default="Healthcare")
    
    with Progress(SpinnerColumn(), TextColumn("Analyzing...")) as progress:
        task = progress.add_task("", total=None)
        analysis = CapabilityMapper().analyze_domain(domain)
    
    console.print(Panel(analysis, title=f"Capability Analysis: {domain}"))


def find_complementarities():
    task_desc = Prompt.ask("Task to analyze", default="medical diagnosis")
    
    with Progress(SpinnerColumn(), TextColumn("Analyzing...")) as progress:
        task = progress.add_task("", total=None)
        analysis = CapabilityMapper().identify_complementarities(task_desc)
    
    console.print(Panel(analysis, title="Human-AI Complementarities"))


def generate_scenario():
    params = {
        "ai_level": Prompt.ask("AI capability level", default="highly capable"),
        "relationship": Prompt.ask("Human-AI relationship", default="collaborative"),
        "governance": Prompt.ask("Governance approach", default="democratic with AI assistance"),
        "economy": Prompt.ask("Economic model", default="mixed with UBI"),
        "timeframe": Prompt.ask("Timeframe", default="2050")
    }
    
    with Progress(SpinnerColumn(), TextColumn("Generating...")) as progress:
        task = progress.add_task("", total=None)
        scenario = ScenarioGenerator().generate_scenario(params)
    
    scenarios.append(scenario)
    console.print(Panel(scenario, title="Civilization Scenario"))


def design_governance():
    context = Prompt.ask("Governance context", default="national policy-making with AI")
    
    with Progress(SpinnerColumn(), TextColumn("Designing...")) as progress:
        task = progress.add_task("", total=None)
        design = GovernanceDesigner().design_governance(context)
    
    console.print(Panel(design, title="Governance Design"))


def design_economy():
    params = {
        "automation": Prompt.ask("Automation level", default="high"),
        "ownership": Prompt.ask("AI ownership model", default="mixed"),
        "distribution": Prompt.ask("Distribution approach", default="UBI + work")
    }
    
    with Progress(SpinnerColumn(), TextColumn("Designing...")) as progress:
        task = progress.add_task("", total=None)
        design = EconomicDesigner().design_economy(params)
    
    console.print(Panel(design, title="Economic Design"))


def analyze_flourishing():
    scenario = scenarios[-1] if scenarios else Prompt.ask("Describe scenario")
    
    with Progress(SpinnerColumn(), TextColumn("Analyzing...")) as progress:
        task = progress.add_task("", total=None)
        analysis = FlourishingAnalyzer().analyze_flourishing(scenario[:2000])
    
    console.print(Panel(analysis, title="Human Flourishing Analysis"))


def identify_risks():
    arrangement = Prompt.ask("Describe human-AI arrangement")
    
    with Progress(SpinnerColumn(), TextColumn("Analyzing...")) as progress:
        task = progress.add_task("", total=None)
        risks = FlourishingAnalyzer().identify_risks(arrangement)
    
    console.print(Panel(risks, title="Risks to Flourishing"))


def deliberation_guide():
    topic = Prompt.ask("Topic for deliberation", default="AI in healthcare")
    
    with Progress(SpinnerColumn(), TextColumn("Creating guide...")) as progress:
        task = progress.add_task("", total=None)
        guide = ParticipatoryDesign().generate_discussion_guide(topic)
    
    console.print(Panel(guide, title="Public Deliberation Guide"))


def main():
    show_banner()
    
    try:
        ollama.list()
    except Exception:
        console.print("[red]Error: Ollama not running. Start with: ollama serve[/red]")
        sys.exit(1)
    
    while True:
        show_menu()
        choice = Prompt.ask("\nSelect option", default="0")
        
        actions = {
            "1": analyze_domain, "2": find_complementarities, "3": generate_scenario,
            "4": design_governance, "5": design_economy, "6": analyze_flourishing,
            "7": identify_risks, "8": deliberation_guide
        }
        
        if choice == "0":
            console.print("[yellow]Building the future together! 🌐[/yellow]")
            break
        elif choice in actions:
            actions[choice]()
        else:
            console.print("[red]Invalid option[/red]")
        
        console.print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()
