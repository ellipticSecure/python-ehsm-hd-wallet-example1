#!/usr/bin/env python
# -*- mode: python -*-
# Author: Kobus Grobler

import os
import getpass
import sys
import binascii
import csv
import ehsm

if __name__ == '__main__':
    mirkey = ehsm.load_ehsm()

    pin = os.environ.get('TEST_PIN')

    if pin is None:
        pin = getpass.getpass("Enter the device user PIN:")

    pin = bytes(pin, 'utf-8')

    # list of integers representing a bip32 path to the derived key
    # ie. by default this is "m", "m/0" would be [0] and m/0/0 would be [0,0] etc.
    indexes = []
    if len(sys.argv) >= 2:
        for row in csv.reader([sys.argv[1]]):
            for val in row:
                indexes.append(int(val))

    # nul test data if not provided on cmd line
    to_sign_hash = bytes(32)
    if len(sys.argv) >= 3:
        to_sign_hash = binascii.unhexlify(sys.argv[2])
        if len(to_sign_hash) != 32:
            print("provided hash should be 32 bytes long, not " + str(len(to_sign_hash)))
            exit(1)

    # Get the available device slots
    slots = mirkey.enumerate_slots()

    if len(slots) > 0:
        # Use the first available slot
        slot = slots[0]

        # Initialize the library
        mirkey.init()
        try:
            session = mirkey.get_logged_in_rw_session(slot, pin)
            found, handle = mirkey.bip32_has_root_key(session)
            if not found:
                print("No master key found, importing test master key.")
                mirkey.bip32_import_root_key(session, binascii.unhexlify("000102030405060708090a0b0c0d0e0f"))

            sig = mirkey.bip32_sign_data(session, to_sign_hash, indexes)
            print(binascii.hexlify(sig).decode("utf-8"))

        finally:
            mirkey.finalize()
    else:
        print("No devices found")
