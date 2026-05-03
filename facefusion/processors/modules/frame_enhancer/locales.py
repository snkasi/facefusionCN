from facefusion.types import Locales

LOCALES : Locales =\
{
	'zh':
	{
		'help':
		{
			'model': '选择用于帧增强的模型',
			'blend': '将增强后的帧与原图进行混合'
		},
		'uis':
		{
			'blend_slider': '帧增强混合度',
			'model_dropdown': '帧增强模型'
		}
	},
	'en':
	{
		'help':
		{
			'model': 'choose the model responsible for enhancing the frame',
			'blend': 'blend the enhanced into the previous frame'
		},
		'uis':
		{
			'blend_slider': 'FRAME ENHANCER BLEND',
			'model_dropdown': 'FRAME ENHANCER MODEL'
		}
	}
}
