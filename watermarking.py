from PIL import Image, ImageDraw, ImageFont

def add_watermark(image_path, text, position=(10, 10)):
    image = Image.open(image_path).convert("RGBA")
    watermark = Image.new("RGBA", image.size)
    draw = ImageDraw.Draw(watermark)

    # Choose a font (provide the path to a .ttf file)
    font = ImageFont.truetype("/content/sample_data/ARIAL.TTF", 40)
    draw.text(position, text, (255, 255, 255, 128), font=font)

    watermarked_image = Image.alpha_composite(image, watermark)
    watermarked_image.save("watermarked_image.png")

# Add watermark to the image
add_watermark("/content/sample_data/pngtype.jpeg", "Confidential", (50, 50))