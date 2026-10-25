from PIL import Image
from pathlib import Path
src=Path(r'C:\Users\saymo\.codex\generated_images\01a0fe5a-4065-7dc0-818c-9b4ef4fadb4e')
out=Path(r'C:\Users\saymo\Documents\Codex\2026-10-02\cr\outputs')
files={
 'laser-industria.jpg':'exec-a5f9a5a0-dd08-4e58-9bb0-edd3c9f39d71.png',
 'laser-joyeria.jpg':'exec-137bf624-f638-48be-abf4-da505eaa6cc2.png',
 'laser-relojeria.jpg':'exec-67154966-dfd9-4e58-95b9-09fb2ab7f419.png',
 'laser-mascotas.jpg':'exec-f8a9f105-5270-497e-8266-9ed86d44d442.png',
 'laser-boligrafos.jpg':'exec-8fd26697-4d1e-4f84-b505-3e5932707705.png',
 'laser-hosteleria.jpg':'exec-dd6061cf-dd88-423e-ade1-3757e4c78c9b.png',
 'laser-hospital.jpg':'exec-9c79adaa-dc4f-436b-902b-a31125149602.png'}
for name,source in files.items():
 im=Image.open(src/source).convert('RGB')
 w,h=im.size
 target=4/3
 if w/h>target:
  nw=int(h*target); left=(w-nw)//2; im=im.crop((left,0,left+nw,h))
 else:
  nh=int(w/target); top=(h-nh)//2; im=im.crop((0,top,w,top+nh))
 im=im.resize((1100,825),Image.Resampling.LANCZOS)
 im.save(out/name,'JPEG',quality=88,optimize=True,progressive=True)
 print(name, (out/name).stat().st_size)
