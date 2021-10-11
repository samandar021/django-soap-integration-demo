import logging
import os
from io import BytesIO

from lxml import etree
from lxml.etree import XMLParser
from requests import Session
from zeep import Client, Settings
from zeep.plugins import HistoryPlugin
from zeep import Plugin
from zeep.transports import Transport

from argusmain.settings import BASE_DIR

session = Session()
session.verify = True
# you can use any proxy if u want
certificates_folder = os.path.join(BASE_DIR, 'certificates')
session.cert = (
 # you can use public and private keys
)
transport = Transport(session=session)
history = HistoryPlugin()


class Corrector(Plugin):

    def egress(self, envelope, http_headers, operation, binding_options):
        xmlString = etree.tostring(envelope, encoding='unicode')
        xmlString = xmlString.replace("&lt;", "<")
        xmlString = xmlString.replace("&gt;", ">")
        etree.fromstring(xmlString, parser=XMLParser(
            recover=True, strip_cdata=False))
        return envelope, http_headers

    # def ingress(self, envelope, http_headers, client):
    #     return envelope, http_headers


wsdl_url = 'service link  ' # you have to add service link for send POST request

settings = Settings(strict=False, xml_huge_tree=True)
session = Session()
client = Client(
    wsdl_url,
    transport=transport,
    settings=settings, plugins=[history, Corrector()])
logging.getLogger("zeep").propagate = False
client = client.service
