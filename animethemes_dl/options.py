"""
Options for animethemes_dl.
"""
import logging
from .models import Options,DEFAULT

logger = logging.getLogger('animethemes-dl')
OPTIONS = Options(DEFAULT)

def _update_dict(old: dict, new: dict):
    """
    Updates a dict with nested dicts.
    Skips options that do not exist.
    """
    for k,v in new.items():
        if isinstance(v, dict):
            if k in old:
                old[k] = _update_dict(old[k],v)
            else:
                logger.error(f'Cannot change option category {repr(k)}; does not exist.')
        else:
            if k in old:
                old[k] = new[k]
            else:
                logger.error(f'Cannot change value {repr(k)}.')
    
    return old

def setOptions(options: Options):
    """
    Sets `animethemes_dl.OPTIONS`.
    Look at `animethemes_dl.OPTIONS` for defaults.
    """
    global OPTIONS
    OPTIONS = Options(_update_dict(OPTIONS,options))
    
    logger.debug(f'Changed {len(options)} categories in options.')

if __name__ == "__main__":
    from pprint import pprint
    logger.setLevel(level=logging.DEBUG)
    options = {
        'statuses':[1,2,3,4],
        'filter':{
            'spoilers':False,
            'spoiler':True
        },
        'useless': {
            'hello':[]
        }
    }
    setOptions(options)
    pprint(OPTIONS)
