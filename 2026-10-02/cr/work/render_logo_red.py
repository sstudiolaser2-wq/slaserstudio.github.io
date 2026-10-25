from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H,S=1500,700,2; W*=S; H*=S
im=Image.new('RGBA',(W,H),(7,7,9,255))
pts=[(810,160),(493,160),(405,240),(466,300),(739,344),(805,409),(728,485),(415,485)]
def sc(q): return (int(q[0]*S),int(q[1]*S))
def strokecolor(color,width):
 layer=Image.new('RGBA',(W,H),(0,0,0,0)); ImageDraw.Draw(layer).line([sc(p) for p in pts],fill=color,width=width*S,joint='curve'); return layer
# layered red plasma glow
for col,w,blur in [((255,0,30,170),84,24),((255,30,54,220),70,12)]:
 im=Image.alpha_composite(im,strokecolor(col,w).filter(ImageFilter.GaussianBlur(blur*S)))
im=Image.alpha_composite(im,strokecolor((255,0,38,255),78))
im=Image.alpha_composite(im,strokecolor((103,114,124,255),60))
im=Image.alpha_composite(im,strokecolor((224,232,238,255),49))
im=Image.alpha_composite(im,strokecolor((255,255,255,255),3).filter(ImageFilter.GaussianBlur(4*S)))
im=Image.alpha_composite(im,strokecolor((255,255,255,255),2))
d=ImageDraw.Draw(im)
for (a,b) in [((827,142),(855,120)),((398,492),(370,516)),((388,240),(344,240)),((821,409),(868,409))]:
 d.line([sc(a),sc(b)],fill=(255,55,70,255),width=3*S)
for x,y,col in [(862,114,(255,240,240,255)),(363,522,(255,89,98,255))]:
 cx,cy=sc((x,y)); r=5*S; d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=col)
d.line((950*S,140*S,950*S,512*S),fill=(57,48,51,255),width=2*S)
fb=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',83*S); d.text((1030*S,232*S),'STUDIO',font=fb,fill=(247,244,244,255))
fr=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',29*S); x=1034*S
for ch in 'LASER': d.text((x,354*S),ch,font=fr,fill=(255,51,69,255)); x+=int(d.textlength(ch,font=fr))+18*S
rule=Image.new('RGBA',(W,H),(0,0,0,0)); rd=ImageDraw.Draw(rule); rd.line((1032*S,432*S,1370*S,432*S),fill=(255,22,56,255),width=4*S); rd.ellipse((1376*S,427*S,1386*S,437*S),fill=(255,105,112,255))
im=Image.alpha_composite(im,rule.filter(ImageFilter.GaussianBlur(12*S))); im=Image.alpha_composite(im,rule)
im.convert('RGB').resize((1500,700),Image.Resampling.LANCZOS).save(r'C:\Users\saymo\Documents\Codex\2026-10-02\cr\outputs\s-studio-laser-rojo.png')

