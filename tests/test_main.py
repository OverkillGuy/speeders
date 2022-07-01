"""Find the speeders, given input"""

from plates.cli import compute_too_fast
from tests.samples import SAMPLE1_INPUT, SAMPLE2_INPUT


def test_find_no_speeders():
    """Compute (no) speeders from first input"""
    too_fasters = compute_too_fast(SAMPLE1_INPUT)
    assert too_fasters == {}, "Should find no speeders in first sample"


def test_find_speeders():
    """Compute the 4 speeders from second input"""
    too_fasters = compute_too_fast(SAMPLE2_INPUT)
    assert len(too_fasters) == 4, "Should find 4 speeders in second sample"
