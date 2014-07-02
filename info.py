import urllib2

# it runs an open lighttpd showing root...
# it executes and responds back commands from BIN...
url = 'http://192.168.1.1/bin/'

def command(c):
	response = urllib2.urlopen(url+c)
	print response.read();

command('hostname')
command('netstat')
#command('dmesg')
#command('ps')
