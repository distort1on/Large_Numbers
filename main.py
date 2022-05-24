#  Copyright (c) 2022. Illia Popov.
import secrets
import time
import itertools


def find_keypace(number_of_bits):
    return 2 ** number_of_bits


def bruteforce(number_of_bits, target_key):
    start = time.time_ns()

    print(f"{number_of_bits}-bit key:")

    for seq in itertools.product("01", repeat=number_of_bits):
        if "".join(seq) == target_key:
            print(f"Found key {target_key}", end="")
            break

        """
      private_key = secrets.randbits(number_of_bits)
      private_key = bin(private_key)[2:].zfill(8)
      if private_key == target_key:
        print(target_key)
        break
      """

    end = time.time_ns()
    return (end - start) / 1000000


if __name__ == '__main__':
    # Keyspaces of n-bit keys

    bit_sequences = [2 ** i for i in range(3, 13)]

    print("Keyspaces of n-bit keys:\n")
    for sequence in bit_sequences:
        print(f"{sequence}-bit - {find_keypace(sequence)}")

    # Key generation
    print("----------------------------------------------------------------------")
    print("Generated n-bit keys:\n")

    keys = []
    for sequence in bit_sequences:
        private_key_decimal = secrets.randbits(sequence)
        private_key_binary = bin(private_key_decimal)[2:].zfill(sequence)
        keys.append(private_key_binary)
        print(f"{sequence} bit key - {private_key_binary}")

    # Bruteforce
    print("----------------------------------------------------------------------")
    print("Bruteforce time:\n")

    for i in range(len(bit_sequences)):
        if i == 2:
            print(f"{bit_sequences[i]}-bit key: days\n")
        elif i == 3:
            print(f"{bit_sequences[i]}-bit key: years\n")
        elif i == 4:
            print(f"{bit_sequences[i]}-bit key: a lot of years:)\n")
        elif i > 4:
            print(f"{bit_sequences[i]}-bit key: inf\n")
        else:
            print(f" ---{bruteforce(bit_sequences[i], keys[i])} ms---\n")
