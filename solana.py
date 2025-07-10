from solders.keypair import Keypair
from solders.pubkey import Pubkey
import base58
import csv

def create_solana_accounts_csv(num_accounts: int):
    with open("wallets.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Account No", "Public Key", "Public Key (base58)", "Public Key (array)", "Wallet Address"])

        for i in range(num_accounts):
            keypair = Keypair()
            pubkey: Pubkey = keypair.pubkey()

            pubkey_str = str(pubkey)
            pubkey_bytes = bytes(pubkey)  # FIX: works like to_bytes()
            pubkey_base58 = base58.b58encode(pubkey_bytes).decode()
            pubkey_array = list(pubkey_bytes)
            wallet_address = pubkey_str

            writer.writerow([
                f"Account {i + 1}",
                pubkey_str,
                pubkey_base58,
                pubkey_array,
                wallet_address
            ])

    print(f"{num_accounts} Solana accounts created and saved to 'wallets.csv'.")

if __name__ == "__main__":
    count = int(input("How many Solana accounts do you want to generate? "))
    create_solana_accounts_csv(count)
