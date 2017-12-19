xml_start_cfg = '''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE CIM PUBLIC "SYSTEM" "CIM_DTD_V20.dtd"[
<!ENTITY lt      "&#38;#60;">
<!ENTITY gt      "&#62;">
<!ENTITY amp     "&#38;#38;">
<!ENTITY apos    "&#39;">
<!ENTITY quot    "&#34;">]>
<CIM CIMVERSION="2.0" DTDVERSION="2.2">
<DECLARATION>
<DECLGROUP>
<VALUE.OBJECT>
<INSTANCE CLASSNAME="Header">
<PROPERTY NAME="Date" TYPE="string">
	<VALUE></VALUE>
</PROPERTY>
<PROPERTY NAME="Application" TYPE="string">
	<VALUE>test</VALUE>
</PROPERTY>
</INSTANCE>
</VALUE.OBJECT>'''

xml_end_cfg = '''
</DECLGROUP>
</DECLARATION>
</CIM>'''

xml_id_counter = 0

def increment():
		global xml_id_counter
		xml_id_counter += 1
		return xml_id_counter

text = ''
text = text + xml_start_cfg

with open ("/Users/intruder04/dev_projects/python/create_xml/ids.txt", "r") as myfile:
	for sber_id in myfile:
		# sber_id = sber_id.strip('')
		sber_id = sber_id.replace('\n', ' ').replace('\r', '').replace(' ', '')
		# print (sber_id)
		xml_text = '''
		<VALUE.OBJECT>
		<INSTANCE CLASSNAME="IN_PROGRESS">
	<PROPERTY NAME="ID" TYPE="string">
		<VALUE>%(counter)s</VALUE>
	</PROPERTY>
	<PROPERTY NAME="СБ_ID" TYPE="string">
		<VALUE>%(sber_id)s</VALUE>
	</PROPERTY>
		</INSTANCE>
	</VALUE.OBJECT>''' % {'counter': increment(), 'sber_id': sber_id}
		text = text + xml_text

text = text + xml_end_cfg

file_path = "/Users/intruder04/dev_projects/python/create_xml/output.xml"
fh = open(file_path, 'w+')
fh.write(text)














