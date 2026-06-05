import random
target_units = int(input("Enter target units: "))
workers_per_shift = int(input("Enter workers per shift: "))
defect_rate = float(input("Enter defect rate percentage: "))
total_produced = 0
total_defects = 0
print("\n===== PRODUCTION REPORT =====\n")
for shift in range(1, 4):
    shift_produced = 0
    shift_defects = 0
    print(f"\nShift {shift} Started")
    for cycle in range(1, 21):
        if total_produced >= target_units:
            print("\nTarget achieved. Production stopped.")
            break
        chance = random.uniform(0, 100)
        if chance < defect_rate:
            shift_defects += 1
            total_defects += 1
            print(f"Cycle {cycle}: Defective Item → Skipped")
            continue
        shift_produced += 1
        total_produced += 1
        print(f"Cycle {cycle}: Item Produced")
    productivity = shift_produced / workers_per_shift
    print(f"\n--- Shift {shift} Summary ---")
    print("Items Produced :", shift_produced)
    print("Defective Items:", shift_defects)
    print("Worker Productivity:", round(productivity, 2), "items per worker")

print("\n==============================")
print("FINAL PRODUCTION SUMMARY")
print("==============================")
print("Target Units       :", target_units)
print("Total Produced     :", total_produced)
print("Total Defects      :", total_defects)
print("Remaining Units    :", target_units - total_produced)
