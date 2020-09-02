# parses to format "1997-10-28 00:35"

def parsedatetme(have):
    if len(have.split(".")) == 4:
        d, m, y, mi = have.split(".")
        y, h = y.split(",")
    else:
        d, m, yh = have.split(".")
        y, h = yh.split(",")
    h = h.strip()
    y = y.strip()
    if len(d) == 1:
        d = '0' + d
    if len(m) == 1:
        m = '0' + m
    return y + '-' + m + '-' + d + ' ' + h[:2] + ':00'
