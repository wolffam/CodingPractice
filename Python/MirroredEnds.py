# Given a string, look for a mirror image (backwards) string at both the beginning and end of the given string


def mirrored_ends(in_str):
    rev_str = in_str[::-1]
    print(rev_str)
    out = ''
    for ind, letter in enumerate(in_str):
        if letter == rev_str[ind]:
            out += letter
        else:
            break
    return out

print(mirrored_ends('abXYZba'))