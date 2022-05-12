import pprint as pp
import xml.etree.ElementTree as ET

root = ET.parse('master_annotation_BRC.xml')
words = []
for wordElement in root.iter('Sentence'):
    if wordElement.text is not None:
      words.append(wordElement.text)

pp.pprint(words)