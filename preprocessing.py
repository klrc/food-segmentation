import os
import shutil

from PIL import Image

ext = ['jpg', 'jpeg', 'png']
files = os.listdir('.')


def process_image_deprecated(image, mwidth=200, mheight=150):
    w, h = image.size
    if w <= mwidth and h <= mheight:
        return
    if (1.0 * w / mwidth) > (1.0 * h / mheight):
        scale = 1.0 * w / mwidth
        new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)

    else:
        scale = 1.0 * h / mheight
        new_im = image.resize((int(w / scale), int(h / scale)), Image.ANTIALIAS)
    return new_im


def process_image(image, width=200, height=150):
    new_img = image.resize((width, height), Image.BILINEAR)
    return new_img


def mkdirs():
    os.mkdir('resized')
    os.mkdir('resized/img')
    os.mkdir('resized/mask')
    os.mkdir('resized/yaml')


def process(raw_path='raw_imgs', maxidx=-1, target=None):
    foods = os.listdir(raw_path)
    for food in foods:
        if target and food not in target:
            continue
        fp = f'{raw_path}/{food}'
        img_folders = os.listdir(fp)
        img_folders = [x for x in img_folders if x.endswith('_json')]
        for folder in img_folders:
            img_id = folder.split('_')[-2]
            with open(f'{fp}/{folder}/label_names.txt') as f:
                f.readline()
                img_class = f.readline().replace('\n', '')
            img_id = f'{food}{img_id}'
            print(img_id)
            image = Image.open(f'{fp}/{folder}/img.png')
            image = process_image(image)
            image.save(f'resized/img/{img_id}.png')
            image.close()
            mask = Image.open(f'{fp}/{folder}/label.png')
            mask = process_image(mask)
            mask.save(f'resized/mask/{img_id}.{img_class}.png')
            mask.close()
            shutil.copyfile(f'{fp}/{folder}/info.yaml', f'resized/yaml/{img_id}.yaml')
        maxidx -= 1
        if maxidx == 0:
            break


if __name__ == '__main__':
    mkdirs()
    target = ('包子', '猪肉白菜水饺', '清炒土豆丝')
    process(raw_path='network_imgs', target=target)
