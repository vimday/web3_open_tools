下面是完整的 `README.md` 文件内容：

```markdown
# Ethereum Vanity Address Generator

This script generates an Ethereum vanity address based on specified prefix and/or suffix. It also supports generating the address using a mnemonic.

## Prerequisites

Make sure you have Python installed on your system. You will also need to install the required libraries:

```sh
pip install eth-account eth-utils
```

## Usage

### Command Line Arguments

- `--prefix`: Desired prefix of the Ethereum address (optional).
- `--suffix`: Desired suffix of the Ethereum address (optional).
- `--use-mnemonic`: Enable mnemonic mode (optional).

### Example Commands

To run the script, use the following command:

```sh
python vanity_address.py --prefix 123 --suffix abc --use-mnemonic
```

This command will generate an Ethereum address that starts with `123` and ends with `abc`, using a mnemonic for the address generation.

## Script Explanation

The script is divided into two main functions for generating vanity addresses:
- `generate_vanity_address_with_mnemonic`: Generates an address using a mnemonic.
- `generate_vanity_address_without_mnemonic`: Generates a random address without using a mnemonic.

The `main` function parses the command line arguments and calls the appropriate function based on the arguments provided.

## Code

Here is the complete script:

```python
import argparse
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
        
        if address[2:2+len(prefix)] == prefix and address[-len(suffix):] == suffix:
            return account, mnemonic

def generate_vanity_address_without_mnemonic(prefix='', suffix=''):
    prefix = prefix.lower().replace("0x", "")
    suffix = suffix.lower().replace("0x", "")
    
    while True:
        account = Account.create()
        mnemonic = None
        address = account.address.lower()
        
        if address[2:2+len(prefix)] == prefix and address[-len(suffix):] == suffix:
            return account, mnemonic

def main():
    parser = argparse.ArgumentParser(description="Generate an Ethereum vanity address.")
    parser.add_argument("--prefix", type=str, default='', help="Desired prefix of the Ethereum address")
    parser.add_argument("--suffix", type=str, default='', help="Desired suffix of the Ethereum address")
    parser.add_argument("--use-mnemonic", action='store_true', help="Enable mnemonic mode")

    args = parser.parse_args()

    if args.use_mnemonic:
        vanity_account, mnemonic = generate_vanity_address_with_mnemonic(args.prefix, args.suffix)
    else:
        vanity_account, mnemonic = generate_vanity_address_without_mnemonic(args.prefix, args.suffix)

    print("Address:", vanity_account.address)
    print("Private Key:", vanity_account.key.hex())
    if mnemonic:
        print("Mnemonic:", mnemonic)

if __name__ == "__main__":
    main()
```

## Notes

- Generating a vanity address can take a significant amount of time, especially if the prefix or suffix is long.
- Be careful with the generated private key and mnemonic. Store them securely.
```

