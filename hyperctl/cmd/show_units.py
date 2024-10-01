from hyperctl.cmd.configd_request import ConfigdRequest


class ShowUnits:
    def __init__(self) -> None:
        self.configd_request = ConfigdRequest()

    def show_units(self) -> str:
        return self.configd_request.send_request()
