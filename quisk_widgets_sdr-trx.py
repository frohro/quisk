# Please do not change this widgets module for Quisk.  Instead copy
# it to your own quisk_widgets.py and make changes there.
#
# This module is used to add extra widgets to the QUISK screen.

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import math, wx

class BottomWidgets:	# Add extra widgets to the bottom of the screen
  def __init__(self, app, hardware, conf, frame, gbs, vertBox):
    self.config = conf
    self.hardware = hardware
    self.application = app
    self.start_row = config.widget_row			# The first available row
    self.start_col = config.button_start_col	# The start of the button columns
    self.Widgets_0x06(app, hardware, conf, frame, gbs, vertBox)

  def Widgets_0x06(self, app, hardware, conf, frame, gbs, vertBox):
    self.num_rows_added = 1
    start_row = self.start_row
    b1 = app.QuiskCheckbutton(frame, self.OnTest, 'On Test')
    gbs.Add(b1, (start_row, self.start_col), (1, 2), flag=wx.EXPAND)

    
  def OnTest(self, event):
    btn = event.GetEventObject()
    value = btn.GetValue()
    print('In OnTest:', value)