import hashlib

BLOCKSIZE = 65536            # lets read stuff in 64kb chunks!
fileToOpen = input("Enter Filename: ")
hasher = hashlib.md5()
sha1 = hashlib.sha1()

with open(fileToOpen, 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        sha1.update(buf)
        buf = afile.read(BLOCKSIZE)
        
print("MD5: {0}\n".format(hasher.hexdigest()))
print("SHA1: {0}".format(sha1.hexdigest()))
