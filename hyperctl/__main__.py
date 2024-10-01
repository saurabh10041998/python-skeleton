from hyperctl.cmd.configd_request import ConfigdRequest
import argparse


def do_send(send_request: bool) -> None:
    if send_request:
        c = ConfigdRequest()
        print(f"[*] {c.send_request()}")
    else:
        print("Not sending request...")


def hyperctl_entry_point() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--send", action="store_true", required=True, help="Send requiest"
    )
    opts = vars(parser.parse_args())
    do_send(opts["send"])


if __name__ == "__main__":
    exit(hyperctl_entry_point())
