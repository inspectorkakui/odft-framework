from abc import ABC, abstractmethod
from typing import Any, Dict, Tuple

class BaseEnvironment(ABC):
    """
    Abstract Base Class for environments used within the ODFT framework.

    Defines the essential methods an environment must implement to interact
    with the training loop (e.g., RLTrainer).
    """

    @abstractmethod
    def reset(self) -> Tuple[Any, Dict[str, Any]]:
        """
        Resets the environment to its initial state.

        Returns:
            Tuple[Any, Dict[str, Any]]: A tuple containing the initial observation
                                        and auxiliary information (info dict).
        """
        pass

    @abstractmethod
    def step(self, action: Any) -> Tuple[Any, float, bool, bool, Dict[str, Any]]:
        """
        Takes a step in the environment using the provided action.

        Args:
            action (Any): The action to be taken by the agent.

        Returns:
            Tuple[Any, float, bool, bool, Dict[str, Any]]: A tuple containing:
                - observation (Any): The observation after taking the action.
                - reward (float): The reward received for the action.
                - terminated (bool): Whether the episode has ended naturally.
                - truncated (bool): Whether the episode was ended prematurely (e.g., time limit).
                - info (Dict[str, Any]): Auxiliary information from the step.
        """
        pass

    @abstractmethod
    def close(self) -> None:
        """
        Performs any necessary cleanup for the environment.
        """
        pass

    # Optional: Define other common environment methods if needed,
    # such as render(), seed(), etc. These can have default implementations
    # or also be abstract.
    # def render(self, mode='human'):
    #     pass
    #
    # def seed(self, seed=None):
    #     pass