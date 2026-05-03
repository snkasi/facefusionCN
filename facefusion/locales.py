from facefusion.types import Locales

LOCALES : Locales =\
{
	'zh':
	{
		'conda_not_activated': '未激活 conda 环境',
		'python_not_supported': '不支持当前 Python 版本，请升级到 {version} 或更高',
		'curl_not_installed': '未安装 curl',
		'ffmpeg_not_installed': '未安装 ffmpeg',
		'creating_temp': '正在创建临时资源',
		'extracting_frames': '正在以 {resolution} 分辨率和每秒 {fps} 帧提取帧',
		'extracting_frames_succeeded': '提取帧成功',
		'extracting_frames_failed': '提取帧失败',
		'analysing': '正在分析',
		'extracting': '正在提取',
		'streaming': '正在串流',
		'processing': '正在处理',
		'merging': '正在合并',
		'downloading': '正在下载',
		'temp_frames_not_found': '未找到临时帧',
		'copying_image': '正在以 {resolution} 分辨率复制图像',
		'copying_image_succeeded': '复制图像成功',
		'copying_image_failed': '复制图像失败',
		'finalizing_image': '正在以 {resolution} 分辨率生成最终图像',
		'finalizing_image_succeeded': '生成最终图像成功',
		'finalizing_image_skipped': '跳过生成最终图像',
		'merging_video': '正在以 {resolution} 分辨率和每秒 {fps} 帧合并视频',
		'merging_video_succeeded': '合并视频成功',
		'merging_video_failed': '合并视频失败',
		'skipping_audio': '正在跳过音频',
		'replacing_audio_succeeded': '替换音频成功',
		'replacing_audio_skipped': '跳过替换音频',
		'restoring_audio_succeeded': '恢复音频成功',
		'restoring_audio_skipped': '跳过恢复音频',
		'clearing_temp': '正在清理临时资源',
		'processing_stopped': '处理已停止',
		'processing_image_succeeded': '图像处理成功，耗时 {seconds} 秒',
		'processing_image_failed': '图像处理失败',
		'processing_video_succeeded': '视频处理成功，耗时 {seconds} 秒',
		'processing_video_failed': '视频处理失败',
		'choose_image_source': '选择源图像',
		'choose_audio_source': '选择源音频',
		'choose_video_target': '选择目标视频',
		'choose_image_or_video_target': '选择目标图像或视频',
		'specify_image_or_video_output': '指定输出的图像或视频目录',
		'match_target_and_output_extension': '目标文件和输出文件的扩展名需一致',
		'no_source_face_detected': '未检测到源人脸',
		'processor_not_loaded': '无法加载处理器 {processor}',
		'processor_not_implemented': '处理器 {processor} 未正确实现',
		'ui_layout_not_loaded': '无法加载 UI 布局 {ui_layout}',
		'ui_layout_not_implemented': 'UI 布局 {ui_layout} 未正确实现',
		'stream_not_loaded': '无法加载串流 {stream_mode}',
		'stream_not_supported': '不支持串流',
		'job_created': '任务 {job_id} 已创建',
		'job_not_created': '任务 {job_id} 未创建',
		'job_submitted': '任务 {job_id} 已提交',
		'job_not_submitted': '任务 {job_id} 未提交',
		'job_all_submitted': '所有任务已提交',
		'job_all_not_submitted': '所有任务未提交',
		'job_deleted': '任务 {job_id} 已删除',
		'job_not_deleted': '任务 {job_id} 未删除',
		'job_all_deleted': '所有任务已删除',
		'job_all_not_deleted': '所有任务未删除',
		'job_step_added': '步骤已添加到任务 {job_id}',
		'job_step_not_added': '步骤未添加到任务 {job_id}',
		'job_remix_step_added': '步骤 {step_index} 已从任务 {job_id} 混合',
		'job_remix_step_not_added': '步骤 {step_index} 未从任务 {job_id} 混合',
		'job_step_inserted': '步骤 {step_index} 已插入到任务 {job_id}',
		'job_step_not_inserted': '步骤 {step_index} 未插入到任务 {job_id}',
		'job_step_removed': '步骤 {step_index} 已从任务 {job_id} 移除',
		'job_step_not_removed': '步骤 {step_index} 未从任务 {job_id} 移除',
		'running_job': '正在运行排队中的任务 {job_id}',
		'running_jobs': '正在运行所有排队中的任务',
		'retrying_job': '正在重试失败的任务 {job_id}',
		'retrying_jobs': '正在重试所有失败的任务',
		'processing_job_succeeded': '任务 {job_id} 处理成功',
		'processing_jobs_succeeded': '所有任务处理成功',
		'processing_job_failed': '任务 {job_id} 处理失败',
		'processing_jobs_failed': '所有任务处理失败',
		'processing_step': '正在处理步骤 {step_current} / {step_total}',
		'validating_hash_succeeded': '验证 {hash_file_name} 的哈希成功',
		'validating_hash_failed': '验证 {hash_file_name} 的哈希失败',
		'validating_source_succeeded': '验证 {source_file_name} 的源文件成功',
		'validating_source_failed': '验证 {source_file_name} 的源文件失败',
		'deleting_corrupt_source': '正在删除损坏的源文件 {source_file_name}',
		'loading_model_succeeded': '加载模型 {model_name} 成功，耗时 {seconds} 秒',
		'loading_model_failed': '加载模型 {model_name} 失败',
		'time_ago_now': '刚刚',
		'time_ago_minutes': '{minutes} 分钟前',
		'time_ago_hours': '{hours} 小时 {minutes} 分钟前',
		'time_ago_days': '{days} 天 {hours} 小时 {minutes} 分钟前',
		'point': '。',
		'comma': '，',
		'colon': '：',
		'question_mark': '？',
		'exclamation_mark': '！',
		'help':
		{
			'install_dependency': '选择要安装的 {dependency} 版本',
			'skip_conda': '跳过 conda 环境检查',
			'config_path': '选择用于覆盖默认设置的配置文件',
			'temp_path': '指定临时资源的存储目录',
			'jobs_path': '指定任务的存储目录',
			'source_paths': '选择图像或音频路径',
			'target_path': '选择图像或视频路径',
			'output_path': '指定输出图像或视频的目录',
			'source_pattern': '选择图像或音频的通配符模式',
			'target_pattern': '选择图像或视频的通配符模式',
			'output_pattern': '指定输出图像或视频的通配符模式',
			'face_detector_model': '选择用于检测人脸的模型',
			'face_detector_size': '指定传递给面部检测器的帧尺寸',
			'face_detector_margin': '对帧应用上、右、下、左边距',
			'face_detector_angles': '指定检测人脸前旋转帧的角度',
			'face_detector_score': '根据置信度分数过滤检测到的人脸',
			'face_landmarker_model': '选择用于检测面部特征点的模型',
			'face_landmarker_score': '根据置信度分数过滤检测到的面部特征点',
			'face_selector_mode': '使用基于参考的跟踪或简单匹配',
			'face_selector_order': '指定检测到的人脸的排序方式',
			'face_selector_age_start': '根据起始年龄过滤检测到的人脸',
			'face_selector_age_end': '根据结束年龄过滤检测到的人脸',
			'face_selector_gender': '根据性别过滤检测到的人脸',
			'face_selector_race': '根据人种过滤检测到的人脸',
			'reference_face_position': '指定用于创建参考人脸的位置',
			'reference_face_distance': '指定参考人脸和目标人脸之间的相似度',
			'reference_frame_number': '指定用于创建参考人脸的帧号',
			'face_occluder_model': '选择用于生成遮挡掩码的模型',
			'face_parser_model': '选择用于生成区域掩码的模型',
			'face_mask_types': '混合搭配不同的面部掩码类型（可选：{choices}）',
			'face_mask_areas': '选择用于区域掩码的选项（可选：{choices}）',
			'face_mask_regions': '选择用于区域掩码的面部区域（可选：{choices}）',
			'face_mask_blur': '指定应用于方形掩码的模糊程度',
			'face_mask_padding': '对方形掩码应用上、右、下、左内边距',
			'voice_extractor_model': '选择用于提取人声的模型',
			'trim_frame_start': '指定目标视频的起始帧',
			'trim_frame_end': '指定目标视频的结束帧',
			'temp_frame_format': '指定临时资源的格式',
			'keep_temp': '处理完成后保留临时资源',
			'output_image_quality': '指定图像质量，影响图像压缩程度',
			'output_image_scale': '根据目标图像指定输出图像的缩放比例',
			'output_audio_encoder': '指定音频编码器',
			'output_audio_quality': '指定音频质量，影响音频压缩程度',
			'output_audio_volume': '根据目标视频指定音频音量',
			'output_video_encoder': '指定视频编码器',
			'output_video_preset': '平衡视频处理速度和文件大小',
			'output_video_quality': '指定视频质量，影响视频压缩程度',
			'output_video_scale': '根据目标视频指定输出视频的缩放比例',
			'output_video_fps': '根据目标视频指定输出视频的帧率',
			'processors': '加载单个或多个处理器（可选：{choices}，...）',
			'background-remover-model': '选择用于移除背景的模型',
			'background-remover-color': '为背景应用红、绿、蓝和 Alpha 通道值',
			'open_browser': '程序就绪后自动打开浏览器',
			'ui_layouts': '启动单个或多个 UI 布局（可选：{choices}，...）',
			'ui_workflow': '选择 UI 工作流',
			'preview_mode': '选择预览模式（可选：{choices}）',
			'preview_resolution': '选择预览分辨率（可选：{choices}）',
			'download_providers': '使用不同的下载源（可选：{choices}，...）',
			'download_scope': '指定下载范围',
			'benchmark_mode': '选择基准测试模式',
			'benchmark_resolutions': '选择基准测试的分辨率（可选：{choices}，...）',
			'benchmark_cycle_count': '指定每次基准测试的循环次数',
			'execution_device_ids': '指定用于处理的设备编号',
			'execution_providers': '使用不同的推理后端（可选：{choices}，...）',
			'execution_thread_count': '指定处理时的并行线程数',
			'video_memory_strategy': '平衡快速处理和低显存占用',
			'system_memory_limit': '限制处理时可使用的系统内存',
			'log_level': '调整终端中显示的消息详细程度',
			'halt_on_error': '发生错误时停止程序',
			'run': '运行程序',
			'headless_run': '以无界面模式运行程序',
			'batch_run': '以批处理模式运行程序',
			'force_download': '强制自动下载模型并退出',
			'benchmark': '运行基准测试',
			'job_id': '指定任务 ID',
			'job_status': '指定任务状态',
			'step_index': '指定步骤索引',
			'job_list': '按状态列出任务',
			'job_create': '创建草稿任务',
			'job_submit': '提交草稿任务到等待队列',
			'job_submit_all': '提交所有草稿任务到等待队列',
			'job_delete': '删除草稿、排队、失败或已完成的任务',
			'job_delete_all': '删除所有草稿、排队、失败和已完成的任务',
			'job_add_step': '向草稿任务添加步骤',
			'job_remix_step': '从草稿任务的前一步骤进行混合',
			'job_insert_step': '向草稿任务插入步骤',
			'job_remove_step': '从草稿任务移除步骤',
			'job_run': '运行排队中的任务',
			'job_run_all': '运行所有排队中的任务',
			'job_retry': '重试失败的任务',
			'job_retry_all': '重试所有失败的任务'
		},
		'about':
		{
			'fund': '资助 AI 工作站',
			'subscribe': '成为会员',
			'join': '加入我们的社区'
		},
		'uis':
		{
			'apply_button': '应用',
			'benchmark_mode_dropdown': '基准测试模式',
			'benchmark_cycle_count_slider': '基准测试循环次数',
			'benchmark_resolutions_checkbox_group': '基准测试分辨率',
			'clear_button': '清除',
			'common_options_checkbox_group': '选项',
			'download_providers_checkbox_group': '下载源',
			'execution_providers_checkbox_group': '推理后端',
			'execution_thread_count_slider': '执行线程数',
			'face_detector_angles_checkbox_group': '人脸检测角度',
			'face_detector_model_dropdown': '人脸检测模型',
			'face_detector_margin_slider': '人脸检测边距',
			'face_detector_score_slider': '人脸检测置信度',
			'face_detector_size_dropdown': '人脸检测尺寸',
			'face_landmarker_model_dropdown': '面部特征点模型',
			'face_landmarker_score_slider': '面部特征点置信度',
			'face_mask_blur_slider': '人脸掩码模糊度',
			'face_mask_padding_bottom_slider': '人脸掩码下边距',
			'face_mask_padding_left_slider': '人脸掩码左边距',
			'face_mask_padding_right_slider': '人脸掩码右边距',
			'face_mask_padding_top_slider': '人脸掩码上边距',
			'face_mask_areas_checkbox_group': '人脸掩码区域',
			'face_mask_regions_checkbox_group': '人脸掩码面部区域',
			'face_mask_types_checkbox_group': '人脸掩码类型',
			'face_selector_age_range_slider': '人脸选择年龄范围',
			'face_selector_gender_dropdown': '人脸选择性别',
			'face_selector_mode_dropdown': '人脸选择模式',
			'face_selector_order_dropdown': '人脸选择排序方式',
			'face_selector_race_dropdown': '人脸选择人种',
			'face_occluder_model_dropdown': '人脸遮挡模型',
			'face_parser_model_dropdown': '人脸解析模型',
			'voice_extractor_model_dropdown': '人声提取模型',
			'job_list_status_checkbox_group': '任务状态',
			'job_manager_job_action_dropdown': '任务操作',
			'job_manager_job_id_dropdown': '任务 ID',
			'job_manager_step_index_dropdown': '步骤索引',
			'job_runner_job_action_dropdown': '任务操作',
			'job_runner_job_id_dropdown': '任务 ID',
			'log_level_dropdown': '日志级别',
			'output_audio_encoder_dropdown': '输出音频编码器',
			'output_audio_quality_slider': '输出音频质量',
			'output_audio_volume_slider': '输出音频音量',
			'output_image_or_video': '输出',
			'output_image_quality_slider': '输出图像质量',
			'output_image_scale_slider': '输出图像缩放',
			'output_path_textbox': '输出路径',
			'output_video_encoder_dropdown': '输出视频编码器',
			'output_video_fps_slider': '输出视频帧率',
			'output_video_preset_dropdown': '输出视频预设',
			'output_video_quality_slider': '输出视频质量',
			'output_video_scale_slider': '输出视频缩放',
			'preview_frame_slider': '预览帧',
			'preview_image': '预览',
			'preview_mode_dropdown': '预览模式',
			'preview_resolution_dropdown': '预览分辨率',
			'processors_checkbox_group': '处理器',
			'reference_face_distance_slider': '参考人脸距离',
			'reference_face_gallery': '参考人脸',
			'refresh_button': '刷新',
			'source_file': '源文件',
			'start_button': '开始',
			'stop_button': '停止',
			'system_memory_limit_slider': '系统内存限制',
			'target_file': '目标文件',
			'temp_frame_format_dropdown': '临时帧格式',
			'terminal_textbox': '终端',
			'trim_frame_slider': '裁剪帧',
			'ui_workflow': 'UI 工作流',
			'video_memory_strategy_dropdown': '显存策略',
			'webcam_fps_slider': '摄像头帧率',
			'webcam_image': '摄像头',
			'webcam_device_id_dropdown': '摄像头设备 ID',
			'webcam_mode_radio': '摄像头模式',
			'webcam_resolution_dropdown': '摄像头分辨率',
			'processor':
			{
				'age_modifier': 'age_modifier（年龄修改 - 调节面部年龄）',
				'background_remover': 'background_remover（背景移除 - 移除或替换背景）',
				'deep_swapper': 'deep_swapper（深度换脸 - 基于深度学习的 AI 换脸）',
				'expression_restorer': 'expression_restorer（表情恢复 - 还原自然表情）',
				'face_debugger': 'face_debugger（面部调试 - 显示检测调试信息）',
				'face_editor': 'face_editor（面部编辑 - 精细调整五官）',
				'face_enhancer': 'face_enhancer（面部增强 - 提升面部画质）',
				'face_swapper': 'face_swapper（换脸 - 将源人脸替换到目标图像/视频中）',
				'frame_colorizer': 'frame_colorizer（帧上色 - 为黑白图像自动上色）',
				'frame_enhancer': 'frame_enhancer（帧增强 - 超分辨率提升画质）',
				'lip_syncer': 'lip_syncer（唇形同步 - 根据音频驱动嘴型）'
			}
		},
		'choices':
		{
			'face_mask_type':
			{
				'box': '方形（整体面部方形区域掩码）',
				'occlusion': '遮挡（自动检测并排除遮挡物，如手、头发等）',
				'area': '区域（自定义面部区域掩码）',
				'region': '分区（按五官分区进行精确控制）'
			},
			'face_mask_area':
			{
				'upper-face': '上半脸（额头、眉骨区域）',
				'lower-face': '下半脸（鼻子以下区域）',
				'mouth': '嘴部（嘴唇及周围区域）'
			},
			'face_mask_region':
			{
				'skin': '皮肤',
				'left-eyebrow': '左眉毛',
				'right-eyebrow': '右眉毛',
				'left-eye': '左眼',
				'right-eye': '右眼',
				'glasses': '眼镜',
				'nose': '鼻子',
				'mouth': '嘴巴',
				'upper-lip': '上嘴唇',
				'lower-lip': '下嘴唇'
			},
			'face_selector_mode':
			{
				'many': '多人（同时处理所有检测到的人脸）',
				'one': '单人（只处理一张人脸）',
				'reference': '参考（根据参考人脸进行跟踪）'
			},
			'face_selector_order':
			{
				'left-right': '从左到右',
				'right-left': '从右到左',
				'top-bottom': '从上到下',
				'bottom-top': '从下到上',
				'small-large': '从小到大',
				'large-small': '从大到小',
				'best-worst': '从最佳到最差',
				'worst-best': '从最差到最佳'
			},
			'gender':
			{
				'none': '无',
				'female': '女性',
				'male': '男性'
			},
			'race':
			{
				'none': '无',
				'white': '白种人',
				'black': '黑种人',
				'latino': '拉丁裔',
				'asian': '亚裔',
				'indian': '印度裔',
				'arabic': '阿拉伯裔'
			},
			'face_detector_model':
			{
				'many': '多模型（同时使用多种检测器）',
				'retinaface': 'RetinaFace（高精度人脸检测器）',
				'scrfd': 'SCRFD（轻量级快速人脸检测器）',
				'yolo_face': 'YOLO Face（YOLO系列检测器）',
				'yunet': 'YuNet（ ultra-lightweight 检测器）'
			},
			'face_landmarker_model':
			{
				'many': '多模型（同时使用多种特征点检测器）',
				'2dfan4': '2DFAN4（2D 面部特征点检测）',
				'peppa_wutz': 'Peppa Wutz（轻量级特征点检测）'
			},
			'face_occluder_model':
			{
				'many': '多模型（同时使用多种遮挡检测器）',
				'xseg_1': 'XSEG 1（遮挡区域分割模型）',
				'xseg_2': 'XSEG 2（遮挡区域分割模型 V2）',
				'xseg_3': 'XSEG 3（遮挡区域分割模型 V3）'
			},
			'face_parser_model':
			{
				'bisenet_resnet_18': 'BiSeNet ResNet18（轻量级面部解析器）',
				'bisenet_resnet_34': 'BiSeNet ResNet34（更精确的面部解析器）'
			},
			'voice_extractor_model':
			{
				'kim_vocal_1': 'Kim Vocal 1（人声分离模型 V1）',
				'kim_vocal_2': 'Kim Vocal 2（人声分离模型 V2）',
				'uvr_mdxnet': 'UVR MDXNet（Universal Voice Remover 模型）'
			},
			'temp_frame_format':
			{
				'bmp': 'BMP（无损位图格式）',
				'jpeg': 'JPEG（有损压缩格式）',
				'png': 'PNG（无损压缩格式）',
				'tiff': 'TIFF（无损标签图像格式）'
			},
			'video_memory_strategy':
			{
				'strict': '严格（最小显存占用，适合小显存显卡）',
				'moderate': '适中（平衡显存占用和性能）',
				'tolerant': '宽松（优先性能，占用更多显存）'
			},
			'log_level':
			{
				'error': '错误（仅显示错误信息）',
				'warn': '警告（显示错误和警告）',
				'info': '信息（显示详细处理进度）',
				'debug': '调试（显示所有调试信息）'
			},
			'benchmark_mode':
			{
				'warm': '热启动（使用已缓存的模型进行基准测试）',
				'cold': '冷启动（从零加载模型进行基准测试）'
			},
			'ui_workflow':
			{
				'instant_runner': '即时运行（直接处理，不保存任务）',
				'job_runner': '任务管理（创建并运行可管理的任务）',
				'job_manager': '高级管理（多步骤任务编排和编排）'
			},
			'job_status':
			{
				'drafted': '草稿（已创建但未提交）',
				'queued': '排队中（等待执行）',
				'completed': '已完成',
				'failed': '已失败'
			},
			'job_manager_action':
			{
				'job-create': '创建任务（新建一个草稿任务）',
				'job-submit': '提交任务（将草稿提交到执行队列）',
				'job-delete': '删除任务（删除一个或多个任务）',
				'job-add-step': '添加步骤（向任务添加新的处理步骤）',
				'job-remix-step': '混合步骤（基于已有步骤进行混合）',
				'job-insert-step': '插入步骤（在指定位置插入步骤）',
				'job-remove-step': '移除步骤（从任务中移除步骤）'
			},
			'job_runner_action':
			{
				'job-run': '运行任务（执行单个排队任务）',
				'job-run-all': '运行所有任务（执行所有排队任务）',
				'job-retry': '重试任务（重新执行失败任务）',
				'job-retry-all': '重试所有任务（重新执行所有失败任务）'
			},
			'common_option':
			{
				'keep-temp': '保留临时文件（处理完成后不删除临时资源）'
			},
			'preview_mode':
			{
				'default': '默认（标准预览模式）',
				'frame-by-frame': '逐帧（逐帧预览处理效果）',
				'face-by-face': '逐脸（逐张人脸预览处理效果）'
			},
			'webcam_mode':
			{
				'inline': '内联（在界面中直接显示摄像头画面）',
				'udp': 'UDP（通过 UDP 协议串流摄像头画面）',
				'v4l2': 'V4L2（通过 Video4Linux2 协议输出）'
			},
			'execution_provider':
			{
				'cuda': 'CUDA（NVIDIA GPU 加速）',
				'tensorrt': 'TensorRT（NVIDIA 深度学习推理优化）',
				'rocm': 'ROCm（AMD GPU 加速）',
				'migraphx': 'MIGraphX（AMD MIGraphX 推理）',
				'coreml': 'Core ML（Apple 设备推理）',
				'openvino': 'OpenVINO（Intel 硬件推理）',
				'qnn': 'QNN（Qualcomm AI 推理）',
				'directml': 'DirectML（Windows 通用 GPU 加速）',
				'cpu': 'CPU（使用 CPU 进行推理）'
			},
			'download_provider':
			{
				'github': 'GitHub（从 GitHub Releases 下载）',
				'huggingface': 'Hugging Face（从 Hugging Face Hub 下载）'
			},
			'face_debugger_item':
			{
				'bounding-box': '边界框（显示人脸检测框位置）',
				'face-landmark-5': '5 点特征（标记 5 个面部关键点）',
				'face-landmark-5/68': '5/68 点特征（同时显示 5 点和 68 点特征）',
				'face-landmark-68': '68 点特征（标记 68 个面部关键点）',
				'face-landmark-68/5': '68/5 点特征（同时显示 68 点和 5 点特征）',
				'face-mask': '面部掩码（显示面部区域掩码）'
			},
			'expression_restorer_area':
			{
				'upper-face': '上半脸',
				'lower-face': '下半脸'
			},
			'background_remover_color':
			{
				'red': '红色',
				'green': '绿色',
				'blue': '蓝色',
				'black': '黑色',
				'white': '白色',
				'alpha': '透明'
			},
			'output_video_preset':
			{
				'ultrafast': 'Ultrafast（最快处理速度，文件较大）',
				'superfast': 'Superfast（超快速处理）',
				'veryfast': 'VeryFast（很快）',
				'faster': 'Faster（较快）',
				'fast': 'Fast（快速）',
				'medium': 'Medium（平衡速度和质量，默认）',
				'slow': 'Slow（较慢，质量更好）',
				'slower': 'Slower（慢速，高质量）',
				'veryslow': 'VerySlow（最慢，最佳质量）'
			},
			'age_modifier_model':
			{
				'styleganex_age': 'StyleGANEx Age（基于 StyleGAN 的年龄修改模型）'
			},
			'background_remover_model':
			{
				'ben_2': 'BEN v2（Background Eraser V2，通用背景移除）',
				'birefnet_general': 'BiRefNet General（通用高精度背景移除）',
				'birefnet_portrait': 'BiRefNet Portrait（人像优化背景移除）',
				'isnet_general': 'ISNet General（通用实例分割背景移除）',
				'modnet': 'MODNet（实时人像抠图，适合直播场景）',
				'ormbg': 'ORMBG（对象识别背景移除）',
				'rmbg_1.4': 'RMBG 1.4（背景移除 V1.4，速度快）',
				'rmbg_2.0': 'RMBG 2.0（背景移除 V2.0，精度更高）',
				'silueta': 'Silueta（剪影优化背景移除）',
				'u2net_cloth': 'U2Net Cloth（服装场景专用抠图）',
				'u2net_general': 'U2Net General（通用 U2Net 背景移除）',
				'u2net_human': 'U2Net Human（人像专用 U2Net 抠图）',
				'u2netp': 'U2Netp（轻量版 U2Net，速度快）'
			},
			'face_editor_model':
			{
				'live_portrait': 'Live Portrait（基于肖像的实时面部编辑）'
			},
			'face_enhancer_model':
			{
				'codeformer': 'CodeFormer（基于 Transformer 的面部修复）',
				'gfpgan_1.2': 'GFPGAN 1.2（生成式面部修复 V1.2）',
				'gfpgan_1.3': 'GFPGAN 1.3（生成式面部修复 V1.3）',
				'gfpgan_1.4': 'GFPGAN 1.4（生成式面部修复 V1.4）',
				'gpen_bfr_256': 'GPEN BFR 256（256x256 盲人脸修复）',
				'gpen_bfr_512': 'GPEN BFR 512（512x512 盲人脸修复）',
				'gpen_bfr_1024': 'GPEN BFR 1024（1024x1024 高清晰度人脸修复）',
				'gpen_bfr_2048': 'GPEN BFR 2048（2048x2048 超高清人脸修复）',
				'restoreformer_plus_plus': 'RestoreFormer++（增强版面部修复，保留细节）'
			},
			'face_swapper_model':
			{
				'blendswap_256': 'BlendSwap 256（混合风格换脸）',
				'ghost_1_256': 'Ghost 1 256（轻量级换脸 V1）',
				'ghost_2_256': 'Ghost 2 256（轻量级换脸 V2）',
				'ghost_3_256': 'Ghost 3 256（轻量级换脸 V3）',
				'hififace_unofficial_256': 'HiFiFace 256（高保真换脸，非官方）',
				'hyperswap_1a_256': 'HyperSwap 1A 256（高性能换脸 V1A）',
				'hyperswap_1b_256': 'HyperSwap 1B 256（高性能换脸 V1B）',
				'hyperswap_1c_256': 'HyperSwap 1C 256（高性能换脸 V1C）',
				'inswapper_128': 'InsSwapper 128（基于 InsightFace 的经典换脸）',
				'inswapper_128_fp16': 'InsSwapper 128 FP16（FP16 加速版，更快）',
				'simswap_256': 'SimSwap 256（可模拟任意人脸的换脸）',
				'simswap_unofficial_512': 'SimSwap 512（512x512 高清非官方版）',
				'uniface_256': 'UniFace 256（通用统一换脸模型）'
			},
			'frame_colorizer_model':
			{
				'ddcolor': 'DDColor（基础版色彩恢复）',
				'ddcolor_artistic': 'DDColor Artistic（艺术风格色彩恢复）',
				'deoldify': 'DeOldify（经典版 AI 上色）',
				'deoldify_artistic': 'DeOldify Artistic（艺术风格 AI 上色）',
				'deoldify_stable': 'DeOldify Stable（稳定版 AI 上色，画面更连贯）'
			},
			'frame_enhancer_model':
			{
				'clear_reality_x4': 'Clear Reality X4（清晰真实风格超分辨率）',
				'face_dat_x4': 'Face DAT X4（面部专用 DAT 超分辨率）',
				'lsdir_x4': 'LSDir X4（轻量快速超分辨率）',
				'nomos8k_sc_x4': 'Nomos8K SC X4（8K 级超分辨率）',
				'real_esrgan_x2': 'Real-ESRGAN X2（2倍超分辨率，保留真实细节）',
				'real_esrgan_x2_fp16': 'Real-ESRGAN X2 FP16（2倍 FP16 加速版）',
				'real_esrgan_x4': 'Real-ESRGAN X4（4倍超分辨率，经典款）',
				'real_esrgan_x4_fp16': 'Real-ESRGAN X4 FP16（4倍 FP16 加速版）',
				'real_esrgan_x8': 'Real-ESRGAN X8（8倍超分辨率，高放大倍率）',
				'real_esrgan_x8_fp16': 'Real-ESRGAN X8 FP16（8倍 FP16 加速版）',
				'real_hatgan_x4': 'Real-HATGAN X4（HATGAN 架构超分辨率）',
				'real_web_photo_x4': 'Real Web Photo X4（网络照片优化超分辨率）',
				'realistic_rescaler_x4': 'Realistic Rescaler X4（逼真缩放超分辨率）',
				'remacri_x4': 'Remacri X4（增强型纹理超分辨率）',
				'siax_x4': 'SiaX X4（SiaX 架构超分辨率）',
				'span_kendata_x4': 'SPAN KendaTa X4（SPAN 架构超分辨率）',
				'swin2_sr_x4': 'Swin2 SR X4（Swin Transformer 超分辨率）',
				'tghq_face_x8': 'TGHQ Face X8（腾讯高质量人脸超分辨率）',
				'ultra_sharp_x4': 'Ultra Sharp X4（极致清晰超分辨率）',
				'ultra_sharp_2_x4': 'Ultra Sharp 2 X4（第二代极致清晰超分辨率）'
			},
			'lip_syncer_model':
			{
				'edtalk_256': 'EDTalk 256（高效对口唇形驱动）',
				'wav2lip_96': 'Wav2Lip 96（经典音频到唇形同步）',
				'wav2lip_gan_96': 'Wav2Lip GAN 96（GAN 增强版唇形同步，更逼真）'
			}
		}
	},
	'en':
	{
		'conda_not_activated': 'conda is not activated',
		'python_not_supported': 'python version is not supported, upgrade to {version} or higher',
		'curl_not_installed': 'curl is not installed',
		'ffmpeg_not_installed': 'ffmpeg is not installed',
		'creating_temp': 'creating temporary resources',
		'extracting_frames': 'extracting frames with a resolution of {resolution} and {fps} frames per second',
		'extracting_frames_succeeded': 'extracting frames succeeded',
		'extracting_frames_failed': 'extracting frames failed',
		'analysing': 'analysing',
		'extracting': 'extracting',
		'streaming': 'streaming',
		'processing': 'processing',
		'merging': 'merging',
		'downloading': 'downloading',
		'temp_frames_not_found': 'temporary frames not found',
		'copying_image': 'copying image with a resolution of {resolution}',
		'copying_image_succeeded': 'copying image succeeded',
		'copying_image_failed': 'copying image failed',
		'finalizing_image': 'finalizing image with a resolution of {resolution}',
		'finalizing_image_succeeded': 'finalizing image succeeded',
		'finalizing_image_skipped': 'finalizing image skipped',
		'merging_video': 'merging video with a resolution of {resolution} and {fps} frames per second',
		'merging_video_succeeded': 'merging video succeeded',
		'merging_video_failed': 'merging video failed',
		'skipping_audio': 'skipping audio',
		'replacing_audio_succeeded': 'replacing audio succeeded',
		'replacing_audio_skipped': 'replacing audio skipped',
		'restoring_audio_succeeded': 'restoring audio succeeded',
		'restoring_audio_skipped': 'restoring audio skipped',
		'clearing_temp': 'clearing temporary resources',
		'processing_stopped': 'processing stopped',
		'processing_image_succeeded': 'processing to image succeeded in {seconds} seconds',
		'processing_image_failed': 'processing to image failed',
		'processing_video_succeeded': 'processing to video succeeded in {seconds} seconds',
		'processing_video_failed': 'processing to video failed',
		'choose_image_source': 'choose an image for the source',
		'choose_audio_source': 'choose an audio for the source',
		'choose_video_target': 'choose a video for the target',
		'choose_image_or_video_target': 'choose an image or video for the target',
		'specify_image_or_video_output': 'specify the output image or video within a directory',
		'match_target_and_output_extension': 'match the target and output extension',
		'no_source_face_detected': 'no source face detected',
		'processor_not_loaded': 'processor {processor} could not be loaded',
		'processor_not_implemented': 'processor {processor} not implemented correctly',
		'ui_layout_not_loaded': 'ui layout {ui_layout} could not be loaded',
		'ui_layout_not_implemented': 'ui layout {ui_layout} not implemented correctly',
		'stream_not_loaded': 'stream {stream_mode} could not be loaded',
		'stream_not_supported': 'stream not supported',
		'job_created': 'job {job_id} created',
		'job_not_created': 'job {job_id} not created',
		'job_submitted': 'job {job_id} submitted',
		'job_not_submitted': 'job {job_id} not submitted',
		'job_all_submitted': 'jobs submitted',
		'job_all_not_submitted': 'jobs not submitted',
		'job_deleted': 'job {job_id} deleted',
		'job_not_deleted': 'job {job_id} not deleted',
		'job_all_deleted': 'jobs deleted',
		'job_all_not_deleted': 'jobs not deleted',
		'job_step_added': 'step added to job {job_id}',
		'job_step_not_added': 'step not added to job {job_id}',
		'job_remix_step_added': 'step {step_index} remixed from job {job_id}',
		'job_remix_step_not_added': 'step {step_index} not remixed from job {job_id}',
		'job_step_inserted': 'step {step_index} inserted to job {job_id}',
		'job_step_not_inserted': 'step {step_index} not inserted to job {job_id}',
		'job_step_removed': 'step {step_index} removed from job {job_id}',
		'job_step_not_removed': 'step {step_index} not removed from job {job_id}',
		'running_job': 'running queued job {job_id}',
		'running_jobs': 'running all queued jobs',
		'retrying_job': 'retrying failed job {job_id}',
		'retrying_jobs': 'retrying all failed jobs',
		'processing_job_succeeded': 'processing of job {job_id} succeeded',
		'processing_jobs_succeeded': 'processing of all jobs succeeded',
		'processing_job_failed': 'processing of job {job_id} failed',
		'processing_jobs_failed': 'processing of all jobs failed',
		'processing_step': 'processing step {step_current} of {step_total}',
		'validating_hash_succeeded': 'validating hash for {hash_file_name} succeeded',
		'validating_hash_failed': 'validating hash for {hash_file_name} failed',
		'validating_source_succeeded': 'validating source for {source_file_name} succeeded',
		'validating_source_failed': 'validating source for {source_file_name} failed',
		'deleting_corrupt_source': 'deleting corrupt source for {source_file_name}',
		'loading_model_succeeded': 'loading model {model_name} succeeded in {seconds} seconds',
		'loading_model_failed': 'loading model {model_name} failed',
		'time_ago_now': 'just now',
		'time_ago_minutes': '{minutes} minutes ago',
		'time_ago_hours': '{hours} hours and {minutes} minutes ago',
		'time_ago_days': '{days} days, {hours} hours and {minutes} minutes ago',
		'point': '.',
		'comma': ',',
		'colon': ':',
		'question_mark': '?',
		'exclamation_mark': '!',
		'help':
		{
			'install_dependency': 'choose the variant of {dependency} to install',
			'skip_conda': 'skip the conda environment check',
			'config_path': 'choose the config file to override defaults',
			'temp_path': 'specify the directory for the temporary resources',
			'jobs_path': 'specify the directory to store jobs',
			'source_paths': 'choose the image or audio paths',
			'target_path': 'choose the image or video path',
			'output_path': 'specify the image or video within a directory',
			'source_pattern': 'choose the image or audio pattern',
			'target_pattern': 'choose the image or video pattern',
			'output_pattern': 'specify the image or video pattern',
			'face_detector_model': 'choose the model responsible for detecting the faces',
			'face_detector_size': 'specify the frame size provided to the face detector',
			'face_detector_margin': 'apply top, right, bottom and left margin to the frame',
			'face_detector_angles': 'specify the angles to rotate the frame before detecting faces',
			'face_detector_score': 'filter the detected faces based on the confidence score',
			'face_landmarker_model': 'choose the model responsible for detecting the face landmarks',
			'face_landmarker_score': 'filter the detected face landmarks based on the confidence score',
			'face_selector_mode': 'use reference based tracking or simple matching',
			'face_selector_order': 'specify the order of the detected faces',
			'face_selector_age_start': 'filter the detected faces based on the starting age',
			'face_selector_age_end': 'filter the detected faces based on the ending age',
			'face_selector_gender': 'filter the detected faces based on their gender',
			'face_selector_race': 'filter the detected faces based on their race',
			'reference_face_position': 'specify the position used to create the reference face',
			'reference_face_distance': 'specify the similarity between the reference face and target face',
			'reference_frame_number': 'specify the frame used to create the reference face',
			'face_occluder_model': 'choose the model responsible for the occlusion mask',
			'face_parser_model': 'choose the model responsible for the region mask',
			'face_mask_types': 'mix and match different face mask types (choices: {choices})',
			'face_mask_areas': 'choose the items used for the area mask (choices: {choices})',
			'face_mask_regions': 'choose the items used for the region mask (choices: {choices})',
			'face_mask_blur': 'specify the degree of blur applied to the box mask',
			'face_mask_padding': 'apply top, right, bottom and left padding to the box mask',
			'voice_extractor_model': 'choose the model responsible for extracting the voices',
			'trim_frame_start': 'specify the starting frame of the target video',
			'trim_frame_end': 'specify the ending frame of the target video',
			'temp_frame_format': 'specify the temporary resources format',
			'keep_temp': 'keep the temporary resources after processing',
			'output_image_quality': 'specify the image quality which translates to the image compression',
			'output_image_scale': 'specify the image scale based on the target image',
			'output_audio_encoder': 'specify the encoder used for the audio',
			'output_audio_quality': 'specify the audio quality which translates to the audio compression',
			'output_audio_volume': 'specify the audio volume based on the target video',
			'output_video_encoder': 'specify the encoder used for the video',
			'output_video_preset': 'balance fast video processing and video file size',
			'output_video_quality': 'specify the video quality which translates to the video compression',
			'output_video_scale': 'specify the video scale based on the target video',
			'output_video_fps': 'specify the video fps based on the target video',
			'processors': 'load a single or multiple processors (choices: {choices}, ...)',
			'background-remover-model': 'choose the model responsible for removing the background',
			'background-remover-color': 'apply red, green blue and alpha values of the background',
			'open_browser': 'open the browser once the program is ready',
			'ui_layouts': 'launch a single or multiple UI layouts (choices: {choices}, ...)',
			'ui_workflow': 'choose the ui workflow',
			'preview_mode': 'choose the preview mode (choices: {choices})',
			'preview_resolution': 'choose the preview resolution (choices: {choices})',
			'download_providers': 'download using different providers (choices: {choices}, ...)',
			'download_scope': 'specify the download scope',
			'benchmark_mode': 'choose the benchmark mode',
			'benchmark_resolutions': 'choose the resolutions for the benchmarks (choices: {choices}, ...)',
			'benchmark_cycle_count': 'specify the amount of cycles per benchmark',
			'execution_device_ids': 'specify the devices used for processing',
			'execution_providers': 'inference using different providers (choices: {choices}, ...)',
			'execution_thread_count': 'specify the amount of parallel threads while processing',
			'video_memory_strategy': 'balance fast processing and low VRAM usage',
			'system_memory_limit': 'limit the available RAM that can be used while processing',
			'log_level': 'adjust the message severity displayed in the terminal',
			'halt_on_error': 'halt the program once an error occurred',
			'run': 'run the program',
			'headless_run': 'run the program in headless mode',
			'batch_run': 'run the program in batch mode',
			'force_download': 'force automate downloads and exit',
			'benchmark': 'benchmark the program',
			'job_id': 'specify the job id',
			'job_status': 'specify the job status',
			'step_index': 'specify the step index',
			'job_list': 'list jobs by status',
			'job_create': 'create a drafted job',
			'job_submit': 'submit a drafted job to become a queued job',
			'job_submit_all': 'submit all drafted jobs to become a queued jobs',
			'job_delete': 'delete a drafted, queued, failed or completed job',
			'job_delete_all': 'delete all drafted, queued, failed and completed jobs',
			'job_add_step': 'add a step to a drafted job',
			'job_remix_step': 'remix a previous step from a drafted job',
			'job_insert_step': 'insert a step to a drafted job',
			'job_remove_step': 'remove a step from a drafted job',
			'job_run': 'run a queued job',
			'job_run_all': 'run all queued jobs',
			'job_retry': 'retry a failed job',
			'job_retry_all': 'retry all failed jobs'
		},
		'about':
		{
			'fund': 'fund ai workstation',
			'subscribe': 'become a member',
			'join': 'join our community'
		},
		'uis':
		{
			'apply_button': 'APPLY',
			'benchmark_mode_dropdown': 'BENCHMARK MODE',
			'benchmark_cycle_count_slider': 'BENCHMARK CYCLE COUNT',
			'benchmark_resolutions_checkbox_group': 'BENCHMARK RESOLUTIONS',
			'clear_button': 'CLEAR',
			'common_options_checkbox_group': 'OPTIONS',
			'download_providers_checkbox_group': 'DOWNLOAD PROVIDERS',
			'execution_providers_checkbox_group': 'EXECUTION PROVIDERS',
			'execution_thread_count_slider': 'EXECUTION THREAD COUNT',
			'face_detector_angles_checkbox_group': 'FACE DETECTOR ANGLES',
			'face_detector_model_dropdown': 'FACE DETECTOR MODEL',
			'face_detector_margin_slider': 'FACE DETECTOR MARGIN',
			'face_detector_score_slider': 'FACE DETECTOR SCORE',
			'face_detector_size_dropdown': 'FACE DETECTOR SIZE',
			'face_landmarker_model_dropdown': 'FACE LANDMARKER MODEL',
			'face_landmarker_score_slider': 'FACE LANDMARKER SCORE',
			'face_mask_blur_slider': 'FACE MASK BLUR',
			'face_mask_padding_bottom_slider': 'FACE MASK PADDING BOTTOM',
			'face_mask_padding_left_slider': 'FACE MASK PADDING LEFT',
			'face_mask_padding_right_slider': 'FACE MASK PADDING RIGHT',
			'face_mask_padding_top_slider': 'FACE MASK PADDING TOP',
			'face_mask_areas_checkbox_group': 'FACE MASK AREAS',
			'face_mask_regions_checkbox_group': 'FACE MASK REGIONS',
			'face_mask_types_checkbox_group': 'FACE MASK TYPES',
			'face_selector_age_range_slider': 'FACE SELECTOR AGE',
			'face_selector_gender_dropdown': 'FACE SELECTOR GENDER',
			'face_selector_mode_dropdown': 'FACE SELECTOR MODE',
			'face_selector_order_dropdown': 'FACE SELECTOR ORDER',
			'face_selector_race_dropdown': 'FACE SELECTOR RACE',
			'face_occluder_model_dropdown': 'FACE OCCLUDER MODEL',
			'face_parser_model_dropdown': 'FACE PARSER MODEL',
			'voice_extractor_model_dropdown': 'VOICE EXTRACTOR MODEL',
			'job_list_status_checkbox_group': 'JOB STATUS',
			'job_manager_job_action_dropdown': 'JOB_ACTION',
			'job_manager_job_id_dropdown': 'JOB ID',
			'job_manager_step_index_dropdown': 'STEP INDEX',
			'job_runner_job_action_dropdown': 'JOB ACTION',
			'job_runner_job_id_dropdown': 'JOB ID',
			'log_level_dropdown': 'LOG LEVEL',
			'output_audio_encoder_dropdown': 'OUTPUT AUDIO ENCODER',
			'output_audio_quality_slider': 'OUTPUT AUDIO QUALITY',
			'output_audio_volume_slider': 'OUTPUT AUDIO VOLUME',
			'output_image_or_video': 'OUTPUT',
			'output_image_quality_slider': 'OUTPUT IMAGE QUALITY',
			'output_image_scale_slider': 'OUTPUT IMAGE SCALE',
			'output_path_textbox': 'OUTPUT PATH',
			'output_video_encoder_dropdown': 'OUTPUT VIDEO ENCODER',
			'output_video_fps_slider': 'OUTPUT VIDEO FPS',
			'output_video_preset_dropdown': 'OUTPUT VIDEO PRESET',
			'output_video_quality_slider': 'OUTPUT VIDEO QUALITY',
			'output_video_scale_slider': 'OUTPUT VIDEO SCALE',
			'preview_frame_slider': 'PREVIEW FRAME',
			'preview_image': 'PREVIEW',
			'preview_mode_dropdown': 'PREVIEW MODE',
			'preview_resolution_dropdown': 'PREVIEW RESOLUTION',
			'processors_checkbox_group': 'PROCESSORS',
			'reference_face_distance_slider': 'REFERENCE FACE DISTANCE',
			'reference_face_gallery': 'REFERENCE FACE',
			'refresh_button': 'REFRESH',
			'source_file': 'SOURCE',
			'start_button': 'START',
			'stop_button': 'STOP',
			'system_memory_limit_slider': 'SYSTEM MEMORY LIMIT',
			'target_file': 'TARGET',
			'temp_frame_format_dropdown': 'TEMP FRAME FORMAT',
			'terminal_textbox': 'TERMINAL',
			'trim_frame_slider': 'TRIM FRAME',
			'ui_workflow': 'UI WORKFLOW',
			'video_memory_strategy_dropdown': 'VIDEO MEMORY STRATEGY',
			'webcam_fps_slider': 'WEBCAM FPS',
			'webcam_image': 'WEBCAM',
			'webcam_device_id_dropdown': 'WEBCAM DEVICE ID',
			'webcam_mode_radio': 'WEBCAM MODE',
			'webcam_resolution_dropdown': 'WEBCAM RESOLUTION',
			'processor':
			{
				'age_modifier': 'age_modifier (adjust facial age)',
				'background_remover': 'background_remover (remove or replace background)',
				'deep_swapper': 'deep_swapper (deep learning face swapping)',
				'expression_restorer': 'expression_restorer (restore natural expressions)',
				'face_debugger': 'face_debugger (show detection debug info)',
				'face_editor': 'face_editor (fine-tune facial features)',
				'face_enhancer': 'face_enhancer (improve face image quality)',
				'face_swapper': 'face_swapper (swap source face onto target)',
				'frame_colorizer': 'frame_colorizer (auto-colorize B&W images/videos)',
				'frame_enhancer': 'frame_enhancer (super-resolution upscaling)',
				'lip_syncer': 'lip_syncer (audio-driven lip sync)'
			}
		},
		'choices':
		{
			'face_mask_type':
			{
				'box': 'Box (overall face box mask)',
				'occlusion': 'Occlusion (detect and exclude occlusions like hands, hair)',
				'area': 'Area (custom face area mask)',
				'region': 'Region (fine-grained per-feature region mask)'
			},
			'face_mask_area':
			{
				'upper-face': 'Upper Face (forehead and brow area)',
				'lower-face': 'Lower Face (below the nose)',
				'mouth': 'Mouth (lips and surrounding area)'
			},
			'face_mask_region':
			{
				'skin': 'Skin',
				'left-eyebrow': 'Left Eyebrow',
				'right-eyebrow': 'Right Eyebrow',
				'left-eye': 'Left Eye',
				'right-eye': 'Right Eye',
				'glasses': 'Glasses',
				'nose': 'Nose',
				'mouth': 'Mouth',
				'upper-lip': 'Upper Lip',
				'lower-lip': 'Lower Lip'
			},
			'face_selector_mode':
			{
				'many': 'Many (process all detected faces)',
				'one': 'One (process a single face)',
				'reference': 'Reference (track based on reference face)'
			},
			'face_selector_order':
			{
				'left-right': 'Left to Right',
				'right-left': 'Right to Left',
				'top-bottom': 'Top to Bottom',
				'bottom-top': 'Bottom to Top',
				'small-large': 'Small to Large',
				'large-small': 'Large to Small',
				'best-worst': 'Best to Worst',
				'worst-best': 'Worst to Best'
			},
			'gender':
			{
				'none': 'None',
				'female': 'Female',
				'male': 'Male'
			},
			'race':
			{
				'none': 'None',
				'white': 'White',
				'black': 'Black',
				'latino': 'Latino',
				'asian': 'Asian',
				'indian': 'Indian',
				'arabic': 'Arabic'
			},
			'face_detector_model':
			{
				'many': 'Many (use all detectors)',
				'retinaface': 'RetinaFace (high-precision face detector)',
				'scrfd': 'SCRFD (lightweight fast face detector)',
				'yolo_face': 'YOLO Face (YOLO-based detector)',
				'yunet': 'YuNet (ultra-lightweight detector)'
			},
			'face_landmarker_model':
			{
				'many': 'Many (use all landmark detectors)',
				'2dfan4': '2DFAN4 (2D facial landmark detection)',
				'peppa_wutz': 'Peppa Wutz (lightweight landmark detector)'
			},
			'face_occluder_model':
			{
				'many': 'Many (use all occlusion detectors)',
				'xseg_1': 'XSEG 1 (occlusion segmentation model)',
				'xseg_2': 'XSEG 2 (occlusion segmentation V2)',
				'xseg_3': 'XSEG 3 (occlusion segmentation V3)'
			},
			'face_parser_model':
			{
				'bisenet_resnet_18': 'BiSeNet ResNet18 (lightweight face parser)',
				'bisenet_resnet_34': 'BiSeNet ResNet34 (more accurate face parser)'
			},
			'voice_extractor_model':
			{
				'kim_vocal_1': 'Kim Vocal 1 (voice separation V1)',
				'kim_vocal_2': 'Kim Vocal 2 (voice separation V2)',
				'uvr_mdxnet': 'UVR MDXNet (Universal Voice Remover)'
			},
			'temp_frame_format':
			{
				'bmp': 'BMP (uncompressed bitmap)',
				'jpeg': 'JPEG (lossy compressed)',
				'png': 'PNG (lossless compressed)',
				'tiff': 'TIFF (lossless tagged image)'
			},
			'video_memory_strategy':
			{
				'strict': 'Strict (minimum VRAM, for low-end GPUs)',
				'moderate': 'Moderate (balance VRAM and performance)',
				'tolerant': 'Tolerant (prioritize performance, use more VRAM)'
			},
			'log_level':
			{
				'error': 'Error (show only errors)',
				'warn': 'Warn (show errors and warnings)',
				'info': 'Info (show processing progress)',
				'debug': 'Debug (show all debug info)'
			},
			'benchmark_mode':
			{
				'warm': 'Warm (benchmark with cached models)',
				'cold': 'Cold (benchmark with fresh model loads)'
			},
			'ui_workflow':
			{
				'instant_runner': 'Instant Runner (process directly without saving tasks)',
				'job_runner': 'Job Runner (create and manage tasks)',
				'job_manager': 'Job Manager (advanced multi-step task orchestration)'
			},
			'job_status':
			{
				'drafted': 'Drafted (created but not submitted)',
				'queued': 'Queued (waiting to execute)',
				'completed': 'Completed',
				'failed': 'Failed'
			},
			'job_manager_action':
			{
				'job-create': 'Create Task (new drafted job)',
				'job-submit': 'Submit Task (queue a drafted job)',
				'job-delete': 'Delete Task (remove one or more jobs)',
				'job-add-step': 'Add Step (append a processing step)',
				'job-remix-step': 'Remix Step (mix from an existing step)',
				'job-insert-step': 'Insert Step (insert at a specific position)',
				'job-remove-step': 'Remove Step (delete a step from job)'
			},
			'job_runner_action':
			{
				'job-run': 'Run Task (execute a single queued job)',
				'job-run-all': 'Run All Tasks (execute all queued jobs)',
				'job-retry': 'Retry Task (re-run a failed job)',
				'job-retry-all': 'Retry All Tasks (re-run all failed jobs)'
			},
			'common_option':
			{
				'keep-temp': 'Keep Temp (do not delete temporary resources after processing)'
			},
			'preview_mode':
			{
				'default': 'Default (standard preview)',
				'frame-by-frame': 'Frame by Frame (preview each processed frame)',
				'face-by-face': 'Face by Face (preview each face individually)'
			},
			'webcam_mode':
			{
				'inline': 'Inline (display webcam feed in the UI)',
				'udp': 'UDP (stream via UDP protocol)',
				'v4l2': 'V4L2 (output via Video4Linux2)'
			},
			'execution_provider':
			{
				'cuda': 'CUDA (NVIDIA GPU acceleration)',
				'tensorrt': 'TensorRT (NVIDIA deep learning inference)',
				'rocm': 'ROCm (AMD GPU acceleration)',
				'migraphx': 'MIGraphX (AMD MIGraphX inference)',
				'coreml': 'Core ML (Apple device inference)',
				'openvino': 'OpenVINO (Intel hardware inference)',
				'qnn': 'QNN (Qualcomm AI inference)',
				'directml': 'DirectML (Windows generic GPU acceleration)',
				'cpu': 'CPU (CPU-based inference)'
			},
			'download_provider':
			{
				'github': 'GitHub (download from GitHub Releases)',
				'huggingface': 'Hugging Face (download from Hugging Face Hub)'
			},
			'face_debugger_item':
			{
				'bounding-box': 'Bounding Box (show face detection boxes)',
				'face-landmark-5': '5-Point Landmark (mark 5 facial keypoints)',
				'face-landmark-5/68': '5/68-Point Landmark (show both 5 and 68 point landmarks)',
				'face-landmark-68': '68-Point Landmark (mark 68 facial keypoints)',
				'face-landmark-68/5': '68/5-Point Landmark (show both 68 and 5 point landmarks)',
				'face-mask': 'Face Mask (show face region mask)'
			},
			'expression_restorer_area':
			{
				'upper-face': 'Upper Face',
				'lower-face': 'Lower Face'
			},
			'background_remover_color':
			{
				'red': 'Red',
				'green': 'Green',
				'blue': 'Blue',
				'black': 'Black',
				'white': 'White',
				'alpha': 'Alpha (Transparent)'
			},
			'output_video_preset':
			{
				'ultrafast': 'Ultrafast (fastest processing, larger file)',
				'superfast': 'Superfast (very fast processing)',
				'veryfast': 'Very Fast (quick processing)',
				'faster': 'Faster (faster processing)',
				'fast': 'Fast (quick processing)',
				'medium': 'Medium (balance speed and quality, default)',
				'slow': 'Slow (slower, better quality)',
				'slower': 'Slower (slow, high quality)',
				'veryslow': 'Very Slow (slowest, best quality)'
			},
			'age_modifier_model':
			{
				'styleganex_age': 'StyleGANEx Age (StyleGAN-based age modification)'
			},
			'background_remover_model':
			{
				'ben_2': 'BEN v2 (Background Eraser V2, general purpose)',
				'birefnet_general': 'BiRefNet General (high-precision general background removal)',
				'birefnet_portrait': 'BiRefNet Portrait (portrait-optimized background removal)',
				'isnet_general': 'ISNet General (instance segmentation background removal)',
				'modnet': 'MODNet (real-time portrait matting, ideal for live streaming)',
				'ormbg': 'ORMBG (object recognition background removal)',
				'rmbg_1.4': 'RMBG 1.4 (background removal V1.4, fast)',
				'rmbg_2.0': 'RMBG 2.0 (background removal V2.0, higher accuracy)',
				'silueta': 'Silueta (silhouette-optimized background removal)',
				'u2net_cloth': 'U2Net Cloth (clothing-specific matting)',
				'u2net_general': 'U2Net General (general U2Net background removal)',
				'u2net_human': 'U2Net Human (human-focused U2Net matting)',
				'u2netp': 'U2Netp (lightweight U2Net, fast)'
			},
			'face_editor_model':
			{
				'live_portrait': 'Live Portrait (real-time portrait-based face editing)'
			},
			'face_enhancer_model':
			{
				'codeformer': 'CodeFormer (Transformer-based face restoration)',
				'gfpgan_1.2': 'GFPGAN 1.2 (Generative Face Prior GAN V1.2)',
				'gfpgan_1.3': 'GFPGAN 1.3 (Generative Face Prior GAN V1.3)',
				'gfpgan_1.4': 'GFPGAN 1.4 (Generative Face Prior GAN V1.4)',
				'gpen_bfr_256': 'GPEN BFR 256 (256x256 Blind Face Restoration)',
				'gpen_bfr_512': 'GPEN BFR 512 (512x512 Blind Face Restoration)',
				'gpen_bfr_1024': 'GPEN BFR 1024 (1024x1024 High-Def Face Restoration)',
				'gpen_bfr_2048': 'GPEN BFR 2048 (2048x2048 Ultra HD Face Restoration)',
				'restoreformer_plus_plus': 'RestoreFormer++ (Enhanced face restoration with detail preservation)'
			},
			'face_swapper_model':
			{
				'blendswap_256': 'BlendSwap 256 (blended style face swapping)',
				'ghost_1_256': 'Ghost 1 256 (lightweight face swap V1)',
				'ghost_2_256': 'Ghost 2 256 (lightweight face swap V2)',
				'ghost_3_256': 'Ghost 3 256 (lightweight face swap V3)',
				'hififace_unofficial_256': 'HiFiFace 256 (high-fidelity face swap, unofficial)',
				'hyperswap_1a_256': 'HyperSwap 1A 256 (high-performance face swap V1A)',
				'hyperswap_1b_256': 'HyperSwap 1B 256 (high-performance face swap V1B)',
				'hyperswap_1c_256': 'HyperSwap 1C 256 (high-performance face swap V1C)',
				'inswapper_128': 'InsSwapper 128 (InsightFace-based classic face swap)',
				'inswapper_128_fp16': 'InsSwapper 128 FP16 (FP16 accelerated, faster)',
				'simswap_256': 'SimSwap 256 (simulates arbitrary face swapping)',
				'simswap_unofficial_512': 'SimSwap 512 (512x512 HD unofficial version)',
				'uniface_256': 'UniFace 256 (unified general face swap model)'
			},
			'frame_colorizer_model':
			{
				'ddcolor': 'DDColor (basic color restoration)',
				'ddcolor_artistic': 'DDColor Artistic (artistic style colorization)',
				'deoldify': 'DeOldify (classic AI colorization)',
				'deoldify_artistic': 'DeOldify Artistic (artistic style AI colorization)',
				'deoldify_stable': 'DeOldify Stable (stable version, smoother results)'
			},
			'frame_enhancer_model':
			{
				'clear_reality_x4': 'Clear Reality X4 (clear realistic super-resolution)',
				'face_dat_x4': 'Face DAT X4 (face-specific DAT super-resolution)',
				'lsdir_x4': 'LSDir X4 (lightweight fast super-resolution)',
				'nomos8k_sc_x4': 'Nomos8K SC X4 (8K-level super-resolution)',
				'real_esrgan_x2': 'Real-ESRGAN X2 (2x super-resolution, preserves real details)',
				'real_esrgan_x2_fp16': 'Real-ESRGAN X2 FP16 (2x FP16 accelerated)',
				'real_esrgan_x4': 'Real-ESRGAN X4 (4x super-resolution, classic)',
				'real_esrgan_x4_fp16': 'Real-ESRGAN X4 FP16 (4x FP16 accelerated)',
				'real_esrgan_x8': 'Real-ESRGAN X8 (8x super-resolution, high magnification)',
				'real_esrgan_x8_fp16': 'Real-ESRGAN X8 FP16 (8x FP16 accelerated)',
				'real_hatgan_x4': 'Real-HATGAN X4 (HATGAN architecture super-resolution)',
				'real_web_photo_x4': 'Real Web Photo X4 (web photo optimized super-resolution)',
				'realistic_rescaler_x4': 'Realistic Rescaler X4 (realistic scaling super-resolution)',
				'remacri_x4': 'Remacri X4 (enhanced texture super-resolution)',
				'siax_x4': 'SiaX X4 (SiaX architecture super-resolution)',
				'span_kendata_x4': 'SPAN KendaTa X4 (SPAN architecture super-resolution)',
				'swin2_sr_x4': 'Swin2 SR X4 (Swin Transformer super-resolution)',
				'tghq_face_x8': 'TGHQ Face X8 (Tencent high-quality face super-resolution)',
				'ultra_sharp_x4': 'Ultra Sharp X4 (ultra-sharp super-resolution)',
				'ultra_sharp_2_x4': 'Ultra Sharp 2 X4 (2nd gen ultra-sharp super-resolution)'
			},
			'lip_syncer_model':
			{
				'edtalk_256': 'EDTalk 256 (efficient audio-driven lip sync)',
				'wav2lip_96': 'Wav2Lip 96 (classic audio-to-lip synchronization)',
				'wav2lip_gan_96': 'Wav2Lip GAN 96 (GAN-enhanced lip sync, more realistic)'
			}
		}
	}
}
