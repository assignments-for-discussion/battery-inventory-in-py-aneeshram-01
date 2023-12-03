def calculate_soh(present_capacity, rated_capacity=120):
# Calculate State of Health (SoH) as a percentage
    soh = (present_capacity / rated_capacity) * 100
    return soh

def count_batteries_by_health(present_capacities):
    counts = {'healthy': 0, 'exchange': 0, 'failed': 0}

    for capacity in present_capacities:
        soh = calculate_soh(capacity)
        print(f"Present Capacity: {capacity} Ah")
        print(f"SoH: {soh:.2f}%")
        # Classify the battery and update counts
        if 80 < soh <= 100:
            print("Classified as healthy")
            counts['healthy'] += 1
        elif 62 <= soh <= 80:
            print("Classified for exchange")
            counts['exchange'] += 1
        else:
            print("Classified as failed")
            counts['failed'] += 1

    return counts


def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities = [113, 116, 80, 95, 92, 70]
    counts = count_batteries_by_health(present_capacities)
     # Print the final counts
    print("\nCounts:")
    print("Healthy batteries:", counts["healthy"])
    print("Exchange batteries:", counts["exchange"])
    print("Failed batteries:", counts["failed"])
    assert counts["healthy"] == 2
    assert counts["exchange"] == 3
    assert counts["failed"] == 1
    print("\nDone counting:)")


if __name__ == '__main__':
  test_bucketing_by_health()
