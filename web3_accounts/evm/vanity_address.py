import argparse
import time
from eth_account import Account
from eth_account.hdaccount import generate_mnemonic
import eth_utils

def generate_vanity_address_with_mnemonic(prefix='', suffix=''):
    Account.enable_unaudited_hdwallet_features()
    prefix = prefix.lower().replace("0x", "")
    suffix = suffix.lower().replace("0x", "")
    
    while True:
        mnemonic = generate_mnemonic(num_words=12, lang="english")
        account = Account.from_mnemonic(mnemonic)
        address = account.address.lower()
        
        if address_matches(address, prefix, suffix):
            return account, mnemonic

def generate_vanity_address_without_mnemonic(prefix='', suffix=''):
    prefix = prefix.lower().replace("0x", "")
    suffix = suffix.lower().replace("0x", "")
    
    while True:
        account = Account.create()
        mnemonic = None
        address = account.address.lower()
        
        if address_matches(address, prefix, suffix):
            return account, mnemonic

def address_matches(address, prefix, suffix):
    return (not prefix or address[2:2+len(prefix)] == prefix) and \
           (not suffix or address[-len(suffix):] == suffix)

def main():
    parser = argparse.ArgumentParser(description="Generate an Ethereum vanity address.")
    parser.add_argument("--prefix", type=str, default='', help="Desired prefix of the Ethereum address")
    parser.add_argument("--suffix", type=str, default='', help="Desired suffix of the Ethereum address")
    parser.add_argument("--use-mnemonic", action='store_true', help="Enable mnemonic mode")

    args = parser.parse_args()

    start_time = time.time()

    if args.use_mnemonic:
        vanity_account, mnemonic = generate_vanity_address_with_mnemonic(args.prefix, args.suffix)
    else:
        vanity_account, mnemonic = generate_vanity_address_without_mnemonic(args.prefix, args.suffix)

    elapsed_time = time.time() - start_time

    print("Address:", vanity_account.address)
    print("Private Key:", vanity_account.key.hex())
    if mnemonic:
        print("Mnemonic:", mnemonic)
    print("Time Elapsed: {:.2f} seconds".format(elapsed_time))

if __name__ == "__main__":
    main()

