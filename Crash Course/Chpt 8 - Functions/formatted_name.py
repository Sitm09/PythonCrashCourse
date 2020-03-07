## Page 142, Chpt 8 - Functions

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' '+ last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

muscian = get_formatted_name('jimi', 'hendrix')
print(muscian)
