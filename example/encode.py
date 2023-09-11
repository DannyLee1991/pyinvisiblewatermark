import invisiblewatermark as ivwm

# 图片加水印示例
ivwm.generate_watermark(
    img_fp="data/origin.png",
    wm_txt="hello world!",
    save_to="data/encode.png",
    font="font/ZiTiQuanWeiJunHei-W1-2.ttf"
)
