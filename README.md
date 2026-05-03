FaceFusion CN
=============

> 行业领先的人脸操作平台 · 完整中文本地化版本

[![Build Status](https://img.shields.io/github/actions/workflow/status/facefusion/facefusion/ci.yml.svg?branch=master)](https://github.com/facefusion/facefusion/actions?query=workflow:ci)
[![Coverage Status](https://img.shields.io/coveralls/facefusion/facefusion.svg)](https://coveralls.io/r/facefusion/facefusion)
![License](https://img.shields.io/badge/license-OpenRAIL--AS-green)


CN 版本特性
-----------

本版本基于官方 [facefusion](https://github.com/facefusion/facefusion) 开发，针对中文用户做了以下改进：

### 1. 完整中文本地化

- 所有 UI 界面、菜单、按钮、提示信息均已翻译为中文
- 翻译不仅准确，还结合中文语境做了友好化处理，便于理解
- 默认启动即为中文界面，无需额外配置

### 2. NSFW 检测解除

- 移除了内容安全检测（NSFW）限制，解锁全部使用场景
- 不再对输入内容进行敏感内容拦截

### 3. WebUI 配置持久化

- 所有 WebUI 中的设置会自动保存，下次打开时自动恢复
- 状态保存在 `~/.facefusion/ui_state.json`，无需每次重新调整

> **提示：** 以上修改仅针对本仓库的本地副本，不影响官方原版 facefusion 项目。如需了解更多信息，请参阅 [facefusion 官方文档](https://docs.facefusion.io)。


Preview
-------

![Preview](https://raw.githubusercontent.com/facefusion/facefusion/master/.github/preview.png?sanitize=true)


Installation
------------

Be aware, the [installation](https://docs.facefusion.io/installation) needs technical skills and is not recommended for beginners. In case you are not comfortable using a terminal, our [Windows Installer](http://windows-installer.facefusion.io) and [macOS Installer](http://macos-installer.facefusion.io) get you started.


Usage
-----

Run the command:

```
python facefusion.py [commands] [options]

options:
  -h, --help                                      show this help message and exit
  -v, --version                                   show program's version number and exit

commands:
    run                                           run the program
    headless-run                                  run the program in headless mode
    batch-run                                     run the program in batch mode
    force-download                                force automate downloads and exit
    benchmark                                     benchmark the program
    job-list                                      list jobs by status
    job-create                                    create a drafted job
    job-submit                                    submit a drafted job to become a queued job
    job-submit-all                                submit all drafted jobs to become a queued jobs
    job-delete                                    delete a drafted, queued, failed or completed job
    job-delete-all                                delete all drafted, queued, failed and completed jobs
    job-add-step                                  add a step to a drafted job
    job-remix-step                                remix a previous step from a drafted job
    job-insert-step                               insert a step to a drafted job
    job-remove-step                               remove a step from a drafted job
    job-run                                       run a queued job
    job-run-all                                   run all queued jobs
    job-retry                                     retry a failed job
    job-retry-all                                 retry all failed jobs
```


Documentation
-------------

Read the [documentation](https://docs.facefusion.io) for a deep dive.
