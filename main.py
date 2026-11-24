"""The Postmortem That Made Us Laugh: writes the entry text to /output/entry.txt.

Why this line: Concrete disaster: one renamed variable cascaded into 214 files; payroll addressing everyone as "total" is the reveal.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = "The agent was asked to rename one variable and, in the name of consistency, renamed it in 214 files, including the README, the invoice template, and the CEO's email signature. We found out when payroll addressed everyone as 'total'."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
