import re
from marshmallow import Schema, fields, INCLUDE, post_load
from marshmallow.utils import missing


class Seller(Schema):
    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE

    sellerId = fields.Int()
    name = fields.Str()
    address = fields.Str()
    branch = fields.Str()
    licenceNumber = fields.Str()
    sellerType = fields.Str()
    showContactForm = fields.Bool()

    phone = fields.Str()
    phoneWhenToCall = fields.Str()
    alternativePhone = fields.Str()

    profileImage = fields.Str()
    standardLogo = fields.Str()
    squareLogo = fields.Str()
    backgroundColour = fields.Str()


class ListingMedia(Schema):
    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE

    images = fields.List(fields.Dict(keys=fields.Str(), values=fields.Str()), default=[])

    totalImages = fields.Int()
    hasVideo = fields.Bool(default=False)
    hasVirtualTour = fields.Bool(default=False)
    hasBrochure = fields.Bool(default=False)


class ListingBER(Schema):
    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE

    rating = fields.Str()
    code = fields.Str()
    epi = fields.Str()


class ListingPoint(Schema):
    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE

    point_type = fields.Str(data_key="type")
    coordinates = fields.List(fields.Int())


class ListingPRS(Schema):
    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE

    totalUnitTypes = fields.Int()
    subUnits = fields.List(fields.Nested(lambda: Listing()))
    tagLine = fields.Str()
    location = fields.Str()
    aboutDevelopment = fields.Str()
    brochure = fields.Str()


class Listing(Schema):
    URL_BASE = "https://daft.ie"
    PRICE_RE = re.compile(r'[0-9,]+')

    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE

    def convert_price(self, value):
        matches = self.PRICE_RE.findall(value)
        if matches:
            price_int = int(matches[0].replace(',', ''))
            if "week" in value:
                price_int *= 4.34
            return price_int
        return missing

    def convert_bed_and_bath(self, value):
        matches = re.findall(r'\d+', value)
        if matches:
            return int(matches[0])
        return missing

    def get_url(self, seo_friendly_path):
        return "".join([self.URL_BASE, seo_friendly_path])

    @post_load
    def post_load(self, data, **kwargs):
        data['url'] = self.get_url(data['seoFriendlyPath'])
        return data

    id = fields.Int()
    title = fields.Str()

    seoTitle = fields.Str()
    seoFriendlyPath = fields.Str()
    sections = fields.List(fields.Str(), default=[])
    saleType = fields.List(fields.Str(), default=[])
    featuredLevel = fields.Str()

    publishDate = fields.Int()
    price = fields.Method(deserialize="convert_price")
    abbreviatedPrice = fields.Str()
    category = fields.Str()
    state = fields.Str()

    numBedrooms = fields.Method(deserialize="convert_bed_and_bath")
    numBathrooms = fields.Method(deserialize="convert_bed_and_bath")
    propertyType = fields.Str()
    daftShortcode = fields.Str()

    seller = fields.Nested(Seller, default=Seller())
    media = fields.Nested(ListingMedia, default=ListingMedia())
    image = fields.Dict(keys=fields.Str(), values=fields.Str())
    ber = fields.Nested(ListingBER, default=ListingBER())
    prs = fields.Nested(ListingPRS, default=ListingPRS())
