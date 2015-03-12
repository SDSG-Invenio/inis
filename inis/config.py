# -*- coding: utf-8 -*-
import sys

CFG_SITE_LANGS = ["en"]

CFG_SITE_NAME = "INIS Input Management"
CFG_SITE_NAME_INTL = {
    "en": CFG_SITE_NAME
}

DEPOSIT_TYPES = [
    "inis.modules.deposit.workflows.upload:upload",
]

PACKAGES = [
    "inis.base",
    "inis.demosite",
    "inis.modules.deposit",
    "invenio.modules.*",
    "invenio.base",
]

try:
    from inis import instance_config
    sys.modules[__name__] = instance_config
    del instance_config
except ImportError:
    pass

CFG_SUMBISSION_ERRORS = {
    0: 'The following fulltext files have names that do not correspond to any known TRN:',
    1: 'The following files do not contain TTF metadata (or TRN tag "001" is missing):',
}

# name of the role giving superadmin rights
SUPERADMINROLE = 'superadmin'

# name of the webaccess webadmin role
WEBACCESSADMINROLE = 'webaccessadmin'

DEF_ROLES = (
    (SUPERADMINROLE, 'superuser with all rights', 'deny any'),
    (WEBACCESSADMINROLE, 'WebAccess administrator', 'deny any'),
    ('anyuser', 'Any user', 'allow any'),
    ('basketusers', 'Users who can use baskets', 'allow any'),
    ('loanusers', 'Users who can use loans', 'allow any'),
    ('groupusers', 'Users who can use groups', 'deny any'),
    ('alertusers', 'Users who can use alerts', 'allow any'),
    ('messageusers', 'Users who can use messages', 'allow any'),
    ('holdingsusers', 'Users who can view holdings', 'allow any'),
    ('statisticsusers', 'Users who can view statistics', 'allow any'),
    ('claimpaperusers', 'Users who can perform changes to their own paper attributions without the need for an operator\'s approval', 'allow any'),
    ('claimpaperoperators', 'Users who can perform changes to _all_ paper attributions without the need for an operator\'s approval', 'deny any'),
    ('paperclaimviewers', 'Users who can view "claim my paper" facilities.', 'allow all'),
    ('paperattributionviewers', 'Users who can view "attribute this paper" facilities', 'allow all'),
    ('paperattributionlinkviewers', 'Users who can see attribution links in the search', 'allow all'),
    ('authorlistusers', 'Users who can user Authorlist tools', 'deny all'),
    ('holdingpenusers', 'Users who can view Holding Pen', 'deny all'),
)


CFG_MEMBERS_DICT = {
    "Afghanistan": """<b>INIS Liaison Officer</b><br>
Mr. Khoshal Ahmad Stanikzai<br>
GM Technical Cooperation<br>
Afghan Atomic Energy High Commission (AAEHC)<br>
Silo Main Street, KABUL, AFGHANISTAN<br>
Mobile: +93 (0) 700 246 957<br>
Email: khoshal@aaehc.gov.af<br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Mr. Bismillah Burhan<br>
Afghan Atomic Energy High Commission (AAEHC)<br>
Silo Main Street, KABUL, AFGHANISTAN<br>
Mobile: +93 (0) 776161003<br>
Email: besburhan@yahoo.com<br>""",
    "African Union (AU)": """<b>INIS Liaison Officer<br>
</b>Mr. Atef Wahba Ghabrial<br>
Chief, Science and Technology Department<br>
African Union (AU)<br>
P.O. Box 3243, Addis Ababa, Ethiopia<br>
Telex: 21046 OAU<br>
Telephone: 517700<br>
Cable: OAU, ADDIS ABABA<br>
Facsimile: +251(1) 517844""",
    "Albania": """<b>INIS Liaison Officer</b><br>
Ms. Flutura Bogdani<br>
Institute of Nuclear Physics<br>
P.O. box 85, Tirana, Albania<br>
Telephone: +355 4 376341<br>
Telex: 2166 itd<br>
Cable: ALFIB TIRANA (ALBANIE)<br>
Facsimile: +355 4 362596<br>
Email: inp@albaniaonline.net""",
    "Algeria": """<b>INIS Liaison Officer</b><br>
Mr. Djaber Krizou<br>
Chef de Département Formation et Informatique<br>
Centre de recherche nucléaire de Birine (CRNB)<br>
Commissariat à l'énergie atomique (COMENA)<br>
B.P. 180, 17230 Birine, Djelfa, Algeria<br>
Telephone: +213 714 09733<br>
Facsimile: +213 27 872952<br>
Email: kridja67@hotmail.com<br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Mr. Salim Asselah<br>
CERIST-Oran<br>
Cite du Chercheur (ex IAP), Es-senia ORAN, 31000, Algeria<br>
Telephone: +213 6 419697 or +213 6 419698<br>
Facsimile: +213 6 419699<br>
Email: rsalim@wissal.dz or pop-oran@mail.alnet.dz<br>
<br>
<b>Document Delivery Service</b><br>
Centre de Recherche sur l'Information Scientifique et Technique<br>
Mailing address: 03 Rue des Freres Aissou, Ben Aknoun Alge - Agerie<br>
Point of contact: Noureddine Meftouh<br>
Telephone: +213 91 62 05 at 08<br>
Fax: +213 91 21 26<br>
Email: nmeftouh@mail.cerist.dz<br>
URL: <a href="http://www.cerist.dz">http://www.cerist.dz</a>""",
    "Arab Atomic Energy Agency (AAEA)": """<b>INIS Liaison Officer<br>
</b>Ms. Nahla Nasr<br>
Division of Science and Technology, Arab Atomic Energy Agency (AAEA)<br>
7, Rue de L'assistance, Cité ElKhadhra, 1003 Tunis, Tunisia<br>
Telephone: +216 71 808 400<br>
Facsimile: +216 71 808 450<br>
Facsimile: +216 71 781 820<br>
Email: aaea@aaea.org.tn""",
    "Argentina": """<b>INIS Liaison Officer</b><br>
Ms. Mercedes Bavio<br>
Centro de Información Eduardo Savino (CIES)<br>
Centro Atómico Constituyentes, Comisión Nacional de Energía Atómica<br>
Avenida General Paz 1499, 1650 San Martín, Prov. de Buenos Aires, Argentina<br>
Telephone: +54 11 6772 7038<br>
Facsimile: +54 11 6772 7164<br>
Email: bavio@cnea.gov.ar<br>
URL: <a href="http://www.cnea.gov.ar/cac/ci">http://www.cnea.gov.ar/cac/ci</a><br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Ms. Laura Foz<br>
Centro de Información Eduardo Savino (CIES)<br>
Jefa Servicios al Usuario<br>
Centro Atómico Constituyentes, Comisión Nacional de Energía Atómica<br>
Avenida General Paz 1499<br>
1650 SAN MARTíN, Prov. de Buenos Aires, ARGENTINA<br>
Telephone: +54 11 6772-7946<br>
foz@cnea.gov.ar<br>
<br>
<b>Document Delivery Services</b><br>
Centro de Documentación María Isabel González, CNEA - Centro Atómico Ezeiza - Argentina<br>
Mailing address: Presbitero Juan Gonzólez y Aragán N° 15<br>
(B1802AYA), Partido de Ezeiza, Republica Argentina<br>
Point of contact: Ms. Silvana Semino<br>
Email: sisemino@cae.cnea.gov.ar<br>
Telephone: +54 11 6779 8431<br>
URL: <a href="http://caebis.cnea.gov.ar/IdEN/BIBLIO/index1.htm">http://caebis.cnea.gov.ar/IdEN/BIBLIO/index1.htm</a> Biblioteca Leo Falicov, Instituto Balseiro, CNEA - Argentina<br>
Mailing address: Av. Bustillo 9.500<br>
8400 - San Carlos de Bariloche, Republica Argentina<br>
Point of contact: Ms. Marisa Velazco Aldao<br>
Email: velazcom@cab.cnea.gov.ar<br>
Telephone: 54 2944 5195<br>
Fax: 54 9444 5195<br>
URL: <a href="http://cabbib2.cnea.gov.ar">http://cabbib2.cnea.gov.ar</a><br>
Information Center Autoridad Regulatoria Nuclear - Argentina<br>
Mailing address: Autoridad Regulatoria Nuclear, Centro Atómico Ezeiza, Presbitero Luis Gonzalez y Aragon N° 15<br>
(B1802AYA), Partido de Ezeiza, Republica Argentina<br>
Point of contact: Ms. Maria Alicia Carregado<br>
Email: acarregado@arn.gob.ar<br>
Telephone: +54 11 6779 8481<br>
Fax: +54 11 6779 8182<br>
URL: <a href="http://www.arn.gob.ar/Biblioteca/index.htm">http://www.arn.gob.ar/Biblioteca/index.htm</a><br>""",
    "Armenia": """<b>INIS Liaison Officer</b><br>
Mr. Armen Amirjanyan<br>
Director, Nuclear and Radiation Safety Centre<br>
Armenian Nuclear Regulatory Authority (ANRA)<br>
Tigran Mets St. 4, 6th floor, Yerevan 0010, Armenia<br>
Telephone: +374 1 54 3992<br>
Facsimile: +374 1 54 3992<br>
Email: a.amirjanyan@nrsc.am<br>
URL: <a href="http://www.anra.am">http://www.anra.am</a><br>
<br>
<b>Document Delivery Service</b><br>
Nuclear and Radiation Safety Center<br>
Mailing address: #4 Tigran Mets st.<br>
Point of contact: Ms Tatyana Petrosyan<br>
Telephone: +374 10 54 39 92<br>
Fax: +374 10 54 39 92<br>
Email: t.petrosian@anra.am or a.amirjanyan@nrsc.am""",
    "Australia": """<b>INIS Liaison Officer<br>
</b>Diana Sargent <br>
Cataloguing/INIS Indexing Librarian<br>
Australian Nuclear Science and Technology Organization<br>
Locked Bag 2001 Kirrawee DC NSW 2232 <br>
Australia<br>
Telephone: +61-2 9717 3863<br>
Facsimile: +61-2 9717 9295<br>
Email: diana.sargent@ansto.gov.au; nlhr@ansto.gov.au<br>
URL: <a href="http://www.ansto.gov.au/">http://www.ansto.gov.au/</a><br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Web Services Librarian<br>
Australian Nuclear Science and Technology Organisation<br>
Locked Bag 2001 Kirrawee DC NSW 2232<br>
New Illawarra Road, Lucas Heights NSW, Australia<br>
<br>
<br>
<b>Document Delivery Service</b><br>
ANSTO Library - Australia<br>
Mailing address: ANSTO - Library &amp; Knowledge Management, Locked Bag 2001 Kirrawee DC NSW 2232, New Illawarra Road, Lucas Heights NSW, AUSTRALIA<br>
Point of contact: INIS Liaison Officer<br>
Telephone: +61-2-9717 3363<br>
Fax: +61-2-9717 9295<br>
Email: inis@ansto.gov.au<br>
URL: <a href="http://www.ansto.gov.au">http://www.ansto.gov.au</a>""",
    "Austria": """<b>INIS Liaison Officer</b><br>
Ms. Brigitte Kromp<br>
Österreichische Zentralbibliothek für Physik<br>
Universitat Wien<br>
Boltzmanngasse 5<br>
A-1090 Wien, Austria<br>
Telephone: +43 1 4277 27603<br>
Mobile: +43 664 602 77 27603<br>
Facsimile: +43 1 4277 9276<br>
Email: brigitte.kromp@univie.ac.at<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Mrs Lilian Nowak<br>
Österreichische Zentralbibliothek für Physik<br>
Universitat Wien<br>
Boltzmanngasse 5<br>
A-1090 Wien, Austria<br>
Telephone: +43 1 4277 27600<br>
Facsimile: +43 1 4277 9276<br>
Email: lilian.nowak@univie.ac.at""",
    "Azerbaijan": """<b>INIS Liaison Officer</b><br>
Mr. Adil Garibov<br>
Institute of Radiation Problems of AzNAS<br>
B.Vakhabzade Avenue 9, Baku 1143, Azerbaijan<br>
Telephone: (+994 12) 539 33 91<br>
Facsimile: (+994 12) 539 83 18<br>
Email: gabulov@azdata.net<br>
<br>
<b>Document Delivery Service</b><br>
Institute of Radiation Problems of Azerbaijan<br>
Mailing address: Institute of Radiation Problems of Azerbaijan, National Academy of Sciences, B.Vakhabzade 9, Baku 1143, Yasamal district, Baku, Azerbaijan<br>
Point of contact: Mr. Sharif Mamedzade, Acting Head of INIS<br>
Telephone: (+994 12) 439 33 91<br>
Facsimile: (+994 12) 439 83 18<br>
Email: sharifmamedzade@yahoo.com""",
    "Bangladesh": """<b>INIS Liaison Officer</b><br>
Mr. Md. Karam Newaz<br>
Chief Scientific Officer &amp; Director<br>
Institute of Computer Science, Atomic Energy Research Establishment<br>
AERE, Savar, G.P.O. Box 3787, Ramna, Dhaka, Bangladesh<br>
Telephone: 8802 8130987 or 88028141843<br>
Facsimile: 8802 9142121 or 88028130102<br>
Website: www.baec.org.bd<br>
Email: newaz2017@gmail.com or nlo.baec@gmail.com""",
    "Belarus": """<b>INIS Liaison Officer</b><br>
Mr. U. Ivaniukovich<br>
Belarus INIS Center, Chair of Ecological Information Systems<br>
International A.Sakharov Environmental University<br>
vul. Dawgabrodskaya 23, 220009 Minsk, Belarus<br>
Telephone: +375-17-2308917<br>
Mobile: +375-296886781<br>
Facsimile: +375-17-2306888<br>
Email: u_ivaniukovich@tut.by<br>
URL: <a href="http://www.iseu.by">http://www.iseu.by</a><br>""",
    "Belgium": """<b>INIS Liaison Officer</b><br>
Mr. Alain Sneyers<br>
S.C.K./C.E.N.<br>
Gebouw Scheikunde, Boeretang 200, B-2400 Mol, Belgium<br>
Telephone: +32 14 333137<br>
Facsimile: +32 14 323553<br>
Email: asneyers@sckcen.be<br>
URL: <a href="http://www.sckcen.be">http://www.sckcen.be</a>""",
    "Benin": """<b>INIS Liaison Officer</b><br>
Mr Jérôme Nouhouaï<br>
Institut de Mathématiques et de Sciences Physiques (IMSP), 01BP613, Porto-Novo, Benin<br>
Telephone: +229 20 22 2455 or +229 95 59 2579<br>
Email: jeromenouhouai@yahoo.fr or nouhouai@imsp-uac.org<br>""",
    "Bolivia": """<b>INIS Liaison Officer</b><br>
Ms. Yenny Frances Mamani Tarqui<br>
Instituto Boliviano de Ciencia y Tecnologí a Nuclear (IBTEN)<br>
Casilla Postal 4821, Av. 6 De Agos&gt;&gt;2905, La Paz, Bolivia<br>
Telephone: 00591 2 430309<br>
Cell phone: 00591 72022548<br>
Telex: 2220 CABPUB BV<br>
Cable: IBTEN LAPAZ<br>
Facsimile: 00591 2 433063<br>
Email: ymamani@ibten.gob.bo or yennyfmt@yahoo.com""",
    "Bosnia and Herzegovina": """<b>INIS Liaison Officer</b><br>
Ms. Maida Kahvic<br>
State Regulatory Agency for Radiation and Nuclear Safety<br>
Hamdije Cemerlica 2<br>
71 000 Sarajevo, Bosnia and Herzegovina<br>
Telephone: +387 33 726 300<br>
Facsimile: +387 33 726 301<br>
Email: maida.kahvic@darns.gov.ba<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Mr. Ognjen Borovina<br>
State Regulatory Agency for Radiation and Nuclear Safety<br>
Hamdije Cemerlica 2<br>
71 000 Sarajevo, Bosnia and Herzegovina<br>
Telephone: +387 33 726 300<br>
Facsimile: +387 33 726 301<br>
Email: ognjen.borovina@darns.gov.ba""",
    "Botswana": """<b>INIS Liaison Officer</b><br>
Mr. Enoch Senyatso<br>
Deputy Director<br>
Department of Research, Science and Technology<br>
Ministry of Communications, Science and Technology<br>
Private Bag 00414, Gaborone, Botswana<br>
Telephone: +267 361 3115<br>
Facsimile: +267 318 8487<br>
Email: esenyatso@gov.bw<br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Mr. Stephen Duncan Williams<br>
Deputy Director<br>
Department of Research, Science and Technology<br>
Ministry of Communications, Science and Technology<br>
Private Bag 00414, Gaborone, Botswana<br>
Telephone: +267 361 2007<br>
Facsimile: +267 318 8487<br>
Email: swilliams@gov.bw<br>
<br>
<b>Document Delivery Service</b><br>
Department of Research Science and Technology<br>
Mailing address: Department of Research Science and Technology, Private Bag BR 279, Gabarone, Botswana<br>
Point of contact: The Director<br>
Telephone: +267 361 3100<br>
Fax: +267 318 8487<br>
Email: eselaolo@gov.bw<br>
URL: <a href="http://www.mcst.gov.bw">http://www.mcst.gov.bw</a>""",
    "Brazil": """<b>INIS Liaison Officer</b><br>
INIS Liaison Officer<br>
Ms. Fabiane Dos Reis Braga<br>
National Nuclear Energy Commission of Brazil (CNEN)<br>
Rua General Severiano 90<br>
CEP 22.290-901, Rio de Janeiro - RJ, Brazil<br>
Telephone: +55 21 2173 2050<br>
Email: fabiane@cnen.gov.br<br>
URL: <a href="http://cin.cnen.gov.br/inis-brasil">http://cin.cnen.gov.br/inis-brasil</a><br>
<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Mr Luiz Fernando Sayao<br>
Nuclear Information Centre-CIN<br>
General Coordination of Information Technology- CGTI<br>
National Nuclear Energy Commission of Brazil (CNEN)<br>
Rua General Severiano 90<br>
CEP 22.290-901, Rio de Janeiro - RJ, Brazil<br>
Tel: +55 21 2173 2028<br>
Email: lsayao@cnen.gov.br<br>
<br>
<b>Document Delivery Service</b><br>
Centro de Informações Nucleares - Brasil<br>
Mailing address: 22290-901 Rio de Janeiro, RJ BRASIL<br>
Point of contact: Maria Betania Monte Alto Lambert, INIS Liaison Officer - Brasil<br>
Telephone: +55 21 2173-2032<br>
Fax: +55 21 2173-2043<br>
Email: servir@cnen.gov.br<br>
URL: <a href="http://www.cnen.gov.br">http://www.cnen.gov.br</a><br>
ARIEL IP: 200.156.4.3""",
    "Brazilian-Argentine Agency for Accounting and Control of Nuclear Materials (ABACC)": """<b>INIS Liaison Officer<br>
</b>Ms. Selma Chi-Barreiro<br>
Institutional Relations Officer of ABACC<br>
Av. Rio Branco, 123, Centro, 20040-005 Rio de Janeiro-RJ, Brazil<br>
Telephone: +55 21 3171 1200<br>
Facsimile: +55 21 3171 1248<br>
Email: selmachi@abacc.org.br<br>
URL: <a href="http://www.abacc.org">http://www.abacc.org</a><br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Mr. José Orpet Marques Peixoto<br>
Institutional Relations Officer of ABACC<br>
Av. Rio Branco, 123, Centro, 20040-005 Rio de Janeiro-RJ, Brazil<br>
Telephone: +55 21 3171 1200<br>
Facsimile: +55 21 3171 1248<br>
Email: orpet@abacc.org.br""",
    "Bulgaria": """<b>INIS Liaison Officer</b><br>
Ms. Albena Georgieva<br>
Mailing address: Bulgarian INIS Centre, Nuclear Regulatory Agency, 69 Shipchenski Prokhod, 1574 Sofia, Bulgaria<br>
Telephone: + 359 2 940 6943<br>
Facsimile: + 359 2 940 6919<br>
Email: A.Georgieva@bnra.bg<br>
URL: <a href="http://www.bnra.bg">http://www.bnra.bg</a><br>""",
    "Burkina Faso": """<b>INIS Liaison Officer</b><br>
Mr. Bertrand Windingoudin Sawadogo<br>
Ministére des Ressources Animales<br>
Mailing address: 03 Boîte Postale 7026, Ouagadougou 03, Burkina Faso<br>
Telephone: +226 50 36 5918 or +226 50 36 4179<br>
Email: ilo-bf@live.fr or wbertran1@yahoo.fr<br>""",
    "Cameroon": """<b>INIS Liaison Officer</b><br>
Ms. Annie Wakata<br>
Ministère de la Recherche Scientifique et de l'Innovation<br>
B.P. 1457, Yaoundé, Cameroon<br>
Telephone: + 237 22 22 1334<br>
Facsimile: + 237 22 22 1336<br>
Email: annie_beya@yahoo.fr<br>
<br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Mr. Patrice Ele Abiama<br>
Section des Techniques Nucléaires<br>
Laboratoire de Recherches Energétiques<br>
Institut de Recherches Géologiques et Minières<br>
B.P. 4110, Yaoundé, Cameroon<br>
Telephone: + 237 22 22 2430<br>
Facsimile: + 237 22 22 2441<br>
Email: eleabiama2003@yahoo.fr<br>""",
    "Canada": """<b>INIS Liaison Officer</b><br>
Ms Jeannie Tilson<br>
Section Head, Library and Document Management<b><br>
</b>Canadian Nuclear Laboratories (CNL)<br>
286 Plant Road, Stn 13<br>
Chalk River, Ontario K0J 1J0, Canada<br>
Telephone: +1 613 584-8811 ext. 44626<br>
Facsimile: +1 613 584-8144<br>
Email: jeannie.tilson@cnl.ca<br>
URL: <a href="http://www.aecl.ca">http://www.cnl.ca</a><br>
<span style=" text-decoration: underline;"><br>
</span><b>Document Delivery Service<br>
</b>Canadian Nuclear Laboratories Library, Canadian Nuclear Laboratories (CNL)<br>
Mailing address: The Library, Canadian Nuclear Laboratories, 286 Plant Road, Chalk River, Ontario K0J 1J0<br>
Telephone: 1-613-584-3311, ext. 43900 - The Library Reference Desk<br>
Fax: 1-613-584-8221<br>
Email: librarycr@cnl.ca<br>""",
    "Central African Republic": """<b>INIS Liaison Officer</b><br>
Mr. Kondji Yvon Simplice<br>
University of Bangui<br>
P.O. Box 908, Bangui, Central African Republic<br>
Telephone: +236 05 9473<br>
Email: yskondji@yahoo.fr<br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Mr. Kouagou-Bangassi Thierry Narcisse<br>
Head, Department of Industrial Genius<br>
University of Bangui<br>
P.O. Box 908, Bangui<br>
Central African Republic<br>
Telephone: +236 50 72 94<br>
Email: thierbk@yahoo.fr""",
    "Chad": """<b>INIS Liaison Officer</b><br>
Mr Mbodou Djirab Alifey<br>
Ministère du Pétrole et de l'Energie<br>
<span class="c10">Agence Tchadienne de la Radioprotection et de la Sécurité Nucléaire (ATRSN)<br>
Avenue du Dr Nokouri<br>
Anni Djari, P.O. Box 816<br>
N'DJAMENA 235</span><br>
Chad, Republic of<br>
Telephone: +235 22 52 53 00<br>
Fax: +235 22 52 5300<br>
Email: mbodou_alifei@yahoo.fr<br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Monsieur Hissein Galmaye Abdallah<br>
Ingénieur en Radioprotection<br>
à l’Agence Tchadienne de la Radioprotection et de la Sécurité Nucléaire (ATRSN)<br>
<span class="c10">Avenue du Dr Nokouri<br>
Anni Djari, P.O. Box 816<br>
N'DJAMENA 235</span><br>
Chad, Republic of<br>
Telephone: +235 66 43 06 52<br>
Fax: +235 22 52 53 00<br>
Email: hisseni_gal@yahoo.fr""",
    "Chile": """<b>INIS Liaison Officer</b><br>
Ms. Cecilia Navarette Urbina<br>
Jefe de Bibliotecas<br>
Comisión Chilena de Energí a Nuclear<br>
Av. Nueva Bilbao 12.501, Las Condes, Santiago de Chile<br>
Telephone: +562-3646 165<br>
Facsimile: +562-3646 300<br>
Email: cnavarre1@cchen.cl<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Ms. Victoria Ortiz<br>
<br>
<b>Document Delivery Service</b><br>
Comision Chilena de Energia Nuclear, Departamento de Ingenieria y Sistemas Mailing address: Amunategui 95 - Casilla 188 - D Santiago Chile Point of contact: Lila Trujillo (Biblioteca Centro Nuclear La Reina) Telephone: +56 23646164 Fax: +56 273 8723 Email: ltrujill@gopher.cchen.cl""",
    "China": """<b>INIS Liaison Officer<br>
</b>Mr. Jun Gong<br>
Director<br>
China Institute of Nuclear Information and Economics<br>
43 Fuchenglu, Haidian District 100048 Beijing, People's Republic of China<br>
Telephone: +86 010 88828686<br>
Email: gong1956966@126.com<br>
<br>""",
    "Colombia": """<b>INIS Liaison Officer<br>
</b>Mr. Leopoldo González Oviedo<br>
Servicio Geológico Colombiano - SGC<br>
Ministerio de Minas y Energí a<br>
Diagonal 53, no. 34-53, Santafé de Bogotá, D.C., Colombia<br>
Telephone: +57 1 2221811 ext. 2102 or 57 1 2200102<br>
Facsimile: +57 1 2223597<br>
Email: <a href="mailto:leogonza@sgc.gov.co">leogonza@sgc.gov.co</a>""",
    "Costa Rica": """<b>INIS Liaison Officer<br>
</b>Ms. Maria Eugenia Briceño Meza<br>
Directora<br>
Sistema de Bibliotecas, Documentación e Información (SIBDI)<br>
Universidad de Costa Rica<br>
Apartado Postal 2060, Ciudad Universitaria Rodrigo Facio, San José, Costa Rica<br>
Telephone: +506 22 53 6152<br>
Facsimile: +506 22 34 2809234-2809<br>
Email: ma.briceno@ucr.ac.cr<br>
URL: <a href="http://sibdi.ucr.ac.cr">http://sibdi.ucr.ac.cr</a><br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Ms. Sandra Garro Calderón<br>
Funcionaria del Sistema de Bibliotecas, Documentación e Información (SIBDI)<br>
Universidad de Costa Rica<br>
Apartado Postal 2060, Ciudad Universitaria Rodrigo Facio, San José, Costa Rica<br>
Telephone: +506 22 07 43 54<br>
Facsimile: +506 22 07 4046<br>
Email: sandra.garro@ucr.ac.cr<br>
<br>""",
    "Croatia": """<b>INIS Liaison Officer</b><br>
Ms. Sunčana Podhraški Benković<br>
State Office for Radiological and Nuclear Safety<br>
Frankopanska 11, 10000 Zagreb, Croatia<br>
Telephone: +385 1 488 1786<br>
Facsimile: +385 1 488 1780<br>
Email: suncana.pb@dzrns.hr<br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Ms. Nevenka Novosel<br>
State Office for Radiological and Nuclear Safety<br>
Frankopanska 11, 10 000 Zagreb, Croatia<br>
Telephone: +385 1 4881789<br>
Facsimile: +385 1 4881780<br>
Email: nevenka.novosel@dzrns.hr<br>
<br>
<b>Document Delivery Service</b><br>
National and Univesity Library<br>
Mailing address: Official Publications Collection, Ulica Hrvatske bratske zajednice 4, p.p. 550, 10000 Zagreb, Croatia, Republika Hrvatska<br>
Telephone: 00385 1 6164 111<br>
Fax: 00385 1 6164 186<br>
URL: <a href="http://www.nsk.hr">http://www.nsk.hr</a>""",
    "Cuba": """<b>INIS Liaison Officer</b><br>
Mr. Daniel López Aldama <br>
Director<br>
Centro de Gestión de la Información Desarrollo de la Energí a CUBAENERGIA<br>
Calle 20 No. 4111 esq. 47 y 18A, Miramar, Playa, C. Habana, Cuba<br>
Telephone: +53 (7) 202 7527<br>
Facsimile: + 53 (7) 204 1188<br>
Email: aldama@cubaenergia.cu<br>
URL: <a href="http://www.cubaenergia.cu">http://www.cubaenergia.cu</a><br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Ms. Irayda Oviedo Rivera<br>
Centro de Gestión de la Información Desarrollo de la Energí a CUBAENERGIA<br>
Calle 20 No. 4111 esq. 47 y 18A, Miramar, Playa, C. Habana, Cuba<br>
Telephone: +53 (7) 202 2059<br>
Facsimile: +53 (7) 204 1188<br>
Email: irayda@cubaenergia.cu<br>
URL: <a href="http://www.cubaenergia.cu">http://www.cubaenergia.cu</a><br>
<br>
<b>Document Delivery Service</b><br>
Centro de Informacion de la Energia Nuclear - Cuba<br>
Mailing address: Calle 20 No. 4111, e/47y18A Playa, Ciudad Habana, CUBA<br>
Point of contact: Iraida Oviedo Cabrera<br>
Telephone: 2062059<br>
Fax: 2041188<br>
Email: iraida@cubaenergia.cu<br>""",
    "Cyprus": """<b>INIS Liaison Officer</b><br>
Mr. Andreas Savva<br>
Librarian<br>
Health Science Library<br>
Nicosia General Hospital, Nicosia, Republic of Cyprus<br>
Telephone: + 357 22 301-203<br>
Facsimile: + 357 22 672528<br>
Email: g.h.library@cytanet.com.cy<br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Mr. S. Christofides<br>
Facsimile: + 357 22 801773<br>
Email: cstelios@cytanet.com.cy""",
    "Czech Republic": """<b>INIS Liaison Officer<br>
</b>Mr. Petr Adamek<br>
INIS Office<br>
Preslickova 2679, 10600 Praha 10, Czech Republic<br>
Telephone: +420 222 983 857<br>
Email: INIS@sujb.cz<br>
<br>
<br>
<b>Document Delivery Service</b><br>
Nuclear Research Institute - Czech Republic<br>
Mailing address: Nuclear Research Institute, Library, 25068 Rez, Czech Republic<br>
Point of contact: Ms. Lucie Richterova, Head of the Library<br>
Telephone: +42 0 266 173 402<br>
Email: ric@ujv.cz""",
    "Côte d'Ivoire": """<b>INIS Liaison Officer<br>
</b>Mr. Aka Antonin Koua<br>
Laboratoire de Physique Nucléaire et Radioprotection<br>
UFR SSMT, Université de Cocody<br>
22 BP 582 Abidjan 22<br>
Côte d'Ivoire<br>
Telephone: +225 07 61 2829 / 22 48 3882<br>
Facsimile: +225 2248 3882<br>
Email: antoninkoua@yahoo.fr<br>
<br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Mr. Tekpo Paul-Amewe Dali<br>
Laboratoire de Physique Nucléaire et Radioprotection<br>
UFR SSMT, Université de Cocody<br>
22 BP 582 Abidjan 22<br>
Côte d'Ivoire<br>
Telephone: +225 01 61 1780<br>
Facsimile: +225 2248 3807<br>
Email: paultekpo@yahoo.fr<br>
<br>
<br>
<b>Document Delivery Service</b><br>
Laboratoire de Physique Nucléaire et Radioprotection, UFR SSMT, Université de Cocody<br>
Mailing address: 22 BP 582 Abidjan 22, Côte d'Ivoire<br>
Telephone: +225 07 61 2829 / 22 48 3882<br>
Fax: +225 2248 3882<br>
Email: antoninkoua@yahoo.fr""",
    "Democratic Republic of the Congo": """<b>INIS Liaison Officer<br>
</b>Mr. Michel Kalumvueziko Lundula<br>
Commissariat Général à l' Energie Atomique (CGEA)<br>
Centre Régional d' Etudes Nucléaires de Kinshasa (CREN-K)<br>
c-o UNDP, P.B. 7248, Kinshasa, Democratic Republic of the Congo<br>
Telephone: +243 12 123769646<br>
Facsimile: +243 12 123769646<br>
Email: michelkalum@yahoo.fr<br>""",
    "Denmark": """<b>INIS Liaison Officer<br>
</b>Ms. Birgit Pedersen<br>
Head of Department, Information Service Department<br>
Risoe National Laboratory for Sustainable Energy, Technical University of Denmark - DTU, P.O. Box 49, DK-4000 Roskilde, Denmark<br>
Telephone: +45 4677 4001<br>
Facsimile: +45 4677 4013<br>
Email: bipe@risoe.dtu.dk<br>
URL: <a href="http://www.risoe.dtu.dk">http://www.risoe.dtu.dk</a><br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Ms. Line Nissen<br>
Email: lrni@risoe.dtu.dk<br>
<br>
<b>Document Delivery Service</b><br>
Risø Library - Denmark<br>
Mailing address: Risø National Laboratory for Sustainable Energy, Technical Universtiy of Denmark - DTU, Bldg. 115, P.O. Box 49, DK-4000 Roskilde, Denmark<br>
Telephone: +45 4677 4005<br>
Fax: +45 4677 4013<br>
Email: bibl@risoe.dtu.dk<br>
URL: <a href="http://www.risoe.dtu.dk">http://www.risoe.dtu.dk</a>""",
    "Ecuador": """<b>INIS Liaison Officer<br>
</b>Ms. Hipsy Cifuentes<br>
Centro de Información Nuclear<br>
Comisión Ecuatoriana de Energí a Atómica<br>
Calle Juan Larrea 254 entre Riofrí o y Buenos Aires, Casilla 17-01-2517, Quito, Ecuador<br>
Telephone: 593 2 434 964<br>
Telex: 21461 CEEA ED<br>
Facsimile: 593 2 563336<br>
Email: cin@ceea.gov.ec<br>
<br>
<b>Document Delivery Service</b><br>
INIS/CIN Full Text Service<br>
Mailing address: Comision Ecuatoriana de Energia Atomica, Centro de Informacion Nuclear, Juan Larrea 534 y Riofrio, P. O. Box 17 01 2517, Quito, Ecuador<br>
Point of contact: Nuclear Information Centre<br>
Telephone: 593-2-545861, 545773, 255166<br>
Fax: 593-2-563336<br>
Email: comecen1@comecenat.gov.ec<br>""",
    "Egypt": """<b>INIS Liaison Officer<br>
</b>Ms. Wafaa Abd Elatif abd Elhady<br>
Atomic Energy Authority<br>
Mailing address: Nuclear Information Center, Atomic Energy Authority, 3 Ahmed El Zomer St.<br>
El Zahoor Dist, Naser City-Cairo, EGYPT<br>
Telephone: +20-2-2875926<br>
Telex: 92790 EGTOM UN<br>
Facsimile: +20-2-2876031<br>
Email: wafaa27_helal@yahoo.com<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Ms. Amal Mohamed Salah Eldin<br>
Atomic Energy Authority<br>
Mailing address: Nuclear Information Center, Atomic Energy Authority, 3 Ahmed El Zomer St.<br>
El Zahoor Dist, Naser City-Cairo, EGYPT<br>
Telephone: +20-2-2875926<br>
Telex: 92790 EGTOM UN<br>
Facsimile: +20-2-2876031<br>
Email: amalabdelaziz14@yahoo.com<br>
<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Mr. Mohamad Elsayed Yousef<br>
Atomic Energy Authority<br>
Mailing address: Nuclear Information Center, Atomic Energy Authority, 3 Ahmed El Zomer St.<br>
El Zahoor Dist, Naser City-Cairo, EGYPT<br>
Telephone: +20-2-2875926<br>
Telex: 92790 EGTOM UN<br>
Facsimile: +20-2-2876031<br>
Email: m70elsayed@yahoo.com""",
    "El Salvador": """<b>INIS Liaison Officer<br>
</b>Prof. Oscar Armando Amaya Monterrosa<br>
Escuela de Fisica del la, Universidad de El Salvador<br>
San Salvador, El Salvador<br>
Telephone: +503 22 25 7466<br>
Facsimile: +503 22 25 15 00 ext. 4406<br>
Email: oscar.amaya@ues.edu.sv or amaya_armando@hotmail.com<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Prof. Marco Antonio Ayala Aristondo""",
    "Estonia": """<b>INIS Liaison Officer<br>
</b>Ms Anne Luik-Ristikivi<br>
Library. Institute of Physics<br>
University of Tartu<br>
Riia 142, 51014 Tartu, Estonia<br>
Telephone: +372 737 4625<br>
GSM: +372 5384 4793<br>
Fax: +372 738 3033<br>
anne@fi.tartu.ee<br>""",
    "Ethiopia": """<b>INIS Liaison Officer<br>
</b>Mr. Abebe Woldie Alemu<br>
Head, Science and Technology Information Department<br>
Ethiopian Science and Technology Agency<br>
P.O. Box 2490, Addis Ababa, Ethiopia<br>
Telephone: +251 11 551 1344, ext. 253<br>
Facsimile: +251 11 551 8829<br>
Email: alemuabebe2002@yahoo.com<br>
URL: <a href="http://www.estc.gov.et">http://www.estc.gov.et</a><br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Mr. Muluken Wubayehu<br>
Website Administration Expert<br>
Information Technology Department<br>
Ethiopian Science and Technology Agency<br>
P.O. Box 2490, Addis Ababa, Ethiopia<br>
Telephone: +251 11 573434<br>
Facsimile: +251 11 572715<br>
Email: mulukenw@mail.com<br>""",
    "European Commission (EC)": """<b>INIS Liaison Officer</b><br>
Ms Zdenka Palajova<br>
Research Programme Officer, European Commission<br>
DG Joint Research Centre Unit A.8, Nuclear Safety and Security Coordination<br>
SDME 10/64, B-1049-Brussels BELGIUM<br>
Telephone: +32 2 29 97667<br>
Email: zdenka.palajova@ec.europa.eu""",
    "European Organization for Nuclear Research (CERN)": """<b>INIS Liaison Officer<br>
</b>Mr. Jens Vigen<br>
Scientific Information Service, European Organization for Nuclear Research (CERN)<br>
CH-1211 Geneva 23, Switzerland<br>
Telephone: +41 (22) 7672410<br>
Telex: 419000 CER<br>
Facsimile: +41 (22) 7828611<br>
Email: Jens.Vigen@cern.ch<br>
URL: <a href="http://www.cern.ch">http://www.cern.ch</a><br>
Document delivery point of contact: Corrado Pettenati<br>
Email: Corrado.Pettenati@cern.ch<br>
Delivery services: electronic via http<br>
Request services: e-mail, web<br>
Cost: free of charge""",
    "Finland": """<b>INIS Liaison Officer<br>
</b>Ms. Eva Tolonen<br>
Aalto University Library<br>
P.O. Box 17000, 00076 Aalto, Finland<br>
Telephone: +358-9-47024140<br>
Facsimile: +358-9-47024132<br>
Email: eva.tolonen@aalto.fi<br>
URL: <a href="http://www.aalto.fi">http://www.aalto.fi</a>""",
    "Food and Agricultural Organization of the United Nations (FAO)": """<b>INIS Liaison Officer<br>
</b>Mr. G. Stergiou<br>
Library and Documentation Systems Division<br>
Food and Agriculture Organization of the United Nations (FAO)<br>
Via delle Terme di Caracalla, I-00100 Rome, Italy<br>
Telephone: +390 6 52256642 (switchboard: 52251)<br>
Telex: 625852 / 625853 / 610181 FAO I<br>
Facsimile: +390 6 52254049<br>
Email: gabriel.stergiou@fao.org<br>
URL: <a href="http://www.fao.org">http://www.fao.org</a>""",
    "France": """<b>INIS Liaison Officer<br>
</b>Mr. Jérôme Surmont<br>
CEA-Saclay<br>
DSM/SAC/UST/SVI, Bat 526, Point courrier N°88, F-91191 Gif-sur-Yvette Cedex, France<br>
F-91191 Gif-sur-Yvette Cedex, France<br>
Telephone: +33 (0)1 69 08 32 17<br>
Facsimile: +33 (0)1 69 08 79 26<br>
Email: jerome.surmont@cea.fr<br>
URL: <a href="http://www.cea.fr/">http://www.cea.fr/</a><br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Ms. Odile Mouffron<br>
Group INIS<br>
CEA-Saclay<br>
DSM/SAC/UST/SVI, Bat 526, Point courrier N°88, F-91191 Gif-sur-Yvette Cedex, France<br>
Telephone: +33 (0)1 69 08 5200<br>
Email: odile.mouffron@cea.fr<br>
URL: <a href="http://www-ist.cea.fr/">http://www-ist.cea.fr/</a><br>
<br>
<b>Document Delivery Service</b><br>
INIST-CNRS - France<br>
Mailing address: INIST-CNRS, 2 allée du Parc de Brabois, CS 10310, F-54519, Vandoeuvre-lès-Nancy, France Telephone: +33 (0)3 83 50 46 00<br>
Fax: +33 (0)3 83 50 46 50<br>
Email: <a href="http://international.inist.fr/article2.html">http://international.inist.fr/article2.html</a><br>
URL: <a href="http://international.inist.fr/">http://international.inist.fr/</a><br>""",
    "Gabonese Republic": """<b>INIS Liaison Office<br>
</b>Ms Martine Lekogo Edzougou<br>
Centre National de Prévention et de Protection contre les Rayonnements Ionisants<br>
Ministère du Pétrole, de l'Energie et des Ressources Hydrauliques<br>
BP : 1172, Libreville, Gabon<br>
Telephone: (241) 05 33 75 08<br>
Email: lekmart@yahoo.fr<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Ms Christelle Azouadelly<br>
Direction Générale des Techniques Nucléaires<br>
Ministère du Pétrole, de l'Energie et des Ressources Hydrauliques<br>
BP : 1172, Libreville, Gabon<br>
Telephone: (241) 06 61 82 96<br>
Email: ancat6@yahoo.fr<br>""",
    "Georgia": """<b>INIS Liaison Officer</b><br>
Mr. Irakli N. Maisuradze<br>
Ivane Beritashvili Center of Experimental Biomedicine<br>
Gotua Street 14, 0160, Tbilisi, Georgia<br>
Telephone: +995 32 95 92 54<br>
Telefax: + 995 32 332 867<br>
Email: cooh@cheerful.com<br>
<br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Mr. Mikheil Jorbenadze<br>
Ivane Beritashvili Center of Experimental Biomedicine<br>
14, Gotua str., 1060 Tbilisi, Georgia<br>
Telephone (office): +995 322 273565<br>
Telephone (mobile): +995 5 77 190439<br>
Email: Jorbenadze65@yahoo.com<br>
URL: <a href="http://www.mjorbenadze.webs.com">www.mjorbenadze.webs.com</a><br>
<br>
<b>Document Delivery Service</b><br>
Life Research Sciences Center<br>
Ivane Beritashvili Center of Experimental Biomedicine<br>
Gotua Street 14, 0160, Tbilisi, Georgia<br>
Point of contact: Irakli Maisuradze, Radiation Information Laboratory<br>
Telephone: +995 32 95 92 54<br>
Fax: +995 32 33 28 67<br>
Email: cooh@cheerful.com<br>
URL: <a href="http://www.radiobiology.org.ge">http://www.radiobiology.org.ge</a>""",
    "Germany": """<b>INIS Liaison Officer</b><br>
Ms. Silke Rehme<br>
Fachinformationszentrum Karlsruhe (FIZ Karlsruhe)-Leibniz Institute for Information Infrastructure<br>
Hermann-von-Helmholtz-Platz 1, 76344 Eggenstein-Leopoldshafen, Germany<br>
Telephone: +49 7247 808 221<br>
Telefax: +49 7247 808 132<br>
Email: silke.rehme@fiz-karlsruhe.de<br>
URL: <a href="http://www.fiz-karlsruhe.de">http://www.fiz-karlsruhe.de</a> - STN Service Center Europe<br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Ms. Sabrina Eck<br>
FIZ Karlsruhe-Leibniz Institute for Information Infrastructure<br>
Hermann-von-Helmholtz-Platz 1, 76344 Eggenstein-Leopoldshafen, Germany<br>
Telephone: +49 7247 808-257<br>
Telefax: +49 7247 808 666<br>
Email: sabrina.eck@fiz-karlsruhe.de<br>
<br>
<b>Document Delivery Service</b><br>
FIZ Karlsruhe Document Delivery Service - Germany<br>
Mailing address: Fachinformationszentrum Karlsruhe, Hermann-von-Helmholtz-Platz 1, D-76344 Eggenstein-Leopoldshafen, Germany<br>
Point of contact: FIZ AutoDoc<br>
Telephone: +49 7247 808555<br>
Fax: +49 7247 808295<br>
Email: autodoc@fiz-karlsruhe.de<br>
URL: <a href="http://autodoc.fiz-karlsruhe.de">http://autodoc.fiz-karlsruhe.de</a>""",
    "Ghana": """<b>INIS Liaison Officer<br>
</b>Ms. E.A. Agyeman<br>
Library<br>
Ghana Atomic Energy Commission<br>
P.O. Box 80, Legon, Accra, Ghana<br>
Telephone: +233 21 400303 and 400310<br>
Cable: GHANATOM-ACCRA<br>
Telex: 2554 GAEC GH<br>
Facsimile: +233 21 400807<br>
Email: e.agyeman@gaecgh.org<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Mr. Richard Asare<br>
School of Nuclear and Allied Sciences<br>
Ghana Atomic Energy Commission<br>
P.O. Box LG80, Legon, Accra, Ghana<br>
Telephone: +233 20 8717649<br>
Facsimile: +233 21 400807<br>
Email: snas@operamail.com or Aquasie26@yahoo.com<br>""",
    "Greece": """<b>INIS Liaison Officer<br>
</b>Ms. Vasso Tafili<br>
Greek Atomic Energy Commission<br>
P.O. Box 60092, 153 10 Aghia Paraskevi, Attikis, Athens, Greece<br>
Telephone: +30 210 650 6714<br>
Facsimile: +30 210 650 6748<br>
Email: vtafili@eeae.gr<br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Attn: Mr. Potiriades<br>
Greek Atomic Energy Commission""",
    "Guatemala": """<b>INIS Liaison Officer<br>
</b>Mr. Jorge Guillén<br>
Ministerio de Energí a y Minas, Dirección General de Energí a Nuclear<br>
Avenida Petapa 24, Calle 21-12, Apartado Postal 1421, Zona 12, Codigo 01812, Ciudad de Guatemala, Guatemala<br>
Telephone: (502) 4-770746 or 4-770747<br>
Telex: 5516 petgua gu<br>
Facsimile: (502) 4-762007<br>
Email: jorge_mo@hotmail.com<br>
<br>
<b>Document Delivery Service</b><br>
Centro de Informacion Nuclear CIN<br>
Mailing address: Dirección General de Energí a, 24 Calle 21-12 zona 12, Guatemala. Apdo Postal 1421""",
    "Haiti": """<b>INIS Liaison Officer</b>
<p>Michel Alain Louis<br>
Director, Laboratoire de Tamarinier<br>
2 Rue la Retraite Lilavois 35, Bon Repos, Haiti<br>
Telephone: +509 3681 8472/3994-8472<br>
Email: michelalainlouis@yahoo.com<br>
</p>""",
    "Hungary": """<b>INIS Liaison Officer<br>
</b>Mr. Sandor Zsiga<br>
Budapest University of Technology and Economics<br>
National Technical Information Center and Library (BME-OMIKK)<br>
Budafoki ùt 4-6. "K" building 2/84, H-1111 Budapest, Hungary<br>
Telephone: (361) 463 3542<br>
Email: szsiga@omikk.bme.hu<br>
<br>
<b>Document Delivery Service</b><br>
BME OMIKK<br>
Mailing address: BME OMIKK, Budafoki ùt 4-6. "K" building 2/84, H-1111 Budapest, Hungary<br>
Point of contact: Sandor Zsiga<br>
Telephone: +(361) 463 3542<br>
Email: zsiga@info.omikk.bme.hu""",
    "India": """<b>INIS Liaison Officer</b><br>
Dr. G. Ravi Kumar<br>
Head, Scientific Information Resource Division<br>
Bhabha Atomic Research Centre (BARC)<br>
Trombay, Mumbai 400 085, India<br>
Telephone:+91 22 25593685 or 25592073<br>
Facsimile: +91 22 2550 5151<br>
Email: headsird@barc.gov.in or gurazada@barc.gov.in<br>
<br>
<b>Document Delivery Service</b><br>
National Document Delivery Service (India)<br>
Mailing address: Bhabha Atomic Research Centre, Trombay, Mumbai - 400 085, India<br>
Point of contact: Mr. K. Bhanumurthy, Head, Scientific Information Resource Division<br>
Telephone: +91 22 25593685 or 25592073<br>
Fax: +91 22 25505151<br>
Email: headsird@barc.gov.in or aditya@barc.gov.in<br>
URL: <a href="http://www.barc.gov.in">http://www.barc.gov.in</a>; webmaster@barc.gov.in""",
    "Indonesia": """<b>INIS Liaison Officer</b><br>
Mr. Heru Umbar<b>a<br>
</b>Head, Centre for Informatics and Nuclear Strategic Zone Utilization<br>
National Nuclear Energy Agency (BATAN)<br>
Puspitek, Serpong-Tangerang, Gedung 71, 15310 Jakarta, Indonesia<br>
Telephone: +62 21 7560567/75, +62 21 7560924/25<br>
Facsimile: +62 21 7560895<br>
Email: umbara@batan.go.id<br>
URL: <a href="http://www.batan.go.id">http://www.batan.go.id<br>
</a><b><br>
Alternate</b> <b>INIS Liaison Officer</b><br>
Mr. Budi Prasetyo<br>
National Nuclear Energy Agency (BATAN)<br>
Puspitek, Serpong-Tangerang, Gedung 71, 15310 Jakarta, Indonesia<br>
Telephone: +62 21 7560567/75, +62 21 7560924/25<br>
Facsimile: +62 21 7560895<br>
Email: <a href="mailto:budipras@batan.go.id">budipras@batan.go.id<br>
</a>URL: <a href="http://www.batan.go.id">http://www.batan.go.id</a><b><br>
</b><br>
<b>Document Delivery Service</b><br>
National Atomic Energy Agency - Indonesia<br>
Mailing address: Informatics Development Centre, Puspiptek Area Serpong-Tangerang, P.O. Box 4274, Jakarta 12042, Indonesia<br>
Point of contact: INIS Liaison Officer for Indonesia, Mr. K. Heryudo<br>
Telephone: +62 21 7560905<br>
Fax: +62 21 7560923<br>
Email: Kasihw@Batan.go.id""",
    "International Atomic Energy Agency (IAEA)": """<b>INIS Liaison Officer<br>
</b>Mr. Dobrica Savic<br>
Head,Nuclear Information Section, Department of Nuclear Energy<br>
International Atomic Energy Agency (IAEA)<br>
Vienna International Centre, P.O. Box 100, A-1400 Vienna, Austria<br>
Telephone: +43 1 2600 ext. 25107<br>
Facsimile: +43 1 26007<br>
Email: d.savic@iaea.org<br>
Twitter: <a href="https://twitter.com/INISsecretariat">@INISsecretariat</a><br>
URL: <a href="http://www.iaea.org">http://www.iaea.org</a><br>
<a href="http://www.iaea.org/inisnkm">http://www.iaea.org/inis</a>""",
    "International Centre for Scientific and Technical Information (ICSTI)": """<b>INIS Liaison Officer</b><br>
Ms. Marina Y. Tumanova<br>
Head, Department of Co-ordination and Planning<br>
International Centre for Scientific and Technical Information (ICSTI)<br>
21-B, Kuusinen St., 125252 Moscow, Russian Federation<br>
Telephone: +7 499 198 7441<br>
Facsimile: +7 499 943 0089 or 943 1511<br>
Email: marina@icsti.su<br>
URL: <a href="http://www.icsti.su/portal/index.html">http://www.icsti.su/portal/index.html</a><br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Mr. Alexei I. Lovtzov<br>
Head, Department of Information Analysis and Network Technologies<br>
International Centre for Scientific and Technical Information (ICSTI)<br>
21-B, Kuusinen St., 125252 Moscow, Russian Federation<br>
Telephone: +7 499 198 7421<br>
Facsimile: +7 499 943 0089 or 943 1511<br>
Email: alov@icsti.su""",
    "International Commission on Radiological Protection (ICRP)": """<b>INIS Liaison Officer</b><br>
International Commission on Radiological Protection (ICRP)<br>
Health Protection Agency CRCE<br>
Chilton, Oxon OX11 0RQ, United Kingdom<br>
Telephone: +44 1235 822649<br>
Facsimile: +44 1235 833891""",
    "International Institute for Applied Systems Analysis (IIASA)": """<b>INIS Liaison Officer<br>
</b>International Institute for Applied Systems Analysis (IIASA)<br>
A-2361 Laxenburg, Austria<br>
Telephone: +43 2236 807384<br>
Facsimile: +43 2236 71 313 or 804 412<br>
URL: <a href="http://www.iiasa.ac.at/">http://www.iiasa.ac.at/</a>""",
    "International Organization for Standardization (ISO)": """<b>INIS Liaison Officer<br>
</b>Mr. Nicolas Fleury<br>
Director, Marketing, Communication &amp; Information<br>
Central Secretariat<br>
International Organization for Standardization (ISO)<br>
1, ch. de la Voie-Creuse, P.O. Box 56, CH-1211 Geneva 20, Switzerland<br>
Telephone: +41 22 749 0316<br>
Facsimile: + 41 22 749 3430<br>
Email: fleury@iso.org<br>
URL: <a href="http://www.iso.org/">http://www.iso.org/</a>""",
    "Iran": """<b>INIS Liaison Officer</b><br>
Ms. Faranak Zomorodpoush<br>
Atomic Energy Organization of Iran<br>
P.O. Box 13145-1349, Tehran, Islamic Republic of Iran<br>
Telephone: +98 21 820 62348<br>
Facsimile: +98 21 882 21246<br>
Email: fzomorod@aeoi.org.ir<br>
URL: <a href="http://www.aeoi.org.ir">http://www.aeoi.org.ir</a><br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Ms. Laleh Torabi<br>
Atomic Energy Organization of Iran<br>
P.O. Box 13145-1349, Tehran, Islamic Republic of Iran<br>
Telephone: +98 21 820 62348<br>
Facsimile: ++98 21 882 21246<br>
Email: ltorabi@aeoi.org.ir<br>
<br>
<b>Document Delivery Service</b><br>
IRAN document delivery within the national boundaries<br>
Mailing address: Atomic Energy Organization of Iran (AEOI), Research Support Center (RSC),
 End of North Kargar Ave, P O Box 13145-1349, Tehran - IRAN<br>
Point of contact: Ms. Faranak Zomorodpoush Head, AEOI-RSC<br>
Telephone: +98 21 820 62348<br>
Fax: +98 21 882 21246<br>
Email: <a href="mailto:fzomorod@aeoi.org.ir">fzomorod@aeoi.org.ir</a><br>
URL: <a href="http://www.aeoi.org.ir">http://www.aeoi.org.ir</a>""",
    "Iraq": """<b>INIS Liaison Officer<br>
</b>Mr. Saad M. Abdul Razak<br>
Atomic Energy Affairs Directorate<br>
Ministry of Science and Technology<br>
P.O. Box 2026<br>
Baghdad - AL-Jadryia, Iraq<br>
Telephone: +964-17762276<br>
Email: ILO_IQsm@most.gov.iq &nbsp;<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Mr. R.A. Al-Shaheed<br>
Iraqi Atomic Energy Commission<br>
Dar Iben Hayan for Information<br>
<br>
<b>Document Delivery Service</b><br>
Atomic Energy Affairs Directorate<br>
Mailing address: P.O. Box 2026, Baghdad - AL-Jadryia, IRAQ<br>
Point of contact: Mr. Saad M. Abdul Razak, INIS Liaison Officer<br>
Telephone: +964-17762276<br>
Email: NLO_Iraq@most.gov.iq or smmu1958@yahoo.com<br>""",
    "Ireland": """<b>INIS Liaison Officer<br>
</b>Ms. Isabella Bolger<br>
Radiological Protection Institute of Ireland<br>
3 Clonskeagh Square, Clonskeagh Road, Dublin 14, Ireland<br>
Telephone: +353 1 2697766<br>
Facsimile: +353 1 269 7437<br>
Email: bbolger@rpii.ie<br>
<br>
<b>Document Delivery Service</b><br>
Radiological Protection Institute of Ireland<br>
Mailing address: 3 Clonskeagh Square, Clonskeagh Road, Dublin 14, IRELAND<br>
Point of contact: Ms Isabella Bolger, INIS Liaison Officer<br>
Telephone: +353 1 269 77 66<br>
Fax: +353 1 283 06 38<br>
Email: bbolger@rpii.ie<br>
URL: <a href="http://www.rpii.ie">http://www.rpii.ie</a><br>""",
    "Israel": """<b>INIS Liaison Officer<br>
</b>Mr. Tomer Keidar<br>
Nuclear Research Centre Negev<br>
Israel Atomic Energy Commission<br>
P.O. Box 9001, Beer-Sheva 84190, Israel<br>
Telephone: +972 8 656 7429<br>
Facsimile: +972 8 656 8106 or +972 8 655 4848<br>
Email: tomerk@nrcn.org.il<br>
URL: http://www.iaec.gov.il<br>
<br>
<b>Alternate Liaison Officer<br>
</b>Ms. Mina Baskin<br>
Nuclear Research Centre Negev<br>
Israel Atomic Energy Commission<br>
P.O. Box 9001, Beer-Sheva 84190, Israel<br>
Telephone: 972-8-656-7489<br>
Email: minab@nrcn.org.il<br>
<br>
<b>Document Delivery Service</b><br>
NRCN Library - Israel<br>
Mailing address: NRCN, P.O. Box 9007, Beer-Sheva 84/90, Israel<br>
Point of contact: Alex Yosef, librarian<br>
Telephone: 972-8-6568298<br>
Fax: 972-8-6569007<br>
Email: lib@nrcn.org.il<br>
URL: <a href="http://www.iaec.gov.il">http://www.iaec.gov.il</a>""",
    "Italy": """<b>INIS Liaison Officer<br>
</b>Ms. Monica Sala<br>
ENEA - C.R. Casaccia<br>
Biblioteca Centrale s.p. 035<br>
Via Anguillarese 301, S. Maria di Galeria, 00060 Roma, Italy<br>
Telephone: +390 6 30486560<br>
Facsimile: +390 6 30484267<br>
Email: sala_m@casaccia.enea.it<br>
URL: <a href="http://www.enea.it">http://www.enea.it</a><br>
<br>
<b>Document Delivery Service</b><br>
NCL full text document delivery service - Italy<br>
Mailing address: ENEA - CR Casaccia, Via Anguillarese 301, 00060 - S. Maria di Galeria, ROMA, Italy<br>
Point of contact: Mr Giulio Marconi<br>
Telephone: +39-06-30483743<br>
Fax: +39-06-30484267<br>
Email: biblioteca@casaccia.enea.it<br>
URL: <a href="http://www.enea.it">http://www.enea.it</a>""",
    "Japan": """<b>INIS Liaison Officer<br>
</b>Mr. Minoru Yonezawa<br>
INIS and Nuclear Information Management Section<br>
General Manager<br>
Intellectual Resources Department<br>
Japan Atomic Energy Agency (JAEA)<br>
2-4 Shirakata-Shirane, Tokai-mura, Naka-gun, Ibaraki, 319-1195, Japan<br>
Telephone:+81 29 282 5376<br>
Facsimile: +81 29 282 6718<br>
Email: inismail@jaea.go.jp<br>
URL: <a href="http://www.jaea.go.jp/english/index.shtml">http://www.jaea.go.jp/english/index.shtml</a><br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Mr. Yukinobu Mineo<br>
Deputy General Manager<br>
INIS and Nuclear Information Management Section<br>
Intellectual Resources Department<br>
Japan Atomic Energy Agency (JAEA)<br>
2-4 Shirakata-Shirane, Tokai-mura, Naka-gun, Ibaraki, 319-1195, Japan<br>
Telephone:+81 29 282 5376<br>
Facsimile: +81 29 282 6718<br>
Email: inismail@jaea.go.jp<br>
<br>
<b>Document Delivery Service</b><br>
NDL Document Delivery Service - Japan<br>
Mailing address: ILL-Section, Kansai-kan of the National Diet Library(NDL) Japan, 8-1-3 Seikadai, Seika-cho, Soraku-gun, Kyoto Pref., 619-0287, JAPAN<br>
Fax: +81 774 94 9112<br>
URL: <a href="http://www.ndl.go.jp/en/index.html">http://www.ndl.go.jp/en/index.html</a><br>
<br>
<p>JST Document Delivery Service - Japan<br>
Mailing address: Japan Science and Technology Agency(JST), Library, 10 Hikarigaoka, Tokyo 179-8910, JAPAN<br>
Fax: +81 3 3979 2210<br>
URL: <a href="http://sciencelinks.jp/j-east/">http://sciencelinks.jp/j-east/</a></p>

<br>
<br>
<p>IPDL Document Delivery Service - Japan<br>
Mailing address: Industrial Property Digital Library (IPDL), Tokkyocho Chosha 2F., 3-4-3 Kasumigaseki Chiyoda-ku, Tokyo 100-0013, JAPAN<br>
Telephone: +81 3 5690 3500<br>
Fax: +81 3 5690 3536<br>
Email: helpdesk@ipdl.inpit.go.jp<br>
URL: <a href="http://www.ipdl.inpit.go.jp/homepg_e.ipdl">http://www.ipdl.inpit.go.jp/homepg_e.ipdl</a><br>
</p>""",
    "Joint Institute for Nuclear Research (JINR)": """<b>INIS Liaison Officer<br>
</b>Mr. Boris M. Starchenko<br>
Joint Institute for Nuclear Research (JINR)<br>
ul. Joliot-Curie, 6, Dubna, Moscowskaya Oblast, 141980 Russian Federation<br>
Telephone: +7 49621 65057 or +7 49621 65311<br>
Telex: 911621 Dubna SU<br>
Facsimile: +7 49621 65916 or +7 49621 65891<br>
Email: inis@jinr.ru<br>
URL: <a href="http://www.jinr.ru/">http://www.jinr.ru/</a><br>
Document delivery services: electronic via http<br>
Request services: e-mail, World Wide Web<br>
Cost: free of charge for the JINR staff""",
    "Jordan": """<b>INIS Liaison Officer<br>
</b>Ms. Wafa'a Khliefat<br>
Head, Programming and System Development Section<br>
Jordan Atomic Energy Commission<br>
P.O. Box 70, Amman 11934, Jordan<br>
Facsimile: +962 6 5200471<br>
Telephone: +962 6 5200460<br>
Email: wafaa.khliefat@jaec.gov.jo<br>
URL: <a href="http://www.jo-aec.org">http://www.jo-aec.org</a><br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Ms. Randa Al-Qudah<br>
Jordan Atomic Energy Commission<br>
P.O. Box 70<br>
Amman 11934<br>
Jordan<br>
Facsimile: +962 6 5230900<br>
Telephone: +962 6 5230978<br>
Email: jaec1@go.com.jo or jaec2@go.com.jo<br>
<br>
<br>
<b>Document Delivery Service</b><br>
Jordan Atomic Energy Commission - Jordan<br>
Mailing address: Jordan Atomic Energy Commission, P. O. Box 70, Amman 11934, Jordan<br>
Point of contact: INIS Liaison Officer<br>
Telephone: +962 6 5230978<br>
Fax: +962 6 5230900<br>
Email: jaecl@go.com.jo""",
    "Kazakhstan": """<b>INIS Liaison Officer<br>
</b>Ms. Irina Doktorovich<br>
Chief Specialist<br>
Institute of Radiation Safety and Ecology of the Kazakhstan National Nuclear Centre<br>
Krasnoarmeiskaya, 2, 071 100 Kurchatov, Republic of Kazakhstan<br>
Telephone: +7 72251 23413<br>
Facsimile: +7 72251 22806<br>
Email: irbe@nnc.kz<br>
<br>
<b>Document Delivery Service</b><br>
Committee of Atomic Energy of the Republic of Kazakhstan<br>
Mailing address: Committee of Atomic Energy of the Republic of Kazakhstan, 4 L. Chaikina Str., Almaty, 480020, Republic of Kazakhstan<br>
Point of contact: Namazkulova Karlygash, Scientific Collaborator<br>
Telephone: +7-3272-534345<br>
Fax: +7-3272-607220<br>
Email: adm@atom.almaty.kz; inis@atom.almaty.kz""",
    "Kenya": """<b>INIS Liaison Officer<br>
</b>Mr. Komen Chepkonga<br>
National Commission for Science, Technology and Innovation<br>
P.O. Box 30623-00100, Nairobi, Kenya<br>
Telephone: +254 20 2219420<br>
Mobile: &nbsp;+254 770 433366<br>
Email: kchepkonga@nacosti.go.ke<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Librarian, NCST<br>""",
    "Korea": """<b>INIS Liaison Officer<br>
</b>Mr. Byong-Hyon Bak<br>
Deputy Director<br>
Nuclear Policy Division, Atomic Energy Bureau<br>
Ministry of Education, Science and Technology (MEST), Central Government Complex, 55 Sjong-no, Jongno-gu, 110-760 Seoul, Republic of Korea<br>
Telephone: +82 2 2100 6964<br>
Facsimile: +82 2 2100 6965<br>
Email: stbbh@mest.go.kr<br>
URL:<a href="http://www.mest.go.kr">http://www.mest.go.kr</a><br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Mr. Ji-Ho Yi<br>
Head, Technical Information Department<br>
Korea Atomic Energy Research Institute (KAERI)<br>
150 Dukjin-dong, Yeuseung-gu, Daejeon 305-353, Republic of Korea<br>
Telephone: +82 (42) 8682195<br>
Facsimile: +82 (42) 8619561<br>
Email: jhlee4@kaeri.re.kr<br>
URL:<a href="http://www.kaeri.re.kr">http://www.kaeri.re.kr</a>""",
    "Kuwait": """<b>INIS Liaison Officer<br>
</b>Mr. Ahmad Khalid Al-Jassar<br>
Chief Engineer, Power Stations Projects<br>
Ministry of Electricity and Water, P.O. Box 12, Safat, 13001 Safat, Kuwait<br>
Telephone: +965 5371720<br>
Facsimile: +965 5371721<br>
Email: ajassar@mew.gov.kw""",
    "Kyrgyz Republic": """<b>INIS Liaison Officer</b><br>
Mr. Kubanychbek Noruzbaev<br>
Department of Ecology and Nature Management<br>
Ministry of Ecology and Emergencies, 142 Gorkogo Str., 720005 Bishkek, Kyrgyzstan<br>
Telephone: +996 312 54 9152<br>
Facsimile: +996 312 54 9152<br>
Email: demos@intranet.kg<br>
<br>
<b>Document Delivery Service</b><br>
Ministry of Ecology and Emergencies<br>
Mailing address: 142 Gorkogo Str., 720005, Bishkek, Kyrgyzstan<br>
Point of contact: Dept. of Ecology and Nature Management, Mr. Kubanychbek Noruzbaev<br>
Telephone: +996 312 54 9152<br>
Fax: +996 312 54 9152<br>
Email: demos@intranet.kg""",
    "Latvia": """<b>INIS Liaison Officer<br>
</b>State Environmental Service<br>
Radiation Safety Centre<br>
Rupniecibas Street 23, Riga, LV-1045, Latvia<br>
Telephone: +371 67084207<br>
Facsimile: +371 67084299<br>
Email: <a href="mailto:pasts@rdc.vvd.gov.lv">pasts@rdc.vvd.gov.lv</a><br>
URL: <a href="http://www.rdc.gov.lv">www.rdc.vvd.gov.lv</a>""",
    "Lebanon": """<b>INIS Liaison Officer<br>
</b>Ms. Mona Shbaro<br>
Lebanese Atomic Energy Commission<br>
National Council for Scientific Research<br>
P.O. Box 11-8281, 2260 Beirut, Lebanon<br>
Telephone: +961 1 45 0811<br>
Facsimile: +961 1 45 0810<br>
Email: dirlaec@cnrs.edu.lb<br>
<br>
<br>
<b>Document Delivery Service</b><br>
Centre de Documentation et d'Information Scientifique - Lebanon<br>
Mailing address: P.O. Box 11-8281, Inu Fakhri Dagher, Cite Sportive, Beirut, LEBANON<br>
Telephone: +961 1 840260/1/2/3/4<br>
Fax: +961 822639<br>
Email: ahabib@cnrs.edu.lb, usearch@cnrs.edu.lb<br>
URL: <a href="http://www.cnrs.edu.lb">http://www.cnrs.edu.lb</a><br>""",
    "Libya": """<b>INIS Liaison Officer<br>
</b>Ms. Moufida Ali Sunni<br>
Head Unit of the Library, Tajoura Nuclear Research Centre<br>
P.O. Box 30878, Tajoura, Libya<br>
Telephone: +218 21 361 4135<br>
Mobile: +218 925 430 182<br>
Facsimile: +218 21-4871474<br>
Email: moufida81@hotmail.com or moufida@yahoo.com<br>""",
    "Lithuania": """<b>INIS Liaison Officer<br>
</b>Mr. Gediminas Karalius<br>
Strategic Project Division<br>
Ministry of Energy<br>
Gedimino avenue 38/Vasario 16-osios st. 2, LT-01104 Vilnius, Lithuania<br>
Telephone: +370 5 261 2782<br>
Email: g.karalius@enmin.lt<br>
<br>
<b>Document Delivery Service</b><br>
National Library of Lithuania - Lithuania<br>
Mailing address: National Library of Lithuania, Gedimino pr. 51, 2600 Vilnius, Lithuania<br>
Point of contact: Ausra Vaskeviciene, Head, Department of Electronic Information<br>
Telephone: +370 2 612 687<br>
Email: auvask@rc.lrs.lt, biblio@lnb.lrs.lt<br>
Telephone: +370 2 629 023<br>
Fax: +370 2 627 129<br>
URL: <a href="http://www.lnb.lrs.lt">http://www.lnb.lrs.lt</a>""",
    "Luxembourg": """<b>INIS Liaison Officer<br>
</b>Mr. Patrick Majerus<br>
Radioprotection Division, Ministry of Health<br>
Allée Marconi, Villa Louvigny, L-2120 Luxembourg, Luxembourg<br>
Telephone: +352 478 5670<br>
Facsimile: +352 46 7521<br>
Email: patrick.majerus@ms.etat.lu<br>
URL:<a href="http://www.ms.etat.lu/">http://www.ms.etat.lu/</a><br>
<br>""",
    "Madagascar": """<b>&nbsp;INIS Liaison Officer</b><br>
Prof Raoelina Andriambololona<br>
Director General<br>
Madagascar Institut National des Sciences et Techniques Nucléaires (INSTN)<br>
Madagascar INSTN<br>
B.P. 4279, Antananarivo 101, Madagascar<br>
Telephone: +261 20 22 355 84 or +261 20 24 714 03<br>
Facsimile: +261 20 22 355 83<br>
Email: raoelinasp@yahoo.fr or instn@moov.mg or jacquelineraoelina@hotmail.com<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Mr Tokiniaina Ravo Raymond Ranaivoson<br>
Madagascar Institut National des Sciences et Techniques Nucléaires (INSTN)<br>
Madagascar INSTN<br>
B.P. 4279, Antananarivo 101, Madagascar<br>
Telephone: +261 20 22 355 84 or +261 20 24 714 03<br>
Facsimile: +261 20 22 355 83<br>
Email: instn@moov.mg or tokhiniaina@gmail.com<br>""",
    "Malaysia": """<b>INIS Liaison Officer<br>
</b>Mr. Iberahim Ali<br>
Director, Information Management Division<br>
Malaysian Nuclear Agency, Ministry of Science, Technology and Innovation<br>
Bangi, 43000 Kajang, Selangor D.E., Malaysia<br>
Telephone: +603 8928 2918<br>
Email: iberahim@nuclearmalaysia.gov.my<br>
URL: <a href="http://www.nuclearmalaysia.gov.my/">http://www.nuclearmalaysia.gov.my/</a><br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Ms. Habibah Adnan<br>
Information Management Division<br>
Malaysian Nuclear Agency, Ministry of Science, Technology and Innovation<br>
Bangi, 43000 Kajang, Selangor D.E., Malaysia<br>
Telephone: +603-8 9 250 510<br>
Email: habibah@nuclearmalaysia.gov.my<br>
<br>
<br>
<b>Document Delivery Service</b><br>
Information Management Division, MINT - Malaysia<br>
Mailing address: Malaysian Nuclear Agency (Nuclear Malaysia), Bangi, 43000 Kajang, Selangor D.E., Malaysia<br>
Point of contact: INIS Liaison Officer for Malaysia<br>
Telephone: +603-8 9 250 510<br>
Fax: +603-8 9 112 154<br>
Email: sam@nuclearmalaysia.gov.my<br>
URL: <a href="http://www.mint.gov.my">http://www.mint.gov.my</a>""",
    "Mali": """<b>INIS Liaison Officer<br>
</b>Mr. Adama Yoro Sidibe<br>
Direction nationale de l'énergie<br>
Bâtiment A1, Complexe de l'ex-CRES, Plateau de Badalabougou, B.P. 1872, Bamako, Mali<br>
Telephone: +223 222 4538<br>
Facsimile: +223 223 7396<br>
Email: dnenergy@mmee.gov.ml""",
    "Mauritania": """<b>INIS Liaison Officer<br>
</b>Mr. Assane Gaye<br>
Centre National des Ressources en Eau au Ministere de l'Hydraulique et de l'Assainissement<br>
B.P. 170, Nouakchott, Mauritania<br>
Facsimile: +22 252 43 923<br>""",
    "Mauritius": """<b>INIS Liaison Officer<br>
</b>Mr. Rajcoomar Bikoo<br>
Head, Technical Unit, Ministry of Public Utilities<br>
Level 10, Air Mauritius Building, President John Kennedy Street, Port Louis, Mauritius<br>
Telephone: + 230 210 0896<br>
Facsimile: + 230 208 6497 or 210 7408 or 208 7893&nbsp;<br>
Email: rbikoo@mail.gov.mu<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Mr. Radhamohun Mungur<br>
Ag Principal Planner, Ministry of Public Utilities<br>
Level 10, Air Mauritius Building, President John Kennedy Street, Port Louis, Mauritius<br>
Telephone: +230 210 3164 or 210 1697<br>
Facsimile: + 230 208 6497<br>
Email: ramungur@mail.gov.mu<br>""",
    "Mexico": """<b>INIS Liaison Officer<br>
</b>Mr. Javier M. Ortega Escalona<br>
Chief, Information and Documentation Center(CIDN)<br>
National Institute of Nuclear Research (ININ)<br>
Carretera Mexico - Toluca s/n, La Marquesa, Ocoyoacac, Mexico C.P. 52750, Mexico<br>
Telephone: +52 55 53297221<br>
Facsimile: +52 55 53297299<br>
Email: javier.ortega@inin.gob.mx<br>
URL: <a href="http://www.inin.gob.mx">http://www.inin.gob.mx</a><br>
<br>
<b>Document Delivery Service</b><br>
Centro de Informacion y Documentacion Nuclear - Mexico<br>
Mailing address: Instituto Nacional de Investigaciones Nucleares (ININ),
 Apdo. Postal 18-1027, México, D.F., Mexico Point of contact: Lic. Claudia Martinez-Gasca, Lic. Claudio Fernandez-Ortega<br>
Telephone: +52 55 5329 7221<br>
Fax: +52 55 5329 7299<br>
Email: claudia.martinez@inin.gob.mx, claudio.fernandez@inin.gob.mx<br>
URL: <a href="http://www.inin.gob.mx">http://www.inin.gob.mx</a>""",
    "Middle Eastern Radioisotope Centre for the Arab Countries (MERRCAC)": """<b>INIS Liaison Officer<br>
</b>Mr. Ashraf Taha Mahmoud<br>
Middle Eastern Radioisotope Centre for the Arab Countries (MERRCAC)<br>
Malaeb El-Gamaa St., P.O. Box 12311, Dokki, Cairo, Egypt<br>
Telephone: +20 2 3370588 0106608040<br>
Facsimile: +20 2 3371082<br>
Email: merrcac_ashraf@hotmail.com<br>
URL: <a href="http://www.merrcac.com/">http://www.merrcac.com/</a><br>
Delivery services: mail, fax, papaer, electronic<br>
Request services: phone, mail, fax, email<br>
<br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Mr. Maysa Talaat Abd Elmoteleb<br>
Telephone: +20 2 3370588 0103778369<br>
Facsimile: +20 2 3371082<br>
Email: merrcac@yahoo.com""",
    "Mongolia": """<b>INIS Liaison Officer<br>
</b>Mr. Gendengiin Altan-Och<br>
P.O. Box 46/877<br>
14201 Ulaanbaatar<br>
Mongolia<br>
Telephone: +976-1 327123<br>
Facsimile: +976-1 372918<br>
Email: altanoch@parliament.mn<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Mr. Nambaryn Gansukh<br>
Nuclear Research Centre<br>
Mongolian State University""",
    "Morocco": """<b>INIS Liaison Officer<br>
</b>Mr. Abdeslam El Hamdaoui<br>
Chef du Service au CNESTEN<br>
Centre National de L' Energie des Sciences et des Techniques Nucléaires (CNESTEN)<br>
BP 1382, RP 10001, Rabat, Morocco<br>
Telephone: +2126 68 71 92 48 <br>
Email: elhamdaoui@cnesten.org.ma or hamdaoui15@yahoo.com<br>
URL: <a href="http://www.cnesten.org.ma">http://www.cnesten.org.ma</a><br>
<br>
<b>Document Delivery Service</b><br>
Centre de l'Energie, des Sciences et des Techniques Nucléaires (CNESTEN) - Morocco<br>
Mailing address: CNESTEN, 65, rue Tansift, Agdal, Rabat - Maroc<br>
Point of contact: Ms Fatiha MAZOUR, INIS Liaison Officer for Morocco<br>
Telephone: 212 7 778704/08/12<br>
Fax: 212 7 779978<br>
Email: cnesten@pop.mox.azure.net<br>""",
    "Mozambique": """<b>INIS Liaison Officer<br>
</b>Mr. Alexandre Maria Maphossa<br>
Faculdade de Ciências, Departamento de Fí sica<br>
Universidade Eduardo Mondlane, Maputo, Mozambique<br>
Telephone: +258 82 487 6420<br>
Email: maphossa@zebra.uem.mz<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Mr. Rego João Afonso<br>
Faculdade de Ciências<br>
Departamento de Fí sica<br>
Universidade Eduardo Mondlane<br>
Maputo<br>
Mozambique<br>
Telephone: +258 82 423 4620<br>
Email: afonsorego@uem.mz""",
    "Myanmar": """<b>INIS Liaison Officer<br>
</b>Technical Information Centre<br>
Myanmar Scientific and Technological Research Department<br>
Ministry of Science and Technology, No. 6, Kaba Aye Pagoda Road, Yankin P.O., Yangon, Myanmar<br>
Telephone: +95 1 663071<br>
Facsimile: +95 1 665292""",
    "Namibia": """<b>INIS Liaison Officer<br>
</b>Mr. Joseph Eiman<br>
Ministry of Health and Social Services<br>
National Radiation Protection Services<br>
Main Office Building, Basement Level, Office 1W02, , Harvey Street, Windhoek, Namibia<br>
Telephone: +264 61 203 2758<br>
Facsimile: +264 61 234 083<br>
Email: jeiman@mhss.gov.na<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Mr. Axel Tibinyane<br>
Ministry of Health and Social Services<br>
National Radiation Protection Services<br>
Main Office Building, Basement Level, Office 1W02, , Harvey Street, Windhoek, Namibia<br>
Telephone: +264 61 203 2767<br>
Facsimile: +264 61 234 083<br>
Email: atibinyane@mhss.gov.na<br>""",
    "Netherlands": """<b>INIS Liaison Officer<br>
</b>Mr. J.C. Kuijper<br>
Senior Consultant - Nuclear Reactor Physics<br>
NRG <br>
Iepenlaam 129NL-1741 TD Schagen, The Netherlands<br>
Telephone: +31 224 56 4506<br>
Mobile: +31 6 4022 9728<br>
Facsimile: +31 224 56 8608<br>
Email: jimkuijper@gmail.com<br>
Web: <a href="http://www.nrg.eu/">http://www.nrg.eu/</a> &amp;
 <a href="Web 2: http://www.nucleartechnologie.nl">http://www.nucleartechnologie.nl</a><br>""",
    "New Zealand": """<b>INIS Liaison Officer<br>
</b>Library<br>
Institute of Geological and Nuclear Sciences<br>
P.O. Box 30-368, Lower Hutt, New Zealand<br>
Telephone: (+64-4) 570 4825<br>
Facsimile: (+64-4) 569 9074<br>
Email: p.muir@gns.cri.nz""",
    "Nicaragua": """<b>INIS Liaison Officer<br>
</b>Ms. Andrea Marcela Castillo Arias<br>
Universidad Nacional Autónoma de Nicaragua<br>
UNAN-Managua, Apartado 663, ENEL Central 2000 m al Sur, Nicaragua<br>
Telephone: +505 2522 9014 or +505 8600 8695<br>
Facsimile: (505) 2774943<br>
Email: andrieta_castillo@yahoo.com<br>""",
    "Niger": """<b>INIS Liaison Officer<br>
</b>Mr Harouna Ibrahim<br>
Direction des Applications et de l'Electricité Nucléaire<br>
Chef de la Division Applications Nucléaires<br>
Téléphone Bureau: +227 20736530<br>
Téléphone Portable: +227 96274786 / +227 94320898 / +227 93747724<br>
Facsimile: +227 20732759<br>
B.P.: 11700 Niamey - NIGER<br>
Email: ibrharou2000@yahoo.fr<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Ms Mariama Hamidou<br>
Direction des Applications et de l'Electricité Nucléaire<br>
Chef de la division Sûreté, conventions et Traités Nucléaires<br>
Email: hamida_marie@yahoo.fr""",
    "Nigeria": """Director General<br>
Nigeria Atomic Energy Commission<br>
Attention: Mr. Tamuno Johnnie<br>
9 Kwame Nkrumah Crescent, Asokoro, P.M.B. 646, Garki, Abuja, Nigeria<br>
Telephone: +234 931 46512<br>
Facsimile: +234 931 46515<br>
Email: inis@nigatom.org or dgnaec@nigatom.org or tamuno.johnnie@nigatom.org.ng<br>
<br>
<b>Document Delivery Service</b><br>
National Nuclear Information Service<br>
Mailing address: National Nuclear Information Service, Nigeria Atomic Energy Commission No. 9,
 Kwame Nkrumah Cresent Asokoro P.M.B., 646 Garki, Abuja<br>
Point of contact: Director General, Nigeria Atomic Energy Commission<br>
Telephone: +234 9 3146513<br>
Fax: +234 9 3146515<br>
Email: inis@nigatom.org or dgnaec@nigatom.org or tamuno.johnnie@nigatom.org.ng<br>""",
    "Norway": """<b>INIS Liaison Officer<br>
</b>Ms. Elin Berge<br>
ETDE Coordinator<br>
Enova, Norwegian Energy Agency<br>
Prof. Brochs gt. 2<br>
7030 Trondheim, Norway<br>
Telephone: +47 73 19 04 3<br>
Mobile: +47 971 97 871<br>
Email: Elin.Berge@enova.no<br>
URL: <a href="http://www.enova.no">http://www.enova.no</a>""",
    "OECD-Nuclear Energy Agency (NEA)": """<b>INIS Liaison Officer<br>
</b>Mr. Juan Manuel Galan<br>
OECD/Nuclear Energy Agency (NEA)<br>
12, boulevard des Iles, F-92130 Issy-les-Moulineaux, France<br>
Telephone: +33 (1) 45 24 1008<br>
Telefax: +33 (1) 45 24 1110<br>
Email: Juan-Manuel.Galan@oecd.org<br>
URL: <a href="http://www.oecd-nea.org">http://www.oecd-nea.org</a>""",
    "Oman": """<b>INIS Liaison Officer<br>
</b>Ms. Faiza Saif Al-Siyabi<br>
Peaceful Nuclear Technology Office<br>
Ministry of Foreign Affairs<br>
P.O. Box 252, PC 113, Muscat, Oman<br>
Telephone: +968 2 460 2726<br>
Facsimile: +968 2 460 3517<br>
Email: pnto.mofa@hotmail.com<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Ms. Amal Talib Al-Alawi<br>
Peaceful Nuclear Technology Office<br>
Ministry of Foreign Affairs<br>
P.O. Box 252, PC 113, Muscat, Oman""",
    "Pakistan": """<b>INIS Liaison Officer<br>
</b>Ms. Jabeen Akhter<br>
Head, Scientific Information Division<br>
Pakistan Institute of Nuclear Science and Technology (PINSTECH)<br>
Nilore, Pakistan<br>
Telephone: +92 51 924 8790<br>
Facsimile: +92 51 924 8808<br>
Email: jabeen@pinstech.org.pk""",
    "Panama": """<b>INIS Liaison Officer<br>
</b>Mr. Octavio Castillo Sánchez<br>
Director del Sistema de la Biblioteca<br>
Estafeta Universitaria, Biblioteca Simón Bolí var, Universidad de Panamá, Panamá, Republic of Panama<br>
Telephone: (+507) 223 87 86<br>
Facsimile: (+507) 223 37 34<br>
Telex: 2661 CAB PUB, Attn: VIP PG<br>
Email: biblis2@up.ac.pa<br>
<br>
<b>Document Delivery Service</b><br>
Instituto Peruano de Energia Nuclear-IPEN - Peru<br>
Mailing address: Av. Canada 1470, Lima 41 - PERU, P.O. Box 1687<br>
Point of contact: Jose Prado Cuba<br>
INIS Liaison Officer - PERU<br>
Telephone: +51-1 2248845, 2248940, 2248950<br>
Fax: +51-1 2248991<br>
Email: aprado@ipensc.gob.pe<br>
URL: <a href="http://rcp.net.pe/IPEN/">http://rcp.net.pe/IPEN/</a>""",
    "Paraguay": """<b>INIS Liaison Officer<br>
</b>Mr. Victor Rodrí guez Gauto<br>
Director del Centro de Información Nuclear, Comisión Nacional de Energí a Atómica<br>
Universidad Nacional de Asunción, Campus Universitario, San Lorenzo, Paraguay<br>
Telephone:+595 21 585 618<br>
Facsimile: +595 21 585 618<br>
Email: varg614@yahoo.com<br>""",
    "Peru": """<b>INIS Liaison Officer<br>
</b>Mr. Antonio Prado-Cuba<br>
Jefe del Centro de Información y Documentación<br>
Instituto Peruano de Energí a Nuclear (IPEN), Av. Canada No. 1470, Apartado 1687, Lima, Peru<br>
Telephone: +51-1 4885040,&nbsp;4885050<br>
Facsimile: +51-1 4885224<br>
Email:aprado@ipen.gob.pe<br>
URL: <a href="http://www.ipen.gob.pe">http://www.ipen.gob.pe</a><br>
<a href="http://www.rcp.net.pe/IPEN/">Peruvian Institute of Nuclear Energy-IPEN</a>""",
    "Philippines": """<b>INIS Liaison Officer<br>
</b>Ms. Isabel M. Amiscaray<br>
Scientific Library and Documentation Centre<br>
Philippine Nuclear Research Institute<br>
Commonwealth Avenue, P.O. Box 213 U.P., Diliman, Quezon City, Philippines<br>
Telephone: +632 9296011-19<br>
Facsimile: 632 9201646<br>
Email:imamiscaray@yahoo.com<br>
URL: <a href="http://www.pnri.dost.gov.ph/">http://www.pnri.dost.gov.ph/</a><br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Ms. Elnora L. Conti<br>
<br>
<b>Document Delivery Service</b><br>
Philippine Nuclear Research Institute<br>
Mailing address: Commonwealth Avenue, Diliman, P.O. Box 213 U.P., 1314 Central, Quezon City,
 PHILIPPINES 1101 Point of contact: INIS Liaison Officer for the Philippines<br>
Telephone: (632) 9296011 to 19<br>
Fax: (632) 9201646<br>
Email: imamiscaray@yahoo.com<br>""",
    "Poland": """<b>INIS Liaison Officer<br>
</b>Mr. Adam Turowiecki<br>
National Atomic Energy Agency<br>
Department of Training and Public Information - INIS Section<br>
ul. Krucza 36<br>
00-522 Warsaw<br>
Poland<br>
Facsimile: +48 22 695 9815<br>
Email: <a href="mailto:atr@zfja-gate.fuw.edu.pl">atr@zfja-gate.fuw.edu.pl</a><br>
<br>
<b>Document Delivery Service</b><br>
Institute of Nuclear Chemistry and Technology - Poland<br>
Mailing address: Dorodna 16, 03-195 Warsaw, Poland<br>
Point of contact: Bozena Bursa<br>
Telephone: (+48-22) 811-25-78<br>
Fax: (+48-22) 811-15-32<br>
Email: bbursa@orange.ichtj.waw.pl<br>
URL: <a href="http://www.ichtj.waw.pl">http://www.ichtj.waw.pl</a><br>
<br>
<p>Institute of Nuclear Physics - Poland<br>
Mailing address: Radzikowskiego 152, 31-342 Cracow, Poland<br>
Point of contact: Barbara Komendera-Swiatek<br>
Telephone: (+48-12) 637-02-22 ext. 328<br>
Fax: (+48-12) 637-54-41<br>
Email: dyrektor@ifj.edu.pl<br>
URL: <a href="http://www.ifj.edu.pl">http://www.ifj.edu.pl</a></p>

<br>
<br>
<p>Institute of Atomic Energy - Poland<br>
Mailing address: 05-400 Otwock-Swierk, Poland<br>
Point of contact: Klemens Kruszewski<br>
Telephone: (+48-22) 779-82-55, 779-95-20<br>
Fax: (+48-22) 779-38-88<br>
Email: jjmilcz@cx1.cyf.gov.pl<br>
URL: <a href="http://www.IAE.cyf.gov.pl">http://www.IAE.cyf.gov.pl</a></p>

<br>
<br>
<p>Soltan Institute for Nuclear Studies - Poland<br>
Mailing address: 05-400 Otwock-Swierk, Poland<br>
Point of contact: Anna Nowik<br>
Telephone: (+48-22) 779-96-05<br>
Fax: (+48-22) 779-34-81<br>
Email: sins@ipj.gov.pl<br>
URL: <a href="http://www.ipj.gov.pl">http://www.ipj.gov.pl</a></p>""",
    "Portugal": """<b>INIS Liaison Officer<br>
</b>Mr. José Gonçalves Marques<br>
Instituto Tecnológico e Nuclear<br>
Estrada Nacional No. 10, P-2685 Sacavem, Portugal<br>
Telephone: +351-21-9550021<br>
Facsimile: +351-21-9941039<br>
Email: jmarques@itn.mces.pt<br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Mr. Antonio Ramalho<br>""",
    "Provisional Technical Secretariat of the Preparatory Commission for the Comprehensive Nuclear-Test-Ban Treaty Organization (CTBTO)": """<b>INIS
     Liaison Officer<br>
</b>Annika Thunborg<br>
Preparatory Commission for the Comprehensive <br>
Nuclear-Test-Ban Treaty Organization (CTBTO)<br>
Vienna International Center, PO Box 1200<br>
1400, Vienna, Austria<br>
T +43 (1) 260 30 6375<br>
M +43 (699) 1459 6375<br>
Email: <a href="mailto:Annika.thunborg@ctbto.org">Annika.thunborg@ctbto.org<br>
</a><a href="http://www.ctbto.org">www.ctbto.org<span style=" font-family: 'Times New Roman';"><br>
</span></a><b><br>
Alternate <b>INIS Liaison Officer<br>
</b></b>Thomas Mützelburg<br>
Preparatory Commission for the Comprehensive <br>
Nuclear-Test-Ban Treaty Organization (CTBTO)<br>
Vienna International Center, PO Box 1200<br>
1400, Vienna, Austria<br>
T +43 (1) 260 30 6421<br>
M +43 (699) 1459 6421<br>
Email: <a href="mailto:thomas.muetzelburg@ctbto.org">thomas.muetzelburg@ctbto.org<br>
</a><a href="http://www.ctbto.org">www.ctbto.org</a>""",
    "Qatar": """<b>INIS Liaison Officer</b><br>
Ms. Sophia Abdulgader Al-Haj<b><br>
</b>Ministry of Environment<br>
P.O. Box 7634, Doha, Qatar<br>
Telephone: +974 4420 1236<br>
Facsimile: +974 4420 7000<br>
Email: sahaj@moe.gov.qa<br>
URL: <a href="http://www.qatarenv.org/">http://www.qatarenv.org/</a><br>
<br>
<b>Document Delivery Service</b><br>
Supreme Council for the Environment and Natural Reserves (SCENR)<br>
Mailing address: PO Box 7634, City Center Street, Doha, Qatar<br>
Point of contact: INIS Liaison Officer of Qatar<br>
Telephone: +974 420 7930<br>
Fax: +974 420 7000<br>
Email: rarkuwari@moe.gov.qa ot amibrahem@moe.gov.qa<br>
URL: <a href="http://www.qatarenv.org">http://www.qatarenv.org</a>""",
    "Republic of Moldova": """<b>INIS Liaison Officer<br>
</b>Ms. Janna Nikolaeva<br>
Central Scientific Library, Academy of Sciences of Moldova<br>
5, Academiei str., MD-2028 Chisinau, Republic of Moldova<br>
Telephone: +373 22 73 8010<br>
Facsimile: +373 22 27 8425<br>
Email: jeanne68@mail.ru<br>""",
    "Romania": """<b>INIS Liaison Officer<br>
</b>Institute of Atomic Physics<br>
P.O. Box MG-3, 407 Atomistilor Street<br>
RO-077125 Magurele, Ilfov, Romania<br>
Telephone: +4021 4574493<br>
Facsimile: +4021 4574456<br>
Email: a.fazacas@ifa-mg.ro<br>
URL: <a href="http://www.nipne.ro/">http://www.nipne.ro</a><br>
<a href="http://www.nipne.ro/inis/inisb.html">NIPNE - INIS<br>
<br>
</a><b>Alternate INIS Liaison Officer<br>
</b>Ms Elena Daniela Gugiu<br>
Institute of Nuclear Research Pitesti<br>
Reactor Physics Safety and Nuclear Fuel Performances Division<br>
Campului &nbsp;Street No. 1<br>
Pitesti- Mioveni P.O. Box 078<br>
Romania<br>
Telephone: +4021 3400 ext. 624<br>
Mobile: _40746 173 292<br>
Email: daniela.gugiu@nuclear.ro""",
    "Russian Federation": """<b>INIS Liaison Officer<br>
</b>Mr. Viacheslav M. Kupriyanov<br>
National Research Nuclear University (NRNU)- MEPHI<br>
Obninsk Institute for Nuclear Power Engineering<br>
Studgorodok 1, Obninsk, 249040, Russian Federation<br>
Email: info@iate.obninsk.ru<br>
Tel: +7 484 393 6931<br>
Fax: +7 484 397 0822<br>
Email: kvm.enpran@gmail.com; rus.inis@yandex.ru<br>
<b><br>
Alternate INIS Liaison Officer<br>
</b>Mr. Anatoliy Tolstenkov<br>
Moscow Engineering Physics Institute<br>
(State University) Russia MEPhI<br>
115409 Kashirskoe sh., 31<br>
Lab. 405, National INIS Center<br>
115409 Moscow, Russian Federation<br>
Tel: +7 499 463 4280<br>
Fax: +7 848 439 30501<br>
Email: rus.inis@yandex.ru<br>
<br>
<b>Document Delivery Service</b><br>
International Information Division, Atominform - Russian Federation<br>
Mailing address: Dmitrovskoye Shosse 2, P.O. Box 971, Moscow 127434, RUSSIAN FEDERATION<br>
Point of contact: Mr. Oleg G. Mikhnevitch, Head of Division<br>
Telephone: +7495 2283590<br>
Fax: +7495 7779680<br>
Email: mikhnev@ainf.ru""",
    "Saudi Arabia": """<b>INIS Liaison Officer</b><br>
King Abdulaziz City for Science and Technology<br>
P.O. Box 6086, Riyadh - 11442, Kingdom of Saudi Arabia<br>
Telephone: +966 1 4813240 and 4813276<br>
Telex: 401590-KACST SJ<br>
Facsimile: +966 1 4813861<br>
Email: GID@kacst.edu.sa<br>
<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Mr. Iyas Al-Hajiri<br>
Deputy Director General, Information Systems<br>
Telephone: +966 1 488 3555, Ext. 2281<br>
<br>
<b>Document Delivery Service</b><br>
King Abdulaziz City for Science and Technology - Saudi Arabia<br>
Mailing address: PO Box 6086 Riyadh 11442<br>
Point of contact: Hamad A. Al-Saadoon, INIS Liaison Officer for Saudi Arabia<br>
Telephone: +4813240 or +4813276<br>
Fax: +4813861<br>
Telex: 404017 - 4011590 KACST S.J.<br>
Email: GID@kacst.edu.sa""",
    "Senegal": """<b>INIS Liaison Officer<br>
</b>Mr. Mouhamadou Moustapha Sow<br>
Director<br>
Centre National de Documentation Scientifique et Technique (CNDST)<br>
61, Bd El Hadji Djily MBAYE, BP. 36005, Dakar RP, Sénégal<br>
Telephone: +221 33 821 51 63/822 96 19<br>
Email: foyresow@gmail.com or moustapha.sow@cndst.gouv.sn<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Ms. Oulimata Diagne<br>
Centre National de Documentation Scientifique et Technique (CNDST)<br>
61, Bd El Hadji Dfjily MBAYE, BP. 36005, Dakar RP, Sénégal<br>
Telephone: +221 33 821 51 63/822 96 19<br>
Email: oulidiange@yahoo.fr or oulimata.diagne@cndst.sn""",
    "Serbia": """<b>INIS Liaison Officer<br>
</b>Mr. Branislav Djuraševic<br>
Institute of Nuclear Sciences 'VINCA'<br>
P. O. Box 522, 11001 Belgrade, Serbia<br>
Telephone: +381 11 806 6518<br>
Facsimile: +381 11 3440100<br>
Email: bdjuras@vinca.rs<br>
URL: <a href="http://www.vin.bg.ac.yu">http://www.vin.bg.ac.yu</a><br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Ms. Milena Matic<br>
Univerzitetska Biblioteka "Svetozar Markovic"<br>
Kralja Aleksandra 71, 11001 Belgrade, Serbia<br>
Telephone: +381 11 3370507<br>
Facsimile: +381 11 3370354<br>
Email: melani@beotel.rs<br>""",
    "Seychelles": """<b>INIS Liaison Officer<br>
</b>Mr. Jonathan Bonnelame<br>
Ministry of Foreign Affairs<br>
Maison Quéau de Quinssy<br>
Mont Fleuri, Victoria, Seychelles<br>
Telephone: +248 4 283509<br>
Facsimile: +248 4 224845<br>
Email: jbonnelame@mfa.gov.sc<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Ms. Sandra Michel<br>
Ministry of Foreign Affairs<br>
P.O. Box 656, Mont Fleuri, Mahé, Seychelles<br>
Telephone: +248 283531<br>
Facsimile: +248 224845<br>
Email: smichel@mfa.gov.sc""",
    "Synchrotron-light for Experimental Science and Applications in the Middle East (SESAME)": """<b>INIS Liaison Officer<br>
</b>Mr. Mohamed Yasser Khalil<br>
Administrative Director, SESAME<br>
Next to Princess Rahma University College<br>
P.O. Box 7, 19252 Allan, Jordan<br>
Telephone: +962 5 3511349, Ext. 225<br>
Facsimile: +962 5 3511423<br>
Email: my_khalil@yahoo.com<br>
URL: <a href="http://www.sesame.org.jo/">http://www.sesame.org.jo/</a><br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Ms. Sonia Al-Faques<br>
Administrative Assistant, SESAME<br>
Next to Princess Rahma University College<br>
P.O. Box 7, 19252 Allan, Jordan<br>
Telephone: +962 5 3511349, Ext. 203<br>
Facsimile: +962 5 3511423<br>
Email: Sonia@sesame.org.jo""",
    "United Nations Industrial Development Organization (UNIDO)": """<b>INIS Liaison Officer<br>
</b><br>
Statistics and Information Networks Branch<br>
United Nations Industrial Development Organization (UNIDO)<br>
Vienna International Centre, Room D2075, P.O. Box 300, A-1400 Vienna, Austria<br>
Telephone: +43 1 26026 ext. 3666<br>
Facsimile: +43 1 269 2669<br>
URL: <a href="http://www.unido.org">http://www.unido.org</a>""",
    "United Nations Scientific Committee on the Effects of Atomic Radiation (UNSCEAR)": """<b>INIS Liaison Officer<br>
</b>United Nations Scientific Committee on the Effects of Atomic Radiation (UNSCEAR)<br>
Vienna International Centre, Room E0419, P.O. Box 500, A-1400 Vienna, Austria<br>
Telephone: +43 1 26060 ext. 4331<br>
Facsimile: +43 1 260605902""",
    "World Council of Nuclear Workers (WONUC)": """<b>INIS Liaison Officer<br>
</b>Mr. Christophe Chaubard-Willm<br>
World Council of Nuclear Workers (WONUC)<br>
49, rue Lauriston, 75116 Paris, France<br>
Telephone: +33 1 39 48 52 20<br>
Facsimile: +33 1 39 48 51 51<br>
Email: cchaubardwillm@cogema.fr""",
    "World Energy Council (WEC)": """<b>INIS Liaison Officer<br>
</b>World Energy Council (WEC)<br>
Österr. Forschungszentrum Seibersdorf Ges.m.b.H., A-2444 Seibersdorf, Austria<br>
Telephone: (02254) 780 2755<br>
Telex: 14-353 fzs<br>
Facsimile: (02254) 7 4060""",
    "World Health Organization (WHO)": """<b>INIS Liaison Officer<br>
</b>Library and Information Network for Knowledge (LNK)<br>
World Health Organization (WHO)<br>
Avenue Appia, CH-1211 Geneva 27, Switzerland<br>
Telephone: +41 22 7912111 ext. 2073<br>
Telex: 415 416<br>
Facsimile: +41 22 7910746<br>
URL: <a href="http://www.who.ch/">http://www.who.ch/</a>""",
    "World Meteorological Organization (WMO)": """<b>INIS Liaison Officer<br>
</b>Mr. Rupa Kumar Kolli<br>
Chief, World Climate Applications &amp; CLIPS Division<br>
World Climate Programme Department<br>
World Meteorological Organization (WMO)<br>
7bis Avenue de la Paix, Case Postale 2300, CH-1211 Geneva 2, Switzerland<br>
Telephone: +41 22 730 8377<br>
Facsimile: +41 22 730 8042<br>
Email: RKolli@wmo.int<br>
URL: <a href="http://www.wmo.ch/">http://www.wmo.ch/</a>""",
    "World Nuclear Assosiation (WNA)": """<b>INIS Liaison Officer<br>
</b>Mr. Warwick Pipe<br>
Information Officer<br>
World Nuclear Association<br>
Carlton House, 22a St. Jame's Square, London SWIY 4JH, United Kingdom<br>
Telephone: +44 20 7451 1526<br>
Facsimile: +44 20 7839 1501<br>
Email: pipe@world-nuclear.org<br>
URL: <a href="http://www.world-nuclear.org/">http://www.world-nuclear.org/</a><br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Mr. Serge Gorlin<br>
Writer and Analyst<br>
World Nuclear Association<br>
Carlton House, 22a St. Jame's Square, London SWIY 4JH, United Kingdom<br>
Telephone: +44 20 7451 1540<br>
Facsimile: +44 20 7839 1501<br>
Email: gorlin@world-nuclear.org""",
    "World Nuclear University (WNU)": """<b>INIS Liaison Officer<br>
</b>Mr. Warwick Pipe<br>
Information Officer,<br>
World Nuclear Association<br>
Carlton House, 22a St. Jame's Square, London SWIY 4JH, United Kingdom<br>
Telephone: +44 20 7451 1526<br>
Facsimile: +44 20 7839 1501<br>
Email: pipe@world-nuclear.org<br>
URL: <a href="http://www.world-nuclear-university.org/">http://www.world-nuclear-university.org/</a><br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Mr. Serge Gorlin<br>
Writer and Analyst<br>
World Nuclear Association<br>
Carlton House, 22a St. Jame's Square, London SWIY 4JH, United Kingdom<br>
Telephone: +44 20 7451 1540<br>
Facsimile: +44 20 7839 1501<br>
Email: gorlin@world-nuclear.org""",
    "Sierra Leone": """<b>INIS Liaison Officer<br>
</b>Mr. Josephus J. Kongo<br>
Radiation Protection Board Secretariat<br>
Ministry of Energy and Water Resources<br>
Electricity House, 5th Floor<br>
Siaka Stevens Street, Freetown, Sierra Leone<br>
Telephone: +232 76 610754<br>
Facsimile: +232 22 224527<br>
Email: josiekongo@yahoo.com<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Mr. Richard Lamboi<br>
Radiation Protection Board Secretariat<br>
Ministry of Energy and Water Resources<br>
Electricity House, 5th Floor<br>
Siaka Stevens Street, Freetown, Sierra Leone<br>
Telephone: +232 76 618967<br>
Facsimile: +232 22 224527<br>
Email: richardlamboi@yahoo.com<br>
<br>
<b>Document Delivery Service</b><br>
Radiation Protection Board Secretariat, Ministry of Energy and Water Resources<br>
Mailing address: Electricity House, 5th Floor, Siaka Stevens Street, Freetown, Sierra Leone<br>
Telephone: +232 76 610754<br>
Fax: +232 22 224527<br>
Email: josiekongo@yahoo.com""",
    "Singapore": """<b>INIS Liaison Officer<br>
</b>Head, Library and Information Services Centre<br>
National Institute of Education, Nanyang Technological University<br>
1 Nanyang Walk, Singapore 637616<br>
Telephone: (65) 6790-3625<br>
Facsimile: (65) 6896-9031<br>
Email: yvonne.yin@nie.edu.sg<br>
URL: <a href="http://www.nie.edu.sg">www.nie.edu.sg</a><br>
<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Mr. Paul Lee<br>
Telephone: (65) 6790-3815<br>
Email: paul.lee@nie.edu.sg""",
    "Slovakia (the Slovak Republic)": """<b>INIS Liaison Officer<br>
</b>Mr. Karol Janko<br>
Nuclear Regulatory Authority<br>
Bajkalska 27, P.O.Box 24, SK-82007 Bratislava, Slovak Republic<br>
Tel: +421 2 58 22 11 24<br>
Fax: +421 2 58 22 11 66<br>
Email: Karol.Janko@ujd.gov.sk<br>
<br>
<b>Document Delivery Service</b><br>
Faculty of Natural Sciences<br>
Mailing address: Comenius University<br>
Mlynska Dolina Ch-1, 842 15 Bratislava, Slovak Republic<br>
Point of contact: Mr. Pavol Rajec<br>
Telephone: +4217 60296245<br>
Fax: +4217 65424685<br>
Email: rajec@fns.uniba.sk<br>
URL: <a href="http://www.fns.uniba.sk">http://www.fns.uniba.sk</a><br>""",
    "Slovenia": """<b>INIS Liaison Officer<br>
</b>Ms. Polonca Mekicar<br>
Slovenian Nuclear Safety Administration<br>
Ministry of Environment and Spatial Planning<br>
Zelezna cesta 16, P.O. Box 5759, SI-1001 Ljubljana, Republic of Slovenia<br>
Telephone: +386 1 472 1173<br>
Facsimile: +386 1 472 11 99<br>
Email: polonca.mekicar@gov.si<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Mr. Venceslav Kostadinov<br>
Slovenian Nuclear Safety Administration<br>
Ministry of Environment and Spatial Planning<br>
Zelezna cesta 16. P.O. Box 5759, SI-1001 Ljubljana, Republic of Slovenia<br>
Telephone: +386 1 472 1157<br>
Facsimile: +386 1 472 1199<br>
Email: venceslav.kostadinov@gov.si<br>
URL: <a href="www.gov.si/ursjv">www.gov.si/ursjv</a>""",
    "South Africa": """<b>INIS Liaison Officer<br>
</b>Ms. M.J.S. Scheepers<br>
Consulting Librarian<br>
Library and Archival Services<br>
Nuclear Energy Corporation of South Africa (NECSA)<br>
P.O. Box 582, Pretoria 0001, South Africa<br>
Telephone: +27 12 305-5546<br>
Facsimile: +27 12 305-5709<br>
Email: mjss@necsa.co.za<br>
URL: <a href="http://www.necsa.co.za/">http://www.necsa.co.za</a><br>""",
    "Spain": """<b>INIS Liaison Officer</b><br>
Ms. Marisa Marco Arboli<br>
Jefe Division Gestion de Conocimiento<br>
Centro de Investigaciones Energéticas, Medioambientales y Tecnológicas (CIEMAT)<br>
Avenida Complutense 22, E-28040 Madrid, Spain<br>
Telephone: +34 91 346 63 36<br>
Facsimile: +34 91 346 60 05<br>
Email: marisa.marco@ciemat.es<br>
URL: <a href="http://www.ciemat.es">http://www.ciemat.es</a><br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Ms. Izaskun Alberdi Larrañaga<br>
Jefe del Servicio de Documentación y Biblioteca<br>
Centro de Investigaciones Energéticas, Medioambientales y Tecnológicas (CIEMAT)<br>
Avenida Complutense 22, E-28040 Madrid, Spain<br>
Telephone: +34 91 346 63 39<br>
Facsimile: +34 91 346 60 05<br>
Email: Izaskun.alberdi@ciemat.es""",
    "Sri Lanka": """<b>INIS Liaison Officer<br>
</b>Ms. H.L.C. Nanayakkara<br>
Atomic Energy Authority<br>
Baseline Road 60-460, Orugodawatta, Wellampitiya, Colombo 11, Sri Lanka<br>
Tel: (941) 533427, or 533428 or 533449<br>
Cable: LANKATOM, COLOMBO<br>
Fax: (941) 533448<br>
Email: <a href="mailto:chulika@aea.gov.lk">chulika@aea.gov.lk</a><br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Mr. H.M.K. Soysa<br>
Email: srlaea@slt.lk<br>""",
    "Sudan": """<b>INIS Liaison Officer<br>
</b>Ms. Hayat Ali Salih<br>
Nuclear Information Unit<br>
Sudan Atomic Energy Commission (SAEC), <br>
P.O. Box 3001, Khartoum, Sudan<br>
Telephone: +249 183286493<br>
Email: hayatsaec1@gmail.com""",
    "Sweden": """<b>INIS Liaison Officer<br>
</b>Ms. Sara Laurentz<br>
Swedish INIS Centre<br>
KTH Royal Institute of Technology<br>
Osquars backe 25, SE-100 44 Stockholm, Sweden<br>
Telephone: +46 8 7909660<br>
Email: laurentz@kth.se<br>
URL: <a href="http://www.kth.se/ece">http://www.kth.se/ece</a><br>""",
    "Switzerland": """<b>INIS Liaison Officer<br>
</b>Mr. Reiner Mailaender<br>
Research Coordinator<br>
Swiss Federal Safery Inspectorate ENSI<br>
Industriestrasse 19, CH-5200 Brugg, Switzerland<br>
Telephone: +41 56 460 8400<br>
Facsimile: +41 56 460 84 99<br>
Email: Reiner.Mailaender@ensi.ch<br>
URL: <a href="http://www.ensi.ch/">http://www.ensi.ch/</a><br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Mr. Jean-Marc Suter<br>
Suter Consulting<br>
Aarstrasse 98, CH-3005 Bern, Switzerland<br>
Telephone: +41 31 311 4942<br>
Facsimile: +41 31 3114943<br>
Email: suter@suterconsulting.com<br>""",
    "Syrian Arab Republic": """<b>INIS Liaison Officer<br>
</b>Mr. Raek Al-Shanaa<br>
Atomic Energy Commission of Syria<br>
P.O. Box 6091, Damascus, Syrian Arab Republic<br>
Telex: atenco 411420 ATENCO SY<br>
Cable: TAKA<br>
Telephone: +963-11-2132580<br>
Facsimile: +963-11-6112289<br>
Email: atomic@aec.org.sy<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Mr. Raed Al-Hallack<br>
Email: rhallack@aec.org.sy""",
    "Tajikistan": """<b>INIS Liaison Officer<br>
</b>Mr. Ilkhom Mirsaidov<br>
Head, Tajik INIS Centre<br>
Nuclear and Radiation Safety Agency<br>
Academy of Sciences of the Republic of Tajikistan<br>
17 Hakimzoda street, 734025, Dushanbe, Republic of Tajikistan<br>
Telephone: +992 372 27 7791 or +992 372 27 2022<br>
Facsimile: +992 372 21 5548<br>
Email: agentilhom@mail.ru<br>
<br>
<b>Document Delivery Service</b><br>
Tajikistan INIS Center<br>
Nuclear and Radiation Safety Agency, Academy of Sciences, Republic of Tajikistan<br>
Mailing address: Nuclear and Radiation Safety Agency, Academy of Sciences, Republic of Tajikistan,
 17 Hakimzoda Street, 734003, Dushanbe, Tajikistan<br>
Point of contact: Ulmas Mirsaidov, Director, Nuclear and Radiation Safety Agency<br>
Telephone: (992 372) 21 50 83 or 21 50 84<br>
Fax: (992 372) 21 49 11<br>
Email: academy@science.tajik.net""",
    "Thailand": """<b>INIS Liaison Officer<br>
</b>Ms. Punnapa Rakudomchock<br>
Bureau of Atomic Energy Administration, Office of Atoms for Peace<br>
Vibhavadi Rangsit Rd., Chatuchuk, Bangkok 10900, Thailand<br>
Telephone: 66 2596 7600 ext. 1813<br>
Facsimile: 66 2561 3013<br>
Email: punnapa@oaep.go.th<br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Ms. P. Patumthong""",
    "The Former Yugoslav Republic of Macedonia (FYROM)": """<b>INIS Liaison Officer</b><br>
Ms. Pandorka Stoimenovska<br>
National and University Library<br>
"St. Kliment Ohridski"<br>
Goce Delcev 6, P.O. Box 566, 1000 Skopje, The Former Yugoslav Republic of Macedonia<br>
Telephone: +389 2 3 115 177 ext.: 110<br>
Facsimile: +389 2 3 226 846<br>
Email: pandorka@nubsk.edu.mk<br>
<br>
<b>Document Delivery Service</b><br>
National and University Library 'St. Kliment Ohridski', INIS Center<br>
Mailing address: Bul. Goce Delcev 6, P O Box 566, 1000 Skopje, Macedonia<br>
Telephone: +389 2 3 115 177 ext: 152 or (389) 2 3 230 874<br>
Fax: +389 2 3226-846<br>""",
    "Tunisia": """<b>INIS Liaison Officer</b><br>
Ms. Najet Khemiri<br>
Library<br>
Centre National des Sciences et Technologies Nucléaires (CNSTN)<br>
TN-2020 Sidi Thabet, Tunisia<br>
Telephone: +216 71 537 410 or +216 71 544<br>
Facsimile: +216 71 537 555<br>
Email: N.Khemiri@CNSTN.rnrt.tn""",
    "Turkey": """<b>INIS Liaison Officer<br>
</b>Ms. Olcay Sahin Seckin<br>
Head, Nuclear Documentation Center<br>
Turkish Atomic Energy Authority (TAEK)<br>
Eskisehir Yolu 9. Km.<br>
06530 Ankara<br>
Turkey<br>
Telephone: +90 312 295 8882<br>
Facsimile: +90 312 295 8959<br>
Email: olcay.seckin@taek.gov.tr""",
    "Uganda": """<b>INIS Liaison Officer</b><br>
Mr. Emmanuel Wamala<br>
Ministry of Energy and Mineral Development<br>
Amber House, 29-33 Kampala Road, P.O. Box 7270, Kampala, Uganda<br>
Telephone: +256 312 372 757<br>
Mobile: +256 712 971 338<br>
Facsimile: +256 414 349 342<br>
Email: ewamala@energy.go.ug""",
    "Ukraine": """<b>INIS Liaison Officer</b><br>
Ms. Zhanna I. Pysanko<br>
Institute for Nuclear Research<br>
Prospect Nauki 47, 03680 Kyiv 28, Ukraine<br>
Telephone: +380 44 525 4370<br>
Facsimile: +380 44 525 4463<br>
Email: interdep@kinr.kiev.ua""",
    "United Arab Emirates (UAE)": """<b>INIS Liaison Officer<br>
</b>Mr. Salem Abdullah Taleb<br>
Ministry of Energy<br>
P.O.Box 99979, Dubai, United Arab Emirates<br>
Telephone: +971 4 294 5555<br>
Facsimile: +971 4 294 5005<br>
Email: sataleb@moenr.gov.ae<br>
URL: <a href="http://www.moenr.gov.ae">http://www.moenr.gov.ae</a><br>
<br>
<b>Alternate INIS Liaison Officers</b><br>
Ms. Fawzeya Al Marzooqi<br>
Ms. Aayda Al Shehhi<br>""",
    "United Kingdom of Great Britain and Northern Ireland (UK)": """<b>INIS Liaison Officer</b><br>
Ms. Loveli Sanayat<br>
Nuclear Decommissioning and Security Directorate<br>
Department of Energy and Climate Change<br>
3 Whitehall Place<br>
London SW1A 2HH<br>
United Kingdom<br>
Telephone: +44 300 068 5912<br>
Email: <a href="mailto:loveli.sanayat@decc.gsi.gov.uk">loveli.sanayat@decc.gsi.gov.uk<br>
</a><br>
<b>Document Delivery Service</b><br>
British Library Document Supply Centre (BLDSC) - United Kingdom<br>
Mailing address: Boston Spa, Wetherby, West Yorkshire, LS23 7BQ, United Kingdom<br>
Point of contact: Customer Services<br>
Telephone: +44 1937 546060<br>
Fax: +44 1937 546333<br>
Email: For general queries about the BLDSC or to register as a customer: dsc-customer-services@bl.uk
 To order documents without registering as a customer: dsc-lexicon@bl.uk<br>
URL: General information on the BLDSC: <a href="http://www.bl.uk/services/bsds/dsc/">http://www.bl.uk/services/bsds/dsc/</a><br>
Access to our catalogues and a document ordering link: <a href="http://www.bl.uk/services/bsds/dsc/">http://opac97.bl.uk/</a><br>""",
    "Tanzania": """<b>INIS Liaison Officer</b><br>
Mr. Ebenezer Kimaro<br>
Tanzania Atomic Energy Commission (TAEC)<br>
P.O. Box 743, Arusha, United Republic of Tanzania<br>
Telephone: +255 27 2508554<br>
Facsimile: +255 27 2509709<br>
Email: taec@habari.co.tz or saronga02@yahoo.co.uk<br>
URL: <a href="http://www.taec.or.tz/"> http://www.taec.or.tz/</a><br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Mr. Shovi F. Sawe<br>
Telephone: +255 27 2508554<br>
Facsimile: +255 27 2509709<br>
Email: shovisawe@hotmail.com or nrcnim@habari.co.tz<br>""",
    "United States of America": """<b>INIS Liaison Officer<br>
</b>Mr. Brian A. Hitson<br>
Associate Director for Administration and Information Services<br>
Office of Scientific and Technical Information (OSTI), Department of Energy (DOE)<br>
P.O. Box 62, 1 Science.gov Way, Oak Ridge, Tennessee 37831, USA<br>
Telephone: +1 865 576-1199<br>
Facsimile: + 865 576-3589<br>
Email: hitsonb@osti.gov<br>
URL: <a href="http://www.osti.gov/">Department of Energy, Office of Scientific and Technical Information</a><br>
<a href="http://www.doe.gov/">Department of Energy</a><br>
<a href="http://www.nasa.gov/">National Aeronautics and Space Administration</a><br>
<a href="http://www.nrc.gov/">Nuclear Regulatory Commission</a><br>
<a href="http://wwwofe.er.doe.gov/">U.S. Department of Energy Office of Science</a><br>
<a href="http://www.rw.doe.gov/">U.S. Department of Energy Office of Civilian Radioactive Waste Management</a><br>
<a href="http://www.ne.doe.gov/">U.S. Department of Energy Office of Nuclear Energy</a><br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Ms. Deborah E. Cutler<br>
International Program Manager<br>
Office of Scientific and Technical Information (OSTI), Department of Energy (DOE)<br>
P.O. Box 62, 1 Science.gov Way, Oak Ridge, Tennessee 37831, USA<br>
Telephone: +1 865 576-1272<br>
Facsimile: +1 865 576-2865<br>
Email: cutlerd@osti.gov<br>
<br>
<b>Document Delivery Service</b><br>
United States Document Delivery services via the public DOE Information Bridge<br>
Mailing address: U.S. Government Printing Office<br>
Point of contact: GPO Access User Support Team<br>
Telephone: 1-202-512-1530 (DC Metro area) or toll free at 1-888-293-6498 (International)<br>
Fax: 1-202-512-1262<br>
Email: gpoaccess@gpo.gov<br>
URL: <a href="http://www.osti.gov/bridge">http://www.osti.gov/bridge</a>""",
    "Uruguay": """<b>INIS Liaison Officer<br>
</b>Ms. Ana Rebellato Rodriguez<br>
Dirección Nacional de Mineria y Geologì a-DINAMIGE<br>
Hervidero 2861<br>
Casilla de Correo 10844<br>
P.O. Box 11800 - Montevideo<br>
Uruguay<br>
Telephone: +598 2 200 1953<br>
Facsimile: +598 2 200 7113<br>
Email: biblioteca@dinamige.miem.gub.uy<br>
Delivery services: mail, fax, electronic, paper<br>
Request services: mail, fax, email<br>
Cost: actually free of charge<br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Ms. S. Fascioli de Turenne""",
    "Uzbekistan": """<b>INIS Liaison Officer<br>
</b>Ms. Makhtuba Kadirova<br>
Head, International Relations Division<br>
Institute of Nuclear Physics<br>
Uzbekistan Academy of Sciences<br>
Tashkent, Ulughbek, 100214<br>
Uzbekistan<br>
Telephone: +998 71 289 3779<br>
Facsimile: +998 71 150 3080<br>
Email: kadyrova@inp.uz<br>
Delivery services: hard copies, microfiche<br>
Request services: e-mail, fax<br>
Cost: will be agreed at the time of the request<br>
<br>
<b>Alternate INIS Liaison Officer</b><br>
Mr. M. Salimov<br>
Institute of Nuclear Physics<br>""",
    "Venezuela": """<b>INIS Liaison Officer<br>
</b>Ms. Xiomara Jayaro<br>
Jefe de la Biblioteca "Marcel Roche"<br>
Instituto Venezolano de Investigaciones Cientí ficas (IVIC)<br>
Apartado. 21827, Caracas 1020-A, Venezuela<br>
Telephone: +58 2 504 1516 or 58 2 504 1515<br>
Telex: 21657<br>
Facsimile: +582 504 1423<br>
Email: <a href="mailto:xjayaro@ivic.ve">xjayaro@ivic.ve</a> and <a href="mailto:bibliotk@ivic.ivic.ve">bibliotk@ivic.ivic.ve</a><br>
<br>
<b>Alternate INIS Liaison Officer<br>
</b>Ms. Yadira Rojas<br>
Dirección General Sectorial de Energí a, Ministerio de Energí a y Minas<br>
Parque Central, Torre Oeste, Piso 14, Avenida Lecuna, Caracas 1015-A, Venezuela<br>
Telephone: +58 2 5076712 and 5076715<br>
Telex: 21692 MEM VC<br>
Telefax: +58 2 5754386<br>
<br>
<b>Document Delivery Service</b><br>
BIBLIOTECA MARCEL ROCHE. INSTITUTO VENEZOLANO DE INVESTIGACIONES CIENTIFICAS (IVIC)<br>
Mailing address: BIBLIOTECA MARCEL ROCHE, 8424 NW 56 STREET, SUITE CCS 00201, MIAMI FLORIDA 33166, USA<br>
Point of contact: ROSA MARí A LEóN LIVINALLY<br>
Telephone: 58-212-5041516 (INIS office); 58-212-5041236 and 58-212-5041282 (library permanent services): 58-212-5041237 (distance document delivery)<br>
Fax: 58-212-5041423<br>
Email: rleon@ivic.ve; infoivic@ivic.ve (distance document delivery)<br>
URL: <a href="http://zeus.ivic.ve/biblioteca/">http://zeus.ivic.ve/biblioteca/</a><br>
Delivery services: MAIL, FAX, ARIEL, PAPER, ELECTRONIC (PDF, PIXTOOLS)<br>
Request services: EMAIL, MAIL, FAX, web<br>
Cost: From our collection http://zeus.ivic.ve/biblioteca/solicinfo/indextsrif.html Courier Services fees (2001-10-25):
 USA $24; EUROPE $42. Service by out sourcing, without discounts. Possible discounts to users from developing countries: We have agreements with Latin American
 Countries (ARCAL-RRIAN http://www.cnea.gov.ar/rrian/ ) for electronic delivery; and we can make agreements with other developing countries""",
    "Vietnam": """<b>INIS Liaison Officer<br>
</b>Mr. Nguyen Hoang Anh<br>
Information Centre<br>
Vietnam National Atomic Energy Commission (VINATOM)<br>
59 Ly Thuong Kiet Street, Ha Noi, Vietnam<br>
Telephone: +84 4 8243591<br>
Facsimile: +84 4 8266133<br>
Email: hoanganh_ohayo@yahoo.com or hoanganh58@hn.vnn.vn<br>
Document delivery services: Photocopies (through mail), e-form (Scanned from printed form) (through e-mail)<br>
Request services: mail, fax, e-mail<br>
Cost: free of charge""",
    "Yemen": """<b>INIS Liaison Officer<br>
</b>Mr. Abdul Aziz Al-Shehari<br>
National Atomic Energy Commission (NATEC)<br>
P.O. Box 4720, Sanaa, Republic of Yemen<br>
Telephone: +967 1 259159<br>
Facsimile: +967 1 259460<br>
Email: library@natec.gov.ye<br>""",
    "Zambia": """<b>INIS Liaison Officer<br>
</b>Mr. Bernard M. Chisenga<br>
Head, Information Services Unit<br>
National Council for Scientific Research<br>
P.O. Box 310158, 15302 Chelston, Lusaka, Zambia<br>
Telephone: (260-1) 281081-6 or 283533<br>
Facsimile: (260-1) 283533<br>
Email: nisiris@zamnet.zm<br>""",
    "Zimbabwe": """<b>INIS Liaison Officer<br>
</b>Mr. Justice Chipuru<br>
Radiation Protection Authority of Zimbabwe <br>
1 McCaw Drive<br>
Avondale<br>
Box A1710<br>
Harare<br>
Zimbabwe<br>
Telephone: +263 4 335 792, +263 4 335 627<br>
Email: jchipuru@rpaz.co.zw<br>
<br>""",
}

CFG_MEMBERS_NAMES = CFG_MEMBERS_DICT.keys()
CFG_MEMBERS_NAMES.sort()
