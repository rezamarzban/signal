### Find the minimum (Vmin) and maximum (Vmax) values of a wave signal at any frequency + 100MHz crystal oscillator

**Board:** `Raspberry Pi Pico`

**Firmware:** `RPI-PICO-20240602-v1.23.0.uf2`

**IDE:** `Android Micro REPL App`

**Input PIN:** `ADC 26`

**Input resistor:** `1K Ohm`

**Oscillator:** `100MHz external crystal oscillator for testing`

**Notes:** 
* The frequency of the input signal doesn't affect the finder.
* The input resistance to the input pin affects the values of Vmin and Vmax at input pin point. the finder finds the values of Vmin and Vmax at the input pin point. to understand this, you need to be proficient in electronics and Ohm's law. For correct voltage measurement use voltage divider circuit using proper resistors **R<sub>1</sub>** and **R<sub>2</sub>**, Connect **V<sub>out</sub>** of voltage divider circuit to input pins directly.
* It is not a real-time finder, so do not change the testing circuit components during the finding process. It takes time to find the values of Vmin and Vmax. 
* Restart the app for each circuit testing or after any changes in the circuit components.
* Vmin and Vmax should be between 0V and 3.3V. For other voltages measurement use voltage divider circuit using proper resistors **R<sub>1</sub>** and **R<sub>2</sub>**, Connect **V<sub>out</sub>** of voltage divider circuit to input pins directly.
* Never connect the testing circuit directly to the input pins. Always use suitable resistance.
* If Vmin equals Vmax, the input signal is not a wave. Therefore, the simplest tool to determine if a testing oscillator circuit is correct or not?!
