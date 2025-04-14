from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

# Assuming Experience is defined elsewhere, e.g., in core.experience
# from .experience import Experience
# For now, use 'Any' placeholder
Experience = Any

class BaseAgent(ABC):
    """
    Abstract Base Class for agents within the ODFT framework.

    Defines the essential methods an agent must implement to interact
    with the training loop and environment.
    """

    @abstractmethod
    def predict_action(self, observation: Any, info: Optional[Dict[str, Any]] = None) -> Any:
        """
        Predicts the next action based on the current observation and info.

        Args:
            observation (Any): The current environment observation.
            info (Optional[Dict[str, Any]]): Auxiliary information from the environment.

        Returns:
            Any: The predicted action.
        """
        pass

    @abstractmethod
    def update(self, experiences: List[Experience], config: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Updates the agent's policy based on a batch of experiences.

        Args:
            experiences (List[Experience]): A list of experiences to learn from.
            config (Optional[Dict[str, Any]]): Configuration relevant to the update step.

        Returns:
            Dict[str, Any]: A dictionary containing information about the update process
                            (e.g., loss, learning rate). Return an empty dict if no
                            relevant info is generated.
        """
        pass

    @abstractmethod
    def save(self, path: str) -> None:
        """
        Saves the agent's state (e.g., model weights, internal parameters) to a specified path.

        Args:
            path (str): The directory or file path to save the state.
        """
        pass

    @classmethod
    @abstractmethod
    def load(cls, path: str, config: Optional[Dict[str, Any]] = None) -> 'BaseAgent':
        """
        Loads the agent's state from a specified path.

        Args:
            path (str): The directory or file path to load the state from.
            config (Optional[Dict[str, Any]]): Configuration needed for loading.

        Returns:
            BaseAgent: An instance of the agent loaded with the saved state.
        """
        pass

    def train_mode(self) -> None:
        """
        Sets the agent to training mode (e.g., enables dropout, gradient tracking).
        Default implementation does nothing, subclasses should override if needed.
        """
        pass

    def eval_mode(self) -> None:
        """
        Sets the agent to evaluation mode (e.g., disables dropout, stops gradient tracking).
        Default implementation does nothing, subclasses should override if needed.
        """
        pass