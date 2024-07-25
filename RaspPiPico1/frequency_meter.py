from machine import Pin, Timer
import time

# Initialize PWM (GP18 is PWM0)
pwm = machine.PWM(machine.Pin(18))

# PWM configuration for generating a 28KHz square wave
pwm.freq(28000)
pwm.duty_u16(32768)  # 50% duty cycle

# Define the GPIO pin and other variables
pin = Pin(15, Pin.IN)  # Replace 15 with your desired GPIO pin
edge_count = 0

# Define the edge detection interrupt handler
def edge_handler(pin):
    global edge_count
    edge_count += 1

# Attach the edge detection interrupt handler to the pin
pin.irq(trigger=Pin.IRQ_RISING, handler=edge_handler)

# Function to measure frequency
def measure_frequency(duration_ms):
    global edge_count
    
    # Reset edge count
    edge_count = 0
    
    # Wait for the specified duration
    time.sleep(duration_ms / 1000)
    
    # Calculate frequency
    frequency = edge_count / (duration_ms / 1000)
    return frequency

# Set the measurement duration (e.g., 1000 ms = 1 second)
measurement_duration = 1000  # in milliseconds

# Measure and print the frequency
while True:
    frequency = measure_frequency(measurement_duration)
    print("Frequency: {:.2f} Hz".format(frequency))
    time.sleep(1)  # Wait for 1 second before next measurement
  
