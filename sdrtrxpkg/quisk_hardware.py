# This is the hardware file to support the SDR-TRX radio designed by Rob Frohne, KL7NA.

import traceback, time, math
import _quisk as QS

from quisk_hardware_model import Hardware as BaseHardware

DEBUG = 0

# Define the name of the hardware and the items on the hardware screen (see quisk_conf_defaults.py):
################ Receivers SdrTrx, The SdrTrx radio by Rob Frohne, KL7NA
## hardware_file_name		Hardware file path, rfile
# This is the file that contains the control logic for each radio.
# hardware_file_name = 'sdrtrxpkg/quisk_hardware_sdr-trx_UDP_16bit.py'

## widgets_file_name			Widget file path, rfile
# This optional file adds additional controls for the radio.
# widgets_file_name = ''

## SDRTRX_15_MHz_Frequequency	15 MHz WWV frequency, number
# The way I did it is to have the user 
# tune the SDR to 15 MHz WWV and then type that frequency in, and the correction 
# is calculated from it.  I could use that box, but would like to set the label 
# to something more appropriate to my Si5351A.  :-)
SDRTRX_15_MHz_Frequequency = 15000000

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

## pico_address				IP address, string
# The IP address of the SDR-TRX radio.
pico_address = '192.168.1.149'

class Hardware(BaseHardware):
  def __init__(self, app, conf):
    BaseHardware.__init__(self, app, conf)
