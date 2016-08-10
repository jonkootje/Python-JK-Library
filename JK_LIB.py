# JK_LIB IS A PYTHON LIBRARY BY WEB-SJ
# ------------------------------------
# Visit our website: http://www.web-sj.com
# Contact us: info@web-sj.com


import urllib.request
import json
import os.path
import pickle


def readfile(path):
	file_data = open(path, 'r')
	return file_data.read()

def writefile(path, data):
	file = open(path, 'w')
	file.write(data)
	file.close()
	return 1

def getjson(url):
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
	headers={'User-Agent':user_agent,} 

	request=urllib.request.Request(url,None,headers)
	response = urllib.request.urlopen(request)
	data = json.loads(response.read().decode("utf-8"))
	return data

def writeinline(text):
	print(text, end="")
	return True

def serialize(data):
	return pickle.dumps(data)

def unserialize(data):
	return pickle.loads(data)

class database:
	
	__currentdb = False
	__dbpath = "JKDB/"

	def __init__(self, name, directory = "JKDB"):
		if (not os.path.exists(self.__dbpath)):
			os.makedirs(self.__dbpath)
		if (not self.exist(name)):
			self.create(name)

		self.__dbpath = directory + "/"
		self.set(name)
		return None

	def exist(self, name):
		return os.path.isfile(self.__dbpath + name)

	def set(self, name):
		self.__currentdb = name
		return False

	def push(self, data):
		return self.__pushdata(data)

	def create(self, name):
		if (self.exist(name)):
			return False
		else:
			prev = self.__currentdb
			self.__currentdb = name
			self.__pushdata({})
			self.__currentdb = prev
			return True

	def get(self):
		return self.__getdata()

	def __pushdata(self, data):
		path = self.__dbpath + self.__currentdb + ".jkdb"
		pickle.dump(data, open(path, 'wb'))
		return True
	def __getdata(self):
		return pickle.load(open(self.__dbpath + self.__currentdb + ".jkdb", "rb"))
