from facefusion.types import Locales

LOCALES : Locales =\
{
	'zh':
	{
		'help':
		{
			'model': '选择用于深度换脸的模型',
			'morph': '在源人脸和目标人脸之间进行融合过渡'
		},
		'uis':
		{
			'model_dropdown': '深度换脸模型',
			'morph_slider': '深度换脸融合度'
		}
	},
	'en':
	{
		'help':
		{
			'model': 'choose the model responsible for swapping the face',
			'morph': 'morph between source face and target faces'
		},
		'uis':
		{
			'model_dropdown': 'DEEP SWAPPER MODEL',
			'morph_slider': 'DEEP SWAPPER MORPH'
		}
	}
}
