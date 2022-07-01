"""Reference inputs used multiple times for testing purposes"""

from datetime import time

from plates.model import PlateDetectionEvent, PlateDetections

SAMPLE1_SPEEDLIMIT = 50
SAMPLE1_EVENT1_PLATE = "OZ-15-ZU"
SAMPLE1_EVENT1_DETECTORID = 1
SAMPLE1_EVENT1_TIME = time(hour=9, minute=0, second=0)
SAMPLE1_TOOFAST1_PLATE = "NV-71-PU"
SAMPLE1_TOOFAST1_SPEED = 56
SAMPLE1_SINGLEHIT1_PLATE = "WS-LP-74"  # Hit only one detector in sample
SAMPLE1_INPUT = """50
1 09:00:00 OZ-15-ZU
2 09:00:04 WS-LP-74
1 09:00:07 97-YC-51
1 09:00:10 NV-71-PU
2 09:00:21 OZ-15-ZU
2 09:04:58 CN-70-OT"""
SAMPLE1_OBJ = PlateDetections(
    reference_speed=50,
    events=[
        PlateDetectionEvent(detector_id=1, plate="OZ-15-ZU", timestamp=time(9, 0)),
        PlateDetectionEvent(detector_id=2, plate="WS-LP-74", timestamp=time(9, 0, 4)),
        PlateDetectionEvent(detector_id=1, plate="97-YC-51", timestamp=time(9, 0, 7)),
        PlateDetectionEvent(detector_id=1, plate="NV-71-PU", timestamp=time(9, 0, 10)),
        PlateDetectionEvent(detector_id=2, plate="OZ-15-ZU", timestamp=time(9, 0, 21)),
        PlateDetectionEvent(detector_id=2, plate="CN-70-OT", timestamp=time(9, 4, 58)),
    ],
)

SAMPLE_SPEEDLIMIT2 = 50
SAMPLE_PLATE2 = "QW-23-56"
SAMPLE_INPUT2 = """50
    1 12:00:33 QW-23-56
    1 12:01:39 GF-PY-26
    2 12:00:43 QW-23-56
    1 12:00:46 02-RV-WE
    2 12:00:59 02-RV-WE
    2 12:01:56 GF-PY-26
    1 12:01:15 CF-QW-46
    2 12:02:13 WM-20-PF
    2 12:01:27 CF-QW-46
    1 12:01:28 03-LC-TF
    2 12:01:39 03-LC-TF
    1 12:01:56 WM-20-PF
"""
