# 9D ARRAY @djambuken

9D ARRAY is a colorful, interactive command-line array solver. Enter exactly nine comma-separated numbers, or generate nine random values within a range you choose. Random bounds may be any finite numbers supported by Python, including negative and decimal values. The solver displays the entered order, ascending order, and descending order, then calculates the median and range. Type `RESET` to start again or `QUIT` to exit.

## Run from a terminal

Python 3 is required. The program uses only Python's standard library, so no packages need to be installed.

Clone the repository and start the solver:

```sh
git clone https://github.com/djambuken/9D-ARRAY.git
cd 9D-ARRAY
python3 9Darray.py
```

If the repository is already cloned, run it from the repository directory:

```sh
python3 9Darray.py
```

## Example input

```text
1,2,3,4,5,6,7,8,9
```

For a random array in a range you choose, enter the command and its minimum and maximum, separated by commas:

```text
RANDOM,-1000,1000
```

You can also enter `RANDOM` by itself; the program will then ask for the minimum and maximum. For example, `RANDOM,-2.5,8.75` generates values in a custom decimal range. Bounds must be finite numbers, and the minimum must not exceed the maximum.
