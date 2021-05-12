# please run with python3 tests.py


from spyne import ComplexModel, String, Integer, Array, DateTime, ByteArray, Unicode, Decimal, ServiceBase, rpc, Application, AnyDict
# from exim.models import ExportFSS
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from django.views.decorators.csrf import csrf_exempt
from spyne.server.django import DjangoApplication


class Man(ComplexModel):
    __namespace__ = ''
    ManName = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    ManFathername = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    ManFamily = String(max_len=100).customize(max_occurs=1, min_occurs=0)

    @staticmethod
    def generate():
        return {
            'ManName': 'hello',
            'ManFathername': 'hello',
            'ManFamily': 'hello',
        }


class transport(ComplexModel):
    __namespace__ = ''
    DeclaredType = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    DeclaredTypeCode = Integer.customize(max_occurs=1, min_occurs=0)
    Number = String.customize(max_occurs=1, min_occurs=0)

    @staticmethod
    def generate():
        return {
            'DeclaredType': 'hello',
            'DeclaredTypeCode': 0,
            'Number': 'hello',
        }


class consignor(ComplexModel):
    __namespace__ = ''
    Name = String(max_len=255).customize(max_occurs=1, min_occurs=0)
    Code = String(max_len=10).customize(max_occurs=1, min_occurs=0)
    Identifier = String(max_len=36).customize(max_occurs=1, min_occurs=0)
    Place = String(max_len=512).customize(max_occurs=1, min_occurs=0)
    Address = String(max_len=512).customize(max_occurs=1, min_occurs=0)
    AddressCode = String(max_len=36).customize(max_occurs=1, min_occurs=0)
    Agent = String(max_len=255).customize(max_occurs=1, min_occurs=0)
    AgentCode = Integer.customize(max_occurs=1, min_occurs=0)
    Behalf = String(max_len=512).customize(max_occurs=1, min_occurs=0)
    man = Man
    Type = Integer.customize(max_occurs=1, min_occurs=0)

    @staticmethod
    def generate():
        return {
            'Name': 'hello',
            'Code': 0,
            'Identifier': '0000000000',
            'Place': 'hello',
            'Address': 'hello',
            'AddressCode': 0,
            'Agent': 'hello',
            'AgentCode': 0,
            'Behalf': 'hi',
            'man': Man,
            'Type': 0,
        }


class consignee(ComplexModel):
    __namespace__ = ''
    Name = String(max_len=255).customize(max_occurs=1, min_occurs=0)
    Code = String(max_len=10).customize(max_occurs=1, min_occurs=0)
    Identifier = String(max_len=36).customize(max_occurs=1, min_occurs=0)
    Place = String(max_len=512).customize(max_occurs=1, min_occurs=0)
    Address = String(max_len=512).customize(max_occurs=1, min_occurs=0)
    AddressCode = String(max_len=36).customize(max_occurs=1, min_occurs=0)
    Agent = String(max_len=255).customize(max_occurs=1, min_occurs=0)
    AgentCode = Integer.customize(max_occurs=1, min_occurs=0)
    Behalf = String(max_len=512).customize(max_occurs=1, min_occurs=0)
    # man = Man
    Type = Integer.customize(max_occurs=1, min_occurs=0)

    @staticmethod
    def generate():
        return {
            'Name': 'hello',
            'Code': 0,
            'Identifier': '0000000000',
            'Place': 'hello',
            'Address': 'hello',
            'AddressCode': 'hi',
            'Agent': 'hi',
            'AgentCode': 0,
            'Behalf': 'hi',
            'Type': 0,
        }


class disinfection(ComplexModel):
    __namespace__ = ''
    Date = DateTime.customize(max_occurs=1, min_occurs=0)
    Method = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    Chemical = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    TemperatureTimes = String(max_len=100).customize(
        max_occurs=1, min_occurs=0)
    Concentration = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    AdditionalInfo = String(max_len=2000).customize(max_occurs=1, min_occurs=0)

    @staticmethod
    def generate():
        return {
            'Date': 'hello',
            'Method': 'hello',
            'Chemical': 'hello',
            'TemperatureTimes': 'hello',
            'Concentration': 'hello',
            'AdditionalInfo': 'hello',
        }


class productDescription(ComplexModel):
    __namespace__ = ''
    NameRus = String(max_len=255).customize(max_occurs=1, min_occurs=0)
    NameEng = String(max_len=255).customize(max_occurs=1, min_occurs=0)
    NameBotanic = String(max_len=255).customize(max_occurs=1, min_occurs=0)
    Code = Integer.customize(max_occurs=1, min_occurs=0)
    HS = String(max_len=512).customize(max_occurs=1, min_occurs=0)
    # we have to find datatype of HSCode
    HSCode = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    OriginPlace = String(max_len=512).customize(max_occurs=1, min_occurs=0)
    OriginCountry = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    OriginCountryCode = String(max_len=2).customize(max_occurs=1, min_occurs=0)
    Manufacturer = String(max_len=255).customize(max_occurs=1, min_occurs=0)
    ManufacturerCode = Integer.customize(max_occurs=1, min_occurs=0)
    Quantity = Decimal(max_len=3).customize(max_occurs=1, min_occurs=0)
    QuantityUnit = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    QuantityUnitCode = String(max_len=3).customize(max_occurs=1, min_occurs=0)
    QuantityGross = Decimal(max_len=3).customize(max_occurs=1, min_occurs=0)
    QuantityGrossUnit = String(max_len=100).customize(
        max_occurs=1, min_occurs=0)
    QuantityGrossUnitCode = String(
        max_len=3).customize(max_occurs=1, min_occurs=0)
    QuantitySpecial = Decimal(max_len=3).customize(max_occurs=1, min_occurs=0)
    QuantitySpecialUnit = String(max_len=100).customize(
        max_occurs=1, min_occurs=0)
    QuantitySpecialUnitCode = String(
        max_len=3).customize(max_occurs=1, min_occurs=0)
    Packages = Integer.customize(max_occurs=1, min_occurs=0)
    PackagesUnit = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    PackagesUnitCode = String(max_len=3).customize(max_occurs=1, min_occurs=0)
    # we have to find datatypes of PackagesType and PackagesTypeCode
    PackagesType = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    PackagesTypeCode = String(max_len=100).customize(
        max_occurs=1, min_occurs=0)
    PackagesDescription = String(max_len=512).customize(
        max_occurs=1, min_occurs=0)
    Volume = Decimal(max_len=3).customize(max_occurs=1, min_occurs=0)
    VolumeUnit = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    VolumeUnitCode = String(max_len=3).customize(max_occurs=1, min_occurs=0)
    Marking = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    AdditionalInfo = String(max_len=2000).customize(max_occurs=1, min_occurs=0)

    @staticmethod
    def generate():
        return {
            'NameRus': 'hello',
            'NameEng': 'hello',
            'NameBotanic': 'hello',
            'Code': 'hello',
            'HS': 'hi',
            'HSCode': 'hello',
            'OriginPlace': 'Tashkent',
            'OriginCountry': 'hello',
            'OriginCountryCode': 'hello',
            'Manufacturer': 'hi',
            'ManufacturerCode': 0,
            'Quantity': 'hello',
            'QuantityUnit': 'hello',
            'QuantityUnitCode': 90,
            'QuantityGross': 'hello',
            'PackagesUnit': 'hello',
            'PackageUnitCode': 'hello',
            'PackagesType': 'hi',
            'PackagesTypeCode': 0,
            'PackagesDescription': 'hi',
            'Volume': 0,
            'VolumeUnit': 'hi',
            'VolumeUnitCode': 0,
            'Marking': 'hi',
            'AdditionalInfo': 'hi',
        }


class certificate(ComplexModel):
    __namespace__ = ''
    ID = Integer.customize(max_occurs=1, min_occurs=0)
    GUID = Unicode(128, pattern='[^@]+@[^@]+')
    SendDateTime = DateTime.customize(max_occurs=1, min_occurs=0)
    Number = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    Date = DateTime.customize(max_occurs=1, min_occurs=0)
    Blanc = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    DepartureCountry = String(max_len=100).customize(
        max_occurs=1, min_occurs=0)
    DepartureCountryCode = String(max_len=2).customize(
        max_occurs=1, min_occurs=0)
    DestinationCountry = String(max_len=100).customize(
        max_occurs=1, min_occurs=0)
    DestinationCountryCode = String(
        max_len=2).customize(max_occurs=1, min_occurs=0)
    EntryCheckpoint = String(max_len=255).customize(max_occurs=1, min_occurs=0)
    EntryCheckpointCode = Integer.customize(max_occurs=1, min_occurs=0)
    Consignor = consignor
    Consignee = consignee
    Transport = transport
    Disinfection = disinfection
    Productdescription = productDescription
    GeneralMarking = String(max_len=512).customize(max_occurs=1, min_occurs=0)
    GeneralQuarantineCondition = String(
        max_len=512).customize(max_occurs=1, min_occurs=0)
    GeneralBaseDocument = String(max_len=512).customize(
        max_occurs=1, min_occurs=0)
    GeneralAdditionalDeclaration = String(
        max_len=512).customize(max_occurs=1, min_occurs=0)
    GeneralMandatoryActions = String(
        max_len=512).customize(max_occurs=1, min_occurs=0)
    AdditionalInfo = String(max_len=2000).customize(max_occurs=1, min_occurs=0)
    Inspector = String(max_len=255).customize(max_occurs=1, min_occurs=0)
    AnnexDoc = String(max_len=100000).customize(max_occurs=1, min_occurs=0)
    AnnexText = String(max_len=100000).customize(max_occurs=1, min_occurs=0)
    # PDF = ByteArray.customize(max_occurs=1, min_occurs=0)

    #         'Blanc'omize(max_occurs=1, min_occurs=0)
    # PDF = ByteArray.customize(max_occurs=1, min_occurs=0)

    @staticmethod
    def generate():
        return {
            'ID': 'hello',
            # Guid
            'SendDateTime': 'hello',
            'Number': 'hello',
            'Date': 'hello',
            'Blanc': 'hi',
            'DepartureCountry': 'hello',
            'DepartureCountryCode': 'hello',
            'DestinationCountry': 'hello',
            'DestinationCountryCode': 'hello',
            'consignor': Consignor,
            'consignee': Consignee,
            'transport': Transport,
            'disinfection': Disinfection,
            'productDescription': ProductDescription,
            'GeneralMarking': 'hello',
            'GeneralQuarantineCondition': 'Карантинных объектов не обнаружено',
            'GeneralBaseDocument': 'hi',
            'GeneralAdditionalDeclaration': 'hello',
            'GeneralMandatoryActions': 'hello',
            'AdditionalInfo': 'hello',
            'Inspector': 'hello',
        }


class request91(ComplexModel):
    __namespace__ = ''
    GUID = Unicode(128, pattern='[^@]+@[^@]+')
    SendDateTime = DateTime.customize(max_occurs=1, min_occurs=0)
    Certificate = certificate
    Status = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    StatusCode = Integer.customize(max_occurs=1, min_occurs=0)
    Inspector = String(max_len=255).customize(max_occurs=1, min_occurs=0)

    @staticmethod
    def generate():
        return{
            # 'GUID':
            'SendDateTime': 'hello',
            'certificate': Certificate,
            'Status': 'Выдан',
            'StatusCode': 'I dnt find',
            'Inspector': 'hello',
        }


# def statement_generator(invoice_payment_number=None):
#     return {
#         "id": invoice_payment_numberExportFSSApplicationStatusStep,
#     }

class ArgusFitoView(ServiceBase):
    @rpc(request91,
         _returns=AnyDict,
         _out_variable_name="PhytosanitaryControlRequest")
    def Request91(ctx, request91):
        try:
            logging.info(
                f'Initialized objects {str(request91).encode("utf-8")} ')
            success_status = None
            success_status_code = None
            # agreement_number = None
            # info_service = []
            # subject_info_len = 0
            # service_type = None
            if request91.Status == "4":
                success_status_code = Post_codes.not_matched
                success_status = Post_codes.dictionary_ru.get(
                    success_status_code)
            elif request91.Status == "9":
                success_status_code = Post_codes.post
                success_status = Post_codes.dictionary_ru.get(
                    success_status_code)
            else:
                pass

        except Exception as e:
            logging.info(f'Exception occurred: {str(e)}')


def on_method_return_string(ctx):
    # ctx.out_string[0] = ctx.out_string[0].replace(b'xs', b'tns')
    ctx.out_string[0] = ctx.out_string[0].replace(
        b'uzu:request91', b'uzu:Request91')


ArgusFitoView.event_manager.add_listener('method_return_string',
                                         on_method_return_string)

application = Application([ArgusFitoView],
                          tns='https://argusgate.fitorf.ru/srv/ws/uz2',
                          #   tns='https://argusgate.fitorf.ru',
                          name="ArgusfitoBinding",
                          in_protocol=Soap11(validator='soft'),
                          out_protocol=Soap11(),
                          )

# wsgi = WsgiApplication(application)


# if __name__ == '__main__':

#     import logging

#     from wsgiref.simple_server import make_server

#     logging.basicConfig(level=logging.DEBUG)
#     logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

#     logging.info("listening to http://127.0.0.1:8010")
#     logging.info("wsdl is at: http://localhost:8010/?wsdl")

#     server = make_server('127.0.0.1', 8010, wsgi)
#     server.serve_forever()


argus_api = DjangoApplication(application)


def get_wsdl_file(request):
    with open('fito/UZ21.swdl', 'r') as f:
        docs = f.read()
    return HttpResponse(docs, content_type='text/xml; charset=utf-8')


@csrf_exempt
def service_dispatch(request):
    if request.get_full_path() in ('/srv/ws/uz2?wsdl',
                                   '/srv/ws/uz2_uz2?wsdl'):
        return get_wsdl_file(request)
    return argus_api(request)
