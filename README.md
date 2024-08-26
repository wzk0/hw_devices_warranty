# 华为设备序列号批量查询

> 用于批量查询华为设备序列号的脚本.

## 用法

clone此仓库, 确保本地安装有`Firefox`, `python3`.

安装依赖:

```shell
pip3 install selenium # 模拟浏览器操作
pip3 install ddddocr  # 识别验证码
pip3 install openpyxl # 表格操作
pip3 install requests
```

以此指令启动`Firefox`

```shell
firefox.exe -marionette -start-debugger-server 2828
```

> 请将`firefox.exe`换成具体的文件位置.

随后运行`app.py`即可.

## 说明

经过多次测试, 目前程序内使用的休眠时间在网络相对稳定的情况下能够实现最快效率(吧).

> 差不多是1s查询一个.

每次查询完毕, 成功的结果将以`json`的格式保存至`outputs`文件夹, 失败的结果将保存至`error.xlsx`, 

只需将`error.xlsx`重命名为`base.xlsx`, 再重新运行`app.py`即可.

在查完(某次运行完发现`error.xlsx`为空或是发现剩下的序列号都无效时)后, 进入`outputs`文件夹, 运行`plus.py`即可将所有`json文件`合并导出至`all.xlsx`.

## 其他

本地验证码的识别实现:

[sml2h3/ddddocr](https://github.com/sml2h3/ddddocr)
