#!/usr/bin/env python3
"""
ODFT Framework: Main entry point for running experiments.
"""
import os
import sys
import logging
import argparse
import yaml
from pathlib import Path

# Set up basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_config(config_path):
    """Load configuration from YAML file."""
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        logger.info(f"Successfully loaded configuration from {config_path}")
        return config
    except Exception as e:
        logger.error(f"Error loading configuration from {config_path}: {e}")
        sys.exit(1)

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run an ODFT Framework experiment.")
    parser.add_argument(
        "--config", "-c", type=str, required=True,
        help="Path to the experiment configuration YAML file."
    )
    parser.add_argument(
        "--mode", "-m", type=str, choices=["train", "evaluate"], default=None,
        help="Override 'mode' setting in config. Options: train, evaluate."
    )
    parser.add_argument(
        "--checkpoint", type=str, default=None,
        help="Override checkpoint path for loading a model/agent state."
    )
    parser.add_argument(
        "--episodes", "-e", type=int, default=None,
        help="Override number of episodes to run."
    )
    parser.add_argument(
        "--device", "-d", type=str, default=None,
        help="Device to run on ('cpu', 'cuda', 'cuda:0', etc.)."
    )
    return parser.parse_args()

def main():
    """Main entry point."""
    args = parse_args()
    
    # Load configuration
    config = load_config(args.config)
    
    # Override config values with command-line arguments if provided
    if args.mode:
        config["run"]["mode"] = args.mode
        logger.info(f"Overriding run mode to: {args.mode}")
    
    if args.checkpoint:
        config["run"]["checkpoint_to_load"] = args.checkpoint
        logger.info(f"Overriding checkpoint path to: {args.checkpoint}")
    
    if args.episodes:
        if config["run"]["mode"] == "train":
            config["run"]["num_episodes_train"] = args.episodes
        else:
            config["run"]["num_episodes_eval"] = args.episodes
        logger.info(f"Overriding number of episodes to: {args.episodes}")
    
    if args.device:
        if "device" not in config:
            config["device"] = args.device
        logger.info(f"Setting device to: {args.device}")
    
    # Determine which example to run based on config path
    config_path = Path(args.config)
    example_name = config_path.stem
    
    # Import the correct module dynamically
    try:
        # Path should be like: config/examples/trading_agent/trading_agent.yaml
        # So we extract 'trading_agent' from the path
        example_module = config_path.parent.name
        logger.info(f"Running example: {example_module}")
        
        # Import the main_loop from the appropriate example
        exec(f"from odft_framework.examples.{example_module}.main_loop import main as example_main")
        
        # Run the example's main function with our config
        locals()["example_main"](config)
        
    except ImportError as e:
        logger.error(f"Could not import example module: {e}")
        logger.error(f"Make sure the config file is correctly placed in config/examples/<example_name>/{example_name}.yaml")
        sys.exit(1)
    except Exception as e:
        logger.exception(f"Error running experiment: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()