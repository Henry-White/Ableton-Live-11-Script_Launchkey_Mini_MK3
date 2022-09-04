# uncompyle6 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchkey_MK3\device.py
# Compiled at: 2022-06-10 17:15:31
# Size of source mod 2**32: 3734 bytes
from __future__ import absolute_import, print_function, unicode_literals
from future.moves.itertools import zip_longest
from past.builtins import unicode
from _Generic.Devices import parameter_bank_names
from ableton.v2.base import listens_group, liveobj_valid, task
from ableton.v2.control_surface.control import control_list
from novation.simple_device import SimpleDeviceParameterComponent
from novation.simple_device_navigation import SimpleDeviceNavigationComponent

class DeviceComponent(SimpleDeviceNavigationComponent, SimpleDeviceParameterComponent):

    def __init__(self, show_notification=None, *a, **k):
        (super(DeviceComponent, self).__init__)(*a, **k)
        self._show_on_scroll_task = self._tasks.add(task.sequence(task.wait(0.1), task.run(self.show_device_name_and_bank)))

    def _on_bank_select_button_checked(self, button):
        super(DeviceComponent, self)._on_bank_select_button_checked(button)
        self.show_device_name_and_bank()

    def _on_bank_select_button_released(self):
        self.show_device_name_and_bank()

    def _scroll_device_chain(self, direction):
        super(DeviceComponent, self)._scroll_device_chain(direction)
        self._show_on_scroll_task.restart()

    def show_device_name_and_bank(self):
        device = self._device_provider.device

    def _on_device_lock_button_toggled(self):
        super(DeviceComponent, self)._on_device_lock_button_toggled()

    def update(self):
        super(DeviceComponent, self).update()
        parameters = self.selected_bank if self._parameter_controls else []
