# Open Mjpg Streamer automatically (webcam) while turning on Pi3


### STEPs:

**1. Check the virtual document after setup the webcam and pi3 detects the webcam.**

**2. Set up  fswebcam for taking photos.**
     (1)`$sudo apt-get update`
     (2)`$sudo apt-get -y install fswebcam`

**3. Set up MJPG-Streamer server to build up streamer.**
     (1)`$sudo apt-get update`
     (2)`$sudo apt-get -y install subversion`
     (3)`$sudo apt-get -y install libjpeg8-dev`
     (4)`$sudo apt-get -y install imagemagick`

**4. Download the origin codes of MJGP-Streamer.**
     (1)`$svn co https://svn.code.sf.net/p/mjpg-streamer/code`

**5. Switch to "/home/pi/code/mjpg-steamer"document under terminal.**
     (1)`$cd /home/pi/code/mjpg-steamer`
     (2)`$sudo make`

**6. Start MJPG-Streamer server to test steamer.**
     (1)`$cd /home/pi/code/mjpg-steamer`
     (2)`$./mjpg_streamer -i "./input_uvc.so" -o "./output_http.so -w ./www`
     If your webcam does not support MJPEG , please use below command to use YUYV format instead of MJPEG format.
     (1)`$./mjpg_streamer -i "./input_uvc.so -y" -o "./output_http.so -w ./www`

**7. Open chrome  and type URL as below:**
     http://localhost:8080 or
     http://X.X.X.X:8080   ( your ip address )

**8. Create a python program " mjpg.py".**

**9. Create a shell "mjgp.sh".**

**10. The last step is that:** 
      (1)`$sudo nano ~/.config/lxsession/LXDE-pi/autostart`
      Then add a row of script: `@sh /home/pi/personal/mjpg.sh`
      (About shell, pleaer refer to ../raspberry/tutorial/shell/)

**11. Now, you can turn off and turn on your pi3 to test this function to check if it works or not.**

