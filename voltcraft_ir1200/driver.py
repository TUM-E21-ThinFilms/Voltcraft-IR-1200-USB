# Copyright (C) 2016, see AUTHORS.md
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from protocol import VoltcraftIR1200Protocol

class VoltcraftIR1200Driver(object):

    def __init__(self, transport, protocol=None):

        if protocol is None:
            protocol = VoltcraftIR1200Protocol()

        self._transport = transport
        self._protocol = protocol


    def clear(self):
        self._protocol.clear(self._transport)

    def read(self):
        return self._protocol.read(self._transport)
