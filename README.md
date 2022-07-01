# Plates experiment

Solving a fun StackOverflow problem in Python



## Dependencies

- [Python](https://www.python.org/) 3.9 or later (use of typing hints)
- [Poetry](https://python-poetry.org) package manager, to install development
  dependencies and generate virtual environment.

## Usage

### Run the code

Install the module first:

    make install
    # or
	poetry install

Then inside the virtual environment, launch the script:

    # Run single command inside virtualenv
    poetry run speeders -f input_2.txt

    # or
    # Load the virtualenv first
    poetry shell
    # Then launch the script, staying in virtualenv
    speeders -f input_2.txt

Sample output:

    The following 4 cars went over the speed limit:
    QW-23-56 - 72 km/h
    02-RV-WE - 55 km/h
    CF-QW-46 - 60 km/h
    03-LC-TF - 65 km/h


### Reuse the python module

Use this package as you would any python module:

	# Get a virtualenv going first, such as via poetry
	poetry shell
	python3
	>>> from plates import match

## Original problem statement


See [the original problem on Stack Overflow](https://codereview.stackexchange.com/questions/277750/print-a-list-of-license-plate-numbers-of-all-cars-that-went-over-the-speed-limit).
> I have to print a list of license plate numbers of all cars that went over the speed limit, as well as the average speed of each of those cars.

> The first line contains the maximum speed (in km/h) for the road that the detectors are placed on. All other lines start with the number of the detector that was passed (1 or 2), followed by the time on which the car passed the detector, and then followed by the license plate number of that car.

Example input:

    50
    1 09:00:00 OZ-15-ZU
    2 09:00:04 WS-LP-74
    1 09:00:07 97-YC-51
    1 09:00:10 NV-71-PU
    2 09:00:21 OZ-15-ZU
    [...]
    2 09:04:58 CN-70-OT

Example output:

    The following cars went over the speed limit:
    GH-23-NN - 68 km/h
    NV-71-PU - 56 km/h
    CN-70-OT - 70 km/h
    18-IP-VU - 59 km/h

Input:

    50
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

Output:

    The following cars went over the speed limit:
    QW-23-56 - 72 km/h
    02-RV-WE - 55 km/h
    CF-QW-46 - 60 km/h
    03-LC-TF - 65 km/h

Note from implementor: the distance between detector plates is NOT stipulated,
which is required to capture speed as distance over time. Sample implementation
shows this to be `200`.

## Development

### Python setup

This repository uses Python 3.9 or above, using
[Poetry](https://python-poetry.org) as package manager to define a Python
package inside `src/plates/`.

`poetry` will create virtual environments if needed, fetch
dependencies, and install them for development.

This codebase uses [pre-commit](https://pre-commit.com) to run linting tools
like `flake8`, formatters like `black`, and type checking via `mypy`.

Use `pre-commit install` to install git pre-commit hooks to force running these
checks before any code can be committed, use `make lint` to run these manually.

Testing is provided by `pytest` separately in `make test`.

Installation of `poetry` and `pre-commit` is recommended via
[pipx](https://pypa.github.io/pipx/).


For ease of development, a `Makefile` is provided, use it like this:

	make  # equivalent to "make all" = install lint docs test build
	# run only specific tasks:
	make install
	make lint
	make test
	# Combine tasks:
	make install test

## License

This project is released under GPLv3. See `COPYING` file for GPLv3 license
details.
