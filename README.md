# daft-scraper

- [daft-scraper](#daft-scraper)
- [Install](#install)
  - [Via Pip](#via-pip)
  - [Via Git](#via-git)
- [Example Usage](#example-usage)


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
