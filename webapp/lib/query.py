import requests
import json


def get_pubmed_api_key():
    try:
        with open("creds.json", "r") as file:
            credentials = json.load(file)
            return credentials.get("pubmed", None)
    except FileNotFoundError:
        return None


PUBMED_API = get_pubmed_api_key()


def search_pubmed(author_name):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    search_url = base_url + "esearch.fcgi"
    fetch_url = base_url + "efetch.fcgi"

    # Step 1: Perform a PubMed search to get the list of PubMed IDs for the author
    search_params = {
        "db": "pubmed",
        "term": f"{author_name}[Author]",
        "retmode": "json",
        "retmax": 40,
    }
    search_response = requests.get(search_url, params=search_params)
    search_data = search_response.json()

    # Step 2: Fetch details for each publication using the PubMed IDs
    publications = []

    if "esearchresult" in search_data and "idlist" in search_data["esearchresult"]:
        pubmed_ids = search_data["esearchresult"]["idlist"]
        for pubmed_id in pubmed_ids:
            fetch_params = {
                "db": "pubmed",
                "id": pubmed_id,
                "rettype": "abstract",
                "retmode": "xml",
                "api_key": PUBMED_API,
            }
            fetch_response = requests.get(fetch_url, params=fetch_params)
            publications.append(fetch_response.text)

    return publications
