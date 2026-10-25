from PIL import Image
from pathlib import Path
p=Path(r'C:\Users\saymo\.codex\generated_images\01a0fe5a-4065-7dc0-818c-9b4ef4fadb4e\exec-65bad7f5-a523-4618-a250-a14d122a59fa.png')
out=Path(r'C:\Users\saymo\Documents\Codex\2026-10-02\cr\outputs\laser-proceso-hero.jpg')
im=Image.open(p).convert('RGB'); w,h=im.size
# preserve original aspect and resize to 1600px wide
nw=1600; nh=round(h*nw/w); im=im.resize((nw,nh),Image.Resampling.LANCZOS)
im.save(out,'JPEG',quality=88,optimize=True,progressive=True)
print(im.size, out.stat().st_size)
