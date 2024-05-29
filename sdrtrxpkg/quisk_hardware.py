# This is the hardware file to support the SDR-TRX radio designed by Rob Frohne, KL7NA.

import traceback, time, math
import _quisk as QS

from quisk_hardware_model import Hardware as BaseHardware

DEBUG = 0

# Define the name of the hardware and the items on the hardware screen (see quisk_conf_defaults.py):
################ Receivers SdrTrx, The SdrTrx radio by Rob Frohne, KL7NA
## hardware_file_name		Hardware file path, rfile
# This is the file that contains the control logic for each radio.
#hardware_file_name = 'sdrtrxpkg/quisk_hardware.py'

## widgets_file_name			Widget file path, rfile
# This optional file adds additional controls for the radio.
#widgets_file_name = ''

## si570_xtal_freq			Si570 crystal frequency, integer
# This is the Si570 startup frequency in Hz.  114.285MHz is the typical
# value from the data sheet; you can use 'usbsoftrock calibrate' to find
# the value for your device.
si570_xtal_freq = 114285000

## rx_max_amplitude_correct		Max ampl correct, number
# If you get your I/Q samples from a sound card, you will need to correct the
# amplitude and phase for inaccuracies in the analog hardware.  The correction is
# entered using the controls from the "Rx Phase" button on the config screen.
# You must enter a positive number.  This controls the range of the control.
rx_max_amplitude_correct = 0.2

## rx_max_phase_correct			Max phase correct, number
# If you get your I/Q samples from a sound card, you will need to correct the
# amplitude and phase for inaccuracies in the analog hardware.  The correction is
# entered using the controls from the "Rx Phase" button on the config screen.
# You must enter a positive number.  This controls the range of the control in degrees.
rx_max_phase_correct = 10.0

class Hardware(BaseHardware):
  def __init__(self, app, conf):
    BaseHardware.__init__(self, app, conf)
