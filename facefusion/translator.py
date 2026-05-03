import importlib
import os
from typing import List, Optional, Tuple

from facefusion.types import Language, LocalePoolSet, Locales

LOCALE_POOL_SET : LocalePoolSet = {}
CURRENT_LANGUAGE : Language = 'en' if os.environ.get('FACEFUSION_LANGUAGE') == 'en' else 'zh'


def __autoload__(module_name : str) -> None:
	try:
		__locales__ = importlib.import_module(module_name + '.locales')
		load(__locales__.LOCALES, module_name)
	except ImportError:
		pass


def load(__locales__ : Locales, module_name : str) -> None:
	LOCALE_POOL_SET[module_name] = __locales__


def get(notation : str, module_name : str = 'facefusion') -> Optional[str]:
	if module_name not in LOCALE_POOL_SET:
		__autoload__(module_name)

	current = LOCALE_POOL_SET.get(module_name).get(CURRENT_LANGUAGE)

	for fragment in notation.split('.'):
		if fragment in current:
			current = current.get(fragment)

			if isinstance(current, str):
				return current

	return None


def translate_choice(choice_key : str, choice_value : str = None, module_name : str = 'facefusion') -> Tuple[str, str]:
	choice_value = choice_value if choice_value is not None else choice_key
	translated = get('choices.' + choice_key, module_name)
	return (translated, choice_value) if translated else (choice_value, choice_value)


def translate_choices(choices : List[str], prefix : str = '', module_name : str = 'facefusion') -> List[Tuple[str, str]]:
	return [ translate_choice(prefix + '.' + choice if prefix else choice, choice, module_name) for choice in choices ]
