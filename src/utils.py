import yaml
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Run ML Pipeline for Admission Prediction"
    )
    parser.add_argument(
        "--config",
        type=str,
        default="config.yaml",
        help="Path to YAML configuration file",
    )
    return parser.parse_args()

def load_config(config_path):

    if not os.path.exists(config_path):
        full_path = os.path.abspath(config_path)
        raise FileNotFoundError(
            f"Configuration file not found at: {full_path}"
        )
    else:
        with open(config_path, "r", encoding="utf-8") as f:
            cfg_dict = yaml.safe_load(f)
            return cfg_dict


def format_time_period(seconds):
    """Converts a duration in seconds into a human-readable string with an appropriate unit."""
    # Hours
    if seconds >= 3600:
        return f"{seconds / 3600:.2f} hrs"

    # Minutes
    if seconds >= 60:
        return f"{seconds / 60:.2f} mins"

    # Seconds
    if seconds >= 1:
        return f"{seconds:.2f} s"

    # Milliseconds 
    return f"{seconds * 1000:.2f} ms"