# 华为设备序列号批量查询

> 用于批量查询华为设备序列号的脚本.

## 用法

clone此仓库, 确保本地安装有`Firefox`, `python3`.

安装依赖:

```shell
pip3 install selenium #模拟浏览器操作
pip3 install ddddocr  #识别验证码
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

最终结果将写入`success.json`, 但由于本地ocr识别验证码的不确定性, 加上网络的不稳定性, 一些序列号的结果将无法被查询到.

但无需担心, 失败的序列号将以列表的变量类型写入`error`文件, 只需打开此文件复制内容后, 替换`app.py`第十一行的`ids`变量, 再次运行即可.

> 注意再次运行前将`success.json`内的数据进行转移保存.

## 其他

本地验证码的识别实现:

[sml2h3/ddddocr](https://github.com/sml2h3/ddddocr)

json转excel表格:

[Online JSON to EXCEL Converter](https://products.aspose.app/cells/conversion/json-to-xlsx)