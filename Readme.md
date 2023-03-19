## Introduction     
The ClubEtudiants Scraper Class is a Python class for scraping the ClubEtudiants website (https://clubetudiants.ma/), specifically for downloading files from the "Exemples des anciens concours" page. The class uses the Selenium WebDriver to navigate and interact with the webpage.
## Installation
Before using the ClubEtudiants Scraper Class, the following packages need to be installed:

- Selenium
- ChromeDriver (or another WebDriver depending on the browser used)

## Usage

To use the ClubEtudiants Scraper Class, first import the class:
```python 
from clubetudiants_scraper import ClubEtudiantsScraper
```

Create an instance of the ClubEtudiantsScraper class:

```python 
scraper = ClubEtudiantsScraper()
```
Then, call the download_files() method with the email and password credentials for the website:
```python 
scraper.download_files(email, password)
```
The download_files() method will download all available files from the "Exemples des anciens concours" page to a "downloads" directory in the current working directory. If the "downloads" directory does not exist, it will be created.

## Configuration

The ClubEtudiants Scraper Class can be configured with a logger object to output logs to a file or console. The logger object should be created before creating an instance of the ClubEtudiantsScraper class. By default, the logger level is set to WARNING, but this can be changed when initializing the logger object.

Example:

```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh = logging.FileHandler('scraper.log')
fh.setFormatter(formatter)
logger.addHandler(fh)

scraper = ClubEtudiantsScraper(logger=logger)
```
## License
The ClubEtudiants Scraper Class is released under the MIT License. Please see the LICENSE file for details.