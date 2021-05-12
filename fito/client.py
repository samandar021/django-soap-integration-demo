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
session.proxies = {
    'http': 'http://192.168.145.2:3128',
    'https': 'https://192.168.145.2:3128'
}
certificates_folder = os.path.join(BASE_DIR, 'certificates')
session.cert = (
    os.path.join(certificates_folder, 'karantin_public_key.pem'),
    os.path.join(certificates_folder, 'karantin_private_key.pem')
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


wsdl_url = 'https://hub.ephytoexchange.org/hub/DeliveryService?wsdl'
# wsdl_url = 'https://uat-hub.ephytoexchange.org/hub/DeliveryService?wsdl'
settings = Settings(strict=False, xml_huge_tree=True)
session = Session()
client = Client(
    wsdl_url,
    transport=transport,
    settings=settings, plugins=[history, Corrector()])
logging.getLogger("zeep").propagate = False
client = client.service
