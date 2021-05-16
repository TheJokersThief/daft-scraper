# daft-scraper

A python library for scraping housing data from Daft.ie.

_Inspired by the wonderful [daftlistings library](https://github.com/AnthonyBloomer/daftlistings)._

[![TheJokersThief](https://circleci.com/gh/TheJokersThief/daft-scraper.svg?style=svg)](<LINK>)

- [daft-scraper](#daft-scraper)
- [Install](#install)
  - [Via Pip](#via-pip)
  - [Via Git](#via-git)
- [Real-life Usage](#real-life-usage)
- [Example Usage](#example-usage)
- [Using the CLI](#using-the-cli)
  - [`search` command](#search-command)


# Install

## Via Pip
You can install the library using pip:

```
pip install daft-scraper
```

## Via Git
The project uses [poetry](https://python-poetry.org/), so you'll need poetry to install the dependencies and setup the project.

```
git clone git@github.com:TheJokersThief/daft-scraper.git
cd daft-scraper
make install
```

# Real-life Usage

* [Daft2BigQuery](https://github.com/TheJokersThief/Daft2BigQuery): A project that pulls housing information from Daft and puts it in GCP BigQuery for data modelling.

# Example Usage

```python
from daft_scraper.search import DaftSearch, SearchType
from daft_scraper.search.options import (
    PropertyType, PropertyTypesOption, Facility, FacilitiesOption,
    PriceOption, BedOption
)
from daft_scraper.search.options_location import LocationsOption, Location

options = [
    PropertyTypesOption([PropertyType.APARTMENT]),
    FacilitiesOption([Facility.PARKING, Facility.SERVICED_PROPERTY]),
    LocationsOption([Location.SWORDS_DUBLIN]),
    PriceOption(0, 999999),
    BedOption(1, 4),
]

api = DaftSearch(SearchType.RENT)
listings = api.search(options)

for listing in listings:
    print(listing.title)

```

# Using the CLI

The CLI is included as an easy way for me test things and get some quick results :) Let me know if you have any suggestions!

To install the CLI, clone the repo and install the dependencies with `make install`.

```
$ poetry run daft search --max-pages 1 property-for-rent --location cork --location galway
     id    price  title                                                                    propertyType    url
-------  -------  -----------------------------------------------------------------------  --------------  --------------------------------------------------------------------------------------------------
2315059  3328     The Elysian, Eglinton Road, Co. Cork                                     Apartments      https://daft.ie/for-rent/the-elysian-eglinton-road-co-cork/2315059
2588837   570     Parchment Square, Model Farm Road, Cork, Co. Cork                        Apartments      https://daft.ie/for-rent/parchment-square-model-farm-road-cork-co-cork/2588837
2310295   759.5   Nido Curraheen Point, Farranlea Road, Co. Cork                           Apartments      https://daft.ie/for-rent/nido-curraheen-point-farranlea-road-co-cork/2310295
2292251   954.8   From Here - Student Living, Galway Central, Fairgreen Road, Co. Galway   Apartments      https://daft.ie/for-rent/from-here-student-living-galway-central-fairgreen-road-co-galway/2292251
2590894   495     BUNK CO LIVING, Kiltartan house Forster Street, Co. Galway               Apartments      https://daft.ie/for-rent/bunk-co-living-kiltartan-house-forster-street-co-galway/2590894
2575994   650     Steelworks, 9/10 Copley Street, Ballintemple, Cork City, Cork, Co. Cork  Apartments      https://daft.ie/for-rent/steelworks-9-10-copley-street-ballintemple-cork-city-cork-co-cork/2575994
2327420  1028.58  Lee Point, South Main Street, Co. Cork                                   Apartments      https://daft.ie/for-rent/lee-point-south-main-street-co-cork/2327420
2751036  2400     16A The Long Walk, Co. Galway                                            House           https://daft.ie/for-rent/house-16a-the-long-walk-co-galway/2751036
2745585  1588     Wellington Road, Co. Cork                                                Apartment       https://daft.ie/for-rent/apartment-wellington-road-co-cork/2745585
2626561  2800     3 Saint Joseph's Terrace, Gould Street, Co. Cork                         House           https://daft.ie/for-rent/house-3-saint-josephs-terrace-gould-street-co-cork/2626561
2737101  1800     CHURCHFIELDS SALTHILL, Salthill, Co. Galway                              House           https://daft.ie/for-rent/house-churchfields-salthill-salthill-co-galway/2737101
2759058  1400     24 Rutland Place, South Terrace, Co. Cork                                Apartment       https://daft.ie/for-rent/apartment-24-rutland-place-south-terrace-co-cork/2759058
2629695  1750     56 Caiseal Cam, Roscam, Co. Galway                                       House           https://daft.ie/for-rent/house-56-caiseal-cam-roscam-co-galway/2629695
2737848  1500     Dark Rd, Kilcolgan, Co. Galway                                           House           https://daft.ie/for-rent/house-dark-rd-kilcolgan-co-galway/2737848
2758935  1200     Hollyville, Turners Cross, Co. Cork                                      House           https://daft.ie/for-rent/house-hollyville-turners-cross-co-cork/2758935
2737834  1800     11 Shangort Park, Knocknacarra, Co. Galway                               House           https://daft.ie/for-rent/house-11-shangort-park-knocknacarra-co-galway/2737834
2757337   950     Apartment 3, 13 Harbour Row, Cobh, Co. Cork                              House           https://daft.ie/for-rent/house-apartment-3-13-harbour-row-cobh-co-cork/2757337
2756288  4500     Meizelljob, Coast Road, Fountainstown, Co. Cork                          House           https://daft.ie/for-rent/house-meizelljob-coast-road-fountainstown-co-cork/2756288
2756231  1500     Garrai De Brun, Fort Lorenzo, Taylor's Hill, Co. Galway                  House           https://daft.ie/for-rent/house-garrai-de-brun-fort-lorenzo-taylors-hill-co-galway/2756231
2632714  1650     3 Bothar An tSlÃ©ibhe, Moycullen, Co. Galway                             House           https://daft.ie/for-rent/house-3-bothar-an-tsl-ibhe-moycullen-co-galway/2632714
```

## `search` command

| argument  | description |
|---|---|
| search_type | The type of search you want to initiate. For the possible values, check out the [SearchType Enum](daft_scraper/search/__init__.py). |

For any flag that can take `[multiple]` arguments, you can supply the flag multiple times.

| flag  | description |
|---|---|
| --headers | The attributes to print out for each listing. [multiple] |
| --location | Which location you want to search for. For all the possible values, check out the [Location Enum](daft_scraper/search/options_location.py) [multiple] |
| --max-pages | Each page is 20 results, this sets the limit on the number of pages fetched. |
| --min-price | Minimum price. |
| --max-price | Maximum price. |
| --min-beds | Minimum number of bedrooms. |
| --max-beds | Maximum number of bedrooms. |
| --min-lease | Minimum term on the lease (in months). |
| --max-lease | Maximum term on the lease (in months). |
| --property-type | The type of property to search for. For all possible values, checkout the [PropertyType Enum](/daft_scraper/search/options.py) |
| --facility | Which facilities must the listing include. [multiple] |
| --media-type | Which media types must the listing include. [multiple] |
| --sort | How should the results be sorted. For all possible views, check out the [Sort Enum](daft_scraper/search/options). |
| --furnishing | Should the listing be furnished or unfurnished. |
