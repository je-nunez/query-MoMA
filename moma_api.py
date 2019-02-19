#!/usr/bin/env python3

"""
   Queries the Museum of Modern Art's RESTful API v1.
"""

from __future__ import print_function
import sys
import json
import requests


class MoMAv1(object):
    """
       Class to query the Museum of Modern Art's RESTful API v1.
    """

    # The base URL for all the MoMA v1 REST-API requests:
    v1_base_api = "https://collectionapi.metmuseum.org/public/collection/v1/"
    debug = True

    def __init__(self, debug_value=False):
        """Constructor."""
        super().__init__()
        self.debug = debug_value

    def _moma_url(self, query_path):
        """
           Receives a relative query_path into MoMA and returns the full URL
           of the MoMA API to make that query_path.
        """

        if isinstance(query_path, (list, tuple)):
            return self.v1_base_api + "/".join(query_path)
        elif isinstance(query_path, str):
            return self.v1_base_api + query_path

        return None

    def query(self, query_str):
        """
           Receives an arbitrary query string and does a search using the MoMA
           API on that query string. Returns a Python dictionary with the
           results, if any, or None in case of error.
        """

        url = self._moma_url("search")
        res = requests.get(url, params={'q': query_str})

        if self.debug:
            print(url, res.status_code)

        if res.status_code == 200:
            return json.loads(res.text)

        return None

    def retrieve_object(self, object_id):
        """
           Receives an object_id in the MoMA database. Returns a Python
           dictionary with the data about that object id, if any, or None in
           case of error.
        """

        url = self._moma_url(["objects", str(object_id)])
        res = requests.get(url)

        if self.debug:
            print(url, res.status_code)

        if res.status_code == 200:
            return json.loads(res.text)

        return None


def main():
    """
       Main function: queries the MoMA API on a search term, and then lists
       the data fields of the object-ids returned by the search.
    """

    if len(sys.argv) != 2:
        sys.exit("This script expects one command-line argument to search.")

    query_string = sys.argv[1]
    moma = MoMAv1()
    result = moma.query(query_string)
    if result and ("objectIDs" in result):
        # print(",".join(map(str, result["objectIDs"])))
        for object_id in result["objectIDs"]:
            moma_entry = moma.retrieve_object(object_id)
            print(str(moma_entry))
    else:
        print("No results.")


if __name__ == "__main__":
    main()
