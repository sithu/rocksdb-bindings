from rdb import RDB

import hashlib 

import random

import concurrent.futures

def _map(arg):
  key = arg
  # create drow instance
  db = RDB(f'/tmp/boost_{key:09d}.rdb')
  for i in range(100000):
    value = f'{random.random()}'
    ha   = hashlib.sha256(bytes(value, 'utf8')).hexdigest()
    db.put(ha, value)
    val = db.get(ha)

args = list(range(20))

with concurrent.futures.ProcessPoolExecutor(max_workers=20) as exe:
  exe.map(_map, args)
