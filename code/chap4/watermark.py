from PIL import Image, ImageDraw,ImageFont
# 打水印玩

def create_watermark(img_path,content,id,size=24):
    im = Image.open(img_path).convert('RGBA')
    txt = Image.new('RGBA', im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(txt)
    num = len(content)
    font = ImageFont.truetype('simkai.ttf', size)
    d.text((txt.size[0] - size*num, txt.size[1] - (size+2)), content,font=font, fill=(255, 255, 255, 255))
    out = Image.alpha_composite(im, txt)
    l = img_path.split('.')
    filename,ext = l[-2].split('/')[-1],l[-1]
    new_name = ''.join(('./data/',filename,'_',str(id),'.png'))
    out.save(new_name)


if __name__ == '__main__':
    names = ['真无聊无真','花丛97']
    import glob
    for path in glob.glob('./data/fig*.jpg'):
        for i in range(2):
            create_watermark(path,'古剑奇谭吧@%s'%names[i],i)
