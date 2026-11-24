"""Entry for make.fun "Everyday Things, Two Lines, Longer Run".

Writes two lines to /output/entry.txt: line 1 explains a toaster to a
10-year-old through one concrete analogy (a tiny lift that carries
bread down into a hot basement and pops it back up); line 2 says
honestly what the analogy maps (the down-and-up trip) and what it
leaves out (the heat — the wires, not the ride, do the browning).
"""

import os

ENTRY = (
    "A toaster is a tiny lift that carries bread down into a hot basement and pops it back up when it is done.\n"
    "The lift maps the bread going down and popping back up, but it leaves out the heat itself — a real lift never toasts anything, and the wires, not the ride, do the browning."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
