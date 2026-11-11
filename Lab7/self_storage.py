import math


def parse_rental(text):
    if not isinstance(text, str):
        return None
    parts = text.split(':')
    if len(parts) != 2:
        return None
    unit, months = parts
    unit = unit.strip()
    if not unit:
        return None
    try:
        months = float(months)
    except ValueError:
        return None
    if not math.isfinite(months) or months <= 0:
        return None
    return unit.title(), months


def duration_average(months_csv):
    if not isinstance(months_csv, str):
        return None
    try:
        values = [int(r) for r in months_csv.split(',')]
    except ValueError:
        return None
    if any(v <= 0 for v in values):
        return None
    return sum(values) // len(values)


def payable_rent(text):
    if not isinstance(text, str):
        return None
    parts = text.split('|')
    if len(parts) != 2:
        return None
    try:
        rent = float(parts[0])
        discount = float(parts[1])
    except ValueError:
        return None
    if not (math.isfinite(rent) and math.isfinite(discount)):
        return None
    if rent < 0 or discount < 0:
        return None
    total = rent * 1.18 - discount
    if not math.isfinite(total):
        return None
    return max(total, 0)


def main():
    print("==== Running parse_rental ====")
    user_input = input("Enter unit:months (e.g. medium:6): ")
    result = parse_rental(user_input)
    print("Unit and Months:", result)

    print("\n==== Running duration_average ====")
    user_input = input("Enter rental months as CSV (e.g. 3,6,12): ")
    result = duration_average(user_input)
    print("Average Duration:", result)

    print("\n==== Running payable_rent ====")
    user_input = input("Enter rent|discount (e.g. 2400|200): ")
    result = payable_rent(user_input)
    print("Payable Rent:", result)

if __name__ == "__main__":
    main()