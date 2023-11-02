from dataclasses import dataclass

@dataclass
class viewmodel_result:
    headline: str
    publication: str
    liveLink: str
    archiveLink: str
    excerpt: []
    author: str
    authors_title: str
    datePublished: str #is this a str?
    dateArchived: str
    typeOfPiece: str
    typeOfSource: str
