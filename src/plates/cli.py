"""Command line entrypoint for speeder calculation"""
import argparse
import sys

from plates.main import compute_too_fast


def parse_arguments(arguments: list[str]) -> argparse.Namespace:
    """Parse generic arguments, given as parameters"""
    parser = argparse.ArgumentParser(
        "speeders", description="Detect speeders from plate detection logs"
    )
    parser.add_argument(
        "-f",
        "--input-file",
        type=argparse.FileType("r"),
        required=True,
        help="Input file for that day's detection logs",
    )
    return parser.parse_args(arguments)


def main():
    """Calculate who is speeding, based on detector information"""
    args = parse_arguments(sys.argv[1:])
    detections_log = args.input_file.read()
    speeders = compute_too_fast(detections_log)
    print(f"The following {len(speeders)} cars went over the speed limit:")
    for plate, speed in speeders.items():
        print(f"{plate} - {speed:.0f} km/h")
