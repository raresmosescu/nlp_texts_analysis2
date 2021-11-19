from PIL import Image, ImageDraw, ImageFont

def generate_by_dict(dict):
  height = 20
  for item in dict:
    height += 25
  
  img = Image.new('RGB', (300, height), color = (73, 109, 137))
  fnt = ImageFont.truetype('arial.ttf', 20)
  draw = ImageDraw.Draw(img)
  position = 10
  for item in dict:
    # print(item, dict[item])
    draw.text((10, position), f'{item}: {dict[item]}', font=fnt, fill=(255,255,0))
    position += 25
  
  img.save('core/static/text_analyzer_results.png')
