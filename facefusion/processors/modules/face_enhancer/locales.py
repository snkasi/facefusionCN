from facefusion.types import Locales

LOCALES : Locales =\
{
	'zh':
	{
		'help':
		{
			'model': '选择用于增强面部的模型',
			'blend': '将增强后的面部与原图进行混合',
			'weight': '指定应用于面部的增强强度'
		},
		'uis':
		{
			'blend_slider': '面部增强混合度',
			'model_dropdown': '面部增强模型',
			'weight_slider': '面部增强强度'
		}
	},
	'en':
	{
		'help':
		{
			'model': 'choose the model responsible for enhancing the face',
			'blend': 'blend the enhanced into the previous face',
			'weight': 'specify the degree of weight applied to the face'
		},
		'uis':
		{
			'blend_slider': 'FACE ENHANCER BLEND',
			'model_dropdown': 'FACE ENHANCER MODEL',
			'weight_slider': 'FACE ENHANCER WEIGHT'
		}
	}
}
