# Intended to hold all Document Objects and Methods
from xml.dom import minidom
from xml.dom.minidom import parse
import os
import csv

# TODO function to handle vertical CSV, not current horizontal format

# Object with one value, list of URL and Lang Codes
class Mapping:
    def __init__(self, pairs):
        self.allPairs = pairs 



class Document:
    def __init__(self) -> None:
        pass


    # Function to take CSV (Horizontal Format) and Input and return List of Mapping Objects
    def from_csv(self, file):
        mappings = []
        with open(file, mode='r', encoding='utf-8-sig', newline='') as csvfile:
            csvreader = csv.DictReader(csvfile, delimiter=',')
            for row in csvreader:
                urlsAndCodes = []
                for value in row.values():
                    urlsAndCodes.append(value)
                allPairsDict = {urlsAndCodes[i]: [] for i in range(0, len(urlsAndCodes), 2)}
                for i in range(0, len(urlsAndCodes), 2):
                    allPairsDict[urlsAndCodes[i]].append(urlsAndCodes[i + 1])
                m1 = Mapping(allPairsDict)
                mappings.append(m1)
        return mappings


    # Returns boilerplate for XML
    def create_base_doc(self):
        root = minidom.Document()
        urlSetElem = root.createElement('urlset')
        urlSetElem.setAttribute('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
        urlSetElem.setAttribute('xmlns:xhtml', 'http://www.w3.org/1999/xhtml')
        root.appendChild(urlSetElem)
        return root


    # Input XML file to remove select entries
    def from_xml(self, xml_file, removal_csv):
        pass

    # Takes list of Mappings from 'from_csv' method
    def build_url_entries(self, root, mappings):
        urlSetElem = root.childNodes[0]
        for map in mappings:
            for pair in map.allPairs:
                if pair:
                    urlElem = root.createElement('url')
                    urlSetElem.appendChild(urlElem)
                    locElem = root.createElement('loc')
                    urlElem.appendChild(locElem)
                    locElem.appendChild(root.createTextNode(pair))
                    for pair in map.allPairs:
                        if map.allPairs[pair][0] != '':
                            if len(map.allPairs[pair]) == 1:
                                xhtmlElem = root.createElement('xhtml:link')
                                xhtmlElem.setAttribute('rel', 'alternate')
                                xhtmlElem.setAttribute('hreflang', map.allPairs[pair][0])
                                xhtmlElem.setAttribute('href', pair)

                                urlElem.appendChild(xhtmlElem)
                            elif len(map.allPairs[pair]) > 1:
                                for i in range(len(map.allPairs[pair])):
                                    xhtmlElem = root.createElement('xhtml:link')
                                    xhtmlElem.setAttribute('rel', 'alternate')
                                    xhtmlElem.setAttribute('hreflang', map.allPairs[pair][i])
                                    xhtmlElem.setAttribute('href', pair)
                                    urlElem.appendChild(xhtmlElem)
        return root


    def export(self, root, filename):
        xml_str = root.toprettyxml(indent = "\t")
        save_path_file = filename
        with open(save_path_file, "w") as f:
            f.write(xml_str)
