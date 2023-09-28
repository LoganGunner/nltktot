from nltk import *



###################################[ Constants ]######################################

USERNAMEEXPRESSION = "<[A-Za-z0-9]+>" # RegEx for usernames contained between <>
SYSTEMUSERNAME = "-!-" # The tag for system messages, change based on system/chat log origins
TIMESTAMPEXPRESSION = "\[[0-9]{2}:[0-9]{2}:[0-9]{2}(\.[0-9]{1,3})?\]" # RegEx for timestamp as [HH:MM:SS.MS]
KEYWORDS = [ # List of Keywords to reference
    'torchlight2', 'tl2'
]
AIRFRAMES = {
    
}
ACRONYMS = {
    'ACO': 'airspace control', 'ADA': 'air defense', 'AC': 'attack', 'AFTTP': 'Air Force tactics, techniques, and', 'AI': 'air', 'ALSA': 'Air Land Sea Application', 
    'AMD': 'air mobility', 'AO': 'area of', 'AOC': 'air operations', 'AOR': 'area of', 'ASOC': 'air support operations', 'ASR': 'air support', 'ATO': 'air tasking', 
    'BCD': 'battlefield coordination', 'BCT': 'brigade combat', 'BDA': 'battle damage', 'BFT': 'blue force', 'C2': 'command and', 'C2DO': 'command and control duty', 
    'CAC': 'common access', 'CAOC': 'combined air operations', 'CAS': 'close air', 'CASEVAC': 'casualty', 'CFACC': 'combined force air component', 
    'CJTF': 'coalition joint task', 'CCA': 'close combat', 'CCDR': 'combatant', 'CCO': 'central control', 'COD': 'combat operations', 'COP': 'common operational', 
    'CCSG': 'commander, carrier strike', 'CSARDO': 'combat search and rescue duty', 'CSG': 'carrier strike', 'DCA': 'defensive', 'DEC': 'dynamic effects', 
    'DSN': 'Defense Switched', 'DT': 'dynamic', 'DTL': 'dynamic targeting', 'ESG': 'expeditionary strike', 'FARP': 'forward arming and refueling', 'FM': 'field', 
    'FRAGORD': 'fragmentary', 'FSE': 'fire support', 'GCC': 'Geographic combatant', 'IAW': 'in accordance', 'IDN': 'initial distribution', 'IED': 'improvised explosive', 
    'INFLTREPS': 'In-flight', 'IO': 'information', 'IODO': 'information operations duty', 'IP': 'internet', 'ISRD': 'intelligence, surveillance, and reconnaissance', 
    'IT': 'information', 'IWDO': 'Irregular warfare duty', 'J-3': 'operations directorate of a joint staff; operations staff', 
    'J-6': 'communications system directorate of a joint staff;', 'control,': 'communications, and computer systems staff', 'JADOCS': 'joint automated deep operations coordination', 
    'JFC': 'joint force', 'JOA': 'joint operations', 'JP': 'joint', 'JPRC': 'joint personnel recovery', 'JSTARS': 'joint surveillance target attack radar', 
    'JTAC': 'joint terminal attack', 'JTF': 'joint task', 'Lemay': 'Center Curtis E. LeMay Center for Doctrine Development', 'Education': '', 'LNO': 'liaison', 'LAN': 'local area', 
    'MCCDC': 'Marine Corps Combat Development', 'MCRP': 'Marine Corps reference', 'MEDEVAC': 'medical', 'MND-B': 'Multinational', 'MTI': 'moving target', 
    'MTTP': 'multi-Service tactics, techniques, and', 'NECOS': 'net control', 'NL': '', 'NIPRNET': 'non-secure internet protocol router', 'NTTP': 'Navy tactics, techniques, and', 
    'NWDC': 'Navy Warfare Development', 'ODO': 'operations duty', 'OEF': 'Operation ENDURING', 'OIF': 'Operation IRAQI', 'OPLAN': 'operation', 'OPORD': 'operation', 
    'OPTASKCHAT': 'operation task', 'PCHAT': 'persistent', 'PID': 'positive', 'POI': 'point of', 'POO': 'point of', 'PR': 'personnel', 'RO': 'room', 'ROE': 'rules of', 
    'ROZ': 'restricted operations', 'S-3': 'battalion or brigade operations staff officer (Army;', 'Corps': 'battalion or', 'S-6': 'communications staff', 
    'SADO': 'senior air defense', 'SALT': 'size, activity, location,', 'SALUTE': 'size, activity, location, unit, time, and', 'SATCOM': 'satellite', 
    'SEAD': 'suppression of enemy air', 'SIDO': 'senior intelligence duty', 'SIGACT': 'significant', 'SIPRNET': 'secret internet protocol router', 'SITREP': 'situation', 
    'SODO': 'senior operations duty', 'SOLE': 'special operations liaison', 'SOP': 'standard operating', 'SOR': 'system of', 'SUA': 'special use', 'TACS': 'tactical air control', 
    'TAOC': 'Tactical Air Operations', 'TC': 'tactical', 'TIC': 'troops in', 'TOC': 'tactical operations', 'TRADOC': 'United States Army Training and Doctrine', 
    'TST': 'time-sensitive', 'TTP': 'tactics, techniques and', 'UAS': 'unmanned aircraft', 'UJTL': 'Universal Joint Task', 'UNTL': 'Universal Naval Task', 'US': 'United', 
    'USSOCOM': 'United States Special Operations', 'VOSIP': 'voice over secure internet'
                 }

ABBREVIATIONS = {
    'abn': 'airborne',
    'arr': 'arrived',
    'a/c': 'aircraft',
    'a/f': 'as fragged or airfield depending on context',
    'affirm': 'affirmative',
    'afk': 'away from keyboard',
    'appr': 'approved',
    'aar': 'after action review',
    'a/s': 'airspace',
    'ata': 'actual time of arrival',
    'atd': 'actual time of departure',
    'att': 'at this time (use ‘now’)',
    'bolo': 'be on the lookout for',
    'c': 'copy (acknowledgment of receipt)',
    'ck': 'check',
    'cip': 'come in please (generally used when initiating whispers)',
    'Clr': 'clear',
    'clrd': 'cleared',
    'canx': 'cancel',
    'comm': 'communications',
    'consol': 'consolidate',
    'c/s': 'call sign',
    'dc': 'disconnected',
    'decon': 'deconflict or decontaminate depending on context',
    'decond': 'deconflicted',
    'dep': 'departed',
    'd/o': 'drop off',
    'dz': 'drop zone',
    'enrt': 'en route',
    'eom': 'end of mission',
    'eta': 'estimated time of arrival',
    'etd': 'estimated time of departure',
    'fc': 'frequency change',
    'fl': 'flight level (altitude in hundreds of feet)',
    'ff': 'flight following',
    'ftr': 'failed to radio',
    'g2w': 'good two way communication',
    'gt': 'good test (reply to a “t” ((test)) connectivity check request)',
    'hc': 'how copy',
    'hvt': 'high value target',
    'i+': '(air refueling) instantaneous fuel available',
    'ib': 'Inbound',
    'IFE': 'in flight emergency',
    'ifr': 'instrument flight rules or in flight report depending on context',
    'imm': 'immediate',
    'iso': 'in support of',
    'ivo': 'in vicinity of',
    'lnd': 'landed',
    'lkp': 'last known position',
    'lz': 'landing zone',
    'max': 'ord maximum ordnance altitude',
    'mc': 'mission complete',
    'msn': 'mission',
    'mt': 'mis-tell (posted info in wrong room)',
    'Mx': 'or maint maintenance',
    'neg': 'negative',
    'nstr': 'nothing significant to report',
    'ob': 'outbound',
    'o/c': 'on channel',
    'o/n': 'operations normal',
    'o/s': 'on station',
    'osr': 'operating outside ROZ',
    'o/t': 'on tank (air refueling)',
    'pls': 'please',
    'poi': 'point of injury/impact',
    'poo': 'point of origin',
    'pos': 'position',
    'pri': 'priority',
    'rcvr': 'aircraft receiving air refueling',
    'rhr': 'ROZ hot request',
    'rip': 'relief in place',
    'rqst': 'request',
    'rgr': 'roger',
    'rp': 'release point',
    'rnds': 'rounds',
    'ron': 'remain overnight',
    'roz': 'restricted operating zone',
    'rtb': 'return to base',
    'rtd': 'return to duty',
    'rtn': 'routine',
    'r/r': 'radar/IFF contact and radio communication established',
    'rx': 'receive',
    'sod': 'safe on deck',
    'stby': 'standby (does not imply “working”)',
    'SIPR': 'Secret Internet Protocol Relay (secure network)',
    'sof': 'special operations forces',
    'sp': 'start point',
    's/f': 'show of force',
    'sfc': 'surface',
    't': 'test (request for a connectivity check)',
    'thx': 'thank you',
    'TIC': 'troops in contact',
    't/o': 'takeoff',
    'tn': 'datalink track number',
    'tot': 'time on target',
    'TST': 'time sensitive target',
    'tx': 'transmit',
    'unk': 'unknown',
    'urg': 'urgent',
    'urgsurg': 'urgent surgical',
    'VFR': 'visual flight rules',
    'w/d': 'wheels down',
    'wkg': 'working (standby implied)',
    'wrt': 'with regard to',
    'wspr': 'Whisper',
    'w/u': 'wheels up',
    'wx': 'Weather',
    'yw': 'you’re welcome',
    '*': '(single asterisk) used to make an immediate correction to previous posting',
    '***': '(three asterisks) used to denote a VIP onboard a specific a/c',
    '.': '(period) used to check server connectivity; no reply is required'
}



######################################################################################

file = open('IRCsamplechat.txt')

chats = open('chatmessages.txt', "w")

for line in file.readlines():
   # line = line.strip("\n")
    timestamp = re.search(TIMESTAMPEXPRESSION, line).group()
    username = re.search(USERNAMEEXPRESSION, line)
    if not username:
        username = re.search(SYSTEMUSERNAME, line)
    if username:
        username = username.group()
        message = re.split(username, line)[-1]
    else: message = re.split(TIMESTAMPEXPRESSION, line)[-1]

    chats.write(message)

chats.close()

chats = open('chatmessages.txt', 'r').read()

textList = Text(word_tokenize(chats))
for word in KEYWORDS:
    textList.concordance(word)