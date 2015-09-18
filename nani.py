from moviepy.editor import *

clip = (VideoFileClip("/Users/Buraka/Bhale.mp4")
        .subclip((1,28.55),(1,29.15))
        .resize(0.8))
clip.write_gif("nani9.gif")

