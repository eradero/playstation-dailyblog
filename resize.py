from PIL import Image

img_path = 'frontend/public/images/playstation-rompe-el-silencio-sobre-el-drm-alivio-o-m-s-inc-gnitas-para-tu-ps5.png'
img = Image.open(img_path)

target_w = 1066
target_h = 600

new_h = 600
new_w = int(img.width * (new_h / img.height))
img_resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)

background = Image.new('RGBA', (target_w, target_h), (255, 255, 255, 0))
offset = ((target_w - new_w) // 2, (target_h - new_h) // 2)
background.paste(img_resized, offset)

background.save(img_path)
print("Resized successfully")
