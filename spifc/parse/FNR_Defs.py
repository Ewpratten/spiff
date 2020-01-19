# Find & Replace defs

from .errors.ParseError import ParseError


def handleClassdef(matches: list) -> str:

    print(matches)
    # Check for required args
    if len(matches) != 5:
        raise ParseError("Failed to parse. Malformed class")

    return f"""
{matches[0]}
class {matches[1]}({matches[2]}):
{matches[3]}

{matches[4]}
"""


fnr = [
    (r"(?s)(.*)(?-s)%c *(.*)\((.*)\) *{$(?s)(.*)(?-s)}(?s)(.*)(?-s)", handleClassdef)
]
