"""Solve speeders"""

from collections import defaultdict

from speeders.model import Plate, PlateDetectionEvent, PlateDetections

# Type alias
DetectionMatches = dict[Plate, list[PlateDetectionEvent]]


def _platematch_events(detections: PlateDetections) -> DetectionMatches:
    """Group plate detection events by plate, unsorted by detector"""
    matched_events = defaultdict(list)
    for event in detections.events:
        matched_events[event.plate].append(event)
    return matched_events


def _sort_matched_events(matched_detections: DetectionMatches) -> DetectionMatches:
    """Sort the matched detection events by time of arrival

    Having time-sorted matching enables speed detection for "reverse" order = detector 2
    hit first, avoiding negative speed issues.
    """
    return {
        plate: sorted(events, key=lambda x: x.timestamp)
        for plate, events in matched_detections.items()
    }


def _remove_singlehits(sorted_detections: DetectionMatches) -> DetectionMatches:
    """Filter out the events that have only one hit, disabling speed calculation

    In order to catch issues in underlying data/assumptions, "wrong" events throw
    ValueError.

    This forces app developer to deal with the following cases without having to do
    ambiguous calculation:

    - > 2 hits = same car came back on the same day
    - Incorrect detector IDs, as code seems to assume ID 1 and 2 ONLY

    """
    nosinglehit_detections = {}

    for plate, events in sorted_detections.items():
        if len(events) > 2:
            # TODO: Consider a more specific Exception type that includes plate +
            # detections in object body, to let developer figure out what to do
            raise ValueError(f"Too many detection events for {plate}: {len(events)}")
        detector_ids = [event.detector_id for event in events]
        if any([d not in [1, 2] for d in detector_ids]):
            raise ValueError(
                f"Detections for {plate} uses detector ID not in (1,2): {detector_ids}"
            )
        if len(events) == 2:
            nosinglehit_detections[plate] = events
    return nosinglehit_detections


def match_events(detections: PlateDetections) -> DetectionMatches:
    """Match plate detection events

    Sorting by time, removing cases that can't detect speed, see internal functions
    docstring

    """
    matched_detections = _platematch_events(detections)
    sorted_detections = _sort_matched_events(matched_detections)
    nosinglehit_detections = _remove_singlehits(sorted_detections)
    return nosinglehit_detections
