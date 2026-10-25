from PIL import Image, ImageDraw, ImageFont, ImageFilter
N=1200; S=2; W=H=N*S
im=Image.new('RGBA',(W,H),(8,11,16,255)); d=ImageDraw.Draw(im)
# subdued orbital hairlines
for rad,col in [(334,(30,42,50,255)),(347,(18,27,34,255))]:
 box=(W//2-rad*S,467*S-rad*S,W//2+rad*S,467*S+rad*S)
 if rad==334: d.ellipse(box,outline=col,width=2*S)
 else:
  for a in range(0,360,7): d.arc(box,a,a+2,fill=col,width=S)
# broad italic chrome monogram
font=ImageFont.truetype('C:/Windows/Fonts/arialbi.ttf',600*S)
mask=Image.new('L',(W,H),0); md=ImageDraw.Draw(mask); md.text((185*S,92*S),'S',font=font,fill=255,stroke_width=0)
mask=mask.filter(ImageFilter.MaxFilter(9))
# metal depth extrusion
extr=Image.new('RGBA',(W,H),(0,0,0,0)); ed=ImageDraw.Draw(extr)
for off in range(25,0,-1): ed.bitmap((off*S,off*S),mask,fill=(19+off,26+off,33+off,255))
im=Image.alpha_composite(im,extr.filter(ImageFilter.GaussianBlur(4*S)))
# subtle cool shadow glow
blur=mask.filter(ImageFilter.GaussianBlur(20*S)); halo=Image.new('RGBA',(W,H),(0,0,0,0)); halo.putalpha(blur.point(lambda a:int(a*.23))); col=Image.new('RGBA',(W,H),(98,149,177,0)); col.putalpha(halo.getchannel('A')); im=Image.alpha_composite(im,col)
# polished multi-band chrome gradient
metal=Image.new('RGBA',(W,H),(0,0,0,0)); px=metal.load(); stops=[(0,(252,255,255)),(.10,(106,119,130)),(.22,(250,253,255)),(.35,(93,105,116)),(.49,(244,249,252)),(.62,(128,140,151)),(.75,(247,251,254)),(.88,(105,118,129)),(1,(237,244,249))]
for y in range(H):
 t=y/H
 for j in range(len(stops)-1):
  if stops[j][0]<=t<=stops[j+1][0]:
   t0,c0=stops[j];t1,c1=stops[j+1];q=(t-t0)/(t1-t0); rgb=tuple(int(c0[k]*(1-q)+c1[k]*q) for k in range(3));break
 for x in range(W): px[x,y]=(*rgb,mask.getpixel((x,y)))
im=Image.alpha_composite(im,metal)
# brand descriptor
fd=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',25*S); text='STUDIO LASER'; dr=ImageDraw.Draw(im)
width=sum(dr.textlength(ch,font=fd) for ch in text)+14*S*(len(text)-1); x=(W-width)/2
for ch in text:
 dr.text((int(x),810*S),ch,font=fd,fill=(203,213,221,255));x+=dr.textlength(ch,font=fd)+14*S
dr.line((410*S,879*S,590*S,879*S),fill=(102,119,131,255),width=2*S)
im.convert('RGB').resize((1200,1200),Image.Resampling.LANCZOS).save(r'C:\Users\saymo\Documents\Codex\2026-10-02\cr\outputs\s-studio-laser-s-futurista.png')

