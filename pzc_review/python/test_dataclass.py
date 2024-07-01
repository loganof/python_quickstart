from dataclasses import dataclass
from typing import Optional, Text, Dict


@dataclass
class TrackerActiveLoop:

    name: Optional[Text]
    is_interrupted: bool
    rejected: bool
    trigger_message: Optional[Dict]

loop = TrackerActiveLoop(
    name="greet",
    is_interrupted=False,
    rejected=False,
    trigger_message={
        "sender": "user",
        "message": "Hello",
        "timestamp": 163222558,
    }
)

print(loop)
