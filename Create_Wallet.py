from eth_account import Account
from eth_account.hdaccount import generate_mnemonic


def enable_hd_wallet_features():
    Account.enable_unaudited_hdwallet_features()


def generate_wallets(num_wallets):
    enable_hd_wallet_features()
    wallets = []

    for i in range(num_wallets):
        mnemonic_phrase = generate_mnemonic(num_words=12, lang='english')
        wallet_account = Account.from_mnemonic(mnemonic_phrase)
        wallet_address = wallet_account.address
        wallet_private_key = wallet_account.key.hex()

        print(f'Account {i + 1}\n'
              f'Seed Phrase: {mnemonic_phrase}\n'
              f'Private Key: {wallet_private_key}\n'
              f'Public Address: {wallet_address}\n'
              '--------------------------')

        wallets.append({
            'seed_phrase': mnemonic_phrase,
            'private_key': wallet_private_key,
            'address': wallet_address
        })

    return wallets


def save_wallets_to_files(wallets):
    with open('ETH_wallet.txt', 'w') as f_addr, \
         open('ETH_Seed.txt', 'w') as f_seed, \
         open('PrivateKey.txt', 'w') as f_priv:

        for w in wallets:
            f_addr.write(w['address'] + '\n')
            f_seed.write(w['seed_phrase'] + '\n')
            f_priv.write(w['private_key'] + '\n')


def main():
    num_wallets = int(input("How many wallets to create? "))
    wallets = generate_wallets(num_wallets)
    save_wallets_to_files(wallets)
    print("✅ Wallets saved to 'ETH_wallet.txt', 'ETH_Seed.txt', and 'PrivateKey.txt'")


if __name__ == "__main__":
    main()

