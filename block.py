# coding:utf-8
import hashlib as hasher
import datetime as date


class Block:
	def __init__(self,index,timestamp,data,previous_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.hash_block()
	def hash_block(self):
		sha = hasher.sha256()
		# sha.update(str(self.index)+str(self.timestamp)+str(self.data)+str(self.previous_hash))
		sha.update(b"self.index"+b"self.timestamp"+b"self.data"+b"self.previous_hash")
		# 返回16进制加密结果
		return sha.hexdigest()
	# 创建一个起源块
def create_genesis_block():
	# 手动构造块链或任意先前块链的散列
	return Block(0,date.datetime.now(),'Genesis_block','0')
	# 起源块后续块链都会以何种方式陆续创建，怎么创建
def next_block(last_block):
	this_index = last_block.index+1
	this_timestamp = date.datetime.now()
	this_data = "hi,I am block "+str(this_index)
	this_hash = last_block.index
	return Block(this_index,this_timestamp,this_data,this_hash)
blockchain = [create_genesis_block()]
previous_block = blockchain[0]
# 在起源块之后追加队列
num_of_block_add = 20
# 添加块到链
for i in range(0,num_of_block_add):
	block_to_add = next_block(previous_block)
	blockchain.append(block_to_add)
	previous_block = block_to_add
	print ('Block #{} has been added to the blockchain'.format(block_to_add.index))
	print ('{} '.format(block_to_add.data))
	print ('hash:{}\n'.format(block_to_add.hash))


