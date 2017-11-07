#!/usr/bin/env python

###########################
# Frosty Survey
# https://github.com/vesche
###########################

import optparse
import os
import subprocess
import sys


def survey(network, domain, share, username, password):
	ip_list = []

	share_ip, share_name = share.split('\\')
	net_ip, cidr = network.split('/')
	breakout = net_ip.split('.')

	print "Scanning...", network
	with open(os.devnull, "wb") as limbo:
		for last_octet in range(15, 16):
			ip = '.'.join(breakout[0:3]) + '.' + str(last_octet)
			result = subprocess.Popen(["ping", "-n", "1", "-w", "200", ip], stdout=limbo, stderr=limbo).wait()
			if result:
				continue
			else:
				ip_list.append(ip)
				print " "*12 + ip + ": ACTIVE"

	raw_input("\nAbout to survey the following hosts:\n" + '\n'.join(ip_list) + "\nENTER to continue or ^C to stop...")

	# clean up previous bats
	os.system("del .\\*.bat")

	# commands to run
	survey_commands = ["ipconfig /all", "systeminfo", "netstat -ano", "sc query", "tasklist /m", "net use"]
	autorun_commands = ["reg query HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
						"reg query HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce"]
						# "reg query HKLM\\System\\CurrentControlSet\\Services",
						# "reg query \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\"",
						# "reg query HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
						# "reg query HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce",
						# "reg query HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
						# "reg query HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Runonce",
						# "reg query HKLM\\CurrentControlSet\\Services\\inf",
						# "reg query \"HKLM\\System\\CurrentControlSet\\Control\\Terminal Server\\Wds\\rdpwd\\StartupPrograms\"",
						# "reg query \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\Userinit\"",
						# "reg query \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\VmApplet\"",
						# "reg query \"HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\Shell\"",
						# "reg query HKLM\\SYSTEM\\CurrentControlSet\\Control\\SafeBoot\\AlternateShell",
						# "reg query HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Run",
						# "dir \"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\"",
						# "reg query \"HKLM\\SOFTWARE\\Microsoft\\Active Setup\\Installed Components\""]
						# "reg query \"HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Active Setup\\Installed Components\"",
						# "reg query \"HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Windows\\IconServiceLib\""]

	# create base.bat
	f_survey = open("base.bat", 'w')
	for line in survey_commands:
		f_survey.write("%s >> C:\\survey.txt\n" % line)
	for line in autorun_commands:
		f_survey.write("%s >> C:\\autoruns.txt\n" % line)
	f_survey.close()

	# iterate for each IP
	for ip in ip_list:
		clean_commands = ["net use \\\\%s /user:%s %s" % (share, username, password),
						  "copy C:\\survey.txt \\\\%s\\%s\\%s_survey.txt" % (share_ip, share_name, ip),
						  "copy C:\\autoruns.txt \\\\%s\\%s\\%s_autoruns.txt" % (share_ip, share_name, ip)]
						  #"del /f /q C:\\survey.bat && del /f /q C:\\survey.txt && del /f /q C:\\autoruns.txt"]

		# create survey.bat
		os.system("copy /y .\\base.bat .\\survey.bat")
		f_survey = open("survey.bat", "a")
		for line in clean_commands:
			f_survey.write("%s\n" % line)
		f_survey.close()

		# create temp.bat to run
		li_temp = ["net use \\\\%s /user:%s %s" % (ip, username, password),
				   "sc \\\\%s start winmgmt" % (ip),
				   "copy .\\survey.bat \\\\%s\\c$\\survey.bat" % (ip),
				   "wmic /node:%s /user:%s\\%s /password:%s process call create \"cmd /c start /min C:\\survey.bat\"" % (ip, domain, username, password)]

		# create temp.bat
		f_temp = open("temp.bat", 'w')
		for line in li_temp:
			f_temp.write("%s\n" % line)
		f_temp.close()

		os.system(".\\temp.bat")


def main():
	survey_text = '''Frosty survey, runs remote commands on systems to survey hosts on a domain.
Must be run with domain admin credentials, creates a survey folder for each host and text files
for command output. This early version only scans /24 networks. For instance entering
10.0.0.0/24 would scan hosts 10.0.0.1-254.'''
	p = optparse.OptionParser(description = survey_text,
							  prog		  = "frosty survey",
							  version	  = "0.1",
							  usage		  = "frosty_survey -n <ip>/<cidr> -d <domain> -s <shareip>\\<sharename> -u <username> -p <password>")
	p.add_option('-n', action='store_true', help='network to scan')
	p.add_option('-d', action='store_true', help='domain name')
	p.add_option('-s', action='store_true', help='share')
	p.add_option('-u', action='store_true', help='username')
	p.add_option('-p', action='store_true', help='password')
	options, arg = p.parse_args()
	survey(network=arg[0], domain=arg[1], share=arg[2], username=arg[3], password=arg[4])


if __name__ == "__main__":
	main()
