from PIL import Image
from pathlib import Path
src=Path(r'C:\Users\saymo\.codex\generated_images\01a0fe5a-4065-7dc0-818c-9b4ef4fadb4e\exec-f1c8d179-bef0-4edc-b0f2-1c9cf8bd42e6.png')
out=Path(r'C:\Users\saymo\Documents\Codex\2026-10-02\cr\outputs\laser-premios-deporte.jpg')
im=Image.open(src).convert('RGB');w,h=im.size;target=4/3
if w/h>target:
 nw=int(h*target);l=(w-nw)//2;im=im.crop((l,0,l+nw,h))
else:
 nh=int(w/target);t=(h-nh)//2;im=im.crop((0,t,w,t+nh))
im.resize((1100,825),Image.Resampling.LANCZOS).save(out,'JPEG',quality=88,optimize=True,progressive=True)
print(im.size,out.stat().st_size)
