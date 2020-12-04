# daft-scraper

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
$ poetry run daft search --max-pages 1 property-for-rent
     id    price  title                                                                       propertyType
-------  -------  --------------------------------------------------------------------------  --------------
1443907     2800  Capital Dock Residence, Grand Canal, Grand Canal Dock, Co. Dublin           Apartments
1446982     2500  Quayside Quarter, North Wall Quay, Dublin 1, Co. Dublin                     Apartments
1442724     2850  Opus, 6 Hanover Quay, Hanover Quay, Dublin 2, Co. Dublin                    Apartments
2621605     1900  Knockrabo, Mount Anville Road, Goatstown, Co. Dublin                        Apartments
2503954     2500  OCCU Scholarstown Wood, Scholarstown Road, Rathfarnham, Co. Dublin          Apartments
2511232     1900  Clancy Quay by Kennedy Wilson, South Circular Road, Dublin 8, Co. Dublin    Apartments
2314852     1700  Elmfield by Havitat, Ballyogan Road, Leopardstown, Co. Dublin               Apartments
1442430     2150  Mount Argus Apartments, Mount Argus Road, Harold's Cross, Co. Dublin        Apartments
1491037     1950  Bridgefield, Northwood, Santry, Co. Dublin                                  Apartments
2621761      430  Archway Court Student Accommodation, Mountjoy Street, Dublin 7, Co. Dublin  Apartments
2524873     2200  Ropemaker Place, Hanover Street East, Dublin 2, Co. Dublin                  Apartments
2329824     1750  Wolfe Tone Lofts by Havitat, Wolfe Tone Street, Dublin 1, Co. Dublin        Apartments
2632723     2000  Heuston South Quarter, St Johns Road West, Dublin 8, Co. Dublin             Apartments
1527608     2808  Node Living, 25 pembroke street upper, Dublin 2, Co. Dublin                 Apartments
2317385     1900  Sandford Lodge by Kennedy Wilson, Sandford Lodge, Ranelagh, Co. Dublin      Apartments
2524752     2350  Whitepines South, Stocking Avenue, Rathfarnham, Co. Dublin                  Apartments
1518281     1850  Marina Village, Greystones, Co. Wicklow                                     Apartments
2287912     1750  Hanbury Mews, Hanbury Lane, Dublin 8, Co. Dublin                            Apartments
2316503     2600  Alto Vetro, Grand Canal Square, Dublin 2, Co. Dublin                        Apartments
2317419     1800  Northbank Apartments, Castleforbes Road, Dublin 1, Co. Dublin               Apartments
```

## `search` command

| argument  | description |
|---|---|
| search_type | The type of search you want to initiate. For the possible values, check out the [SearchType Enum](daft_scraper/search/__init__.py). |

For any flag that can take `[multiple]` arguments, you can supply the flag multiple times.

| flag  | description |
|---|---|
| --headers | The attributes to print out for each listing. [multiple] |
| --locations | Which location you want to search for. For all the possible values, check out the [Location Enum](daft_scraper/search/options_location.py) [multiple] |
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

$ poetry run daft search --max-pages 1 property-for-rent --help
Usage: daft search [OPTIONS] SEARCH_TYPE:[property-for-rent|property-for-
                   sale|sharing|new-homes-for-sale|commercial-properties-for-
                   rent|commercial-properties-for-sale]

Arguments:
  SEARCH_TYPE:[property-for-rent|property-for-sale|sharing|new-homes-for-sale|commercial-properties-for-rent|commercial-properties-for-sale]
                                  [required]

Options:
  --headers TEXT                  [default: id, price, title, propertyType]
  --locations TEXT                [default: ireland]
  --max-pages INTEGER             [default: 9223372036854775807]
  --min-price INTEGER             [default: 0]
  --max-price INTEGER             [default: 9223372036854775807]
  --min-beds INTEGER              [default: 0]
  --max-beds INTEGER              [default: 9223372036854775807]
  --min-lease INTEGER             [default: 0]
  --max-lease INTEGER             [default: 9223372036854775807]
  --property-type [EMPTY|houses|apartments|studio-apartments]
                                  [default: EMPTY]
  --ad-state [published|sale-agreed]
                                  [default: published]
  --facility [EMPTY|alarm|cable-television|dishwasher|garden-patio-balcony|central-heating|internet|microwave|parking|pets-allowed|smoking|serviced-property|dryer|washing-machine|wheelchair-access]
                                  [default: EMPTY]
  --media-type [EMPTY|video|virtual-tour]
                                  [default: EMPTY]
  --sort [EMPTY|publishDateDesc|priceAsc|priceDesc]
                                  [default: EMPTY]
  --furnishing [EMPTY|furnished|unfurnished]
                                  [default: EMPTY]
  --help                          Show this message and exit.
