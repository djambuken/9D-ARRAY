import math
import random
import statistics

ORANGE = "\033[38;5;208m"
RED = "\033[31m"
RESET = "\033[0m"

print(
    f"{ORANGE}#ENTER EXACTLY 9 NUMBERS "
    f"{RED}SPACED BY COMMA OR ENTER RANDOM // 1,2,3,4,5,6,7,8,9{RESET}"
)

entry = input("> ").strip()

if entry.lower() == "random":
    numbers = [random.randint(1, 100) for _ in range(9)]
else:
    parts = [part.strip() for part in entry.split(",")]
    if len(parts) != 9 or any(not part for part in parts):
        print("Invalid input: enter exactly 9 comma-separated numbers, or type RANDOM.")
        raise SystemExit(1)

    try:
        numbers = [float(part) for part in parts]
    except ValueError:
        print("Invalid input: every entry must be a number, or type RANDOM.")
        raise SystemExit(1)

    if not all(math.isfinite(number) for number in numbers):
        print("Invalid input: numbers must be finite values.")
        raise SystemExit(1)

ascending = sorted(numbers)
descending = ascending[::-1]


def format_array(values):
    return ", ".join(f"{value:g}" for value in values)


print("\n1. Entered order:   ", format_array(numbers))
print("2. Ascending order: ", format_array(ascending))
print("3. Descending order:", format_array(descending))
print(f"Median: {statistics.median(numbers):g}")
print(f"Range:  {max(numbers) - min(numbers):g}")
