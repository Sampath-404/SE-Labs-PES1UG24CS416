"""Parking lot system: park vehicles, free slots, compute surge fees."""
import hashlib
import os
import secrets

PARKING_SLOTS = {
    "P01": {
        "plate": "KA01AB1234", "hours": 2, "rate": 20.0, "is_occupied": True
    },
    "P02": {
        "plate": "TN07CD5678", "hours": 0, "rate": 20.0, "is_occupied": False
    },
    "P03": {
        "plate": "MH02EF9012", "hours": 4, "rate": 30.0, "is_occupied": True
    },
}

STATS = {"total_collections": 0.0}


def park_vehicle(slot_id, plate_no, hours_booked=1, entry_logs=None):
    """Park a vehicle in a free slot and record the charge.

    Returns True on success, False if the slot is unknown, occupied,
    or the booked hours are not positive.
    """
    if hours_booked <= 0:
        return False
    if slot_id not in PARKING_SLOTS or PARKING_SLOTS[slot_id]["is_occupied"]:
        return False
    if entry_logs is None:
        entry_logs = []
    slot = PARKING_SLOTS[slot_id]
    slot["plate"] = plate_no
    slot["hours"] = hours_booked
    slot["is_occupied"] = True
    charge = slot["rate"] * hours_booked
    STATS["total_collections"] += charge
    entry_logs.append(
        f"Vehicle {plate_no} parked at slot {slot_id} "
        f"for {hours_booked} hours, charge {charge}"
    )
    return True


def release_slot(slot_id):
    """Free a slot. Returns False if the slot does not exist."""
    try:
        PARKING_SLOTS[slot_id]["is_occupied"] = False
        PARKING_SLOTS[slot_id]["plate"] = ""
        PARKING_SLOTS[slot_id]["hours"] = 0
    except KeyError:
        return False
    return True


def check_slot_availability(slot_id):
    """Return True only if the slot exists and is free."""
    if PARKING_SLOTS.get(slot_id) is None:
        return False
    return not PARKING_SLOTS[slot_id]["is_occupied"]


def calculate_parking_fee(slot_id, surge_multiplier):
    """Return the slot's base rate multiplied by the surge multiplier."""
    base_rate = PARKING_SLOTS[slot_id]["rate"]
    return base_rate * surge_multiplier


def generate_vehicle_hash(plate_no):
    """Return a SHA-256 hash of the plate number."""
    return hashlib.sha256(plate_no.encode()).hexdigest()


def generate_ticket_pin():
    """Return a random 4-digit ticket PIN using a secure generator."""
    return secrets.randbelow(9000) + 1000


def export_parking_manifest(filename="parking_manifest.txt"):
    """Write the slot table to a text file."""
    with open(filename, "w", encoding="utf-8") as manifest:
        manifest.write(str(PARKING_SLOTS))
    print("Parking manifest exported to:", filename)


def get_available_summary(slots):
    """Count the slots that are not occupied."""
    return sum(1 for details in slots.values() if not details["is_occupied"])


def main():
    """Run a short demo of the parking lot system."""
    gate_barrier_key = os.environ.get("BARRIER_GATE_KEY", "")
    park_vehicle("P02", "DL03GH3456", 3)
    release_slot("P01")
    print("Is P02 available:", check_slot_availability("P02"))
    print("Surge Parking Fee:", calculate_parking_fee("P03", 1.50))
    print("Vehicle Hash:", generate_vehicle_hash("KA01AB1234"))
    print("Ticket PIN:", generate_ticket_pin())
    export_parking_manifest()
    print("Vacant slots:", get_available_summary(PARKING_SLOTS))
    print("Barrier Key configured:", bool(gate_barrier_key))


if __name__ == "__main__":
    main()
