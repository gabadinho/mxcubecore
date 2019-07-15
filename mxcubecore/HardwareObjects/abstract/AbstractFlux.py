#
#  Project: MXCuBE
#  https://github.com/mxcube.
#
#  This file is part of MXCuBE software.
#
#  MXCuBE is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  MXCuBE is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with MXCuBE.  If not, see <http://www.gnu.org/licenses/>.

import api

from scipy.interpolate import interp1d

from HardwareRepository.BaseHardwareObjects import HardwareObject


__credits__ = ["MXCuBE collaboration"]
__version__ = "2.3."
__category__ = "General"

# Dose rate for a standard composition crystal, in Gy/s
# As a function of energy in keV
dose_rate_per_photon_per_mmsq = interp1d(
    [4.0, 6.6, 9.2, 11.8, 14.4, 17.0, 19.6, 22.2, 24.8, 27.4, 30.0],
    [
        4590.0e-12,
        1620.0e-12,
        790.0e-12,
        457.0e-12,
        293.0e-12,
        202.0e-12,
        146.0e-12,
        111.0e-12,
        86.1e-12,
        68.7e-12,
        55.2e-12,
    ],
)

class AbstractFlux(HardwareObject):
    def __init__(self, name):
        HardwareObject.__init__(self, name)

        self.dose_rate_per_photon_per_mmsq = dose_rate_per_photon_per_mmsq


    def get_flux(self):
        """Get flux at current transmission in units of photons/s"""
        raise NotImplementedError

    def get_dose_rate(self, energy=None):
        """
        Get dose rate in kGy/s for a standard crystal at current settings.
        Assumes square, top-hat beam with al flux snside the beam size.
        Override in subclasses for different situations

        :param energy: float Energy for calculation of dose rate, in keV.
        :return: float
        """

        energy = energy or api.energy.get_current_energy()

        # NB   Calculation assumes beam sizes in mm
        beam_size = api.beam_info.get_beam_size()

        # Result in kGy/s
        result = (
                self.dose_rate_per_photon_per_mmsq(energy)
                * self.get_flux()
                / beam_size[0]
                / beam_size[1]
                / 1000.  # Converts to kGy/s
        )
        return result

    def update_values(self):
        self.emit("fluxValueChanged", self._value)