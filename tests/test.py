import neoscrypt
from binascii import unhexlify, hexlify

import unittest

# [ z3r0@z3r0dev ]$ sparks-cli getblockhash 1000
# 00000000020ff055aa61a4d11d1d66730d7e0534dc8570dc2d40c45b675b2582
#
# [ z3r0@z3r0dev ]$ sparks-cli getblock 00000000020ff055aa61a4d11d1d66730d7e0534dc8570dc2d40c45b675b2582
#
# {
#   "hash": "00000000020ff055aa61a4d11d1d66730d7e0534dc8570dc2d40c45b675b2582",
#   "confirmations": 277046,
#   "size": 196,
#   "height": 1000,
#   "version": 536870912,
#   "versionHex": "20000000",
#   "merkleroot": "665fabda52881b52894d5b30feead9755d0679ee8fa832f26a82bba039c25745",
#   "tx": [
#     "665fabda52881b52894d5b30feead9755d0679ee8fa832f26a82bba039c25745"
#   ],
#   "time": 1514021201,
#   "mediantime": 1514020761,
#   "nonce": 3752529043,
#   "bits": "1c027039",
#   "difficulty": 104.9865770552124,
#   "chainwork": "000000000000000000000000000000000000000000000000000050622e98170b",
#   "previousblockhash": "00000000022df0e0facb9d2c6f64636cf1d8452ccfd8d3243fa83caa8a6d9259",
#   "nextblockhash": "0000000001f650b5718c1509816f8fb5a351bd8fc6f0ed2da66edcca0aa5f328"
# }

# ------------------------------------------------------------------------------------------------------------------------------------
# sparks_mainnet_1000.json
# ------------------------------------------------------------------------------------------------------------------------------------
# 4  Bytes -> version                     ->  int32_t : 00000020
# 32 Bytes -> previous block header hash  ->  char[32]: 59926d8aaa3ca83f24d3d8cf2c45d8f16c63646f2c9dcbfae0f02d0200000000
# 32 Bytes -> merkle root hash            ->  char[32]: 4557c239a0bb826af232a88fee79065d75d9eafe305b4d89521b8852daab5f66
# 4  Bytes -> time                        ->  uint32_t: 51213e5a
# 4  Bytes -> nBits                       ->  uint32_t: 3970021c
# 4  Bytes -> nonce                       ->  uint32_t: 930cabdf

header_hex = ("00000020"+
             "59926d8aaa3ca83f24d3d8cf2c45d8f16c63646f2c9dcbfae0f02d0200000000"+
              "4557c239a0bb826af232a88fee79065d75d9eafe305b4d89521b8852daab5f66"+
              "51213e5a"+
              "3970021c"+
              "930cabdf")
best_hash = b'82255b675bc4402ddc7085dc34057e0d73661d1dd1a461aa55f00f0200000000'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_neoscrypt_hash(self):
        self.pow_hash = hexlify(neoscrypt.getPoWHash(self.block_header))


if __name__ == '__main__':
    unittest.main()
