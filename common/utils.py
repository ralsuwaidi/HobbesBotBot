
def get_lines(file):
    """get all list"""

    lines = []
    with open(file) as f:
        lines = f.read().splitlines()

    return lines