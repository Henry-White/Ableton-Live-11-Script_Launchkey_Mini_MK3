# uncompyle6 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Launchkey_Mini_MK3\skin.py
# Compiled at: 2022-06-10 17:15:31
# Size of source mod 2**32: 907 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import object
from ableton.v2.control_surface import Skin, merge_skins
# from novation.colors import Mono, Rgb, Blink
from .colors import Mono, Rgb
from novation.skin import skin as base_skin
# from ableton.v2.control_surface.elements import AnimatedColor, Color

class Colors(object):

    class Recording(object):
        On = Rgb.RED
        Off = Rgb.RED_HALF
        Transition = Rgb.RED_BLINK
        CaptureTriggered = Rgb.WHITE

    class TrackNavigation(object):
        On = Mono.HALF
        Pressed = Mono.ON

    class Device:
        Navigation = Rgb.PURPLE_HALF
        NavigationPressed = Rgb.PURPLE

    class SceneNavigation(object):
        On = Mono.HALF
        Pressed = Mono.ON

    class DrumGroup(object):
        PadSelected = Rgb.WHITE
        PadSelectedNotSoloed = Rgb.WHITE
        PadMutedSelected = Rgb.WHITE
        PadSoloedSelected = Rgb.WHITE
        Navigation = Rgb.WHITE_HALF
        NavigationPressed = Rgb.WHITE

    class Session(object):
        RecordButton = Rgb.RED_HALF
        ClipTriggeredPlay = Rgb.GREEN_BLINK
        ClipTriggeredRecord = Rgb.RED_BLINK
        ClipStarted = Rgb.GREEN_PULSE
        ClipRecording = Rgb.RED_PULSE
        ClipEmpty = Rgb.BLACK
        Scene = Rgb.BLACK
        SceneTriggered = Rgb.GREEN_BLINK
        NoScene = Rgb.BLACK
        StopClipTriggered = Rgb.YELLOW_BLINK
        StopClip = Rgb.YELLOW
        StopClipDisabled = Rgb.YELLOW_HALF
        Navigation = Rgb.WHITE_HALF
        NavigationPressed = Rgb.WHITE
        Select = Rgb.WHITE_HALF
        SelectPressed = Rgb.WHITE
        Delete = Rgb.WHITE_HALF
        DeletePressed = Rgb.WHITE
        Duplicate = Rgb.WHITE_HALF
        DuplicatePressed = Rgb.WHITE
        Quantize = Rgb.WHITE_HALF
        QuantizePressed = Rgb.WHITE
        Double = Rgb.CREAM
        DoublePressed = Rgb.WHITE
        ActionTriggered = Rgb.WHITE

    class Mixer(object):
        SoloOn = Rgb.BLUE
        SoloOff = Rgb.BLUE_HALF
        MuteOn = Rgb.ORANGE_HALF
        MuteOff = Rgb.ORANGE
        ArmOn = Rgb.RED
        ArmOff = Rgb.RED_HALF
        EmptyTrack = Rgb.BLACK
        TrackSelected = Rgb.WHITE
        TrackNotSelected = Rgb.WHITE_HALF


skin = merge_skins(*(base_skin, Skin(Colors)))
