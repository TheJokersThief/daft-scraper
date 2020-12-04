import sys
from dataclasses import dataclass
from enum import Enum


class Option():
    def get_params(self):
        return {}

@dataclass
class PriceOption(Option):
    min: int = 0
    max: int = sys.maxsize

    PARAM_KEY = "rentalPrice"

    def get_params(self):
        return {
            f"{PriceOption.PARAM_KEY}_from": self.min,
            f"{PriceOption.PARAM_KEY}_to": self.max,
        }

@dataclass
class BedOption(Option):
    min: int = 0
    max: int = sys.maxsize

    PARAM_KEY = "numBeds"

    def get_params(self):
        return {
            f"{BedOption.PARAM_KEY}_from": self.min,
            f"{BedOption.PARAM_KEY}_to": self.max,
        }

@dataclass
class LeaseLengthOption(Option):
    min: int = 0
    max: int = sys.maxsize

    PARAM_KEY = "leaseLength"

    def get_params(self):
        return {
            f"{LeaseLengthOption.PARAM_KEY}_from": self.min,
            f"{LeaseLengthOption.PARAM_KEY}_to": self.max,
        }


class PropertyType(Enum):
    ALL = None
    HOUSE = "houses"
    APARTMENT = "apartments"
    STUDIO_APARTMENT = "studio-apartments"


@dataclass
class PropertyTypesOption(Option):
    property_types: list[PropertyType]  # pylint: disable=unsubscriptable-object

    def get_params(self):
        if PropertyType.ALL in self.property_types:
            # If we want "all", don't submit any params
            return {}

        return {
            "propertyType": [str(propType) for propType in self.property_types]
        }


class Facility(Enum):
    NONE = None
    ALARM = "alarm"
    CABLE_TELEVISION = "cable-television"
    DISHWASHER = "dishwasher"
    GARDEN_PATIO_BALCONY = "garden-patio-balcony"
    CENTRAL_HEATING = "central-heating"
    INTERNET = "internet"
    MICROWAVE = "microwave"
    PARKING = "parking"
    PETS_ALLOWED = "pets-allowed"
    SMOKING = "smoking"
    SERVICED_PROPERTY = "serviced-property"
    DRYER = "dryer"
    WASHING_MACHINE = "washing-machine"
    WHEELCHAIR_ACCESS = "wheelchair-access"


class FacilitiesOption(Option):
    facilities: list[Facility]  # pylint: disable=unsubscriptable-object

    def get_params(self):
        if self.facilities == [Facility.NONE]:
            # If facility list specifies none, don't return params
            return {}

        return {
            "facilities": [str(facil) for facil in self.facilities]
        }


class MediaType(Enum):
    ALL = None
    VIDEO = "video"
    VIRTUAL_TOUR = "virtual-tour"


@dataclass
class MediaTypesOption(Option):
    media_types: list[MediaType]  # pylint: disable=unsubscriptable-object

    def get_params(self):
        if MediaType.ALL in self.media_types:
            # If we want "all", don't submit any params
            return {}

        return {
            "mediaTypes": [str(propType) for propType in self.media_types]
        }


class KeywordsOption(Option):
    terms = list[str]  # pylint: disable=unsubscriptable-object

    def get_params(self):
        return {
            "terms": self.terms
        }


class AdState(Enum):
    AVAILABLE = "published"
    AGREED = "sale-agreed"


class AdStateOption(Option):
    ad_state: AdState

    def get_params(self):
        return {
            "adState": str(self.ad_state)
        }


class Sort(Enum):
    BEST_MATCH = None
    MOST_RECENT = "publishDateDesc"
    PRICE_ASCENDING = "priceAsc"
    PRICE_DESCENDING = "priceDesc"


class SortOption(Option):
    sort: Sort

    def get_params(self):
        if self.sort == Sort.BEST_MATCH:
            return {}

        return {
            "sort": str(self.sort)
        }


class Furnishing(Enum):
    ALL_FURNISHINGS = None
    FURNISHED = "furnished"
    UNFURNISHED = "unfurnished"

class FurnishingOption(Option):
    furnishing: Furnishing

    def get_params(self):
        if self.furnishing == Furnishing.ALL_FURNISHINGS:
            return {}

        return {
            "furnishing": str(self.furnishing)
        }
