import pyinvisiblewatermark as ivwm

# 图片加水印示例
ivwm.extract_watermark(
    img_fp="data/encode.png",
    save_to="data/decode.png"
)
