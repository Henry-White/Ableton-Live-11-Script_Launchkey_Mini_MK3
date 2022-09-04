# uncompyle6 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchkey_Mini_MK3\elements.py
# Compiled at: 2022-06-10 17:15:31
# Size of source mod 2**32: 682 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object, range
from ableton.v2.control_surface import MIDI_CC_TYPE, MIDI_NOTE_TYPE
from novation.launchkey_elements import SESSION_WIDTH, LaunchkeyElements, create_button
from ableton.v2.control_surface.elements import ButtonMatrixElement

class Elements(LaunchkeyElements):

    def __init__(self, *a, **k):
        (super(Elements, self).__init__)(*a, **k)
        self.record_button_with_shift = self.with_shift(self.record_button)
        self.scene_launch_button_with_shift = self.with_shift(self.scene_launch_buttons_raw[0])
        self.stop_solo_mute_button_with_shift = self.with_shift(self.scene_launch_buttons_raw[1])
        self.device_select_matrix = ButtonMatrixElement(rows=[[create_button((offset + col_index), ('{}_Device_Select_Button_{}'.format(col_index, row_index)), msg_type=MIDI_NOTE_TYPE, channel=0) for col_index in range(SESSION_WIDTH)] for row_index, offset in enumerate(range(64, 87, 16))],
          name='Device_Select_Matrix')
