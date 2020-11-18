import cPickle

def store_index(index, filefolder, filename):
	full_path = str(filefolder + filename + '.pickle')
	with open(full_path, 'wb') as f:
		cPickle.dump(index, f)

def extract_index(file_location):
    with open(file_location, 'rb') as f:
        index = cPickle.load(f)
        return index