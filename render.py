from PIL import Image, ImageDraw, ImageFont
import os, textwrap
lines=[l.rstrip() for l in open("transcript.txt") if "presentation resolver" not in l]
hdr=["Switch x IRC demo (PR #1058) - real miniircd server on localhost, live adapter run","Recorded headless by Tali (AI agent)",""]
f=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",15)
os.makedirs("frames",exist_ok=True)
wrapped=[]
for l in hdr+lines: wrapped += textwrap.wrap(l,140) or [""]
for i in range(1,len(wrapped)+1):
    im=Image.new("RGB",(1280,720),(18,18,24)); d=ImageDraw.Draw(im)
    for j,l in enumerate(wrapped[max(0,i-38):i]):
        c=(120,200,255) if "IRC" in l[:24] else (160,255,160) if "SWITCH" in l[:24] else (220,220,220)
        d.text((16,12+j*18),l,font=f,fill=c)
    im.save(f"frames/{i:03d}.png")
