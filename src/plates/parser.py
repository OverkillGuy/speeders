"""Parse the input file into structure"""

from dataclasses import dataclass
from datetime import time


@dataclass
class PlateDetectionEvent:
    """A single detector's event in time, without context"""

    detector_id: int
    # TODO Consider a more specific type for validating plates aren't Emoji or empty
    plate: str
    # Per input file samples, note the lack of day details (can't use datetime).
    timestamp: time


@dataclass
class PlateDetections:
    """The parsed, uninterpreted version of the plates input file"""

    reference_speed: int
    plates: list[PlateDetectionEvent]
    # Note the missing info of detector ID vs distances, preventing proper
    # distance-over-time computation.


def parse(input_text: str) -> PlateDetections:
    """Parse an input problem text into (un-interpreted) structured objects"""
    return PlateDetections(reference_speed=120, plates=[])
