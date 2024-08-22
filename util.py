from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip,ColorClip,concatenate_videoclips
import moviepy.editor as mp
import os
os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.0.10-Q16-HDRI\magick.exe"

def createClip(path: str, timeCode_S: int,timeCode_E: int):

    clip = VideoFileClip(path).subclip(timeCode_S, timeCode_E)
    segments = [clip.subclip(i, i + 10) for i in range(0, int(clip.duration), 10)]
    segments_resized = [segment.resize((1440,1080)) for segment in segments]
    final_clip = mp.concatenate_videoclips(segments_resized)

    txt_clip = TextClip("Hello World", fontsize=100, color='white', method='caption')
    background = ColorClip(size=txt_clip.size, color=(0, 0, 0), duration=final_clip.duration)

    txt_clip = txt_clip.set_position((60, 900)).set_duration(final_clip.duration)
    background = background.set_position((60, 900)).set_duration(final_clip.duration)

    video_with_text = CompositeVideoClip([final_clip, background])
    video_with_text = CompositeVideoClip([video_with_text, txt_clip])
    video_with_text = video_with_text.set_audio(video_with_text.audio.set_fps(44100))
    return video_with_text


def get_file_paths(directory: str):
    file_paths = []
    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        if os.path.isfile(full_path):
            file_paths.append(full_path)
    return file_paths


def generate_countdown_video(n):
    clips = []
    # Loop to create a TextClip for each number from n to 0
    for i in range(n, -1, -1):
        txt = TextClip(str(i), fontsize=70, color='white', size=(1440, 1080),method='caption')
        txt = txt.set_duration(1)  # Each number will be shown for 1 second
        txt = txt.set_position('center')  # Center the text
        txt = txt.on_color(color=(0, 0, 0))  # Background color is black
        clips.append(txt)

    return concatenate_videoclips(clips, method="compose")

def createBlindClip(path: str, timeCode_S: int,timeCode_E: int):
    clip = createClip(path, timeCode_S, timeCode_E)
    blindClip = generate_countdown_video(15)
    audio = clip.audio
    audio.duration = 16
    blindClip = blindClip.set_audio(audio.set_fps(44100))

    segments = [blindClip.subclip(i, i + 10) for i in range(0, int(blindClip.duration), 10)]
    segments_resized = [segment.resize(height=1080) for segment in segments]
    final_BlindClip = mp.concatenate_videoclips(segments_resized)
    final_BlindClip.duration = 16

    return final_BlindClip

def createFinalClip (path: str, timeCode_S: int,timeCode_E: int):
    blindClip = createBlindClip(path, timeCode_S, timeCode_S+ 16)
    clip = createClip(path,timeCode_S+16, timeCode_E)
    finalClip = concatenate_videoclips([blindClip,clip])
    finalClip = finalClip.volumex(0.8)

    return finalClip