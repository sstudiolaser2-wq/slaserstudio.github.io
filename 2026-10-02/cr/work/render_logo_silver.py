from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H=1500,620; S=2; W*=S; H*=S
im=Image.new('RGB',(W,H),(8,11,16))
# subtle dark radial atmosphere
base=Image.new('RGBA',(W,H),(0,0,0,0)); bd=ImageDraw.Draw(base)
for r in range(600,0,-6):
 alpha=max(0,int(10*(1-r/600)))
 bd.ellipse((600*S-r*S,310*S-r*S,600*S+r*S,310*S+r*S),fill=(20,35,43,alpha))
im=Image.alpha_composite(im.convert('RGBA'),base)
# Heavy silver S with dark extrusion and mask
font=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',470*S)
mask=Image.new('L',(W,H),0); md=ImageDraw.Draw(mask); md.text((82*S,22*S),'S',font=font,fill=255,stroke_width=0)
# thicken the glyph for a bold, sculpted mark
mask=mask.filter(ImageFilter.MaxFilter(9))
# extrusion shadow layers
extr=Image.new('RGBA',(W,H),(0,0,0,0)); ed=ImageDraw.Draw(extr)
for off in range(22,0,-1): ed.bitmap((off*S,off*S),mask,fill=(20+off,28+off,37+off,255))
extr=extr.filter(ImageFilter.GaussianBlur(2*S)); im=Image.alpha_composite(im,extr)
# cast shadow glow
blur=mask.filter(ImageFilter.GaussianBlur(20*S)); glow=Image.new('RGBA',(W,H),(0,0,0,0)); glow.putalpha(blur.point(lambda a:int(a*.38))); glow.putdata([(37,215,125,a) for a in glow.getchannel('A').getdata()]); im=Image.alpha_composite(im,glow)
# metallic vertical gradient clipped to S
metal=Image.new('RGBA',(W,H),(0,0,0,0)); pix=metal.load(); stops=[(0,(255,255,255)),(.16,(151,163,174)),(.30,(247,251,255)),(.47,(92,103,114)),(.63,(226,234,240)),(.80,(124,136,148)),(1,(250,253,255))]
for y in range(H):
 t=y/H
 for i in range(len(stops)-1):
  if stops[i][0]<=t<=stops[i+1][0]:
   t0,c0=stops[i]; t1,c1=stops[i+1]; q=(t-t0)/(t1-t0)
   col=tuple(int(c0[k]*(1-q)+c1[k]*q) for k in range(3)); break
 for x in range(W): pix[x,y]=(*col,mask.getpixel((x,y)))
im=Image.alpha_composite(im,metal)
# bevel highlight along the silhouette
edge=mask.filter(ImageFilter.MinFilter(5)); rim=Image.eval(mask,lambda a:255 if a else 0)
edge=Image.eval(ImageChops.subtract(mask,edge),lambda a:min(255,a*2)) if False else None
# separator and wordmark
d=ImageDraw.Draw(im)
d.line((550*S,132*S,550*S,488*S),fill=(53,64,74,255),width=2*S)
regular=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',94*S)
bold=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',94*S)
d.text((635*S,185*S),'STUDIO',font=bold,fill=(244,247,250,255),stroke_width=0)
laserfont=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',32*S)
def tracked(txt,x,y,font,spacing,color):
 for ch in txt:
  d.text((x,y),ch,font=font,fill=color)
  x+=int(d.textlength(ch,font=font))+spacing*S
tracked('LASER',642*S,334*S,laserfont,18,(184,196,206,255))
# bright green neon rule
rule=Image.new('RGBA',(W,H),(0,0,0,0)); rd=ImageDraw.Draw(rule); rd.line((640*S,420*S,1220*S,420*S),fill=(102,255,0,255),width=4*S); rd.ellipse((1227*S,415*S,1237*S,425*S),fill=(0,245,138,255))
im=Image.alpha_composite(im,rule.filter(ImageFilter.GaussianBlur(10*S))); im=Image.alpha_composite(im,rule)
d=ImageDraw.Draw(im); d.line((640*S,439*S,880*S,439*S),fill=(108,120,130,150),width=S)
im.convert('RGB').resize((1500,620),Image.Resampling.LANCZOS).save(r'C:\Users\saymo\Documents\Codex\2026-10-02\cr\outputs\s-studio-laser-plata.png')
