# -*-　coding:utf-8 -*-

import sys
import codecs
import sqlite3

enc = sys.stdout.encoding
sys.stdin = codecs.getreader(enc)(sys.stdin)

input_stream = "Hello"
ke = 1

con = sqlite3.connect("te.db",isolation_level=None)



def reply(input_stream):
	
	flag = 0
	c = con.cursor()
	c.execute(u"select * from tak")
	for row in c:
		if input_stream == row[0]:
			print u"Syst:"+row[1]
			flag = 1
			break
	
	if flag != 1:
		print u"Syst:"+u"もっとあなたのことが知りたいな"

def data_set():
	con = sqlite3.connect("te.db",isolation_level=None)


	td = u"""
	create table tak(
	  say varchar(100),
	  rep varchar(200)
	);
	"""
	con.executemany(u"insert into tak values(?,?)",
				[(u"こんにちは",u"こんにちわ！"),
				 (u"やあ",u"やっほー"),
				 (u"元気?",u"げんきだよー"),
				 (u"つらい",u"がんばろう")])
	con.commit()
#	c = con.cursor()
#	c.execute(u"select * from tak")
#	for row in c: # rowはtuple
#		print row[0], row[1]

	
if __name__ == '__main__':

#	data_set()


	while ke == 1:
		inst = unicode(raw_input(u"User:"))
		reply(inst)