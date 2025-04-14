from dataclasses import dataclass, field
from typing import Any, Dict, Optional
import datetime

@dataclass
class Experience:
    """
    Represents a single step of interaction between agent and environment.
    Core fields expected by the framework. Can be subclassed for specific domains.

    Attributes:
        observation (Any): Observation from the environment before the action.
        info (Dict[str, Any]): Auxiliary info from the environment before the action.
        agent_action (Any): The action taken by the agent.
        reward (float): The reward received after taking the action.
        terminated (bool): Flag indicating if the episode ended naturally (terminal state reached).
        truncated (bool): Flag indicating if the episode was ended prematurely (e.g., time limit).
        next_observation (Any): Observation from the environment after the action.
        next_info (Dict[str, Any]): Auxiliary info from the environment after the action.
        prompt (Optional[str]): The prompt given to the agent (if applicable).
        timestamp (datetime.datetime): Timestamp of when the experience was recorded.
    """
    # State/Observation info before action
    observation: Any
    info: Dict[str, Any]

    # Action taken
    agent_action: Any

    # Outcome info after action (from Env Step)
    reward: float
    terminated: bool
    truncated: bool
    next_observation: Any
    next_info: Dict[str, Any]

    # Optional fields (useful for ODFT / specific agents)
    prompt: Optional[str] = None
    timestamp: datetime.datetime = field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc))

    # Domain-specific fields can be added via subclassing or in 'info'/'outcome' dicts
    # e.g., benchmark_outcomes: Optional[Dict[str, Dict[str, Any]]] = None
    #       priority: Optional[float] = None

    def __post_init__(self):
        # Ensure next_observation/info are None if the episode ended
        if self.terminated or self.truncated:
            self.next_observation = None
            self.next_info = {}

    @property
    def done(self) -> bool:
        """Convenience property to check if the step was terminal in any way."""
        return self.terminated or self.truncated

    def __str__(self):
        return (
            f"Experience(obs={self.observation}, info={self.info}, action={self.agent_action}, "
            f"reward={self.reward:.2f}, terminated={self.terminated}, truncated={self.truncated}, "
            f"next_obs={self.next_observation}, next_info={self.next_info}, done={self.done}, "
            f"prompt={'...' if self.prompt else None}, timestamp={self.timestamp})"
        )