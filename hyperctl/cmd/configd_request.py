class ConfigdRequest:
    def __init__(self) -> None:
        self.daemon = "configd"

    def send_request(self) -> str:
        return f"sent request to {self.daemon}"
