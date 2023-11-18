#Generate extradata for adding to genesis.json

# Define the signer addresses
signer_addresses = [
    "00a1866c779e7964fe58752872eb9c57ee5602b9",
    "3812bd6e277c8bf7acfd1bca926841f7f8822af8",
    "7fc575994a80dc2c9c4cb9f1d40f0ebddf817138"
    # Add more signer addresses here if needed
]

# Step 1: Concatenate 32 zero bytes
zero_bytes_32 = "00" * 32

# Step 2: Concatenate all signer addresses
all_signer_addresses = ''.join(signer_addresses)

# Step 3: Concatenate 65 further zero bytes
further_zero_bytes_65 = "00" * 65

# Step 4: Combine all the strings
encoded_extradata = zero_bytes_32 + all_signer_addresses + further_zero_bytes_65

# Step 5: Use the result in genesis.json (replace "your_extradata_value" with the encoded_extradata)
genesis_json = {
    "extradata": f"0x{encoded_extradata}"
}

print(genesis_json)
