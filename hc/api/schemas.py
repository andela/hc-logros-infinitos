check = {
    "properties": {
        "name": {"type": "string"},
        "tags": {"type": "string"},
        "priority": {"type": "string"},
        "timeout": {"type": "number", "minimum": 60, "maximum": 7776000},
        "grace": {"type": "number", "minimum": 60, "maximum": 7776000},
        "nag_interval": {"type": "number", "minimum": 60, "maximum": 604800},
        "channels": {"type": "string"}
    }
}
