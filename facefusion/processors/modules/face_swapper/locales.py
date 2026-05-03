from facefusion.types import Locales

LOCALES : Locales =\
{
	'zh':
	{
		'help':
		{
			'model': '选择用于换脸的模型',
			'pixel_boost': '选择换脸的像素增强分辨率',
			'weight': '指定应用于面部的增强强度'
		},
		'uis':
		{
			'model_dropdown': '换脸模型',
			'pixel_boost_dropdown': '换脸像素增强',
			'weight_slider': '换脸强度'
		}
	},
	'en':
	{
		'help':
		{
			'model': 'choose the model responsible for swapping the face',
			'pixel_boost': 'choose the pixel boost resolution for the face swapper',
			'weight': 'specify the degree of weight applied to the face'
		},
		'uis':
		{
			'model_dropdown': 'FACE SWAPPER MODEL',
			'pixel_boost_dropdown': 'FACE SWAPPER PIXEL BOOST',
			'weight_slider': 'FACE SWAPPER WEIGHT'
		}
	}
}
