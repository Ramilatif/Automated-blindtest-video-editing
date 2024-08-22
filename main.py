from moviepy.video.compositing.concatenate import concatenate_videoclips
from util import get_file_paths, createFinalClip, createBlindClip
import os

os.environ["IMAGEMAGICK_BINARY"] = r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"

files = get_file_paths("Song")
allClip = []

for file in files:
    allClip.append(createFinalClip(file, 0, 30))

finalBlindTest = concatenate_videoclips(allClip)
finalBlindTest.write_videofile(
    "FinalBlindTest.mp4",
    codec="h264_amf",
    fps=24,preset="fast",
    bitrate="5000k",
    threads=4
)