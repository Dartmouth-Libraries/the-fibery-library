- The OriginLocation has a lot of overlapping values (e.g. "Baker-Berry" and "Baker-Berry Library Stacks")
  - -> Someone with domain knowledge should go through the list and consolidate

```
'Sherman Art Library', 'Baker-Berry Library',
'Matthews Fuller Health Sciences Library',
'Dartmouth Library Depository', 'Dana Biomedical Library',
'Feldberg Business and Engineering Library', 'Jones Media Center',
'Resource Sharing Library', 'Baker-Berry Library Stacks',
'Sherman Art Library Stacks',
'Dartmouth Library Depository Depository', 'Baker ',
'Baker-Berry Library East Asian', 'Rauner Val ', 'EJ', 'Sherman',
'Baker-Berry', 'Baker-Berry Library Cook',
'Baker-Berry Library Course Reserve', 'Baker-Berry Library Dewey',
'Rauner Alumni ', 'Sherman Art Library Reference',
'Jones Media Center DVD', 'Sherman Art Library Oversize', 'Baker',
'Sherman ', 'DLD', 'Jones Media Center Music Compact Disc',
'Baker-Berry Library Nash Collection', 'Baker-Berry ',
'Baker-Berry Library Oversize', 'Baker Dewey ', 'dld ',
'Baker-Berry Library Reference',
'Feldberg Business and Engineering Library Stacks',
'Baker Reference  ', 'Baker Folio', 'Sherman Art Library Folio',
'Sherman Oversize', 'Kresge Journal', 'Feldberg',
'Baker-Berry Scores', 'Baker-Berry Library Popular Science',
'Baker-Berry Library Japan', 'Sherman Special ', 'Baker reference',
'Baker-Berry Library Korea',
'Feldberg Business and Engineering Library Course Reserve',
'Baker Cook', 'Sherman Art Library Oversize ',
'Baker Music Reference ', 'Sherman Art', 'Sherman Art ', 'dld',
'Rauner Roberts ', 'Sherman Oversize ', 'BAker ',
'Baker-Berry Library Cook Easy', 'Baker-Berry Library CD-ROM',
'Baker Dewey', 'Baker-Berry Library Evans Map Room',
'DLD Microfilm ', 'Baker-Berry Library Nash Oversize',
'Jones Media Center Music Compact Disc ',
'Matthews Fuller Health Sciences Library Stacks',
'Matthews Fuller ', 'Dana Biomedical Library Reference', 'HSL',
'Depository', nan, 'PHYSSCIJOU Baker', 'WALU',
'Matthews Fuller Health Sciences Library Display',
'DEPOSITORY DEPOSITORY', 'EBSCOhost Business Source Ultimate',
'SHERMAN STACKS', 'Taylor & Francis eBooks Complete',
'Ebook Central Perpetual, DDA and Subscription Titles',
'EBSCOhost Academic eBook Collection (North America)',
'Oxford Scholarship Online Complete', 'SpringerLink Books',
'Gale In Context: Environmental Studies', 'SHERMAN REFERENCE',
'Project Muse 2021 Complete', 'Project Muse All Journals',
'Feldberg Business and Engineering Library Permanent Reserve',
'Oxford Handbooks Online Complete', 'Project Muse eBooks 2017',
'BAKER STACKS',
'ProQuest Historical Newspapers: The Jewish Exponent', 'LIBRAweb',
'Oxford Reference Premium Collection',
'Elsevier ScienceDirect Books Complete', 'Brill Academic Journals',
'BAKER DEWEY', 'ACM Digital Library Complete', 'Single Journals',
'Oxford Bibliographies',
'PERSEE - Portail de revues scientifiques en sciences humaines et sociales',
'OpenEdition Freemium for Books', 'Wiley Books',
'EBSCOhost Ebooks', 'Cairn eBooks Humanities',
'Cambridge University Press Journals Digital Archive HSS',
'OReilly Online Learning', 'Oxford Research Encyclopedias',
'Cambridge Core All Books', 'Cambridge University Press eBooks',
'University of California Press Journals', 'JSTOR Books',
'Scholarly Publishing Collective (SPC)', 'Ingenta Connect', 'eJ',
'Dartmouth Library Depository ', 'Project Muse\xa02020 Complete',
'Taylor & Francis Current Content Access',
'Springer Computer Science e-book collection',
'de Gruyter eBooks Complete', 'NCBI Bookshelf', 'SHERMAN READRM',
'Gale eBooks', 'eDuke Books Scholarly Collection 2023',
'Peeters Online Journals', 'BAKER EA REF',
'2023 Brill Journal Collection', 'IngentaConnect Intellect',
'Bloomsbury Collections All Titles', 'Digitalia Hispanica',
'De Gruyter English Language eBook Archive',
'Austrian Academy of Sciences', 'Project Gutenberg Online Catalog',
'American Society Of Civil Engineers ASCE Proceedings',
'Columbia University Press eBooks Archive (1658-1999) on De Gruyter',
'Project MUSE: Universal books',
'e-Duke Books Scholarly Collection 2022', 'SHERMAN OVERSIZE',
'Intellect Journals',
'University of Pennsylvania Press eBooks Archive (1898-1999) on De Gruyter',
'IEEE Electronic Library (IEL)', 'Mens Magazine Archive',
'Elsevier ScienceDirect Books',
'Yale University Press eBooks Archive (pre-2000) on De Gruyter',
'2023 Harvard University Press eBooks on De Gruyter',
'JSTOR Lives of Literature',
'2022 University of Chicago Press eBooks on De Gruyter',
'Rauner Special Collections Library Presses',
'De Gruyter eBook Archive',
'University of California Press eBooks Archive (pre-2000) on De Gruyter',
'Liverpool University Press',
'2023 Stanford University Press eBooks on De Gruyter',
'De Gruyter University Press Ebook Library',
'JSTOR Arts & Sciences XV',
'Elsevier ScienceDirect Journals Complete',
'2023 University of Chicago Press eBooks on De Gruyter', 'BAKER ',
'Cornell University Press eBooks Archive (pre-2000) on De Gruyter',
'Dartmouth Perpetual Access Print Books on De Gruyter',
'Early English Books Online',
'Princeton University Press eBooks Archive (1927-1999) on De Gruyter',
'BAKER JAPAN', 'Psychoanalytic Electronic Publishing Journals',
'SHERMAN READ RM',
'Harvard University Press eBooks Archive (1896-1999) on De Gruyter',
'Baker-Berry Library Japan Oversize', 'FELDBERG PERM RSRV',
'Brill - All E-Book Titles', 'Cairn Humanities eBooks @ Dartmouth'
`

- The DestinationLocation column contains a lot of overlapping values:

```
'Baker-Berry', 'Dana', 'Matthews-Fuller', 'Feldberg', nan,
'NO_RESULTS', 'ProQuest Entertainment Industry Magazine Archive',
'DEPOSITORY DEPOSITORY', 'OAPEN Free',
'Baker-Berry Library Stacks', 'EJ',
'EBSCOhost Academic Search Complete',
'Ebook Central Perpetual, DDA and Subscription Titles',
'Feldberg Business and Engineering Library Stacks',
'Jones Media Center DVD', 'BAKER STACKS', 'Digitalia Hispanica',
'Baker-Berry Library Not Cataloged Reserve',
'Baker-Berry Library East Asian',
'PERSEE - Portail de revues scientifiques en sciences humaines et sociales',
'JSTOR Arts and Sciences VII', 'Factiva', 'FELDBERG PERMRSRV',
'OpenEdition Freemium for Books', 'Baker',
'Elsevier ScienceDirect Journals'
```


- Exploit call number ([Library of Congress Classification](https://www.loc.gov/catdir/cpso/lcco/))
- Electronic vs physical loan (ask Emily about how to tell the difference)

Status:
- Chord diagrams don't change very much from month to month, find other categorical grouping
- Grouping by our own subject area grouping (one chart per subject area), and then dividing by top-level LCC classification works for many








