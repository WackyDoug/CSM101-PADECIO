

#Assignment 1
PADECIO_patients = { "ana": (80, 50, 150, 90, 140, 200, 124),
             "ben": (130, 140, 135, 90, 140, 90, 150, 200),
             "carlo": (90, 100, 95, 90, 140, 140, 120, 130),
}

PADECIO_status = ""

for PADECIO_name, PADECIO_readings in PADECIO_patients.items():
    print(f"Patient Name : {PADECIO_name} ")
    print("Blood Sugary Summary")

    PADECIO_high_count = 0
    for PADECIO_i in PADECIO_readings:

        if PADECIO_i > 120:
            PADECIO_status = "High"
            PADECIO_high_count += 1
        else:
            PADECIO_status = "Normal"

        print(f"{PADECIO_i} - {PADECIO_status}")


    sumMax = max(PADECIO_readings)
    sumMin = min(PADECIO_readings)
    sumAvg = sum(PADECIO_readings) / len(PADECIO_readings)
    sumDiff = sumMax - sumMin

    print(f"Patient {PADECIO_name} Overall Summary")
    print(f"High Counter {PADECIO_high_count} ")
    print(f"Max  {sumMax}")
    print(f"Min  {sumMin}")
    print(f"Avg  {sumAvg:.2f}")
    print(f"Diff {sumDiff}\n")