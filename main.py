from moviepy.video.compositing.concatenate import concatenate_videoclips
from util import get_file_paths,createFinalClip



files = get_file_paths("Song")
allClip = []

for file in files:
    allClip.append(createFinalClip(file, 0, 30))

finalBlindTest = concatenate_videoclips(allClip)
finalBlindTest.write_videofile("FinalBlindTest.mp4", codec="libx264",fps=24)




