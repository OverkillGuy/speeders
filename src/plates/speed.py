"""Calculates the speed of matched detection events"""

from datetime import date, datetime, timedelta

from plates.match import DetectionMatches, Plate

# TODO Consider a type alias that allows annotating units, like TypeVar
Speed = float
SpeedPerPlate = dict[Plate, Speed]


# NOTE: The original problem statement DOES NOT INCLUDE DETECTOR DISTANCE
# Had to guess from given solution it is 200m.
# Proper implementation should have that in the parsed model, not hardcoded here!
DETECTOR_DISTANCE = 0.2


def _calculate_speed(distance: float, time: timedelta) -> Speed:
    """Calculate a speed in km/h given distance (km) and a time"""
    km_per_seconds = distance / time.total_seconds()
    km_per_hour = km_per_seconds * timedelta(hours=1).total_seconds()
    return km_per_hour


def speed_of_detections(matched_detections: DetectionMatches) -> SpeedPerPlate:
    """Compute the speed per plate using timing of matched detections"""
    speeds = {}
    for plate, events in matched_detections.items():
        first_hit_time, second_hit_time = events[0].timestamp, events[1].timestamp
        # Sadly, TIME objects can't be substracted as-is, convert to timedelta first:
        first_hit_datetime, second_hit_datetime = datetime.combine(
            date.today(), first_hit_time
        ), datetime.combine(date.today(), second_hit_time)
        detection_timedelta: timedelta = second_hit_datetime - first_hit_datetime
        speeds[plate] = _calculate_speed(DETECTOR_DISTANCE, detection_timedelta)
    return speeds


def too_fast(max_speed: int, plate_speeds: SpeedPerPlate):
    """Filter speeds that are over the limit, for infringement reporting

    Note the usual danger of comparing floating point values, but we're not checking
    EQUALITY, nor do we care about infractions at/around fraction of speed limit, so
    we're a bit safer.
    """
    return {plate: speed for plate, speed in plate_speeds.items() if speed > max_speed}
