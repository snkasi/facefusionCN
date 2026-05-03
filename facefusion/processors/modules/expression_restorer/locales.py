from facefusion.types import Locales

LOCALES : Locales =\
{
	'zh':
	{
		'help':
		{
			'model': '选择用于恢复面部表情的模型',
			'factor': '从目标面部恢复表情的强度',
			'areas': '选择表情恢复的区域（可选：{choices}）'
		},
		'uis':
		{
			'model_dropdown': '表情恢复模型',
			'factor_slider': '表情恢复强度',
			'areas_checkbox_group': '表情恢复区域'
		}
	},
	'en':
	{
		'help':
		{
			'model': 'choose the model responsible for restoring the expression',
			'factor': 'restore factor of expression from the target face',
			'areas': 'choose the items used for the expression areas (choices: {choices})'
		},
		'uis':
		{
			'model_dropdown': 'EXPRESSION RESTORER MODEL',
			'factor_slider': 'EXPRESSION RESTORER FACTOR',
			'areas_checkbox_group': 'EXPRESSION RESTORER AREAS'
		}
	}
}
