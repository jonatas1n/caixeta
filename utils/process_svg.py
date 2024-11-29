from lxml import etree
import random


translations = {
    'Montenegro': 'Montenegro',
    'Slovenie': 'Slovenia',
    'Croatie': 'Croatia',
    'Serbie': 'Serbia',
    'Macedoine': 'North Macedonia',
    'Bosnie Herzegovine': 'Bosnia and Herzegovina',
    'Albanie': 'Albania',
    'Lituanie': 'Lithuania',
    'Estonie': 'Estonia',
    'Lettonie': 'Latvia',
    'Ukraine': 'Ukraine',
    'Bielorussie': 'Belarus',
    'Moldavie': 'Moldova',
    'Italie': 'Italy',
    'Pologne': 'Poland',
    'Slovaquie': 'Slovakia',
    'Rep Tcheque': 'Czech Republic',
    'Hongrie': 'Hungary',
    'Roumanie': 'Romania',
    'Bulgarie': 'Bulgaria',
    'Grece': 'Greece',
    'Royaume Uni': 'United Kingdom',
    'Irlande': 'Ireland',
    'Islande': 'Iceland',
    'Espagne': 'Spain',
    'Portugal': 'Portugal',
    'Danemark': 'Denmark',
    'Groenland (Danemark)': 'Greenland (Denmark)',
    'Allemagne': 'Germany',
    'Suisse': 'Switzerland',
    'Autriche': 'Austria',
    'France': 'France',
    'Pays-Bas': 'Netherlands',
    'Belgique': 'Belgium',
    'Luxembourg': 'Luxembourg',
    'Suede': 'Sweden',
    'Norvege': 'Norway',
    'Finlande': 'Finland',
    'Russie': 'Russia',
    'Turquie': 'Turkey',
    'Chypre': 'Cyprus',
    'Georgie': 'Georgia',
    'Syrie': 'Syria',
    'Jordanie': 'Jordan',
    'Liban': 'Lebanon',
    'Israel': 'Israel',
    'Koweit': 'Kuwait',
    'Arabie Saoudite': 'Saudi Arabia',
    'Emirats Arabes Unis': 'United Arab Emirates',
    'Qatar': 'Qatar',
    'Yemen': 'Yemen',
    'Oman': 'Oman',
    'Irak': 'Iraq',
    'Iran': 'Iran',
    'Armenie': 'Armenia',
    'Kazakhstan': 'Kazakhstan',
    'Ouzbekistan': 'Uzbekistan',
    'Azerbaidjan': 'Azerbaijan',
    'Turkmenistan': 'Turkmenistan',
    'Tadjikistan': 'Tajikistan',
    'Kirghizistan': 'Kyrgyzstan',
    'Afghanistan': 'Afghanistan',
    'Pakistan': 'Pakistan',
    'Inde': 'India',
    'Sri Lanka': 'Sri Lanka',
    'Nepal': 'Nepal',
    'Bhoutan': 'Bhutan',
    'Bangladesh': 'Bangladesh',
    'Cambodge': 'Cambodia',
    'Birmanie': 'Myanmar',
    'Viet-Nam': 'Vietnam',
    'Malaisie': 'Malaysia',
    'Thailande': 'Thailand',
    'Laos': 'Laos',
    'Brunei': 'Brunei',
    'Indonesie': 'Indonesia',
    'Philippines': 'Philippines',
    'Nouvelle Guinee': 'New Guinea',
    'Mongolie': 'Mongolia',
    'Chine': 'China',
    'Japon': 'Japan',
    'Taiwan': 'Taiwan',
    'Coree du Nord': 'North Korea',
    'Coree de Sud': 'South Korea',
    'Australie': 'Australia',
    'Nouvelle-zelande': 'New Zealand',
    'Canada': 'Canada',
    'USA': 'USA',
    'Mexique': 'Mexico',
    'Cuba': 'Cuba',
    'Jamaique': 'Jamaica',
    'Haiti': 'Haiti',
    'Rep Dominicaine': 'Dominican Republic',
    'Trinite et Tobago': 'Trinidad and Tobago',
    'Porto Rico': 'Puerto Rico',
    'Costa Rica': 'Costa Rica',
    'Belize': 'Belize',
    'Guatemala': 'Guatemala',
    'Honduras': 'Honduras',
    'Salvador': 'El Salvador',
    'Nicaragua': 'Nicaragua',
    'Panama': 'Panama',
    'Colombie': 'Colombia',
    'Venezuela': 'Venezuela',
    'Guyane francaise': 'French Guiana',
    'Surinam': 'Suriname',
    'Guyana': 'Guyana',
    'Equateur': 'Ecuador',
    'Perou': 'Peru',
    'Bresil': 'Brazil',
    'Bolivie': 'Bolivia',
    'Paraguay': 'Paraguay',
    'Uruguay': 'Uruguay',
    'Chili': 'Chile',
    'Argentine': 'Argentina',
    'Maroc': 'Morocco',
    'Algerie': 'Algeria',
    'Tunisie': 'Tunisia',
    'Egypte': 'Egypt',
    'Soudan (contour)': 'Sudan (outline)',
    "Soudan: region d'Abiye (taille)": 'Sudan: Abyei region (size)',
    'Soudan du Sud (contour)': 'South Sudan (outline)',
    'Soudan du Sud: Parc national de Radom (taille)': 'South Sudan: Radom National Park (size)',
    'Mali': 'Mali',
    'Lybie': 'Libya',
    'Sahara occidental': 'Western Sahara',
    'Mauritanie': 'Mauritania',
    'Burkina Faso': 'Burkina Faso',
    'Niger': 'Niger',
    'Tchad': 'Chad',
    'Erythree': 'Eritrea',
    'Djibouti': 'Djibouti',
    'Ethiopie': 'Ethiopia',
    'Somalie': 'Somalia',
    'Gambie': 'Gambia',
    'Senegal': 'Senegal',
    'Guinee Bisau': 'Guinea-Bissau',
    'Guinee': 'Guinea',
    'Sierra Leone': 'Sierra Leone',
    'Liberia': 'Liberia',
    "Cote d'Ivoire": "Ivory Coast",
    'Ghana': 'Ghana',
    'Togo': 'Togo',
    'Benin': 'Benin',
    'Nigeria': 'Nigeria',
    'Cameroun': 'Cameroon',
    'Guinee Eq': 'Equatorial Guinea',
    'Rep Centrafricaine': 'Central African Republic',
    'Gabon': 'Gabon',
    'Congo': 'Congo',
    'Rep dem du Congo (Zaire)': 'Democratic Republic of the Congo (Zaire)',
    'Zambie': 'Zambia',
    'Angola': 'Angola',
    'Ouganda': 'Uganda',
    'Ruanda': 'Rwanda',
    'Burundi': 'Burundi',
    'Kenya': 'Kenya',
    'Tanzanie': 'Tanzania',
    'Nanibie': 'Namibia',
    'Malawi': 'Malawi',
    'Lesotho': 'Lesotho',
    'Mozambique': 'Mozambique',
    'Madagascar': 'Madagascar',
    'Botswana': 'Botswana',
    'Zimbabwe': 'Zimbabwe',
    'Zwaziland': 'Eswatini',
    'Afrique de Sud': 'South Africa',
    'Antarctique': 'Antarctica'
}

def color_svg(svg_file, output_file):
    # Cores predefinidas
    colors = ["#7dc442", "#0c8e9b", "#f1714e", "#f2b237", "#d97e2f"]

    # Carregar o SVG como árvore XML
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(svg_file, parser)
    root = tree.getroot()

    # Namespaces comuns em SVG
    namespaces = {"svg": "http://www.w3.org/2000/svg"}

    # Obter todos os elementos <path>
    paths = root.xpath("//svg:path", namespaces=namespaces)

    # Atribuir cores aos paths, minimizando colisões
    previous_colors = {}
    for i, path in enumerate(paths):
        # Garantir que o elemento tenha um ID
        path_id = path.attrib.get("id", f"path_{i + 1}")
        path_id_translated = translations.get(path_id, path_id)
        path.set("id", path_id_translated)

        # Escolher uma cor diferente da mais recente usada para o vizinho
        parent = path.getparent()
        available_colors = colors[:]
        if parent in previous_colors:
            try:
                available_colors.remove(previous_colors[parent])
            except ValueError:
                pass

        chosen_color = random.choice(available_colors)
        path.set("style", f"fill:{chosen_color};")
        previous_colors[path] = chosen_color

    # Salvar o novo SVG em um arquivo
    tree.write(output_file, pretty_print=True, xml_declaration=True, encoding="utf-8")

input_svg = "location.svg"
output_svg = "output.svg"

color_svg(input_svg, output_svg)
