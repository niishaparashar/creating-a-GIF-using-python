import imageio.v3 as iio

filenames = ['img1.png', 'img2.png']
images = []
for filename in filenames:
    images.append(iio.imread(filename))
    print("Reading images...")
images = [iio.imread(filename) for filename in filenames]

print("Creating GIF...")
iio.imwrite('dance.gif', images, duration=500, loop=0)
print("GIF created successfully!")

