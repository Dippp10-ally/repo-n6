"""Validation helpers for configuration dictionaries."""


def require_config_value(config, key):
    """Return the configured value or raise when it is missing."""
    if not isinstance(config, dict):
        raise TypeError("config must be a dictionary")
    if key not in config or config[key] is None:
        raise ValueError(f"{key} is required")
    value = config[key]
    if isinstance(value, str) and not value.strip():
        raise ValueError(f"{key} must not be empty")
    return value
