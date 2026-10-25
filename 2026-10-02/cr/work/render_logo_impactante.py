from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H,S=1500,700,2; W*=S; H*=S
im=Image.new('RGBA',(W,H),(5,8,11,255))
# cinematic green ambient glow
ambient=Image.new('RGBA',(W,H),(0,0,0,0)); ad=ImageDraw.Draw(ambient)
ad.ellipse((50*S,70*S,650*S,650*S),fill=(0,255,90,55))
im=Image.alpha_composite(im,ambient.filter(ImageFilter.GaussianBlur(100*S)))
# laser streak behind the mark
streak=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(streak)
sd.line((65*S,555*S,520*S,145*S),fill=(0,255,94,230),width=9*S)
sd.line((72*S,548*S,512*S,152*S),fill=(219,255,63,255),width=3*S)
# radiant soft beam
im=Image.alpha_composite(im,streak.filter(ImageFilter.GaussianBlur(24*S))); im=Image.alpha_composite(im,streak)
# chrome S with deep extrusion
font=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',560*S)
mask=Image.new('L',(W,H),0); ImageDraw.Draw(mask).text((35*S,0),'S',font=font,fill=255,stroke_width=0)
mask=mask.filter(ImageFilter.MaxFilter(11))
extr=Image.new('RGBA',(W,H),(0,0,0,0)); ed=ImageDraw.Draw(extr)
for off in range(30,0,-1): ed.bitmap((off*S,off*S),mask,fill=(15+off,20+off,26+off,255))
im=Image.alpha_composite(im,extr.filter(ImageFilter.GaussianBlur(3*S)))
# Silver gradient bands clipped into glyph
metal=Image.new('RGBA',(W,H),(0,0,0,0)); pix=metal.load(); stops=[(0,(255,255,255)),(.10,(103,115,126)),(.23,(255,255,255)),(.35,(110,122,133)),(.50,(246,250,255)),(.65,(84,96,108)),(.80,(239,246,250)),(.92,(112,124,136)),(1,(250,255,255))]
for y in range(H):
 t=y/H
 for i in range(len(stops)-1):
  if stops[i][0]<=t<=stops[i+1][0]:
   t0,c0=stops[i]; t1,c1=stops[i+1]; q=(t-t0)/(t1-t0); col=tuple(int(c0[k]*(1-q)+c1[k]*q) for k in range(3)); break
 for x in range(W): pix[x,y]=(*col,mask.getpixel((x,y)))
im=Image.alpha_composite(im,metal)
# neon edge reflection
blur=mask.filter(ImageFilter.GaussianBlur(26*S)); glow=Image.new('RGBA',(W,H),(0,0,0,0)); glow.putalpha(blur.point(lambda a:int(a*.40))); tint=Image.new('RGBA',(W,H),(0,255,105,0)); tint.putalpha(glow.getchannel('A')); im=Image.alpha_composite(im,tint)
# redraw silver mark above glow
im=Image.alpha_composite(im,metal)
# divider and wordmark
d=ImageDraw.Draw(im)
d.line((599*S,122*S,599*S,577*S),fill=(54,65,74,255),width=2*S)
fb=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',116*S); d.text((690*S,211*S),'STUDIO',font=fb,fill=(247,250,252,255))
fr=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',36*S)
def tracked(text,x,y,spacing,col):
 for ch in text:
  d.text((x,y),ch,font=fr,fill=col); x+=int(d.textlength(ch,font=fr))+spacing*S
tracked('LASER',699*S,365*S,22,(174,185,194,255))
# green neon underline
beam=Image.new('RGBA',(W,H),(0,0,0,0)); bd=ImageDraw.Draw(beam); bd.line((696*S,477*S,1330*S,477*S),fill=(0,255,116,255),width=5*S); bd.ellipse((1337*S,470*S,1351*S,484*S),fill=(215,255,0,255))
im=Image.alpha_composite(im,beam.filter(ImageFilter.GaussianBlur(14*S))); im=Image.alpha_composite(im,beam)
d=ImageDraw.Draw(im); d.line((696*S,499*S,966*S,499*S),fill=(104,115,124,180),width=2*S)
im.convert('RGB').resize((1500,700),Image.Resampling.LANCZOS).save(r'C:\Users\saymo\Documents\Codex\2026-10-02\cr\outputs\s-studio-laser-impactante.png')
