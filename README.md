# 图片隐水印生成/解码

复刻[https://invisiblewatermark.net/](https://invisiblewatermark.net/)的python版本实现。

算法原理，参见:[https://invisiblewatermark.net/how-invisible-watermarks-work](https://invisiblewatermark.net/how-invisible-watermarks-work)

## 安装

```
pip3 install invisiblewatermark
```

## 使用

### 命令行使用

```
# encode
ivwm encode "hello world!" $YOUR_IMAGE_PATH

# decode
ivwm decode $INPUT_IMAGE_PATH $OUTPUT_IMAGE_PATH
```

### 代码使用

```python
# encode
import invisiblewatermark as ivwm

ivwm.generate_watermark(
    img_fp="data/origin.png",
    wm_txt="hello world!",
    save_to="data/encode.png",
    font="font/ZiTiQuanWeiJunHei-W1-2.ttf"
)
```

```python
# decode
import invisiblewatermark as ivwm

# 图片加水印示例
ivwm.extract_watermark(
    img_fp="data/encode.png",
    save_to="data/decode.png"
)
```

## 效果示例

|原图|加水印图|水印解码图|水印文本|
|:-:|:-:|:-:|:-:|
|![](./docs/origin.png)|![](./docs/encode.png)|![](./docs/decode.png)|`hello world!`｜
