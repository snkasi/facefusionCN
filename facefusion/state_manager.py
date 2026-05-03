import json
from pathlib import Path
from typing import Any, Union

from facefusion.app_context import detect_app_context
from facefusion.processors.types import ProcessorState, ProcessorStateKey, ProcessorStateSet
from facefusion.types import State, StateKey, StateSet

STATE_SET : Union[StateSet, ProcessorStateSet] =\
{
	'cli': {}, #type:ignore[assignment]
	'ui': {} #type:ignore[assignment]
}
STATE_FILE = Path.home() / '.facefusion' / 'ui_state.json'


def get_state() -> Union[State, ProcessorState]:
	app_context = detect_app_context()
	return STATE_SET.get(app_context)


def sync_state() -> None:
	STATE_SET['cli'] = STATE_SET.get('ui') #type:ignore[assignment]


def init_item(key : Union[StateKey, ProcessorStateKey], value : Any) -> None:
	STATE_SET['cli'][key] = value #type:ignore[literal-required]
	STATE_SET['ui'][key] = value #type:ignore[literal-required]


def load_ui_state() -> None:
	"""从 JSON 文件加载持久化的 UI 状态"""
	if not STATE_FILE.exists():
		return
	try:
		with open(STATE_FILE, 'r', encoding = 'utf-8') as f:
			saved_state = json.load(f)
		for key, value in saved_state.items():
			if key in STATE_SET['ui']:
				STATE_SET['ui'][key] = value #type:ignore[literal-required]
	except (json.JSONDecodeError, IOError):
		pass


def save_ui_state() -> None:
	"""将当前 UI 状态保存到 JSON 文件"""
	STATE_FILE.parent.mkdir(parents = True, exist_ok = True)
	try:
		with open(STATE_FILE, 'w', encoding = 'utf-8') as f:
			json.dump(STATE_SET['ui'], f, default = str, ensure_ascii = False)
	except IOError:
		pass


def get_item(key : Union[StateKey, ProcessorStateKey]) -> Any:
	return get_state().get(key) #type:ignore[literal-required]


def set_item(key : Union[StateKey, ProcessorStateKey], value : Any) -> None:
	app_context = detect_app_context()
	STATE_SET[app_context][key] = value #type:ignore[literal-required]
	# 在 UI 上下文中自动持久化状态
	if app_context == 'ui':
		save_ui_state()


def sync_item(key : Union[StateKey, ProcessorStateKey]) -> None:
	STATE_SET['cli'][key] = STATE_SET.get('ui').get(key) #type:ignore[literal-required]


def clear_item(key : Union[StateKey, ProcessorStateKey]) -> None:
	set_item(key, None)
