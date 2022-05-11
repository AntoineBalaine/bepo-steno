# vim: set fileencoding=utf-8 :

# #QYPCTHVRIAEOcsthpr*ieao
KEYS = (
 'S', 'B', 'K', 'P', 'M', 'T', 'F', '*', 'R', 'N', 'L', 'Y', 
 'O', 'E', 'A', 'U', 'É', 'I', 'l', 'n', '$', 'D', 'C', 
'#'
 )
IMPLICIT_HYPHEN_KEYS = KEYS
SUFFIX_KEYS = ()
NUMBER_KEY = None
NUMBERS = {}
UNDO_STROKE_STENO = 'Ul$C'
ORTHOGRAPHY_RULES = []
ORTHOGRAPHY_RULES_ALIASES = {}
ORTHOGRAPHY_WORDLIST = None
KEYMAPS = {
	'Keyboard': {
		'#': ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        'B': 'q',
        'E': 'f',
        'P': 'e',
        'O': 'r',
        '*': 'u',
        'D': 'i',
        'L': 'o',
        '$': 'p',
        'A': 'a',
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
		# Suppress adjacent keys to prevent miss-strokes.
		'no-op': (',', '.', ']'),
	},
}

DICTIONARIES_ROOT = 'asset:plover_bepo:dictionaries'
DEFAULT_DICTIONARIES = ( 
"PloverFrance_01_French_SION.json",
"init.json",
"PloverFrance_02_French_Chiffres.json",
"nomsFémininsPluriels.json",
"PloverFrance_03_French_Adverbes.json",
"nomsFémininsSinguliers.json",
"PloverFrance_07_French_User.json",
"nomsMasculinsPluriels.json",
"SténoTroisièmeGroupe.json",
"nomsMasculinsSinguliers.json",
"adjectifsPluriels.json",
"prépositions.json",
"adjectifsSinguliers.json",
"verbesDeuxièmeGroupe.json",
"adjectifsSinguliersFéminins(filtrésPartiellement).json",
"verbesPremierGroupe.json",
) 
