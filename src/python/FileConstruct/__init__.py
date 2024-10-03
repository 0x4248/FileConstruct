# FileConstruct
# Construct custom files with ease.
# 
# Setup.py
# 
# COPYRIGHT NOTICE
# Copyright (C) 2024 0x4248 and contributors
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the license is not changed.
# 
# This software is free and open source. Licensed under the GNU general
# public license version 3.0 as published by the Free Software Foundation.


# Imports
import os
import logging


# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("FileConstructor")


class FileConstructor:
    def __init__(self):
        """Constructor object for creating a file."""
        self.data = bytearray() 
        self.filename = ""
        self.size = 0 
        self.verbose = False

    def set_verbose(self, verbose):
        """Set verbose logging on or off."""
        self.verbose = verbose

    def _log(self, message):
        """Helper function for verbose logging."""
        if self.verbose:
            logger.info(message)

    def PutByte(self, byte_value):
        """Place a single byte into the file."""
        self._log(f"PLACE: {byte_value} LOCATION: {self.size}")
        self.data.append(byte_value & 0xFF)
        self.size += 1

    def PutBytes(self, byte_array):
        """Place an array of bytes into the file."""
        self._log(f"PUTBYTES: {byte_array} LOCATION: {self.size}")
        self.data.extend(byte_array)
        self.size += len(byte_array)

    def PutASCII(self, ascii_string):
        """Place an ASCII string into the file."""
        self._log(f"PUTASCII: {ascii_string} LOCATION: {self.size}")
        self.PutBytes(ascii_string.encode('ascii'))

    def PutString(self, string):
        """Place a string into the file."""
        self._log(f"PUTSTRING: {string} LOCATION: {self.size}")
        self.PutBytes(string.encode('utf-8'))

    def PutInt(self, int_value):
        """Place an integer into the file."""
        self._log(f"PUTINT: {int_value} LOCATION: {self.size}")
        self.PutBytes(int_value.to_bytes(4, 'big'))

    def PutBool(self, bool_value):
        """Place a boolean into the file."""
        self._log(f"PUTBOOL: {bool_value} LOCATION: {self.size}")
        self.PutByte(1 if bool_value else 0)

    def PutBit(self, bit_value):
        """Place a bit (0 or 1) into the file."""
        self._log(f"PUTBIT: {bit_value} LOCATION: {self.size}")
        self.PutByte(bit_value & 1)

    def PutHexStr(self, hex_string):
        """Place a hex string into the file."""
        self._log(f"PUTHEXSTR: {hex_string} LOCATION: {self.size}")
        hex_bytes = bytes.fromhex(hex_string)
        self.PutBytes(hex_bytes)

    def Fill(self, length, pattern):
        """Fill the file with a byte array pattern."""
        self._log(f"FILL: {pattern} LENGTH: {length} LOCATION: {self.size}")
        while len(pattern) < length:
            pattern *= 2  # Repeat the pattern if needed
        self.PutBytes(pattern[:length])

    def ReplaceByte(self, index, byte_value):
        """Replace a byte at a specific index."""
        self._log(f"REPLACEBYTE: {byte_value} LOCATION: {index}")
        self.data[index] = byte_value & 0xFF

    def ReplaceBytes(self, index, byte_array):
        """Replace a byte array at a specific index."""
        self._log(f"REPLACEBYTES: {byte_array} LOCATION: {index}")
        self.data[index:index + len(byte_array)] = byte_array

    def ReplaceASCII(self, index, ascii_string):
        """Replace an ASCII string at a specific index."""
        self._log(f"REPLACEASCII: {ascii_string} LOCATION: {index}")
        self.ReplaceBytes(index, ascii_string.encode('ascii'))

    def ReplaceString(self, index, string):
        """Replace a string at a specific index."""
        self._log(f"REPLACESTRING: {string} LOCATION: {index}")
        self.ReplaceBytes(index, string.encode('utf-8'))

    def ReplaceInt(self, index, int_value):
        """Replace an integer at a specific index."""
        self._log(f"REPLACEINT: {int_value} LOCATION: {index}")
        self.ReplaceBytes(index, int_value.to_bytes(4, 'big'))

    def ReplaceBool(self, index, bool_value):
        """Replace a boolean at a specific index."""
        self._log(f"REPLACEBOOL: {bool_value} LOCATION: {index}")
        self.ReplaceByte(index, 1 if bool_value else 0)

    def ReplaceBit(self, index, bit_value):
        """Replace a bit at a specific index."""
        self._log(f"REPLACEBIT: {bit_value} LOCATION: {index}")
        self.ReplaceByte(index, bit_value & 1)

    def Dump(self):
        """Write the file data to disk."""
        self._log(f"DUMP: {self.filename}")
        if not self.filename:
            raise ValueError("Filename not set.")
        with open(self.filename, 'wb') as f:
            f.write(self.data)
        self._log(f"WROTE: {self.size} BYTES TO: {self.filename}")

    def Load(self, filename):
        """Load a file from disk."""
        self._log(f"LOAD: {filename}")
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '{filename}' not found.")
        with open(filename, 'rb') as f:
            self.data = bytearray(f.read())
        self.size = len(self.data)
        self._log(f"LOADED: {self.size} BYTES FROM: {filename}")
