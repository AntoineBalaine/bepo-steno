# vim: set fileencoding=utf-8 :

# #QYPCTHVRIAEOcsthpr*ieao
KEYS = (
 'S', 'K', 'P', 'M', 'T', 'F', '*', 'R', 'N', 'L', 'Y', 'H', 
 'O', '^', 'E', 'È', 'A', 'À', 'U', 'I', 'l', 'É', 'n', '$', 'B', 'D', 'C', 
'#', 'ß', '.', ','
 )
IMPLICIT_HYPHEN_KEYS = KEYS
SUFFIX_KEYS = ('.', ',', 'ß')
NUMBER_KEY = None
NUMBERS = {}
UNDO_STROKE_STENO = '*'
ORTHOGRAPHY_RULES = []
ORTHOGRAPHY_RULES_ALIASES = {}
ORTHOGRAPHY_WORDLIST = None
KEYMAPS = {
	'Keyboard': {
        'B': 'q',
        'E': 'f',
        'È': 't',
        'P': 'e',
        'O': 'r',
        '*': 'u',
        'D': 'i',
        'L': 'o',
        '$': 'p',
        'A': 'a',
        'À': 'z',
        'U': 's',
        'É': 'w',
        'I': 'd',
        'Y': 'x',
        'K': ('c', 'b'),
        'C': 'h',
        'T': 'j',
        'S': 'k',
        'R': 'l',
        'N': ';',
        'M': '\'',
        'F': '/',
        'n': 'n',
        'l': 'm',
        '.': 'v',
        ',': 'g',
        'H': ('{.}', '{,}'),
        'ß': '{space}',
        '^': 'y'
    },
}

DICTIONARIES_ROOT = 'asset:plover_bepo:dictionaries'
DEFAULT_DICTIONARIES = (
"adjectifsPluriels.json",
"adjectifsSinguliersFéminins(filtrésPartiellement).json",
"adjectifsSinguliers.json",
"_ble.json",
"commandes.json",
"init.json",
"nomsFémininsPluriels.json",
"nomsFémininsSinguliers.json",
"nomsMasculinsPluriels.json",
"nomsMasculinsSinguliers.json",
"PloverFrance_01_French_SION.json",
"PloverFrance_02_French_Chiffres.json",
"PloverFrance_03_French_Adverbes.json",
"PloverFrance_07_French_User.json",
"user.json",
"verbesDeuxièmeGroupe.json",
"verbesPremierGroupe.json",
"verbesTroisièmeGroupe.json",
) 

