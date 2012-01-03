import zipfile
	
def fileiterator(zipf):
	with zipfile.ZipFile(zipf, "r", zipfile.ZIP_STORED) as openzip:
		filelist = openzip.infolist()
		for f in filelist:
			yield(f.filename, openzip.read(f))

def process(zipf, callback):
	with zipfile.ZipFile(zipf, "r", zipfile.ZIP_STORED) as openzip:
		filelist = openZip.infolist()
		for f in filelist:
			callback(f.filename, openzip.read(f))






