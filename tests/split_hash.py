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

import os
import json


path_to_json = 'hashes/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

def readandprint(header_hex, file_name):
    # header_hex
    hhex = header_hex

    _vers = 8      # 4  Bytes -> version                     ->  int32_t
    _pbhh = 64     # 32 Bytes -> previous block header hash  ->  char[32]
    _merh = 64     # 32 Bytes -> merkle root hash            ->  char[32]
    _time = 8      # 4  Bytes -> time                        ->  uint32_t
    _nbts = 8      # 4  Bytes -> nBits                       ->  uint32_t
    _noce = 8      # 4  Bytes -> nonce                       ->  uint32_t

    _vers_hex = hhex[0:_vers]
    _pbhh_hex = hhex[_vers:_vers+_pbhh]
    _merh_hex = hhex[_vers+_pbhh:_vers+_pbhh+_merh]
    _time_hex = hhex[_vers+_pbhh+_merh:_vers+_pbhh+_merh+_time]
    _nbts_hex = hhex[_vers+_pbhh+_merh+_time:_vers+_pbhh+_merh+_time+_nbts]
    _noce_hex = hhex[_vers+_pbhh+_merh+_time+_nbts:_vers+_pbhh+_merh+_time+_nbts+_noce]

    print('{:-<132}'.format(''), end='\n')
    print(file_name)
    print('{:-<132}'.format(''), end='\n')
    print('4  Bytes -> version                     ->  int32_t : '+_vers_hex)
    print('32 Bytes -> previous block header hash  ->  char[32]: '+_pbhh_hex)
    print('32 Bytes -> merkle root hash            ->  char[32]: '+_merh_hex)
    print('4  Bytes -> time                        ->  uint32_t: '+_time_hex)
    print('4  Bytes -> nBits                       ->  uint32_t: '+_nbts_hex)
    print('4  Bytes -> nonce                       ->  uint32_t: '+_noce_hex)



for index, js in enumerate(json_files):
    with open(os.path.join(path_to_json, js)) as json_file:
        json_dict = json.load(json_file)
        header_hex = json_dict['block'][0:160]
        readandprint(header_hex,js)

