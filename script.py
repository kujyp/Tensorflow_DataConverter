from load.loadfile import load_allimage

rootdir = "data"
images = load_allimage(rootdir)

images[50].show()