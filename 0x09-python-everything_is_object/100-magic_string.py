#!/usr/bin/python3

def magic_string():
    # Get the word "BestSchool" n times in a string.
    if hasattr(magic_string, 'calls'):
        magic_string.calls += 1
    else:
        magic_string.calls = 1

    return ', '.join(['BestSchool'] * magic_string.calls)

# Original response
#
# #!/usr/bin/python3
# def magic_string():
#     setattr(magic_string, 'rep', getattr(magic_string, 'rep', -1) + 1)
#     return 'BestSchool' + ', BestSchool' * getattr(magic_string, 'rep', 0)
