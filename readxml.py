import xml.etree.ElementTree as ET
#import xml.dom.minidom as md
#
def main():


	tree = ET.parse("D:\PPTV\Collins\DMC-31218-A-25-20-43-01000-941A-D_002-00_EN-US.XML")
	root=tree.getroot()
	
	print("******** root ********");
	print(root);
	print("******** root.tag *********");
	print(root.tag);
	print("******** root.attrib *********");
	print(root.attrib);
	print("**********************");
	# for child in root:
	# 	print(child.tag,child.attrib);
	# 	for gchild in child:
	# 		print(gchild.tag);
	# 		if gchild.tag == "content "
	# 			for ggchild in gchild:
	# 				print(ggchild.tag);
	
	for con in root.findall('content'):
		for ref in con.findall('refs'):
			for dmref in ref.findall('dmRef'):
				for dmrefI in dmref.findall('dmRefIdent'):
					for dmcod in dmrefI.findall('dmCode'):
						print("InfoCode=",dmcod.get('infoCode'));
						print("infoCodeVariant=",dmcod.get('infoCodeVariant'));
						print("itemLocationCode=",dmcod.get('itemLocationCode'));
						

	# for con in root.findall('content'):
	# 	for illpartcat in con.findall('illustratedPartsCatalog'):
	# 		for catseq in illpartcat.findall('catalogSeqNumber'):
	# 			for itemseq in catseq.findall('itemSeqNumber'):
	# 				print("PartRef=",itemseq.attrib);
	# 				print("QuantityperNextHigherAssy=",itemseq.find('quantityPerNextHigherAssy').text);
	# 				for p in itemseq.iter('descrForPart'):
	# 					print("DescForPart=",p.text);
	#						print("DescforPart=",itemid.find('descrForPart').text);

	print("**********************");
	for con in root.findall('content'):
		for d in con.iter('descrForPart'):
			print("*DescForPart=",d.text);
#	doc=md.parse("D:\PPTV\Collins\DMC-31218-A-25-20-43-01000-941A-D_002-00_EN-US.XML");
#	print(doc.nodeName)
#	print(doc.firstChild)
#	print(doc.firstChild.TagName)
	
if __name__== "__main__": main();
