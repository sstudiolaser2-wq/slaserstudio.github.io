from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H,S=1500,900,2; W*=S; H*=S
im=Image.new('RGBA',(W,H),(5,7,10,255))
# atmospheric green and graphite vignette
amb=Image.new('RGBA',(W,H),(0,0,0,0)); ad=ImageDraw.Draw(amb); ad.ellipse((20*S,20*S,850*S,850*S),fill=(0,255,90,38)); im=Image.alpha_composite(im,amb.filter(ImageFilter.GaussianBlur(130*S)))
# faint diagonal technical framing lines
frame=Image.new('RGBA',(W,H),(0,0,0,0)); fd=ImageDraw.Draw(frame)
fd.line((70*S,735*S,300*S,735*S),fill=(44,56,60,255),width=2*S); fd.line((710*S,130*S,800*S,130*S),fill=(44,56,60,255),width=2*S)
im=Image.alpha_composite(im,frame)
# Oversized, italic chrome S
font=ImageFont.truetype('C:/Windows/Fonts/arialbi.ttf',660*S)
mask=Image.new('L',(W,H),0); ImageDraw.Draw(mask).text((30*S,48*S),'S',font=font,fill=255)
mask=mask.filter(ImageFilter.MaxFilter(11))
# heavy extrusion
extr=Image.new('RGBA',(W,H),(0,0,0,0)); exd=ImageDraw.Draw(extr)
for off in range(34,0,-1): exd.bitmap((off*S,off*S),mask,fill=(12+off,17+off,22+off,255))
im=Image.alpha_composite(im,extr.filter(ImageFilter.GaussianBlur(5*S)))
# cool chrome edge glow
blur=mask.filter(ImageFilter.GaussianBlur(28*S)); halo=Image.new('RGBA',(W,H),(0,0,0,0)); halo.putalpha(blur.point(lambda a:int(a*.40))); tint=Image.new('RGBA',(W,H),(0,235,120,0)); tint.putalpha(halo.getchannel('A')); im=Image.alpha_composite(im,tint)
# metallic reflective vertical bands
metal=Image.new('RGBA',(W,H),(0,0,0,0)); px=metal.load(); stops=[(0,(255,255,255)),(.09,(109,122,134)),(.2,(250,254,255)),(.32,(70,83,95)),(.48,(234,242,248)),(.61,(100,113,125)),(.76,(255,255,255)),(.88,(119,132,144)),(1,(232,242,249))]
for y in range(H):
 t=y/H
 for i in range(len(stops)-1):
  if stops[i][0]<=t<=stops[i+1][0]:
   t0,c0=stops[i];t1,c1=stops[i+1];q=(t-t0)/(t1-t0);rgb=tuple(int(c0[k]*(1-q)+c1[k]*q) for k in range(3));break
 for x in range(W): px[x,y]=(*rgb,mask.getpixel((x,y)))
im=Image.alpha_composite(im,metal)
# A sharp green laser slash cuts across the chrome mark
slash=Image.new('RGBA',(W,H),(0,0,0,0)); sd=ImageDraw.Draw(slash)
sd.line((95*S,654*S,748*S,155*S),fill=(0,255,105,255),width=9*S)
sd.line((110*S,641*S,733*S,165*S),fill=(223,255,85,255),width=3*S)
im=Image.alpha_composite(im,slash.filter(ImageFilter.GaussianBlur(25*S))); im=Image.alpha_composite(im,slash)
# tiny laser flare points
sd=ImageDraw.Draw(im); sd.polygon([(90*S,654*S),(110*S,640*S),(116*S,650*S),(98*S,666*S)],fill=(230,255,117,255)); sd.ellipse((740*S,147*S,758*S,165*S),fill=(238,255,190,255))
# Wordmark block
d=ImageDraw.Draw(im); d.line((850*S,165*S,850*S,705*S),fill=(47,59,65,255),width=2*S)
bold=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',96*S); d.text((925*S,280*S),'STUDIO',font=bold,fill=(245,249,251,255))
regular=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',34*S); x=932*S
for ch in 'LASER': d.text((x,410*S),ch,font=regular,fill=(193,204,211,255)); x+=int(d.textlength(ch,font=regular))+19*S
# neon divider
rule=Image.new('RGBA',(W,H),(0,0,0,0)); rd=ImageDraw.Draw(rule); rd.line((928*S,480*S,1370*S,480*S),fill=(0,255,115,255),width=5*S); rd.ellipse((1370*S,474*S,1382*S,486*S),fill=(212,255,0,255))
im=Image.alpha_composite(im,rule.filter(ImageFilter.GaussianBlur(14*S))); im=Image.alpha_composite(im,rule)
d=ImageDraw.Draw(im); d.text((930*S,535*S),'LASER STUDIO  /  01',font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',17*S),fill=(115,132,142,255))
im.convert('RGB').resize((1500,900),Image.Resampling.LANCZOS).save(r'C:\Users\saymo\Documents\Codex\2026-10-02\cr\outputs\s-studio-laser-atrevida.png')
