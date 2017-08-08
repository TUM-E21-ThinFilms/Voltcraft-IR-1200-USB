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

import slave
import e21_util

from slave.protocol import Protocol
from slave.transport import Timeout
from response import Response
from e21_util.lock import InterProcessTransportLock
from e21_util.error import CommunicationError


class VoltcraftIR1200Protocol(Protocol):
    def __init__(self, logger=None):
        self.logger = logger

    def read(self, transport):
        raw_response = self.read_response(transport)

        resp = []
        for el in raw_response:
            resp.append(el)

        return self.parse_response(resp)

    def parse_response(self, response):
        try:
            return Response(response)
        except RuntimeError as e:
            return None

    def read_response(self, transport):
        with InterProcessTransportLock(transport):
            try:
                resp = transport.read_exactly(21)
                self.logger.debug('Received response: "%s"', repr(resp))
                return resp
            except slave.transport.Timeout:
                raise CommunicationError("Could not read response")

    def clear(self, transport):
        with InterProcessTransportLock(transport):
            try:
                while True:
                    transport.read_bytes(21)
            except Timeout:
                return True
