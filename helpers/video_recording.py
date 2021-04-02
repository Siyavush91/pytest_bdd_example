import os
import time
import threading
import sys
import pyautogui
import shutil
from subprocess import call

if __name__ == '__main__':
    def __run_screenshot_recorder(): 
        number = 0
        while True:
            screenshots_dir = 'video_screenshots'
            os.makedirs(screenshots_dir, exist_ok=True)
            screenshot_name =  os.path.join(screenshots_dir, 'image' + str(number).zfill(4) + '.png')
            pyautogui.screenshot(screenshot_name)
            # TODO: change timer if you want video
            time.sleep(500)
            number += 1

    __run_screenshot_recorder()
    
class VideoScreenshots():
    def terminate(self, pid):
        if pid is not None:
            kill_cmd = 'kill -9 ' + str(pid)
            call(kill_cmd, shell=True)
            self.__save_as_mp4()
            dirpath = os.path.join('video_screenshots')
            if os.path.exists(dirpath) and os.path.isdir(dirpath):
                shutil.rmtree(dirpath)

    def __save_as_mp4(self):
        os.system("ffmpeg -r 1 -pattern_type glob -i 'video_screenshots/*.png' -vcodec mpeg4 -y movie.mp4")

screenshot_capturing = VideoScreenshots()
