### Find the minimum (Vmin) and maximum (Vmax) values of a wave signal in real-time at any frequency

Because the code in this project has sensitive applications, Especially developing HF, VHF and UHF transistor transmitters, So:

${{\color{red}*\ The\ code\ in\ this\ project\ is\ password\ protected}\ }\$

**Board:** `Raspberry Pi Pico`

**Firmware:** `RPI-PICO-20240602-v1.23.0.uf2`

**IDE:** `Android Micro REPL App`

**Input PIN:** `ADC 26`

**Input resistor:** `1K to 1M Ohm`

**Oscillator:** ` `

With this code, the Raspberry Pi Pico becomes an electronics measurement tool that, in special cases, offers more features than a multimeter and an oscilloscope, allowing you to find the Vmin and Vmax of a wave signal at any frequency.

**Notes:** 
* The frequency of the input signal doesn't affect the finder.
* The input resistance to the input pin affects the values of Vmin and Vmax at input pin point. the finder finds the values of Vmin and Vmax at the input pin point. to understand this, you need to be proficient in electronics and Ohm's law. For correct voltage measurement use voltage divider circuit using proper resistors **R<sub>1</sub>** and **R<sub>2</sub>**, Connect **V<sub>out</sub>** of voltage divider circuit to input pins directly.
* It is a real-time finder, allowing you to change the testing circuit components during the process to see the effect on the signal and reverse engineer. 
* Vmin and Vmax should be between 0V and 3.3V. For other voltages measurement use voltage divider circuit using proper resistors **R<sub>1</sub>** and **R<sub>2</sub>**, Connect **V<sub>out</sub>** of voltage divider circuit to input pins directly.
* Never connect the testing circuit directly to the input pins. Always use suitable resistance to limit the current to 1 mA; however, it can be up to 16 mA.
* If Vmin equals Vmax, the input signal is not a wave. Therefore, the simplest tool to determine if a testing oscillator circuit is correct or not?!
