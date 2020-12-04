from marshmallow import Schema, fields, INCLUDE


class Seller(Schema):
    sellerId = fields.Int()
    name = fields.Str()
    phone = fields.Str()
    branch = fields.Str()
    licenceNumber = fields.Str()
    phoneWhenToCall = fields.Str()
    sellerType = fields.Str()
    showContactForm = fields.Bool()

    profileImage = fields.Str()
    standardLogo = fields.Str()
    squareLogo = fields.Str()
    backgroundColour = fields.Str()


class ListingMedia(Schema):
    images = fields.List(fields.Dict(keys=fields.Str(), values=fields.Str()), default=[])

    totalImages = fields.Int()
    hasVideo = fields.Bool(default=False)
    hasVirtualTour = fields.Bool(default=False)
    hasBrochure = fields.Bool(default=False)


class ListingBER(Schema):
    rating = fields.Str()


class ListingPoint(Schema):
    point_type = fields.Str(data_key="type")
    coordinates = fields.List(fields.Int())


class Listing(Schema):

    def create_listing(self):
        return Listing

    class Meta:
        # Include unknown fields in the deserialized output
        unknown = INCLUDE

    id = fields.Str(required=True)
    title = fields.Str()

    seoTitle = fields.Str()
    seoFriendlyPath = fields.Str()
    sections = fields.List(fields.Str(), default=[])
    saleType = fields.List(fields.Str(), default=[])
    featuredLevel = fields.Str()

    publishDate = fields.Int()
    price = fields.Str(default="-1")
    abbreviatedPrice = fields.Str()
    category = fields.Str()
    state = fields.Str()

    numBedrooms = fields.Str(default="-1")
    numBathrooms = fields.Str(default="-1")
    propertyType = fields.Str()
    daftShortcode = fields.Str()

    seller = fields.Nested(Seller, default=Seller())
    media = fields.Nested(ListingMedia, default=ListingMedia())
    ber = fields.Nested(ListingBER, default=ListingBER())
