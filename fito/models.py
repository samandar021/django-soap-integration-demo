from spyne import ComplexModel, String, Integer, Array, DateTime, ByteArray, Unicode, Decimal
# from exim.models import ExportFSS


class Man(ComplexModel):
    __namespace__ = ''
    ManName = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    ManFathername = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    ManFamily = String(max_len=100).customize(max_occurs=1, min_occurs=0)

    # @staticmethod
    # def generate()


class Transport(ComplexModel):
    __namespace__ = ''
    DeclaredType = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    DeclaredTypeCode = Integer.customize(max_occurs=1, min_occurs=0)
    Number = String.customize(max_occurs=1, min_occurs=0)


class Consignor(ComplexModel):
    __namespace__ = ''
    Name = String(max_len=255).customize(max_occurs=1, min_occurs=0)
    Code = String(max_len=10).customize(max_occurs=1, min_occurs=0)
    Identifier = String(max_len=36).customize(max_occurs=1, min_occurs=0)
    Place = String(max_len=512).customize(max_occurs=1, min_occurs=0)
    Address = String(max_len=512).customize(max_occurs=1, min_occurs=0)
    Behalf = String(max_len=512).customize(max_occurs=1, min_occurs=0)
    man = Man
    Type = Integer.customize(max_occurs=1, min_occurs=0)


class Consignee(ComplexModel):
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


class Disinfection(ComplexModel):
    __namespace__ = ''
    Date = DateTime.customize(max_occurs=1, min_occurs=0)
    Method = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    Chemical = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    TemperatureTimes = String(max_len=100).customize(
        max_occurs=1, min_occurs=0)
    Concentration = String(max_len=100).customize(max_occurs=1, min_occurs=0)
    AdditionalInfo = String(max_len=2000).customize(max_occurs=1, min_occurs=0)


class ProductDescription(ComplexModel):
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


class Certificate(ComplexModel):
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
    consignor = Consignor
    consignee = Consignee
    transport = Transport
    disinfection = Disinfection
    productdescription = ProductDescription
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
    PDF = ByteArray.customize(max_occurs=1, min_occurs=0)


class Request91(ComplexModel):
    __namespace__ = ''
    GUID = Unicode(128, pattern='[^@]+@[^@]+')
    SendDateTime = DateTime.customize(max_occurs=1, min_occurs=0)
    certificate = Certificate


# def statement_generator(invoice_payment_number=None):
#     return {
#         "id": invoice_payment_number
#     }
