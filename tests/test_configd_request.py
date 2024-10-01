from hyperctl.cmd.configd_request import ConfigdRequest


def test_send_request():
    c = ConfigdRequest()
    assert c.send_request() == "sent request to configd"
