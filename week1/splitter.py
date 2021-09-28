from PIL import Image
import pygame


def split_animated():
    image = []
    source = "./challenge.gif"
    gif = Image.open(source)
    for frame_index in range(gif.n_frames):
#        print(frame_index)
        gif.seek(frame_index)
        frame_rgba = gif.convert("RGBA")
        pygame_image = pygame.image.fromstring( frame_rgba.tobytes(), frame_rgba.size, frame_rgba.mode)
        image.append(pygame_image)
        pygame.image.save(pygame_image, "tmp/file-{0}.jpeg".format(frame_index))
    return image

def concatenate():
    image_start = 0
    subimages = 12
    counter = 0
    width = Image.open("tmp/file-{0}.jpeg".format("0")).width
    print("Width: ",width)
    image = []
    while counter < 10:
      heigh = calculate_compete_size(counter)
      print("height: ", heigh)
      image.append(Image.new('RGB', (width, heigh)))
      cnt = image_start
      cul_height=0
      while cnt < 120:
          app_image = Image.open("tmp/file-{0}.jpeg".format(cnt))
          image[counter].paste(app_image,(0,cul_height))
          cul_height = cul_height + app_image.height -1
          cnt += 10
      image[counter].save("codes/file-{0}.jpeg".format(counter))
      image_start+=1





      counter+=1



def calculate_compete_size(start):
    counter  = start
    size = 0
    while counter < 120:
        img = Image.open("tmp/file-{0}.jpeg".format(counter))
        size = size + img.height
        counter = counter + 10
    return size






if __name__ == "__main__":
    img = split_animated()
    concatenate()
