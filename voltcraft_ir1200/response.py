

class Response(object):
    def __init__(self, raw_response):
        if not isinstance(raw_response, list):
            raise TypeError("given input must be of type list")

        self._response = raw_response

        if not self._validate():
            raise RuntimeError("given input data is no valid response")

        self._ems = 0
        self._ir = 0
        self._ktype = 0
        self._max = 0
        self._min = 0
        self._diff = 0
        self._avg = 0
        self._alarm_high = 0
        self._alarm_low = 0
        self._flag = 0

        self._assign()

    def _validate(self):
        if not len(self._response) == 21:
            return False

        if not (self._response[0] == 0xFF or self._response[1] == 0xFF):
            return False

        if not self._response[-1] == 0xAA:
            return False

        return True

    def _assign(self):
        self._ems = self._response[2] * 0.1
        self._ir = self._compute_value(self._response[3:5])
        self._ktype = self._compute_value(self._response[5:7])
        self._max = self._compute_value(self._response[7:9])
        self._min = self._compute_value(self._response[9:11])
        self._diff = self._compute_value(self._response[11:13])
        self._avg = self._compute_value(self._response[13:15])
        self._alarm_high = self._compute_value(self._response[15:17])
        self._alarm_low = self._compute_value(self._response[17:19])
        self._flag = self._response[19:20]

    def get_emissivity(self):
        return self._ems

    def get_ir(self):
        return self._ir

    def get_ktype(self):
        return self._ktype

    def get_ir_max(self):
        return self._max

    def get_ir_min(self):
        return self._min

    def get_ir_diff(self):
        return self._diff

    def get_ir_avg(self):
        return self._avg

    def get_ir_low_alarm(self):
        return self._alarm_low

    def get_ir_high_alarm(self):
        return self._alarm_high

    def get_flag(self):
        return self._flag

    def _compute_value(self, hex_list):
        assert len(hex_list) == 2

        if hex_list[0] == 0xFF:
            return (hex_list[0] * 256 + hex_list[1] - 0x10000) * 0.1

        return (hex_list[0] * 256 + hex_list[1]) * 0.1

    def __str__(self):
        return "Response: "+ " ".join(map(hex, self._response))


