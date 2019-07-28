from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

unwanted_entities = ['"', 'Mr', 'Mrs', '’', '—', '-', '”', 'salute', 'Mass']

general = 'scam scandal conflict die death wrongdoing violation infraction abuse dispute contention attack destroy destruct manipulate accuse alleged racketeer ofac unethical unfair competition deceive slander libel nefarious delinquent'
environmental = 'trespass pollution pollute land deforest haze emissions oil dumping toxic poison explosion sewage leak'
legal = 'attorney court crime illegal fraud secret society arrest detain detention indict investigation lawsuit litigation offence prison imprison probe prosecute robbery sanctions syndicate twarrant steal narcotics extortionsentenced blackmail terror ofac unfair competition defendant plaint verdict mafia legal issue guilty felony misdemeanor'
political = 'campaign funding alliance political  politically  politician owned'
social = 'labour demonstration protest deport riot strike human rights discrimination trafficking slavery'
operational = 'counterfeit fake insider malpractice negligence breach price monopoly competition firee explosion contraband cartel data breach complaints license accident unsafe inspection'
financialCrime = 'launder banking bankrupt embezzle insolvency tax evasion accounting insider racketeer fraud laundering finance unfair foreclosure'
corporateGovernance = 'fired terminate whistleblow governance earnings conflict espionage mismanage'
economic = 'economical economic bank fed'
corruption = 'baksheesh fcpa corruption blackmail bribe buy click fraud cook idiom corrupt corruption cybercrime defraud dolus embezzle extort false accounting fix fraud fraudulence fraudulent accounting fraudulently front game-fixing graft impersonate impersonation imposture insider launder malfeasance malpractice match-fixing laundering pay perjury phishing ponzi scheme pyramid scheme rort shell siphon suborn swindle tax evasion vice corrupt'

def big_bag():
	return({
		'general': tokenizer.tokenize(general),
		'environmental': tokenizer.tokenize(environmental),
		'corruption': tokenizer.tokenize(corruption),
		'legal': tokenizer.tokenize(legal),
		'political': tokenizer.tokenize(political),
		'social': tokenizer.tokenize(social),
		'operational': tokenizer.tokenize(operational),
		'financialCrime': tokenizer.tokenize(financialCrime),
		'corporateGovernance': tokenizer.tokenize(corporateGovernance),
		'economic': tokenizer.tokenize(economic)
	})
    
