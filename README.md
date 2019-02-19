# Query-MoMA

Querying the Museum of Modern Art API v1.

# WIP

This project is a *work in progress*. The implementation is *incomplete* and
subject to change. The documentation can be inaccurate.

# Demo

The program expects the search-term on the Museum of Modern Art as its first
command-line argument. E.g., to search for "landscape":

       $ ./moma_api.py landscape
          ...
          {'isPublicDomain': True, 'artistRole': 'Artist', 'department': 'Drawings and Prints', 'objectBeginDate': 1850, 'isHighlight': False, 'locale': '', 'objectEndDate': 1903, 'tags': ['Houses', 'Landscapes', 'Trees'], 'title': 'Landscape', 'artistDisplayBio': 'French, Charlotte Amalie, Saint Thomas 1830–1903 Paris', 'rightsAndReproduction': '', 'geographyType': '', 'artistNationality': 'French', 'subregion': '', 'artistEndDate': '1903', 'artistAlphaSort': 'Pissarro, Camille', 'artistSuffix': '', 'creditLine': 'Rogers Fund, 1924', 'repository': 'Metropolitan Museum of Art, New York, NY', 'locus': '', 'primaryImageSmall': 'https://images.metmuseum.org/CRDImages/dp/web-large/DP807941.jpg', 'city': '', 'objectURL': 'https://www.metmuseum.org/art/collection/search/339645', 'dimensions': '12 7/8 x 9 3/4 in.  (32.7 x 24.8 cm)', 'artistDisplayName': 'Camille Pissarro', 'county': '', 'constituents': [{'role': 'Artist', 'name': 'Camille Pissarro'}], 'state': '', 'additionalImages': ['https://images.metmuseum.org/CRDImages/dp/original/24.66.1.jpg'], 'objectID': 339645, 'period': '', 'portfolio': '', 'accessionNumber': '24.66.1', 'metadataDate': '2019-02-19T00:11:06.427Z', 'classification': 'Drawings', 'excavation': '', 'culture': '', 'medium': 'Watercolor over black chalk on wove paper', 'reign': '', 'linkResource': '', 'dynasty': '', 'objectDate': 'second half 19th century', 'region': '', 'primaryImage': 'https://images.metmuseum.org/CRDImages/dp/original/DP807941.jpg', 'artistPrefix': '', 'artistBeginDate': '1830', 'river': '', 'country': '', 'objectName': 'Drawing'}
          ...

# Notes

The API doesn't require yet some type of API key in order to use it.
The API may rate-limit the queries (which is understandable).
