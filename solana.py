from solders.keypair import Keypair
from solders.pubkey import Pubkey
import base58

def generate_wallets_and_save(num_accounts: int):
    with open("wallet.txt", "w") as wallet_file, \
         open("pvt.csv", "w") as pvt_file, \
         open("pvt2.csv", "w") as pvt2_file:

        for _ in range(num_accounts):
            keypair = Keypair()
            pubkey: Pubkey = keypair.pubkey()

            wallet_address = str(pubkey)
            private_key_base58 = base58.b58encode(bytes(keypair)).decode()
            private_key_array = list(bytes(keypair))

            # Save to files
            wallet_file.write(f"{wallet_address}\n")
            pvt_file.write(f"{private_key_array}\n")
            pvt2_file.write(f"{private_key_base58}\n")  # ✅ raw base58 key only, no extra word

    print("✅ Wallets generated and saved to:")
    print(" - wallet.txt (addresses)")
    print(" - pvt.csv (array format)")
    print(" - pvt2.csv (raw base58 format)")

if __name__ == "__main__":
    count = int(input("How many Solana wallets do you want to generate? "))
    generate_wallets_and_save(count)
