from flask import Flask, render_template
import xml.etree.ElementTree as ET
from lib.query import search_pubmed, parse_authors

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/publications", methods=["GET"])
def get_publications():
    author_name = "aditya ambati"

    if author_name:
        publications = search_pubmed(author_name)

        # Parse XML response from PubMed
        parsed_publications = []
        for xml_data in publications:
            root = ET.fromstring(xml_data)
            print(root)
            try:
                article = {
                    "title": root.find(".//ArticleTitle").text,
                    "journal": root.find(".//Title").text,
                    "year": root.find(".//PubDate/Year").text,
                    "authors": parse_authors(root),
                    "abstract": root.find(".//AbstractText").text,
                }
            except AttributeError:
                continue
            parsed_publications.append(article)
        return render_template("publications.html", publications=parsed_publications)
    else:
        return render_template("error.html", message="Author name not provided")


if __name__ == "__main__":
    app.run(port=5000, threaded=True, host="0.0.0.0")
