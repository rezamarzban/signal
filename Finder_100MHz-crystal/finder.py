from machine import ADC, Pin
import utime
import random

# Initialize ADC (assuming you are using ADC0)
adc = ADC(Pin(26))  # ADC0 is on pin GP26

# Number of samples to read
num_samples = 1000

# Function to read the ADC value and convert it to voltage
def read_voltage(adc):
    # Read the raw ADC value (0-4095)
    raw = adc.read_u16()
    # Convert the raw ADC value to voltage
    voltage = (raw / 65535) * 3.3
    return voltage

# Main function to find Vmin and Vmax
def find_vmin_vmax(adc, num_samples):
    vmin = 3.3  # Initialize to maximum possible voltage
    vmax = 0.0  # Initialize to minimum possible voltage
    
    for _ in range(num_samples):
        voltage = read_voltage(adc)
        if voltage < vmin:
            vmin = voltage
        if voltage > vmax:
            vmax = voltage
        # Print Vmin and Vmax during each iteration
        print("Vmin: {:.2f} V, Vmax: {:.2f} V".format(vmin, vmax))
        # Introduce a random delay between 0.5 to 1.5 seconds
        delay = random.uniform(0.5, 1.5)
        utime.sleep(delay)
    
    return vmin, vmax

# Read and print final Vmin and Vmax
vmin, vmax = find_vmin_vmax(adc, num_samples)
print("Final Vmin: {:.2f} V".format(vmin))
print("Final Vmax: {:.2f} V".format(vmax))
