import os
os.system('LD_LIBRARY_PATH=/usr/local/lib mjpg_streamer -i "input_uvc.so -y" -o "output_http.so -w /home/pi/code/mjpg-streamer/www"')

