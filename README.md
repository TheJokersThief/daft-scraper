# daft-scraper

[![TheJokersThief](https://circleci.com/gh/TheJokersThief/daft-scraper.svg?style=svg)](<LINK>)

- [daft-scraper](#daft-scraper)
- [Install](#install)
  - [Via Pip](#via-pip)
  - [Via Git](#via-git)
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

# Example Usage

```python
from daft_scraper.search import DaftSearch, SearchType
from daft_scraper.search.options import (
    PropertyType, PropertyTypesOption, Facility, FacilitiesOption,
    PriceOption, BedOption
)
from daft_scraper.search.options_location import LocationsOption, Location

api = DaftSearch(SearchType.RENT)
listings = api.search(options)

print(len(listings))
for listing in listings:
    print(listing.get('title'))

```

# Using the CLI

To install the CLI, clone the repo and install the dependencies with `make install`.

```
$ poetry run daft search --max-pages 1 property-for-rent --location cork --location galway
     id    price  title                                                                    propertyType
-------  -------  -----------------------------------------------------------------------  --------------
2315059     3328  The Elysian, Eglinton Road, Co. Cork                                     Apartments
2588837      570  Parchment Square, Model Farm Road, Cork, Co. Cork                        Apartments
2310295      175  Nido Curraheen Point, Farranlea Road, Co. Cork                           Apartments
2292251      220  From Here - Student Living, Galway Central, Fairgreen Road, Co. Galway   Apartments
2590894      495  BUNK CO LIVING, Kiltartan house Forster Street, Co. Galway               Apartments
2575994      650  Steelworks, 9/10 Copley Street, Ballintemple, Cork City, Cork, Co. Cork  Apartments
2327420      237  Lee Point, South Main Street, Co. Cork                                   Apartments
2751036     2400  16A The Long Walk, Co. Galway                                            House
2745585     1588  Wellington Road, Co. Cork                                                Apartment
2626561     2800  3 Saint Joseph's Terrace, Gould Street, Co. Cork                         House
2737101     1800  CHURCHFIELDS SALTHILL, Salthill, Co. Galway                              House
2759058     1400  24 Rutland Place, South Terrace, Co. Cork                                Apartment
2629695     1750  56 Caiseal Cam, Roscam, Co. Galway                                       House
2737848     1500  Dark Rd, Kilcolgan, Co. Galway                                           House
2737834     1800  11 Shangort Park, Knocknacarra, Co. Galway                               House
2757337      950  Apartment 3, 13 Harbour Row, Cobh, Co. Cork                              House
2756288     4500  Meizelljob, Coast Road, Fountainstown, Co. Cork                          House
2756231     1500  Garrai De Brun, Fort Lorenzo, Taylor's Hill, Co. Galway                  House
2632714     1650  3 Bothar An tSlÃ©ibhe, Moycullen, Co. Galway                             House
2750256     1900  Grealishtown, Bohermore, Co. Galway                                      House
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
