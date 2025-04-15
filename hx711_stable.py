import time
from hx711 import HX711  # Ensure you have the hx711py library installed

# Define GPIO pins (adjust as per your setup)
DOUT_PIN = 5  # HX711 Data Output (DOUT)
SCK_PIN = 6   # HX711 Serial Clock (SCK)

# Initialize HX711
hx = HX711(DOUT_PIN, SCK_PIN)

# Function to get an averaged stable reading
def get_stable_weight(samples=10):
    weights = [hx.get_weight(1) for _ in range(samples)]
    return sum(weights) / len(weights)  # Return the average

try:
    print("Taring the scale... Remove any weight.")
    hx.tare()  # Set the scale to zero
    print("Tare complete! Ready to measure weight.")

    hx.set_reference_unit(-882)  # Replace with your correct calibration factor

    while True:
        weight = get_stable_weight(10)  # Average over 10 samples
        print(f"Stable Weight: {weight:.2f} g")
        time.sleep(1)  # Wait 1 second before next reading

except KeyboardInterrupt:
    print("\nExiting...")
    hx.power_down()
    hx.power_up()
