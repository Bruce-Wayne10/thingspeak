The repo contains python codes to send data to thingspeak using write api key and read data from a channel using channel number (for a public channel).

Write data to channel 
Note : Kindly update the key value to your Thingspeak write key value , which can be obtained from API Keys tab in channel menu of your thingspeak account.

Use codes 
1. thingspeaktest.py : To test whether the data is getting pushed to thingspeak channel via your network.
2. thingspeaktestloop.py : Upload the same data in interval of 16s.
3. thingspeaktestserial.py: Upload serial data from device (ttyACM0) connected to your machine. Note : The device may have different address depending on your machine. Type dmesg | grep tty to find your machine.

Read Data
Note : Make sure that you add/edit your channel number in the code.
1. thingspeaktestread.py : returns last posted value from your public channel.
2. thingspeaktestreadtofile.py : saves the last posted value from your public channel to a text file (thingspeak.txt)


To run the code try in terminal 
python filename.py


