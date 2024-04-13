### The data in the QR code is compressed with GZIP. We need to create a bin file first then use
### a decompressor to get the content.
def main():
    with open('data.txt') as f:
        compressed_hex: str = f.read().strip()
    data_bytes: bytes = bytes.fromhex(compressed_hex)

    with open('bin.gz', 'wb') as f:
        f.write(data_bytes)

if __name__ == '__main__':
    main()