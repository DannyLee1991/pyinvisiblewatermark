import typer
from .core import generate_watermark, extract_watermark

app = typer.Typer()


@app.command()
def encode(text: str, path, font=None, font_h: float = 0.025):
    """
    写入图片隐水印
    :param text: 水印文本
    :param path: 被添加水印的图片路径
    :param font: 水印字体 （如需渲染中文，请传入中文字体文件路径）
    :param font_h: 水印文本高度占图片高度百分比
    :return:
    """
    generate_watermark(img_fp=path, wm_txt=text, font=font, font_h=font_h)
    typer.echo("done!")


@app.command()
def decode(path: str, save_to: str = "decode.png", show: bool = False):
    """
    解码隐水印
    :param path: 被解码的图片路径
    :param save_to: 解码后的图片保存路径
    :param show: 是否直接展示结果图
    :return:
    """
    decode_img = extract_watermark(path, save_to)
    if show:
        decode_img.show("")


if __name__ == "__main__":
    app()
