#### Hi everyone. I’m very excited to share that during my 1st semester break at TIFR, I tried to build a stellar spectrometer using my old telescope at my home. 
I made a custom eyepiece using a diffraction grating obtained from a laser pointer, and then used my smartphone to take a photo of "Sirius A" through the telescope. 
I then cropped and analyzed the photo using ImageJ software and did all the processing in Python.
I know there are many limitations in this process, such as:

1. The phone camera is not sensitive to red and infrared regions due to the in-built IR filter in it.


2. The resolution is very poor because the object viewed through the eyepiece appears very small. Cropping reduces the resolution further.


3. I know very little about spectrum processing😅. I just scaled the spectrum and calibrated it using two spectral dips that I found matching — the Hydrogen alpha and Hydrogen gamma lines. The 2nd image is from the Internet.

4. I also have not considered the absorption spectrum of the lens setup of the telescope.

5. Also due to shaking while taking the picture, the image got stretched a bit.


#### Some of the dips matched with the spectrum, while others did not. However, my spectrum looks quite similar to the actual one, so I’m pretty happy with the first attempt🤗. I’ll try to improve on these limitations in the future.

#### Here are all the data files👇
* [Direct view through the eyepiece](/SiriusTelescopeView.jpg)
* [Cropped spectrum that is used for the analysis](/Sirius%20A%20Spectrum%20image.jpg)
* [Pixel Intensity distribution using ImageJ software](/SiriusRawSpectraData.csv)
* [The Jupyter file that contains all the python codes for analysis](/SiriusA_SpectrumAnalysis.ipynb)
* [The raw spectrum before calibration](/RawSpectrumOfSiriusA.png)
* [The calibrated spectrum](/CalibratedSpectrumOfSiriusA.png)
* [The final Spectrum of Sirius A](/SiriusASpectrum_Obtained.png)
