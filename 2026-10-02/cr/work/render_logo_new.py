from PIL import Image, ImageDraw, ImageFont, ImageFilter
S=2; W,H=1200*S,900*S
im=Image.new('RGBA',(W,H),(5,4,10,255)); pts=[(777,181),(470,181),(405,247),(456,300),(737,354),(795,414),(738,473),(431,473)]
def scaled(q): return (int(q[0]*S),int(q[1]*S))
def path_layer(color,width):
 layer=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(layer)
 d.line([scaled(p) for p in pts],fill=color,width=width*S,joint='curve')
 return layer
# magenta-violet aura, then bright laser tube and white-hot core
for radius,color in [(28,(216,35,255,105)),(15,(255,45,205,150)),(7,(90,85,255,220))]:
 im=Image.alpha_composite(im,path_layer(color,20).filter(ImageFilter.GaussianBlur(radius*S)))
im=Image.alpha_composite(im,path_layer((224,45,235,255),17))
im=Image.alpha_composite(im,path_layer((255,247,255,255),3))
d=ImageDraw.Draw(im)
for coords,col,w in [(((777,181),(842,148)),(255,73,215,255),3),(((431,473),(366,506)),(255,73,215,255),3),(((405,247),(325,247)),(255,73,215,255),3),(((795,414),(875,414)),(255,73,215,255),3),(((840,147),(862,136)),(85,236,255,255),2),(((367,507),(345,518)),(85,236,255,255),2)]:
 d.line([scaled(coords[0]),scaled(coords[1])],fill=col,width=w*S)
for x,y,col in [(866,134,(247,216,255,255)),(340,522,(85,236,255,255))]:
 cx,cy=scaled((x,y)); r=5*S; d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=col)
d.line([scaled((310,625)),scaled((890,625))],fill=(48,34,58,255),width=2)
fp='C:/Windows/Fonts/arial.ttf'; bp='C:/Windows/Fonts/arialbd.ttf'
def font(file,size): return ImageFont.truetype(file,size*S)
def tracked(text,y,ft,color,space):
 dr=ImageDraw.Draw(im); widths=[dr.textlength(c,font=ft) for c in text]; x=(W-sum(widths)-space*S*(len(text)-1))/2
 for c,w in zip(text,widths): dr.text((int(x),y*S),c,font=ft,fill=color); x+=w+space*S
tracked('S STUDIO',665,font(bp,58),(248,245,251,255),19)
tracked('LASER',744,font(fp,22),(255,75,217,255),22)
d=ImageDraw.Draw(im); d.line([scaled((492,812)),scaled((708,812))],fill=(155,81,255,255),width=2*S)
im.convert('RGB').save(r'C:\Users\saymo\Documents\Codex\2026-10-02\cr\outputs\s-studio-laser-nuevo.png')
