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

CFG_MEMBERS_DICT = {
    'Afghanistan': """<b>INIS Liaison Officer</b></br>
Mr. Khoshal Ahmad Stanikzai</br>
GM Technical Cooperation</br>
Afghan Atomic Energy High Commission (AAEHC)</br>
Silo Main Street, KABUL, AFGHANISTAN</br>
Mobile: +93 (0) 700 246 957</br>
Email: khoshal@aaehc.gov.af</br>
</br>
<b>Alternate INIS Liaison Officer</b></br>
Mr. Bismillah Burhan</br>
Afghan Atomic Energy High Commission (AAEHC)</br>
Silo Main Street, KABUL, AFGHANISTAN</br>
Mobile: +93 (0) 776161003</br>
Email: besburhan@yahoo.com</br>""",
    'African Union (AU)': """<strong>INIS Liaison Officer<br />
</strong>Mr. Atef Wahba Ghabrial<br />
Chief, Science and Technology Department<br />
African Union (AU)<br />
P.O. Box 3243, Addis Ababa, Ethiopia<br />
Telex: 21046 OAU<br />
Telephone: 517700<br />
Cable: OAU, ADDIS ABABA<br />
Facsimile: +251(1) 517844""",
    'Albania': 'ALB',
    'Algeria': 'DZA',
    'Arab Atomic Energy Agency (AAEA)': """<strong>INIS Liaison Officer<br />
</strong>Ms. Nahla Nasr<br />
Division of Science and Technology, Arab Atomic Energy Agency (AAEA)<br />
7, Rue de L'assistance, Cité ElKhadhra, 1003 Tunis, Tunisia<br />
Telephone: +216 71 808 400<br />
Facsimile: +216 71 808 450<br />
Facsimile: +216 71 781 820<br />
Email: aaea@aaea.org.tn""",
    'Argentina': 'ARG',
    'Armenia': 'ARM',
    'Australia': 'AUS',
    'Austria': 'AUT',
    'Azerbaijan': 'AZE',
    'Bangladesh': 'BGD',
    'Belarus': 'BLR',
    'Belgium': 'BEL',
    'Benin': 'BEN',
    'Bolivia': 'BOL',
    'Bosnia and Herzegovina': 'BIH',
    'Botswana': 'BWA',
    'Brazil': 'BRA',
    'Brazilian-Argentine Agency for Accounting and Control of Nuclear Materials (ABACC)': """<strong>INIS Liaison Officer<br />
</strong>Ms. Selma Chi-Barreiro<br />
Institutional Relations Officer of ABACC<br />
Av. Rio Branco, 123, Centro, 20040-005 Rio de Janeiro-RJ, Brazil<br />
Telephone: +55 21 3171 1200<br />
Facsimile: +55 21 3171 1248<br />
Email: selmachi@abacc.org.br<br />
URL: <a href="http://www.abacc.org">http://www.abacc.org</a><br />
<br />
<b>Alternate INIS Liaison Officer</b><br />
Mr. José Orpet Marques Peixoto<br />
Institutional Relations Officer of ABACC<br />
Av. Rio Branco, 123, Centro, 20040-005 Rio de Janeiro-RJ, Brazil<br />
Telephone: +55 21 3171 1200<br />
Facsimile: +55 21 3171 1248<br />
Email: orpet@abacc.org.br""",
    'Bulgaria': 'BGR',
    'Burkina Faso': 'BFA',
    'Cameroon': 'CMR',
    'Canada': 'CAN',
    'Central African Republic': 'CAF',
    'Chad': 'TCD',
    'Chile': 'CHL',
    'China': 'CHN',
    'Colombia': 'COL',
    'Costa Rica': 'CRI',
    'Croatia': 'HRV',
    'Cuba': 'CUB',
    'Cyprus': 'CYP',
    'Czech Republic': 'CZE',
    "C\xc3\xb4te d'Ivoire": 'CIV',
    'Democratic Republic of the Congo': 'COD',
    'Denmark': 'DNK',
    'Ecuador': 'ECU',
    'Egypt': 'EGY',
    'El Salvador': 'SLV',
    'Estonia': 'EST',
    'Ethiopia': 'ETH',
    'European Commission (EC)': 'EC',
    'European Organization for Nuclear Research (CERN)': """<strong>INIS Liaison Officer<br />
</strong>Mr. Jens Vigen<br />
Scientific Information Service, European Organization for Nuclear Research (CERN)<br />
CH-1211 Geneva 23, Switzerland<br />
Telephone: +41 (22) 7672410<br />
Telex: 419000 CER<br />
Facsimile: +41 (22) 7828611<br />
Email: Jens.Vigen@cern.ch<br />
URL: <a href="http://www.cern.ch">http://www.cern.ch</a><br />
Document delivery point of contact: Corrado Pettenati<br />
Email: Corrado.Pettenati@cern.ch<br />
Delivery services: electronic via http<br />
Request services: e-mail, web<br />
Cost: free of charge""",
    'Finland': 'FIN',
    'Food and Agricultural Organization of the United Nations (FAO)': 'FAO',
    'France': 'FRA',
    'Gabon': 'GAB',
    'Georgia': 'GEO',
    'Germany': 'DEU',
    'Ghana': 'GHA',
    'Greece': 'GRC',
    'Guatemala': 'GTM',
    'Haiti': 'HTI',
    'Hungary': 'HUN',
    'India': 'IND',
    'Indonesia': 'IDN',
    'International Atomic Energy Agency (IAEA)': """International Nuclear Information System (INIS)</br>
Department of Nuclear Energy</br>
International Atomic Energy Agency (IAEA)</br>
P.O. Box 100. A-1400 Vienna, Austria</br>
Tel: +43 1 2600 22842</br>
Fax: +43 1 2600 7""",
    'International Centre for Scientific and Technical Information (ICSTI)': 'ICSTI',
    'International Commission on Radiological Protection (ICRP)': 'ICRP',
    'International Institute for Applied Systems Analysis (IIASA)': 'IIASA',
    'International Organization for Standardization (ISO)': 'ISO',
    'Iran': 'IRN',
    'Iraq': 'IRQ',
    'Ireland': 'IRL',
    'Israel': 'ISR',
    'Italy': 'ITA',
    'Japan': 'JPN',
    'Joint Institute for Nuclear Research (JINR)': 'JINR',
    'Jordan': 'JOR',
    'Kazakhstan': 'KAZ',
    'Kenya': 'KEN',
    'Korea': 'PRK',
    'Kuwait': 'KWT',
    'Kyrgyzstan': 'KGZ',
    'Latvia': 'LVA',
    'Lebanon': 'LBN',
    'Libya': 'LBY',
    'Lithuania': 'LTU',
    'Luxembourg': 'LUX',
    'Macedonia': 'MKD',
    'Madagascar': 'MDG',
    'Malaysia': 'MYS',
    'Mali': 'MLI',
    'Mauritania': 'MRT',
    'Mauritius': 'MUS',
    'Mexico': 'MEX',
    'Middle Eastern Radioisotope Centre for the Arab Countries (MERRCAC)': 'MERRCAC',
    'Moldova': 'MDA',
    'Mongolia': 'MNG',
    'Morocco': 'MAR',
    'Mozambique': 'MOZ',
    'Myanmar': 'MMR',
    'Namibia': 'NAM',
    'Netherlands': 'NLD',
    'New Zealand': 'NZL',
    'Nicaragua': 'NIC',
    'Niger': 'NER',
    'Nigeria': 'NGA',
    'Norway': 'NOR',
    'OECD/Nuclear Energy Agency (NEA)': 'NEA',
    'Oman': 'OMN',
    'Pakistan': 'PAK',
    'Panama': 'PAN',
    'Paraguay': 'PRY',
    'Peru': 'PER',
    'Philippines': 'PHL',
    'Poland': 'POL',
    'Portugal': 'PRT',
    'Provisional Technical Secretariat of the Preparatory Commission for the Comprehensive Nuclear-Test-Ban Treaty Organization (CTBTO)': 'CTBTO',
    'Qatar': 'QAT',
    'Romania': 'ROU',
    'Russian Federation': 'RUS',
    'Saudi Arabia': 'SAU',
    'Senegal': 'SEN',
    'Serbia': 'SRB',
    'Singapore': 'SGP',
    'Slovakia': 'SVK',
    'Slovenia': 'SVN',
    'South Africa': 'ZAF',
    'Spain': 'ESP',
    'Sri Lanka': 'LKA',
    'Sudan': 'SDN',
    'Sweden': 'SWE',
    'Switzerland': 'CHE',
    'Synchrotron-light for Experimental Science and Applications in the Middle East (SESAME)': 'SESAME',
    'Syrian Arab Republic': 'SYR',
    'Tajikistan': 'TJK',
    'Tanzania': 'TZA',
    'Thailand': 'THA',
    'Tunisia': 'TUN',
    'Turkey': 'TUR',
    'Uganda': 'UGA',
    'Ukraine': 'UKR',
    'United Arab Emirates (UAE)': 'ARE',
    'United Kingdom (UK)': 'GBR',
    'United Nations Industrial Development Organization (UNIDO)': 'UNIDO',
    'United Nations Scientific Committee on the Effects of Atomic Radiation (UNSCEAR)': 'UNSCEAR',
    'United States of America (USA)': 'USA',
    'Uruguay': 'URY',
    'Uzbekistan': 'UZB',
    'Venezuela': 'VEN',
    'Viet Nam': 'VNM',
    'World Council of Nuclear Workers (WONUC)': 'WONUC',
    'World Energy Council (WEC)': 'WEC',
    'World Health Organization (WHO)': 'WHO',
    'World Meteorological Organization (WMO)': 'WMO',
    'World Nuclear Assosiation (WNA)': 'WNA',
    'World Nuclear University (WNU)': 'WNU',
    'Yemen': 'YEM',
    'Zambia': 'ZMB',
    'Zimbabwe': 'ZWE'
}


CFG_MEMBERS_NAMES = CFG_MEMBERS_DICT.keys()
