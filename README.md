LBN511-hack
=========

Security flaws found in LBN511 baby monitoring camera.

Once connected to broadcasting wireless signal, http://192.168.1.1 is an viewable file root directory. lighttpd is running with an image dump of live-feed jpegs in /tmp. Simple (crappy) python script will download these images (does not check timestamps, so it will get redundant images). These can be turned into a gif or live feed.

[CGI](http://httpd.apache.org/docs/current/howto/cgi.html) is running as root and will execute commands (notably from /bin and /sbin, such as "netstat" and "ps"). BASH script placed on SDCARD will mount in /SDCARD and is executable as root. Arguments are accepted as long as they are HTML encoded. CURL should be used to execute commands.

Sucessful exploit test was to replace lulluby in /opt/cec/lulluby/1.aac which is a renamed .WAV file: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 5500 Hz. Audio play was invoked with the companion app.

/bin/busybox exists and with running root commands it becomes feasible to install and run an ssh server.

DNS server - port 53
lighttpd - port 80
RTSP - port 554
