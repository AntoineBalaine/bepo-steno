# vim: set fileencoding=utf-8 :

# #QYPCTHVRIAEOcsthpr*ieao
KEYS = (
 'S', 'B', 'K', 'P', 'M', 'T', 'F', '*', 'R', 'N', 'L', 'Y', 
 'O', 'E', 'A', 'à', 'U', 'É', 'I', 'l', 'n', '$', 'D', 'C', 
'#'
 )
IMPLICIT_HYPHEN_KEYS = KEYS
SUFFIX_KEYS = ()
NUMBER_KEY = None
NUMBERS = {}
UNDO_STROKE_STENO = ''
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
        'à': 'z',
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
		# 'arpeggiate': 'space',
		# Suppress adjacent keys to prevent miss-strokes.
		'no-op': (',', '.', ']'),
	},
}

DICTIONARIES_ROOT = 'asset:plover_bepo:dictionaries'
# DEFAULT_DICTIONARIES = ('01_French_SION.json', 'init.json', DICTIONARIES_ROOT)
DEFAULT_DICTIONARIES = ( '01_French_SION.json', '02_French_Chiffres.json', '03_French_Adverbes.json', '04_French_Adjectifs.json', '05_French_Noms.json', '06_French_Verbes.json', '07_French_User.json', 'init.json', DICTIONARIES_ROOT, ) 
