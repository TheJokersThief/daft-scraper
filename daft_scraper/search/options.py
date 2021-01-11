import sys
from dataclasses import dataclass
from enum import Enum
from typing import List


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
            f"{self.PARAM_KEY}_from": self.min,
            f"{self.PARAM_KEY}_to": self.max,
        }


class SalePriceOption(PriceOption):
    PARAM_KEY = "salePrice"


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
    ALL = "EMPTY"
    HOUSE = "houses"
    APARTMENT = "apartments"
    STUDIO_APARTMENT = "studio-apartments"
    DETACHED_HOUSE = "detached-houses"
    SEMI_DETACHED_HOUSE = "semi-detached-houses"
    TERRACED_HOUSE = "terraced-houses"
    END_OF_TERRACE_HOUSE = "end-of-terrace-houses"
    TOWNHOUSE = "townhouses"
    DUPLEX = "duplexes"
    BUNGALOW = "bungalows"
    SITE = "sites"


@dataclass
class PropertyTypesOption(Option):
    property_types: List[PropertyType]

    def get_params(self):
        if PropertyType.ALL in self.property_types:
            # If we want "all", don't submit any params
            return {}

        return {
            "propertyType": [propType.value for propType in self.property_types]
        }


class Facility(Enum):
    NONE = "EMPTY"
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


@dataclass
class FacilitiesOption(Option):
    facilities: List[Facility]

    def get_params(self):
        if self.facilities == [Facility.NONE]:
            # If facility list specifies none, don't return params
            return {}

        return {
            "facilities": [facil.value for facil in self.facilities]
        }


class MediaType(Enum):
    ALL = "EMPTY"
    VIDEO = "video"
    VIRTUAL_TOUR = "virtual-tour"


@dataclass
class MediaTypesOption(Option):
    media_types: List[MediaType]

    def get_params(self):
        if MediaType.ALL in self.media_types:
            # If we want "all", don't submit any params
            return {}

        return {
            "mediaTypes": [propType.value for propType in self.media_types]
        }


@dataclass
class KeywordsOption(Option):
    terms = List[str]

    def get_params(self):
        return {
            "terms": self.terms
        }


class AdState(Enum):
    AVAILABLE = "published"
    AGREED = "sale-agreed"


@dataclass
class AdStateOption(Option):
    ad_state: AdState

    def get_params(self):
        return {
            "adState": self.ad_state.value
        }


class Sort(Enum):
    BEST_MATCH = "EMPTY"
    MOST_RECENT = "publishDateDesc"
    PRICE_ASCENDING = "priceAsc"
    PRICE_DESCENDING = "priceDesc"


@dataclass
class SortOption(Option):
    sort: Sort

    def get_params(self):
        if self.sort == Sort.BEST_MATCH:
            return {}

        return {
            "sort": self.sort.value
        }


class Furnishing(Enum):
    ALL_FURNISHINGS = "EMPTY"
    FURNISHED = "furnished"
    UNFURNISHED = "unfurnished"


@dataclass
class FurnishingOption(Option):
    furnishing: Furnishing

    def get_params(self):
        if self.furnishing == Furnishing.ALL_FURNISHINGS:
            return {}

        return {
            "furnishing": self.furnishing.value
        }
