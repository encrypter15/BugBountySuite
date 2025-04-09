# burpsuite.py—sucking vuln juice from Burp
import logging
import xml.etree.ElementTree as ET
from core.vulnerability_tracker import add_vulnerability

def import_burp_xml(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for issue in root.findall(".//issue"):
            url = issue.find("host").text
            title = issue.find("name").text
            poc = issue.find("requestresponse/request").text or "No PoC"
            severity = issue.find("severity").text
            add_vulnerability(url, title, poc, severity)
        logging.info(f"Imported vulns from {xml_file}—boom!")
    except Exception as e:
        logging.error(f"Burp import failed: {e}")
        raise
