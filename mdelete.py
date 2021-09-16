import ftplib
import sys

class FTP2(ftplib.FTP):
	def __init__(self, host, user, passwd):
		super().__init__(host, user, passwd)

	def mdelete(self, pattern):
		filenames = []
		
		# need save the filenames first, cannot call delete in-between dir callback (per line)
		# can use inner function instead of lambda
		self.dir(pattern, lambda l : filenames.append(l.split()[8]) )	
		
		print(f"python mdelete {filenames}")
		for filename in filenames:
			self.delete(filename)


with FTP2(sys.argv[1], sys.argv[2], sys.argv[3]) as f:
	f.cwd(sys.argv[4])
	f.mdelete(sys.argv[5])