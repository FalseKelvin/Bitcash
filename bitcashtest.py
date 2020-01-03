from bitcash import PrivateKeyTestnet
import sys
import hashlib

privateKey = 'USE YOUR OWN KEY'
key = PrivateKeyTestnet(privateKey) # retrieve instance via private key
wif = key.to_wif() # get the wallet import format
sampleDoc = "./bitcashtest.txt"

def show_address():
    return 'Address: ' + key.address + '\nPrivate Key:' + wif + '\nWallet Balance: ' + str(key.get_balance())

# generates a sha256 hash of the supplied sampleDoc
def get_digest(_sampleDoc):
    hash = hashlib.sha256()

    with open(_sampleDoc, 'rb') as file:
        while True:
            chunk = file.read(hash.block_size)
            if not chunk:
                break
            hash.update(chunk)

    return hash.hexdigest()

# posts the sha256 hash of the sampleDoc to memo
def post_to_memo():
	output = [
		(key.address, 1000, 'satoshi'),
	]
	key.send(output, message='Fiona\'s sampleDoc hash: ' + get_digest(sampleDoc))

print(show_address())
print(get_digest(sampleDoc))
print(post_to_memo())
