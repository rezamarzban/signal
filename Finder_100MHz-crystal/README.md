### Find the minimum (Vmin) and maximum (Vmax) values of a wave signal at any frequency + 100MHz crystal oscillator

**Board:** `Raspberry Pi Pico`

**Firmware:** `RPI-PICO-20240602-v1.23.0.uf2`

**IDE:** `Android Micro REPL App`

**Input PIN:** `ADC 26`

**Input resistor:** `1K Ohm`

**Oscillator:** `100MHz external crystal oscillator for testing`

**Notes:** 
* The frequency of the input signal doesn't affect the finder.
* It is not a real-time finder, so do not change the testing circuit components during the finding process. It takes time to find the values of Vmin and Vmax.
* Restart the app for each circuit testing or after any changes in the circuit components.
* Vmin and Vmax should be between 0V and 3.3V.
* If Vmin equals Vmax, the input signal is not a wave. Therefore, the simplest tool to determine if a testing circuit is an oscillator or not?!
