# vim: set fileencoding=utf-8 :

# #QYPCTHVRIAEOcsthpr*ieao
KEYS = (
 'S', 'K', 'P', 'M', 'T', 'F', '*', 'R', 'N', 'L', 'Y', 
 'O', 'E', 'A', 'U', 'I', 'l', 'n', '$', 'D', 'C', 
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
        'P': 'q',
        'E': 'w',
        'O': 'e',
        '*': 'r',
        'D': 'i',
        'L': 'o',
        '$': 'p',
        'A': 'a',
        'U': 's',
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
		'arpeggiate': 'space',
		# Suppress adjacent keys to prevent miss-strokes.
		'no-op': ('z', ',', '.', ']'),
	},
}

DICTIONARIES_ROOT = 'asset:plover_bepo:dictionaries'
DEFAULT_DICTIONARIES = ('01_French_SION.json', 'init.json', DICTIONARIES_ROOT)
