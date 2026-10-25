from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
S=2; W,H=1200*S,960*S
im=Image.new('RGB',(W,H),(5,7,11))
layer=Image.new('RGBA',(W,H),(0,0,0,0))
d=ImageDraw.Draw(layer)
def p(x,y): return (int(x*S),int(y*S))
def cubic(a,b,c,e,n=60):
 out=[]
 for i in range(n+1):
  t=i/n; u=1-t
  out.append(p(u**3*a[0]+3*u*u*t*b[0]+3*u*t*t*c[0]+t**3*e[0],u**3*a[1]+3*u*u*t*b[1]+3*u*t*t*c[1]+t**3*e[1]))
 return out
# continuous S path
pts=[]
pts += [p(817,202),p(474,202)]
pts += cubic((474,202),(379,202),(320,254),(320,331))[1:]
pts += cubic((320,331),(320,395),(368,431),(454,455))[1:]
pts += [p(736,534)]
pts += cubic((736,534),(822,558),(870,594),(870,658))[1:]
pts += cubic((870,658),(870,735),(811,787),(716,787))[1:]
pts += [p(357,787)]
d.line(pts, fill=(0,229,255,225), width=18*S, joint='curve')
# white-hot laser core
core=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(core).line(pts,fill=(235,255,255,255),width=3*S,joint='curve')
# glow + crisp foreground
im=Image.alpha_composite(im.convert('RGBA'),layer.filter(ImageFilter.GaussianBlur(25*S)))
im=Image.alpha_composite(im,layer)
im=Image.alpha_composite(im,core.filter(ImageFilter.GaussianBlur(5*S)))
im=Image.alpha_composite(im,core)
# laser emitter
ld=ImageDraw.Draw(im)
ld.polygon([p(844,178),p(861,195),p(844,212),p(827,195)],fill=(8,21,26,255),outline=(114,247,255,255),width=2*S)
ld.ellipse((p(840,191),p(848,199)),fill=(244,255,255,255))
ld.line([p(839,185),p(832,178)],fill=(114,247,255,255),width=2*S)
ld.line([p(849,185),p(856,178)],fill=(114,247,255,255),width=2*S)
ld.line([p(853,195),p(864,195)],fill=(114,247,255,255),width=2*S)
# typography
fontpath='C:/Windows/Fonts/arial.ttf'; boldpath='C:/Windows/Fonts/arialbd.ttf'
def font(path,size): return ImageFont.truetype(path,size*S)
def centered_tracking(text,y,fnt,color,tracking):
 widths=[d.textlength(ch,font=fnt) for ch in text]
 total=sum(widths)+tracking*S*(len(text)-1); x=(W-total)/2
 dr=ImageDraw.Draw(im)
 for ch,w in zip(text,widths):
  dr.text((int(x),y*S),ch,font=fnt,fill=color,stroke_width=0)
  x+=w+tracking*S
centered_tracking('S STUDIO',864,font(boldpath,40),(243,247,252,255),15)
centered_tracking('LASER',914,font(fontpath,15),(97,239,255,255),12)
im.convert('RGB').resize((1200,900),Image.Resampling.LANCZOS).save(r'C:\Users\saymo\Documents\Codex\2026-10-02\cr\outputs\s-studio-laser-marca.png')



