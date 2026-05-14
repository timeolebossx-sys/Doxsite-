# 🔍 Doxsite

> Application web de recherche OSINT — scraping, vérification de fuites de données et recherche de profils sociaux.

![Python](https://img.shields.io/badge/Python-65.7%25-3776AB?style=flat-square&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-16.1%25-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Flask](https://img.shields.io/badge/Flask-2.3.3-000000?style=flat-square&logo=flask)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

-----

## 📋 Description

Doxsite est une application web OSINT (Open Source Intelligence) développée en Python/Flask. Elle permet de centraliser la recherche d’informations sur une cible à partir de plusieurs sources : scraping web, vérification de fuites de données (data breaches), recherche de comptes sur les réseaux sociaux et extraction de métadonnées.

> ⚠️ **Avertissement légal** : Cet outil est destiné à un usage éducatif et à des recherches légitimes uniquement. L’utilisation de cet outil pour collecter des informations sur des personnes sans leur consentement peut être illégale selon votre juridiction. L’auteur décline toute responsabilité en cas d’usage abusif.

-----

## ✨ Fonctionnalités

- **🌐 Web Scraping** — Recherche automatisée d’informations sur le web via `WebScraper`
- **💥 Breach Checker** — Vérification de la présence d’une cible dans des bases de données de fuites (`BreachChecker`)
- **👤 Social Finder** — Recherche de comptes et profils sur les réseaux sociaux (`SocialFinder`)
- **📄 Extraction de métadonnées** — Analyse des métadonnées associées à une cible
- **🖥️ Interface web** — Frontend intégré (HTML/CSS/JS) accessible via navigateur

-----

## 🗂️ Structure du projet

```
Doxsite-/
├── app.py                  # Point d'entrée Flask (routes principales)
├── requirements.txt        # Dépendances Python
├── Launch                  # Script de lancement
├── Project structure       # Description de l'architecture
├── LICENSE                 # Licence MIT
├── modules/
│   ├── scraper.py          # Module de scraping web
│   ├── breach.py           # Module de vérification de fuites
│   └── social.py           # Module de recherche sociale
├── templates/
│   └── index.html          # Interface web principale
└── static/                 # Fichiers CSS, JS, images
```

-----

## ⚙️ Prérequis

- Python **3.8+**
- pip
- (Optionnel) Un navigateur compatible avec Selenium (Chrome, Firefox)

-----

## 🚀 Installation

**1. Cloner le dépôt**

```bash
git clone https://github.com/timeolebossx-sys/Doxsite-.git
cd Doxsite-
```

**2. Installer les dépendances**

```bash
pip install -r requirements.txt
```

**3. Lancer l’application**

```bash
python app.py
```

L’application sera accessible à l’adresse : **http://localhost:8080**

-----

## 🔧 Dépendances

|Package       |Version|Rôle                                 |
|--------------|-------|-------------------------------------|
|Flask         |2.3.3  |Serveur web                          |
|requests      |2.31.0 |Requêtes HTTP                        |
|selenium      |4.15.2 |Scraping dynamique                   |
|beautifulsoup4|4.12.2 |Parsing HTML                         |
|python-dotenv |1.0.0  |Gestion des variables d’environnement|
|aiohttp       |3.9.1  |Requêtes HTTP asynchrones            |
|fake-useragent|1.4.0  |Rotation des User-Agents             |

-----

## 📡 API

### `POST /search`

Lance une recherche sur une cible donnée.

**Corps de la requête (JSON) :**

```json
{
  "target": "email@example.com"
}
```

**Réponse (JSON) :**

```json
{
  "web": { ... },
  "breaches": { ... },
  "social": { ... },
  "metadata": { ... }
}
```

-----

## 📝 Licence

Ce projet est sous licence **MIT**. Voir le fichier <LICENSE> pour plus de détails.

-----

## 👤 Auteur

**timeolebossx-sys** — [GitHub](https://github.com/timeolebossx-sys)
