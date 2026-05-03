from facefusion.types import Locales

LOCALES : Locales =\
{
	'zh':
	{
		'help':
		{
			'model': '选择用于帧上色的模型',
			'size': '指定传递给帧上色器的帧尺寸',
			'blend': '将上色后的帧与原图进行混合'
		},
		'uis':
		{
			'blend_slider': '帧上色混合度',
			'model_dropdown': '帧上色模型',
			'size_dropdown': '帧上色尺寸'
		}
	},
	'en':
	{
		'help':
		{
			'model': 'choose the model responsible for colorizing the frame',
			'size': 'specify the frame size provided to the frame colorizer',
			'blend': 'blend the colorized into the previous frame'
		},
		'uis':
		{
			'blend_slider': 'FRAME COLORIZER BLEND',
			'model_dropdown': 'FRAME COLORIZER MODEL',
			'size_dropdown': 'FRAME COLORIZER SIZE'
		}
	}
}
