scp -r pi@192.168.1.214:/home/pi/Videos/ /home/karol/Videos/judasz/new
ssh pi@192.168.1.214 'cd /home/pi/Videos && sudo rm -r *'

source /home/karol/PycharmProjects/movement_record_pi_camera/.venv/bin/activate
python3 /home/karol/PycharmProjects/movement_record_pi_camera/read_and_convert_video.py
deactivate

echo 'deleting new mjpeg videos'
cd /home/karol/Videos/judasz/new && sudo rm -r *
