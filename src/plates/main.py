"""Command line interface to plate detections"""


from plates.match import match_events
from plates.model import PlateDetections
from plates.speed import SpeedPerPlate, speed_of_detections, too_fast


def compute_too_fast(input_text: str) -> SpeedPerPlate:
    """Detect speeders from text input"""
    detections = PlateDetections.parse(input_text)
    matched = match_events(detections)
    speeds = speed_of_detections(matched)
    too_fast_speeds = too_fast(detections.reference_speed, speeds)
    return too_fast_speeds
