import imageio.v3 as iio

filenames = ['chicklet1.png', 'chicklet2.png', 'chicklet3.png', 'chicklet4.png']
images = []

# Read images
for filename in filenames:
  images.append(iio.imread(filename))

# Images to GIF
iio.imwrite('chick.gif', images, duration = 400, loop = 0)