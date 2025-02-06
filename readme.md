```markdown
# Wordlist Genius 📚🔠

**Générateur intelligent de wordlists pour tests de pénétration web**

## 📝 Description

Wordlist Genius est un outil puissant pour créer des wordlists personnalisées et ciblées, spécialement conçu pour :
- Les tests d'intrusion web
- Le directory/file busting
- Les attaques par force brute
- La découverte de ressources cachées

## ✨ Fonctionnalités

### 🛠️ Génération Avancée
- **Transformations Leet** (1337 5p34k)
- **Suffixes de dates** réalistes (2023, 230901, etc.)
- **Extensions de fichiers** communes (.php, .bak, .env)
- **Variations de casse** (Majuscules/Mincules/Capitales)
- **Préfixes/Suffixes** personnalisables

### 🔍 Optimisations Intelligentes
- Filtrage par longueur de mots
- Élimination des doublons
- Génération en flux continu (faible usage mémoire)
- Combinaisons contextuelles
- Support de mots-clés de base

## 📦 Installation

**Prérequis** : Python 3.6+

1. Téléchargement :
```bash
git clone https://github.com/habib26-14/wordlist_gen.git  
cd wordlist_gen
```

## 🚀 Utilisation

### Commande de base
```bash
python3 wordlist_gen.py -o custom_wl.txt
```

### Options Principales
| Option               | Description                                  |
|----------------------|----------------------------------------------|
| `-i, --input`        | Fichier d'entrée avec mots de base           |
| `-o, --output`       | Fichier de sortie (requis)                   |
| `--dates`            | Ajouter des suffixes de date                 |
| `--extensions`       | Ajouter des extensions de fichiers           |
| `--leet`             | Activer les transformations leet             |
| `--prefixes`         | Liste de préfixes (séparés par virgules)     |
| `--suffixes`         | Liste de suffixes (séparés par virgules)     |
| `--uppercase`        | Générer des versions en majuscules           |
| `--lowercase`        | Générer des versions en minuscules           |
| `--capitalize`       | Générer des versions capitalisées            |
| `--min-length`       | Longueur minimale des mots (défaut: 3)       |
| `--max-length`       | Longueur maximale des mots (défaut: 20)      |

## 📌 Exemples

1. Génération basique avec motifs courants :
```bash
python3 wordlist_gen.py -o base_wl.txt --dates --extensions
```

2. Wordlist personnalisée avancée :
```bash
python3 wordlist_gen.py -i my_words.txt -o mega_wl.txt \
  --leet --dates --extensions php,env \
  --prefixes admin,dev,test --suffixes _bak,2023 \
  --capitalize --min-length 5 --max-length 25
```

3. Génération ciblée pour une entreprise :
```bash
python3 wordlist_gen.py -i company_keywords.txt -o company_wl.txt \
  --prefixes dev,prod,staging --suffixes 2023,2022,_backup \
  --leet --extensions json,yml
```

## 💡 Recommandations

1. **Base de mots** : Commencez avec 50-100 mots clés pertinents
2. **Combinaisons** : Utilisez modérément les extensions/dates
3. **Longueur** : Ajustez min/max selon la cible
4. **Leet Speak** : Combiné avec des variations de casse
5. **Optimisation** : Générer plusieurs wordlists spécialisées

## ⚠️ Avertissement

Cette tool est destinée à des **tests de sécurité autorisés** uniquement. Toute utilisation malveillante est strictement interdite et peut entraîner des poursuites judiciaires.

## 🔄 Intégration

Utilisez la wordlist générée avec [Stealth Buster](https://github.com/habib26-14/stealth_buster) pour des scans optimisés :
```bash
python3 stealth_buster.py -u http://cible.com -w custom_wl.txt -t 15 --delay 0.5
```

## 📄 Licence

MIT License - Voir le fichier [LICENSE](LICENSE) pour plus de détails
```

Ce README fournit une documentation complète tout en restant concis. Pour une utilisation professionnelle, vous pourriez ajouter :
- Une section de dépannage
- Des exemples de sorties détaillées
- Un diagramme de génération
- Une matrice de combinaisons possibles
- Un guide de personnalisation avancée