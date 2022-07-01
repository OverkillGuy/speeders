"""Parse the input file into structure"""

from dataclasses import dataclass
from datetime import time

# Declaring a type alias for strings that happen to be plates
# TODO Consider a more specific type for validating plates aren't Emoji, empty...
Plate = str


@dataclass
class PlateDetectionEvent:
    """A single detector's event in time, without context"""

    detector_id: int
    plate: Plate
    # Per input file samples, note the lack of day details (can't use datetime).
    timestamp: time


@dataclass
class PlateDetections:
    """The parsed, uninterpreted version of the plates input file"""

    reference_speed: int
    events: list[PlateDetectionEvent]
    # Note the missing info of detector ID and distances, preventing proper
    # distance-over-time computation.

    @staticmethod
    def parse(input_text: str):
        """Parse an input problem text into (un-interpreted) structured objects"""
        # TODO Consider what happens in case first line DOESN'T parse as number
        first_line, *rest_lines = input_text.split("\n")
        reference_speed = int(first_line)
        events: list[PlateDetectionEvent] = []
        for line in rest_lines:
            detector, time_string, plate = line.split(" ")
            time_obj = time.fromisoformat(time_string)
            event = PlateDetectionEvent(
                detector_id=int(detector), plate=plate, timestamp=time_obj
            )
            events.append(event)
        return PlateDetections(reference_speed=reference_speed, events=events)
