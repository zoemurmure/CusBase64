"""
Author: zoemurmure
Data: 2020/07/31

version: 0.1
"""

class CusBase64(object):
    """
    Customized base64 algorithm
    You can set you own indexing string using the config() method.

    Usage: 
        b = CusBase64()
        b.encode('binary\x00string')  # Output: YmluYXJ5AHN0cmluZw==
        b.decode('YmluYXJ5AHN0cmluZw==') # Output: binary\x00string

        b.config('aABCDEFGHIJKLMNOPQRSTUVWXYZbcdefghijklmnopqrstuvwxyz0123456789+/')
        b.decode('c2UsYi1kYWM0cnUjdFlvbiAjb21wbFU0YP==') # Output: self-destruction complete
    """
    DEFAULT = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    def __init__(self):
        self.idx_str = CusBase64.DEFAULT

    def encode(self, str):
        """
        Encode string using the customized indexing string.

        - args:
            str: String to be encoded
        """
        # Get the binary string
        binary = ''.join([format(ord(c),'0>8b') for c in str])
        # Add additional zero
        binary = self.padding(binary)
        # Get the index in indexing string
        idxs = [int(binary[6*i:6*i+6], 2) for i in range(len(binary)//6)]

        result = ''.join([self.idx_str[i] for i in idxs])
        # add '='
        if len(str)%3 != 0:
            result = result + (3-len(str)%3)*'='
        
        print("%r" % result)


    def decode(self, str):
        """
        Decode string using the customized indexing string.

        - args:
            str: String to be decoded
        """
        if len(str) == 0:
            return

        # remove '='
        while str[-1]=='=':
            str = str[:-1]
        try:
            # Get the binary string
            binary = ''.join([format(self.idx_str.index(c), '0>6b') for c in str])

            # Remove additional zero
            binary = binary[:-(len(binary)%8)]

            result = ''.join([chr(int(binary[8*i:8*i+8], 2)) for i in range(len(binary)//8)])
        except ValueError:
            result = "Please check again!"
        
        print("%r" % result)
    
    def padding(self, binary):
        """
        Add additional zero while encoding string.

        - args:
            binary: Binary format of the string.
        - returns:
            Binary string with additional zero.
        """
        if len(binary)%6 == 0:
            return binary
        n = 6 - len(binary)%6
        binary = binary + n * '0'
        return binary


    def config(self, str):
        """
        Set customized indexing string.
        """
        self.idx_str = str
        print("New indexing string is %r" % self.idx_str)

