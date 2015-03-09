__author__ = "Justin Milanovic"
__copyright__ = "Copyright 2015, HireGround"
__version__ = "1.0.0"
__email__ = "justinmilanovic@gmail.com"
__status__ = "Development"

from os import path

TWITTER_CONSUMER_KEY ="rtSI6qY8er6klGgPFDwNVSWAA"
TWITTER_CONSUMER_SECRET ="1V2k01WMb5zyI40HQwyBuvr7tPSpqtxoDZhsPRDQiyroV7sfuw"
TWITTER_ACCESS_TOKEN ="174059917-9sEm5laVY7qKt8U3lCi072yvPOtJBVOCRknw4IqL"
TWITTER_ACCESS_TOKEN_SECRET = "QhUcqWk06yonYvRYPLonf4c9E3AloLbxCggzoVKkspUb6"

TWITTER_CURSOR_FILE = path.dirname(__file__) + '/data/twitter_cursor_output.p'
TWITTER_STREAM_FILE = path.dirname(__file__)  + '/data/twitter_stream_output.p'
TWITTER_CLEAN_DATA = path.dirname(__file__)  + '/data/twitter_clean_data.txt'

TWITTER_CUSTOM_STOPWORDS = path.dirname(__file__)  + '/data/custom_stopwords.txt'
TWITTER_CUSTOM_PHRASES_LEFT = [' is hiring ', ' is hiring a ', ' is looking for ', ' is looking for a ']
TWITTER_CUSTOM_PHRASES_RIGHT = [' in ', ' at ']

STANFORD_NER = '/usr/share/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz'
STANFORD_NER_JAR = '/usr/share/stanford-ner/stanford-ner.jar'


TWITTER_PUNCTUATION = r"(;|:|\.|,|\|)"
TWITTER_HASHTAGS = r"#\w*"
TWITTER_USERNAME = r"@\w*"
TWITTER_HYPERLINKS = r"http://.*|https://.*"
TWITTER_BRACKETS = r"(\(|\)|\[|\])"
TWITTER_SQUARE_BRACKETS_TEXT = r"\[(.+?)\]"
TWITTER_DASH_SLASH = r"(-|\/|\\)"
TWITTER_CUTOFF = r"\w*\.{3}"
TWITTER_US_STATES = r"^(?-i:A[LKSZRAEP]|C[AOT]|D[EC]|F[LM]|G[AU]|HI|I[ADLN]|K[SY]|LA|M[ADEHINOPST]|N[CDEHJMVY]|O[HKR]|P[ARW]|RI|S[CD]|T[NX]|UT|V[AIT]|W[AIVY])$"
TWITTER_LOCATIONS = r"(Ala(bama|ska)|Arizona|Arkansas|California|Colorado|Connecticut|Delaware|District of Columbia|Florida|Georgia|Hawaii|Idaho|Illinois|Indiana|Iowa|Kansas|Kentucky|Louisiana|Maine|Maryland|Massachusetts|Michigan|Minnesota|Miss(issippi|ouri)|Montana|Nebraska|Nevada|New (Hampshire|Jersey|Mexico|York)|North (Carolina|Dakota)|Ohio|Oklahoma|Oregon|Pennsylvania|Rhode Island|South (Carolina|Dakota)|Tennessee|Texas|Utah|Vermont|Virginia|Washington|West Virginia|Wisconsin|Wyoming|A[KLRZ]|C[AOT]|D[CE]|FL|GA|HI|I[ADLN]|K[SY]|LA|M[ADEINOST]|N[CDEHJMVY]|O[HKR]|PA|RI|S[CD]|T[NX]|UT|V[AT]|W[AIVY])"

TWITTER_REGEX = [TWITTER_HYPERLINKS, TWITTER_HASHTAGS, TWITTER_USERNAME, TWITTER_BRACKETS, TWITTER_SQUARE_BRACKETS_TEXT, TWITTER_CUTOFF, TWITTER_PUNCTUATION, TWITTER_LOCATIONS]









