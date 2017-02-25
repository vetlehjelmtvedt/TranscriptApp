import moviepy.editor as mp
import subprocess
import os
import shutil

with open("path.txt", "r") as file:
    path_dir = file.read()

with open("path_output.txt", "r") as file:
    output_dir = file.read()




class Convert_Extract():


    movie_path = path_dir


    def convert_to_mp4(self):
        clip = mp.VideoFileClip(path_dir)
        new_clip = clip.write_videofile("output.mp4")


    def segmenting(self):
        count = 0
        count_1 = 0
        movie_path = path_dir
        clip = mp.VideoFileClip(movie_path)
        length = clip.duration
        segments_start = length / 10
        seg_len = []
        seg_len.append(0)

        while count != 10:
            seg_len.append(segments_start)
            segment_name = "segment" + str(count + 1)
            count += 1
            segments_start += length / 10

        print(seg_len)

        while count_1 != 10:

            clip_1 = clip.subclip(seg_len[0 + count_1], seg_len[1 + count_1])
            new_clip = clip_1.write_videofile("output/segment_" + str(count_1) + ".mp4")

            count_1 += 1


    def extract_wav(self):


        clip_0 = mp.VideoFileClip("output/segment_0.mp4")
        clip_1 = mp.VideoFileClip("output/segment_1.mp4")
        clip_2 = mp.VideoFileClip("output/segment_2.mp4")
        clip_3 = mp.VideoFileClip("output/segment_3.mp4")
        clip_4 = mp.VideoFileClip("output/segment_4.mp4")
        clip_5 = mp.VideoFileClip("output/segment_5.mp4")
        clip_6 = mp.VideoFileClip("output/segment_6.mp4")
        clip_7 = mp.VideoFileClip("output/segment_7.mp4")
        clip_8 = mp.VideoFileClip("output/segment_8.mp4")
        clip_9 = mp.VideoFileClip("output/segment_9.mp4")

        audio_1 = clip_0.audio.write_audiofile("recordings/0001.wav")
        audio_2 = clip_1.audio.write_audiofile("recordings/0002.wav")
        audio_3 = clip_2.audio.write_audiofile("recordings/0003.wav")
        audio_4 = clip_3.audio.write_audiofile("recordings/0004.wav")
        audio_5 = clip_4.audio.write_audiofile("recordings/0005.wav")
        audio_6 = clip_5.audio.write_audiofile("recordings/0006.wav")
        audio_7 = clip_6.audio.write_audiofile("recordings/0007.wav")
        audio_8 = clip_7.audio.write_audiofile("recordings/0008.wav")
        audio_9 = clip_8.audio.write_audiofile("recordings/0009.wav")
        audio_9 = clip_9.audio.write_audiofile("recordings/00010.wav")






    def transcribe(self):
        counter = 0

        with open("recordings.txt", "w"):
            pass

        while counter != 10:
            with open("recordings.txt", "a") as file:
                file.write("./recordings/000" + str(counter + 1) + ".wav" + "\n")


            counter += 1

        subprocess.call("py -2 ./sttClient.py -credentials 96c260dc-814a-4810-a361-dba8fe6e9b9a:Dqa6Uvn5aSzB -model en-US_BroadbandModel -threads 10")
        shutil.move("C:/Users/vetle/Desktop/IBM_App/output/hypotheses.txt", output_dir + "/transcript.txt")













a = Convert_Extract()
a.convert_to_mp4()
a.segmenting()
a.extract_wav()
a.transcribe()












