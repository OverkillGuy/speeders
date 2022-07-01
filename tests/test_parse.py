"""Tests for parsing an input file"""


from plates.parser import parse
from tests.samples import (
    SAMPLE1_EVENT1_DETECTORID,
    SAMPLE1_EVENT1_PLATE,
    SAMPLE1_EVENT1_TIME,
    SAMPLE1_INPUT,
    SAMPLE1_SPEEDLIMIT,
    SAMPLE1_TOOFAST1_PLATE,
)


def test_parse_simple():
    """Parse the sample plates input"""
    parsed = parse(SAMPLE1_INPUT)
    assert parsed.reference_speed == SAMPLE1_SPEEDLIMIT, "Wrong parsed speed limit"
    first_event = parsed.events[0]
    assert (
        first_event.plate == SAMPLE1_EVENT1_PLATE
    ), "Wrong plates detected in first event"
    assert (
        first_event.detector_id == SAMPLE1_EVENT1_DETECTORID
    ), "Wrong detector ID reported in first event"
    assert (
        first_event.timestamp == SAMPLE1_EVENT1_TIME
    ), "Wrong timestamp parsed in first event"
    all_plates = [event.plate for event in parsed.events]
    assert SAMPLE1_TOOFAST1_PLATE in all_plates, "Missing plate from parsed"
