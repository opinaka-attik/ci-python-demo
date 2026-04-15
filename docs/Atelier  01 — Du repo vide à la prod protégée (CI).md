

---

## 🐍 Atelier DevOps 1 — CI : Du repo vide à la prod protégée

---

## 🏗️ PARTIE 1 — Créer le repo GitHub

### Étape 1 — Créer le repo sur GitHub

1. Aller sur [github.com](https://github.com/) → **"New repository"**
2. Remplir :

|Champ|Valeur|
|---|---|
|Repository name|`ci-python-demo`|
|Visibility|Public|
|Initialize with README|✅ Cocher|

3. Cliquer **"Create repository"**

> ✅ Le repo existe sur GitHub. Il est vide (juste un README).

---

## 💻 PARTIE 2 — Récupérer le repo en local

### Étape 2 — Cloner le repo sur ta machine

```bash
git clone https://github.com/TON_USERNAME/ci-python-demo.git
cd ci-python-demo
```

> ✅ Tu as maintenant le dossier `ci-python-demo/` sur ton disque.

### Étape 3 — Créer la structure du projet

```bash
mkdir tests
mkdir -p .github/workflows
touch app.py
touch requirements.txt
touch tests/test_app.py
touch tests/__init__.py
touch .github/workflows/ci.yml
```

Vérification :

```bash
ls -R
```

Tu dois voir :

```
.github/
    workflows/
        ci.yml
app.py
requirements.txt
tests/
    __init__.py
    test_app.py
```

---

## 📝 PARTIE 3 — Écrire le code

### Étape 4 — Remplir les fichiers

**`app.py`**

```python
def sum(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Division par zéro interdite")
    return a / b
```

**`tests/test_app.py`**

```python
import pytest
from app import sum, divide

def test_sum_entiers():
    assert sum(1, 2) == 3

def test_sum_negatifs():
    assert sum(-1, -1) == -2

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_par_zero():
    with pytest.raises(ValueError, match="Division par zéro"):
        divide(10, 0)
```

**`requirements.txt`**

```
pytest==8.2.0
pytest-cov==5.0.0
```

**`.github/workflows/ci.yml`**

```yaml
name: CI - Qualité du code Python

on:
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Récupération du code
        uses: actions/checkout@v4

      - name: Installation de Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Installation des dépendances
        run: pip install -r requirements.txt

      - name: Lancement des tests + couverture
        run: pytest --cov=app --cov-report=term-missing

      - name: Vérification du seuil de couverture
        run: pytest --cov=app --cov-fail-under=80
```

---

## 🚀 PARTIE 4 — Premier push vers main

### Étape 5 — Pousser le code propre vers main

```bash
git add .
git commit -m "feat: ajout app.py, tests et pipeline CI"
git push origin main
```

> ✅ Le code est sur GitHub, branche `main`. Le pipeline **ne se déclenche pas encore** — il est configuré pour les Pull Requests uniquement.

---

## 🔒 PARTIE 5 — Protéger la branche main

### Étape 6 — Activer la protection de branche

Sur GitHub → ton repo → **Settings** → **Branches**

1. Cliquer **"Add branch protection rule"**
2. Dans "Branch name pattern" : taper `main`
3. Cocher :
    - ✅ **Require a pull request before merging**
    - ✅ **Require status checks to pass before merging**
    - ✅ Dans le champ qui apparaît, chercher et sélectionner **`test`**
    - ✅ **Require branches to be up to date before merging**
4. Cliquer **"Save changes"**

> ✅ Désormais, **personne ne peut pusher directement sur main**. Tout changement doit passer par une Pull Request **ET** les tests doivent passer.

---

## 🧨 PARTIE 6 — Simuler le bug (scénario pédagogique)

### Étape 7 — Créer une branche avec un bug volontaire

```bash
git checkout -b feature/calcul-ameliore
```

Modifier `app.py` — introduire le bug :

```python
def sum(a, b):
    return a - b  # 🐛 BUG VOLONTAIRE
```

Pousser la branche :

```bash
git add app.py
git commit -m "fix: amélioration du calcul (bugué)"
git push origin feature/calcul-ameliore
```

---

## 🔍 PARTIE 7 — Ouvrir une Pull Request et voir le refus

### Étape 8 — Créer la Pull Request

Sur GitHub → ton repo → tu vois la bannière jaune :

> _"feature/calcul-ameliore had recent pushes"_ → Cliquer **"Compare & pull request"**

Remplir :

|Champ|Valeur|
|---|---|
|Title|`fix: amélioration du calcul`|
|Base|`main`|
|Compare|`feature/calcul-ameliore`|

Cliquer **"Create pull request"**

---

### Étape 9 — Observer le pipeline s'exécuter ❌

Sur la page de la PR, descendre jusqu'à la section **"Checks"** :

```
❌ CI - Qualité du code Python / test (pull_request)
   → En cours...  puis  → Échec
```

Cliquer sur **"Details"** pour voir les logs :

```
FAILED tests/test_app.py::test_sum_entiers
FAILED tests/test_app.py::test_sum_negatifs

Expected: 3
Got: -1

2 failed, 2 passed in 0.45s
```

---

### Étape 10 — Constater le BLOCAGE du merge

En bas de la PR, le bouton **"Merge pull request"** est :

```
🔴 Merge pull request   ← GRISÉ, impossible à cliquer

⚠️  "Some checks were not successful"
⚠️  "test" — 2 tests failed
     This check is required before merging.
```

> 🎯 **Moment pédagogique clé ici.** Demander aux apprenants : _"Qu'est-ce qui se serait passé sans ce pipeline ?"_

---

## ✅ PARTIE 8 — Corriger et obtenir le merge autorisé

### Étape 11 — Corriger le bug en local

```bash
# Tu es toujours sur la branche feature/calcul-ameliore
```

Corriger `app.py` :

```python
def sum(a, b):
    return a + b  # ✅ Correction
```

Pousser la correction :

```bash
git add app.py
git commit -m "fix: correction du bug dans sum()"
git push origin feature/calcul-ameliore
```

---

### Étape 12 — Observer le pipeline repasser ✅

Sur la PR GitHub, la section "Checks" se met à jour automatiquement :

```
🟡 En cours...
✅ CI - Qualité du code Python / test — Passed
```

Logs visibles dans "Details" :

```
test_sum_entiers        PASSED
test_sum_negatifs       PASSED
test_divide_normal      PASSED
test_divide_par_zero    PASSED

4 passed in 0.43s
Coverage: 95%  ✅ (seuil: 80%)
```

---

### Étape 13 — Merger ✅

Le bouton est maintenant actif :

```
🟢  Merge pull request   ← CLIQUABLE

✅  "All checks have passed"
✅  test — Passed
```

1. Cliquer **"Merge pull request"**
2. Cliquer **"Confirm merge"**
3. Optionnel : **"Delete branch"**

> 🎉 Le code propre est sur `main`. Le code cassé ne l'a jamais atteint.

---

## 🗺️ Récapitulatif visuel du flux complet

```
[Local]                    [GitHub]
   |                           |
   |-- git push origin main -->|  (code propre initial)
   |                           |
   |-- git checkout -b bug --> |
   |-- git push origin bug --> |  (branche avec bug)
   |                           |
   |                    [Pull Request ouverte]
   |                           |
   |                    [Pipeline déclenché]
   |                           |
   |                    ❌ Tests échouent
   |                    🔴 Merge BLOQUÉ
   |                           |
   |-- correction -----------> |
   |-- git push ------------> |
   |                           |
   |                    ✅ Tests passent
   |                    🟢 Merge AUTORISÉ
   |                           |
   |                    [main protégé ✅]
```

---

## 🎓 Débrief final

|Question à poser|Ce qu'on veut entendre|
|---|---|
|Pourquoi pas pusher direct sur main ?|Personne ne relit, rien ne valide|
|Qui a décidé de bloquer ?|La règle de branche + le pipeline|
|Que se passe-t-il si on n'a pas de tests ?|Le pipeline passe… mais ne prouve rien|
|C'est quoi un quality gate ?|Une porte qui ne s'ouvre que sur conditions|