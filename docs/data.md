# Data

This is an overview of the various datasets that will be used. Some relevant links at the UvA Library:

- [Open data](https://uba.uva.nl/en/support/open-data/open-data.html)

- [Datasets and publication channels](https://uba.uva.nl/en/support/open-data/data-sets-and-publication-channels/data-sets-and-publication-channels.html)

- [Linked Data](https://uba.uva.nl/en/support/open-data/linked-data/linked-data.html)

- [Licences](https://uba.uva.nl/en/support/open-data/licences/licences.html)

## Beeldbank

Images can be retrieved [like this](https://servicetin.adlibhosting.com/te4/wwwopac.ashx?command=getcontent&server=images&value=992001743.jpg&width=800&height=800)

In the dumps on disk, the exported XML files from `uva_alma_beeldbank_dc_new.xml` look like this:

```xml
<ns0:dc xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:ns0="http://www.openarchives.org/OAI/2.0/oai_dc/"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/oai_dc/ http://www.openarchives.org/OAI/2.0/oai_dc.xsd">
  <dc:title>Architecture, peinture et sculpture de la maison de ville d'Amsterdam, repr&#233;sent&#233;e en CIX
figures en taille-douce ...</dc:title>
  <dc:title>Architecture, peinture et sculpture de la maison de ville d'Amsterdam, repr&#233;sent&#233;e en 109
figures en taille-douce</dc:title>
  <dc:description>Titelblad in rood en zwart</dc:description>
  <dc:description>Oorspronkelijk impressum overgeplakt met strookje</dc:description>
  <dc:description>Auteurs: Jacob van Campen, Hubertus Quellinus en Artus Quellinus</dc:description>
  <dc:description>A-E 2 F1 en 109 gegraveerde bladen</dc:description>
  <dc:description>Elektronische reproductie</dc:description>
  <dc:description>gedigitaliseerd</dc:description>
  <dc:description>Beschrijving gedrukte uitgave</dc:description>
  <dc:publisher>A Amsterdam chez Gerard Valk</dc:publisher>
  <dc:contributor>Campen, Jacob van, architect/bouwmeester, 1595-1657. (NL-LeOCL)069356742
https://open-na.hosted.exlibrisgroup.com/alma/31UKB_UAM1_INST/authorities/9839192425805131.jsonld</dc:contributor>
  <dc:contributor>Quellinus, Hubertus, schilder, graveur, 1605?-1688. (NL-LeOCL)069925631
https://open-na.hosted.exlibrisgroup.com/alma/31UKB_UAM1_INST/authorities/9839197814305131.jsonld</dc:contributor>
  <dc:contributor>Quellinus, Artus (Artus), beeldhouwer, 1609-1668. (NL-LeOCL)091438969
https://open-na.hosted.exlibrisgroup.com/alma/31UKB_UAM1_INST/authorities/9839288655305131.jsonld</dc:contributor>
  <dc:date>1719</dc:date>
  <dc:date>1719</dc:date>
  <dc:type>text</dc:type>
  <dc:type />
  <dc:identifier>https://hdl.handle.net/11245/3.3680</dc:identifier>
  <dc:language>fre</dc:language>
  <dc:relation>Architecture, peinture et sculpture de la maison de ville d'Amsterdam, repr&#233;sent&#233;e en CIX
figures en taille-douce ...</dc:relation>
</ns0:dc>
```

The Beeldbank is available as [Linked Open Data](https://lod.uba.uva.nl/UB-UVA/Beeldbank/)

The record in the LOD looks like this:

| predicate                                                 | object                                                                                                                                                                                                                     |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| http://www.w3.org/1999/02/22-rdf-syntax-ns#type           | http://www.europeana.eu/schemas/edm/ProvidedCHO                                                                                                                                                                            |
| http://www.w3.org/1999/02/22-rdf-syntax-ns#type           | https://schema.org/Book                                                                                                                                                                                                    |
| http://purl.org/dc/terms/extent                           | 1 online resource (22 p., 109 bl) titelvignet, portr., grav                                                                                                                                                                |
| http://www.w3.org/2000/01/rdf-schema#label                | Architecture, peinture et sculpture de la maison de ville d'Amsterdam, représentée en CIX figures en taille-douce ...                                                                                                      |
| http://www.europeana.eu/schemas/edm/isShownBy             | https://images.uba.uva.nl/iiif/2/erfgoed!4!3!3!003527334!UBAGWOL63-905_001.jpg/full/full/0/default.jpg                                                                                                                     |
| http://purl.org/dc/elements/1.1/contributor               | http://data.bibliotheken.nl/id/thes/p069925631                                                                                                                                                                             |
| http://purl.org/dc/elements/1.1/contributor               | http://data.bibliotheken.nl/id/thes/p091438969                                                                                                                                                                             |
| http://purl.org/dc/elements/1.1/creator                   | http://data.bibliotheken.nl/id/thes/p069356742                                                                                                                                                                             |
| http://purl.org/dc/elements/1.1/date                      | 1719                                                                                                                                                                                                                       |
| http://purl.org/dc/elements/1.1/description               | Beschrijving gedrukte uitgave                                                                                                                                                                                              |
| http://purl.org/dc/elements/1.1/description               | gedigitaliseerd 2018 Amsterdam, Bibliotheek UvA/HvA NL-AmU                                                                                                                                                                 |
| http://purl.org/dc/elements/1.1/description               | Titelblad in rood en zwart                                                                                                                                                                                                 |
| http://purl.org/dc/elements/1.1/description               | A-E 2 F1 en 109 gegraveerde bladen                                                                                                                                                                                         |
| http://purl.org/dc/elements/1.1/description               | Auteurs: Jacob van Campen, Hubertus Quellinus en Artus Quellinus                                                                                                                                                           |
| http://purl.org/dc/elements/1.1/description               | Oorspronkelijk impressum overgeplakt met strookje                                                                                                                                                                          |
| http://purl.org/dc/elements/1.1/identifier                | https://hdl.handle.net/11245/3.3680                                                                                                                                                                                        |
| http://purl.org/dc/elements/1.1/language                  | http://id.loc.gov/vocabulary/languages/fre                                                                                                                                                                                 |
| http://purl.org/dc/elements/1.1/publisher                 | A Amsterdam, chez Gerard Valk                                                                                                                                                                                              |
| http://purl.org/dc/elements/1.1/source                    | Elektronische reproductie Amsterdam Bibliotheek UvA/HvA 2018 Gedigitaliseerd exemplaar: OTM: OL 63-905 NL-AmU                                                                                                              |
| http://purl.org/dc/elements/1.1/title                     | Architecture, peinture et sculpture de la maison de ville d'Amsterdam, représentée en CIX figures en taille-douce ...                                                                                                      |
| http://purl.org/dc/elements/1.1/type                      | http://vocab.getty.edu/aat/300028051                                                                                                                                                                                       |
| http://purl.org/dc/elements/1.1/type                      | Electronic books                                                                                                                                                                                                           |
| http://purl.org/dc/elements/1.1/type                      | book                                                                                                                                                                                                                       |
| http://purl.org/dc/elements/1.1/type                      | tekst                                                                                                                                                                                                                      |
| http://purl.org/dc/terms/alternative                      | Architecture, peinture et sculpture de la maison de ville d'Amsterdam, représentée en 109 figures en taille-douce                                                                                                          |
| http://purl.org/dc/terms/isFormatOf                       | Gedrukte uitgave: Campen, Jacob van, 1595-1657 Architecture, peinture et sculpture de la maison de ville d'Amsterdam, représentée en CIX figures en taille-douce ... A Amsterdam, : chez Gerard Valk, 1719 (OCoLC)69044401 |
| http://purl.org/dc/terms/medium                           | computer                                                                                                                                                                                                                   |
| http://purl.org/dc/terms/medium                           | online bron                                                                                                                                                                                                                |
| http://purl.org/dc/terms/spatial                          | http://id.loc.gov/vocabulary/countries/ne                                                                                                                                                                                  |
| http://semanticweb.cs.vu.nl/2009/11/sem/hasEndTimeStamp   |                                                                                                                                                                                                                            |
| http://semanticweb.cs.vu.nl/2009/11/sem/hasBeginTimeStamp | 1719                                                                                                                                                                                                                       |
| http://xmlns.com/foaf/0.1/depiction                       | https://images.uba.uva.nl/iiif/2/erfgoed!4!3!3!003527334!UBAGWOL63-905_001.jpg/full/full/0/default.jpg                                                                                                                     |

```{note}
From the above, we can see that using the LOD dump of the Beeldbank is the shortest route to a working dataset for some AI analysis in terms of proof-of-concepts.
```

## TIN

A selection was made, [759 Properties under own management](https://servicetin.adlibhosting.com/te4/wwwopac.ashx?command=search&database=collectTEphotos3&search=pointer%20353&output=xml&limit=100.000&startfrom=1&xmltype=grouped)

Metadata records can be retrieved [like this](https://servicetin.adlibhosting.com/te4/wwwopac.ashx?command=search&database=collectCUE&search=pointer%20108&output=xml&startfrom=1&xmltype=grouped)

Images can be retrieved [like this](https://servicetin.adlibhosting.com/te4/wwwopac.ashx?command=getcontent&server=images&value=992001743.jpg&width=800&height=800)

From the disk dump `wwwopac_TIN_limit100000.xml` records look like this:

```xml
<record priref="41745" created="2008-06-23T12:24:50" modification="2016-11-30T12:58:07" selected="false">
  <creator>Roelofs, Charles</creator>
  <creator>Moritz, Ernst</creator>
  <creator.role>ontwerp</creator.role>
  <creator.role>fotografie</creator.role>
  <performance>
    <New_collect_field>Gelegenheidscombinaties</New_collect_field>
    <performance.production_code>123890453.001</performance.production_code>
    <performance.title>Aias</performance.title>
    <performance.title.lref>21012</performance.title.lref>
    <production.date>1939-05-23</production.date>
  </performance>
  <Reproduction>
    <reproduction.identifier_URL>qm00217.000.jpg</reproduction.identifier_URL>
    <reproduction.reference>qm00217.000</reproduction.reference>
  </Reproduction>
  <institution.name>Theater Instituut Nederland</institution.name>
  <object_category>maquette</object_category>
  <object_name>maquette</object_name>
  <object_number>qm00217.000</object_number>
  <priref>41745</priref>
  <production.date.start>1937</production.date.start>
  <title>Aias</title>
</record>
```

We can see that the TIN set is not available in a LOD format like the Beeldbank, so some data conversion and mapping is required.

## a more thorough data lookthrough

the beeldbank at a glance: 

```{glue:} beeldbank info
```

### Copyright disclaimer

The content of the TIN website is protected by copyright and may not be reproduced, published or distributed without permission from Allard Pierson. Allard Pierson/Stichting TiN is not the rightful owner of the displayed images. Works of which the maker died more than 70 years ago are royalty-free (Dutch Public Domain). For most of the more recent creations you need to require permission from the copyright holders before we provide high-resolution files.
For more information about copyright, see the Copyright Information Site of the University Library.
To request or use (reproductions of) photo or video material, please contact theatercollectie@uva.nl. Rates are available on request.
Loan applications go through Allard Pierson.

### Incorrect terms or terms with a negative connotation

We are aware that titles, descriptions or images shown may contain incorrect terms, loaded terms or terms with a negative connotation. If you have any questions or comments about this, please contact theatercollectie@uva.nl.

## CCT - Cross Cultural Timeline

As used in the exhibition space at the museum. Can be access at this link: https://allardpierson.crossculture.ie/api/

An example entry looks like:

```json
{
  "id": "2",
  "object_id": "apm-5f0974f3029ff",
  "object_type": "object",
  "inventory_num": "Blaeu kast",
  "start": "1664",
  "end": "1750",
  "startperiod": "ad",
  "endperiod": "ad",
  "latlng": "52.37458165865567, 4.892420053465686",
  "theme": "mobility",
  "title_en": "The Atlas Maior by Joan Blaeu",
  "title_nl": " Grooten atlas, oft werelt-beschrijving",
  "sketchfab_id": "",
  "link": "",
  "other": "",
  "about_en": "<span style=\"font-size:18px\">In the 17th century, trade and shipping flourished in Amsterdam. The VOC was founded, new sea routes were explored and voyages of discovery yielded not only a great deal of money but also new geographical knowledge. As a result, the world view became increasingly &#39;stretched&#39; and improved. Amsterdam&#39;s cartography played a major role in the development and dissemination of that world view. One highlight was the Atlas Maior, which was launched in various editions and languages by the Amsterdam printer, publisher and map maker Joan Blaeu in 1662.</span> \\n\r\n\r\n&nbsp; \\n\r\n",
  "about_nl": "<span style=\"font-size:18px\">In de 17de eeuw&nbsp;kwamen de handel en zeevaart in Amsterdam tot grote bloei. De VOC werd opgericht, nieuwe zeeroutes werden verkend en ontdekkingsreizen leverden behalve veel geld ook nieuwe geografische kennis op. Het wereldbeeld werd daardoor steeds verder &lsquo;opgerekt&#39; en verbeterd. In de ontwikkeling en verspreiding van dat wereldbeeld speelde de Amsterdamse cartografie een grote rol. Een hoogtepunt vormde de Atlas Maior of Grooten Atlas, vanaf 1662 in verschillende edities en talen op de markt gebracht door de Amsterdamse drukker, uitgever en kaartenmaker Joan Blaeu.</span> \\n\r\n",
  "material_en": "",
  "material_nl": "",
  "manufactured_en": " Grooten atlas, oft werelt-beschrijving",
  "manufactured_nl": " Grooten atlas, oft werelt-beschrijving",
  "findspot_en": "Amsterdam, J. Blaeu, 1664",
  "findspot_nl": "Amsterdam, J. Blaeu, 1664 ",
  "username": "Wim Hupperetz",
  "ccid": "ccid5e17d20c12ad1",
  "viewcounter": "129",
  "stories": [
    {
      "id": "2",
      "object_id": "apm-5f0974f3029ff",
      "title": "De atlas maior in de Nederlandse canon",
      "about": "\r\n",
      "vimeo": "",
      "source": "Blaeukabinet.png",
      "tags": "{\"tags\":[\"none\",\"\"]}",
      "date": "2020-07-12 17:47:15",
      "username": "Wim Hupperetz",
      "ccid": "ccid5e17d20c12ad1"
    }
  ],
  "images": {
    "images": [
      {
        "image": "Blaeukabinet.png",
        "caption": "Blaeu Cabinet 1664"
      },
      {
        "image": "bleau_detail.png",
        "caption": ""
      }
    ]
  }
}
```

Under which URIs can the images that are mentioned be retrieved?
