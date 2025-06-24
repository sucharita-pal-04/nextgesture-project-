from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL, GUID
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
from utils import distance_to_value

class GestureController:
    def __init__(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume.iid, CLSCTX_ALL, None)
        self.volume = cast(interface, POINTER(IAudioEndpointVolume))
        self.volMin, self.volMax = self.volume.GetVolumeRange()[0:2]

    def apply_controls(self, img, hands):
        left = hands['left']
        right = hands['right']

        if left:
            x1, y1 = left[4]
            x2, y2 = left[8]
            length = distance_to_value(x1, y1, x2, y2)
            brightness = int(distance_to_value(length, 15, 200, 0, 100))
            sbc.set_brightness(brightness)

        if right:
            x1, y1 = right[4]
            x2, y2 = right[8]
            length = distance_to_value(x1, y1, x2, y2)
            vol = distance_to_value(length, 15, 200, self.volMin, self.volMax)
            self.volume.SetMasterVolumeLevel(vol, None)

        return hands['img']
