# -*- coding: utf-8 -*-

import MeCab


te = "r"

def checkWord(te):

	text = raw_input("入力 >>")


	tagger = MeCab.Tagger('Ochasen')
	node = tagger.parseToNode(text)
	keywords = []
	pos = []

	while node:
		if node.feature.split(",")[0] == "助詞" or node.feature.split(",")[0] == "‘ã–¼ŽŒ" or node.feature.split(",")[0] == "Š´“®ŽŒ" or node.feature.split(",")[0] == "Ú‘±ŽŒ" or node.feature.split(",")[0] == "助詞" or node.feature.split(",")[0] == "‹L†" or node.feature.split(",")[0] == "BOS/EOS":
			node = node.next
		else:
#			keywords.append(node.surface)
#	        	pos.append(node.feature.split(",")[0])
			pos.append(node.feature.split(",")[6])
			node = node.next

	return pos


if __name__ == "__main__":
	
	while 1:
		key = checkWord(te)
		string = "思う"
#if string == keywords:
	
		for w in key:
			print w,
			print
