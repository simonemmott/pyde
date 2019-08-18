import string_utils as su
import re
import os.path

def secret(length=30):
    return ''.join(random.choice('abcdefghighjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(length))

def to_snake_case(s, separator='_'):
    if not su.is_string(s):
        return s
    if not su.is_full_string(s):
        return s
    if su.is_snake_case(s, separator=separator):
        return s
    return re.sub('[^a-z0-9]+', separator, s.strip().lower()).strip(separator)
    
def to_kebab_case(s):
    return to_snake_case(s, separator='-')
    
def to_camel_case(s):
    if not su.is_string(s):
        return s
    if not su.is_full_string(s):
        return s
    if su.is_camel_case(s):
        return s[0].lower()+s[1:]
    return su.snake_case_to_camel(re.sub('^[0-9_]+', '', to_snake_case(s)), upper_case_first=False)

def to_class_case(s):
    if not su.is_string(s):
        return s
    if not su.is_full_string(s):
        return s
    if su.is_camel_case(s):
        return s[0].upper()+s[1:]
    sub = re.sub('^[0-9_]+', '', to_snake_case(s))
    camel = su.snake_case_to_camel(sub)
    return camel[0].upper()+camel[1:]

def to_sentence_case(s):
    if not su.is_string(s):
        return s
    if not su.is_full_string(s):
        return s
    h = re.sub('[^a-zA-Z0-9]+', ' ', s.strip()).strip()
    return h[0].upper()+h[1:]

def to_title_case(s):
    if not su.is_string(s):
        return s
    if not su.is_full_string(s):
        return s
    return to_snake_case(s, separator=' ').title()

def to_plural(s):
    if not su.is_string(s):
        return s
    if not su.is_full_string(s):
        return s
    if s[-1:] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return s
    if s[-1:] == 'f':
        return s[:-1]+'ves'
    if s[-2:] == 'us':
        return s[:-2]+'i'
    if s[-2:] == 'ay':
        return s+'s'
    if s[-1:] in ['y', 'i']:
        return s[:-1]+'ies'
    if s[-1:] == 's':
        return s+'es'

    return s+'s'

def build_path(*path):
    return os.path.sep.join(list(path))

def path_exists(*path):
    return os.path.exists(build_path(*path))

def is_number(val):
    try:
        float(val)
        return True
    except:
        return False
