"""Prove we can match events by plate, to find speed"""

from speeders.match import _platematch_events, match_events
from tests.samples import SAMPLE1_EVENT1_PLATE, SAMPLE1_OBJ, SAMPLE1_SINGLEHIT1_PLATE


def test_platematch_events_simple():
    """Match the sample input 1's events using one of the match subfunctions"""
    matched = _platematch_events(SAMPLE1_OBJ)
    assert (
        len(matched[SAMPLE1_EVENT1_PLATE]) == 2
    ), "Should have hit the detectors twice"
    assert len(matched[SAMPLE1_SINGLEHIT1_PLATE]) == 1, "Should have hit detector once"


# TODO More specific tests for the specific subfunctions of match.py


def test_match_events_simple():
    """Compute proper matching for events"""
    matched = match_events(SAMPLE1_OBJ)
    assert (
        len(matched[SAMPLE1_EVENT1_PLATE]) == 2
    ), "Should have hit the detectors twice"
    assert SAMPLE1_SINGLEHIT1_PLATE not in matched, "Shouldn't contain singlehits"
    assert (
        len(matched.keys()) == 1
    ), "Should have found only one proper detection couple"
