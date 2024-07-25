from machine import Pin, Timer, ADC
import time

# Initialize PWM (GP18 is PWM0)
pwm = machine.PWM(machine.Pin(18))

# PWM configuration for generating a 250Hz square wave
pwm.freq(250)
pwm.duty_u16(32768)  # 50% duty cycle

# Use an ADC if the signal is analog, or Pin for digital signals
# Here, we use ADC on pin 26 as an example for an analog signal
adc = ADC(Pin(26))

# For digital signals, you could use:
# signal_pin = Pin(15, Pin.IN)

# Buffer to store signal values
buffer_size = 100
signal_buffer = [0] * buffer_size
buffer_index = 0

# Timer callback to read the signal and store in buffer
def sample_signal(timer):
    global buffer_index
    # Read the analog value (0-65535 for ADC)
    signal_value = adc.read_u16()
    
    # For digital signals, use:
    # signal_value = signal_pin.value()

    # Store the signal value in the buffer
    signal_buffer[buffer_index] = signal_value
    buffer_index = (buffer_index + 1) % buffer_size

# Initialize timer to sample signal at a specific frequency (e.g., 2500 Hz)
sampling_frequency = 2500
timer = Timer()
timer.init(freq=sampling_frequency, mode=Timer.PERIODIC, callback=sample_signal)

try:
    while True:
        # Print the signal buffer contents to Thonny plotter
        for value in signal_buffer:
            print(value)
        time.sleep(0.5)  # Adjust the sleep duration as needed
except KeyboardInterrupt:
    pass  # Handle keyboard interrupt
