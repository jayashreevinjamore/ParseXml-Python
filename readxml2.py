import xml.etree.ElementTree as ET
import csv
#import xml.dom.minidom as md
#
def main():


	tree = ET.parse("D:\PPTV\Collins\DMC-31218-A-25-20-43-01000-941A-D_002-00_EN-US.XML")
	root=tree.getroot()
	#open a file for writing
	Output_file=open('D:\PPTV\Collins\out.csv','w')
	#create csv writer object
	csvwriter=csv.writer(Output_file)
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
	out_head=[]
	
	out_head.append('DescforPart')
	csvwriter.writerow(out_head)
	count=1
	for con in root.findall('content'):
		for d in con.iter('descrForPart'):
			print("DescForPart=",d.text);
			out_det=[]
			out_det.append(count);
			out_det.append(d.text);
			csvwriter.writerow(out_det);
			count=count+1;
	Output_file.close();
#	doc=md.parse("D:\PPTV\Collins\DMC-31218-A-25-20-43-01000-941A-D_002-00_EN-US.XML");
#	print(doc.nodeName)
#	print(doc.firstChild)
#	print(doc.firstChild.TagName)
	
if __name__== "__main__": main();
