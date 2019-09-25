from HardwareRepository import HardwareRepository as HWR
from HardwareRepository.BaseHardwareObjects import Device
import PyTango


class SOLEILFlux(Device):
    def __init__(self, name):
        Device.__init__(self, name)

    def init(self):
        self.flux_channel = self.getChannelObject("flux")

    def getCurrentFlux(self):
        try:
            return self.flux_channel.getValue()
        except PyTango.DevFailed:
            return -1


def test():
    hwr = HWR.getHardwareRepository()
    hwr.connect()

    flux = hwr.getHardwareObject("/flux")

    print("PX1 Flux is ", flux.getCurrentFlux())


if __name__ == "__main__":
    test()
