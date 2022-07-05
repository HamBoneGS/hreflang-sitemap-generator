from xml.dom import minidom
import os
import csv

from mapper import Mapping, Document

doc = Document()

maps = doc.from_csv('/Users/npd_graham/Documents/code/NPD/hreflang_map_gen/Gen Input Files/intuit-formatted-input.csv')

root1 = doc.create_base_doc()

root2 = doc.build_url_entries(root1, maps)

doc.export(root2, 'intuit-hreflang.xml')

