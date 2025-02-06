import argparse
import itertools
import random
import sys
from datetime import datetime

# Configuration des motifs courants
COMMON_PATTERNS = [
    'admin', 'backup', 'test', 'dev', 'api', 
    'wp', 'login', 'config', 'db', 'secret',
    'old', 'new', 'temp', 'tmp', 'bak', 
    'archive', 'sql', 'logs', 'data', 'user'
]

FILE_EXTENSIONS = [
    'php', 'html', 'js', 'json', 'txt',
    'zip', 'tar', 'gz', 'sql', 'env',
    'cfg', 'conf', 'yaml', 'xml', 'bak'
]

DATE_FORMATS = [
    '%Y', '%y', '%m%d%Y', '%Y%m%d', '%d%m%Y',
    '%m%d%y', '%m%d', '%Y-%m-%d', '%d%m%y'
]

LEET_SUBSTITUTIONS = {
    'a': ['4', '@'],
    'e': ['3'],
    'i': ['1', '!'],
    'o': ['0'],
    's': ['5', '$'],
    't': ['7']
}

def generate_dates(years_back=5):
    """Génère des dates pertinentes"""
    current_year = datetime.now().year
    dates = []
    
    # Années
    dates += [str(y) for y in range(current_year - years_back, current_year + 1)]
    
    # Dates complètes
    for year in range(current_year - 2, current_year + 1):
        for month in range(1, 13):
            for day in [1, 15, 28]:
                date = datetime(year, month, day)
                for fmt in DATE_FORMATS:
                    dates.append(date.strftime(fmt))
    
    return list(set(dates))

def leet_transform(word):
    """Transforme un mot en version leet"""
    variants = ['']
    for char in word:
        new_variants = []
        for variant in variants:
            if char.lower() in LEET_SUBSTITUTIONS:
                for sub in LEET_SUBSTITUTIONS[char.lower()]:
                    new_variants.append(variant + sub)
            new_variants.append(variant + char)
        variants = list(set(new_variants))
    return variants

def apply_modifiers(word, args):
    """Applique tous les modificateurs au mot"""
    variants = [word]
    
    # Modification de casse
    if args.uppercase:
        variants.append(word.upper())
    if args.lowercase:
        variants.append(word.lower())
    if args.capitalize:
        variants.append(word.capitalize())
    
    # Transformations leet
    if args.leet:
        variants += leet_transform(word)
    
    return list(set(variants))

def generate_wordlist(args):
    """Génère la wordlist personnalisée"""
    base_words = []
    
    # Lecture des mots de base
    if args.input:
        with open(args.input, 'r') as f:
            base_words = [line.strip() for line in f]
    else:
        base_words = COMMON_PATTERNS
    
    # Génération des dates
    date_suffixes = []
    if args.dates:
        date_suffixes = generate_dates()
    
    # Génération des combinaisons
    for word in base_words:
        # Application des modificateurs
        variants = apply_modifiers(word, args)
        
        for variant in variants:
            # Combinaison avec extensions
            if args.extensions:
                for ext in FILE_EXTENSIONS:
                    yield f"{variant}.{ext}"
            
            # Combinaison avec dates
            if args.dates:
                for date in date_suffixes:
                    yield f"{variant}{date}"
                    yield f"{date}{variant}"
                    if args.extensions:
                        for ext in FILE_EXTENSIONS:
                            yield f"{variant}{date}.{ext}"
            
            # Combinaisons simples
            yield variant
            
            # Ajout de préfixes/suffixes
            if args.prefixes:
                for prefix in args.prefixes.split(','):
                    yield f"{prefix}{variant}"
            if args.suffixes:
                for suffix in args.suffixes.split(','):
                    yield f"{variant}{suffix}"

def main():
    parser = argparse.ArgumentParser(description='Générateur de wordlist intelligent')
    parser.add_argument('-i', '--input', help='Fichier d\'entrée avec mots de base')
    parser.add_argument('-o', '--output', help='Fichier de sortie')
    parser.add_argument('--dates', action='store_true', help='Ajouter des suffixes de date')
    parser.add_argument('--extensions', action='store_true', help='Ajouter des extensions de fichier')
    parser.add_argument('--leet', action='store_true', help='Activer les transformations leet')
    parser.add_argument('--prefixes', help='Liste de préfixes séparés par des virgules')
    parser.add_argument('--suffixes', help='Liste de suffixes séparés par des virgules')
    parser.add_argument('--uppercase', action='store_true', help='Générer des variations en majuscules')
    parser.add_argument('--lowercase', action='store_true', help='Générer des variations en minuscules')
    parser.add_argument('--capitalize', action='store_true', help='Générer des variations capitalisées')
    parser.add_argument('--min-length', type=int, default=3, help='Longueur minimale des mots')
    parser.add_argument('--max-length', type=int, default=20, help='Longueur maximale des mots')
    
    args = parser.parse_args()
    
    # Génération de la wordlist
    word_generator = generate_wordlist(args)
    
    # Filtrage et sauvegarde
    unique_words = set()
    try:
        with open(args.output, 'w') if args.output else sys.stdout as f:
            for word in word_generator:
                if args.min_length <= len(word) <= args.max_length:
                    if word not in unique_words:
                        unique_words.add(word)
                        f.write(f"{word}\n")
    except KeyboardInterrupt:
        print("\n[!] Interruption utilisateur - Sauvegarde partielle...")
    
    print(f"[+] Wordlist générée avec {len(unique_words)} entrées uniques")

if __name__ == '__main__':
    main()