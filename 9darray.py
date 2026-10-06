import math
import random
import statistics

ORANGE = "\033[38;5;208m"
RED = "\033[31m"
LIGHT_GREEN = "\033[92m"
PINK = "\033[38;5;213m"
PURPLE = "\033[38;5;141m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

print(
    f"{ORANGE}#ENTER EXACTLY 9 NUMBERS "
    f"{RED}SPACED BY COMMA OR ENTER RANDOM // "
    f"{LIGHT_GREEN}1{RESET},{PINK}2{RESET},{PURPLE}3{RESET},{CYAN}4{RESET},"
    f"{YELLOW}5{RESET},{ORANGE}6{RESET},{RED}7{RESET},{LIGHT_GREEN}8{RESET},{PINK}9{RESET}"
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


print(f"\n{LIGHT_GREEN}1{RESET}. Entered order:   ", format_array(numbers))
print(f"{PINK}2{RESET}. Ascending order: ", format_array(ascending))
print(f"{PURPLE}3{RESET}. Descending order:", format_array(descending))
print(f"Median: {statistics.median(numbers):g}")
print(f"Range:  {max(numbers) - min(numbers):g}")