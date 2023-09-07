from PIL import Image, ImageDraw, ImageFont
import random
import string


def generate_random_text(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

width, height = 200, 100
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

font = ImageFont.load_default()  
captcha_text = generate_random_text()
draw.text((20, 40), captcha_text, fill='black', font=font)

for _ in range(200):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    draw.point((x, y), fill='gray')

image.save('captcha.png')
image.show()
