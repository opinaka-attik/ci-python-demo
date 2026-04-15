
## 1. Le Pipeline comme Objet Central — Vocabulaire Unifié

### 🧠 Concept : avant de coder un pipeline, maîtriser son vocabulaire

Chaque outil CI/CD (GitHub Actions, GitLab CI, Jenkins) utilise des termes légèrement différents pour les mêmes concepts. Ce vocabulaire est le **métalangage du cours** — il faut le maîtriser indépendamment de l'outil. [dev](https://dev.to/hongster85/cicd-pipelines-understand-in-3-minutes-2g7g)

```
ANATOMIE D'UN PIPELINE CI/CD

  TRIGGER  (déclencheur)
  ─────────────────────
  L'événement qui lance le pipeline.
  Exemples :
    → push sur une branche
    → création d'une Pull Request
    → tag Git (v1.2.0)
    → schedule (cron : tous les jours à 2h)
    → déclenchement manuel
    → API webhook externe

       │
       │ déclenche
       ▼

  PIPELINE  (le workflow complet)
  ───────────────────────────────
  L'ensemble de l'automatisation déclenchée par un trigger.
  = La séquence de stages et de jobs à exécuter.
  Représenté par un fichier YAML versionné dans le repo.

       │
       │ composé de
       ▼

  STAGES  (les étapes ordonnées)
  ──────────────────────────────
  Les grandes phases du pipeline, exécutées dans l'ordre.
  Exemple standard :
    STAGE 1 : validate   (lint, format, sécurité)
    STAGE 2 : build      (compilation, transpilation)
    STAGE 3 : test       (unit, integration, e2e)
    STAGE 4 : package    (Docker image, jar, zip)
    STAGE 5 : deploy     (staging → production)

  Règle : un stage suivant ne démarre QUE si le précédent réussit.

       │
       │ composés de
       ▼

  JOBS  (les unités d'exécution)
  ──────────────────────────────
  Chaque stage contient un ou plusieurs jobs.
  Les jobs d'un MÊME stage s'exécutent en PARALLÈLE.
  Les jobs de stages DIFFÉRENTS s'exécutent en SÉQUENCE.

  Exemple (stage "test") :
    JOB 1 : unit-tests          ─┐
    JOB 2 : integration-tests   ─┤ parallèles
    JOB 3 : e2e-tests           ─┘

       │
       │ composés de
       ▼

  STEPS  (les commandes individuelles)
  ─────────────────────────────────────
  Chaque job est une liste de steps — des commandes exécutées
  séquentiellement dans le même environnement.

  Exemple (job "unit-tests") :
    STEP 1 : checkout du code
    STEP 2 : installer Node.js 20
    STEP 3 : npm ci
    STEP 4 : npm run test:unit
    STEP 5 : publier le rapport de couverture

       │
       ▼

  RUNNER  (l'environnement d'exécution)
  ─────────────────────────────────────
  La machine (VM, container) qui exécute les jobs.
  Types :
    → Hosted runner   : machine fournie par GitHub/GitLab (ubuntu-latest)
    → Self-hosted runner : votre propre serveur ou VM

  ARTEFACT  (le livrable du pipeline)
  ────────────────────────────────────
  Un fichier produit par le pipeline et transmis entre jobs
  ou conservé à la fin.
  Exemples :
    → Image Docker
    → Fichier .jar ou .zip
    → Rapport de tests (JUnit XML)
    → Rapport de couverture (LCOV)
    → Binary compilé
```

### 📋 Correspondance vocabulaire — GitHub Actions vs GitLab CI vs Jenkins

| Concept | GitHub Actions | GitLab CI | Jenkins |
|---|---|---|---|
| Fichier de config | `.github/workflows/*.yml` | `.gitlab-ci.yml` | `Jenkinsfile` |
| Pipeline complet | `workflow` | `pipeline` | `pipeline` |
| Étape ordonnée | — (implicite via `needs:`) | `stage` | `stage` |
| Unité d'exécution | `job` | `job` | `stage` / `step` |
| Commande individuelle | `step` | `script` | `step` |
| Machine d'exécution | `runner` | `runner` | `agent` / `node` |
| Déclencheur | `on:` | `only:` / `rules:` | `triggers {}` |
| Variable secrète | `secrets.NOM` | `$CI_NOM` ou variable protégée | `credentials('id')` |
| Livrable | `artifact` | `artifact` | `archiveArtifacts` |

***

## 2. Les Outils du Marché en 2026 — Positionnement

### 🧠 Concept : chaque outil occupe un espace précis — choisir selon le contexte

Il n'y a pas de "meilleur outil CI/CD" absolu. Le bon choix dépend de : la plateforme Git utilisée, les contraintes d'hébergement (cloud vs on-premise), la taille de l'équipe, et les compétences disponibles. [scribd](https://www.scribd.com/document/789901677/Comparison)

```
CARTOGRAPHIE DES OUTILS CI/CD EN 2026

  CLOUD / HÉBERGÉ                           SELF-HOSTED / ON-PREMISE
  ──────────────────                         ─────────────────────────

  GitHub Actions          ◄──────────────── Jenkins
  [hébergé par GitHub]                       [open-source, votre infra]
  → 68% adoption open-source en 2025         → 1800+ plugins
  → Gratuit jusqu'à 2000 min/mois            → Contrôle total
  → Marketplace de 20 000+ actions           → Courbe d'apprentissage steep
  → Idéal : startups, open-source,           → Idéal : grands comptes,
             équipes GitHub-first              systèmes legacy, multi-VCS

  GitLab CI               ◄──────────────── GitLab CI (self-hosted)
  [intégré à GitLab.com]                     [GitLab Community Edition]
  → Plateforme DevOps complète               → Même fonctionnalités
  → Registry, board, wiki intégrés           → Hébergé chez vous
  → Idéal : équipes DevOps complètes         → Idéal : secteur bancaire,
             projets GitLab-first              santé, administration

  CircleCI                                   Drone CI
  [cloud-first, performant]                  [léger, Docker-native]
  → Configuration fine du cache              → Idéal : petites équipes
  → Bonne performance sur gros pipelines     → Config simple

  ArgoCD                                     Tekton
  [GitOps pour Kubernetes]                   [Kubernetes-native CI/CD]
  → Synchronise Git → K8s cluster            → Idéal : infra K8s avancée
  → Idéal : déploiement K8s continu          → Plus complexe à setup
```

### 📋 Guide de choix rapide

| Situation | Outil recommandé | Raison |
|---|---|---|
| Projet GitHub, petite équipe | **GitHub Actions** | Zéro setup, intégré, gratuit |
| Équipe full DevOps, monorepo | **GitLab CI** | Plateforme complète en un seul outil |
| Grande entreprise, multi-VCS | **Jenkins** | Flexibilité maximale, plugins métier |
| Contraintes cloud très strictes | **GitLab CE self-hosted** | Données sur votre infra |
| Déploiement continu sur K8s | **ArgoCD + GitHub Actions** | GitOps natif |
| Performance et cache agressif | **CircleCI** | Optimisé pour la vitesse |

> 💡 **Pour ce cours** : nous utilisons **GitHub Actions** comme outil principal (syntaxe moderne, adoption massive, runners gratuits) et **GitLab CI** + **Jenkins** en Partie 9 pour la comparaison. La logique apprise sur l'un se transfère directement aux autres — seule la syntaxe change.

***

## 3. Observer un Pipeline Existant — Atelier Pratique

### 🧠 Objectif : apprendre à lire un pipeline avant d'en écrire un

Avant d'écrire la moindre ligne de YAML, l'exercice fondamental est de **décortiquer un pipeline existant** — identifier chaque composant dans l'interface GitHub Actions, comprendre son exécution, son temps, ses artefacts.

### 💻 Illustration — Anatomie d'un workflow GitHub Actions réel

```yaml
# .github/workflows/ci.yml
# ← Ce fichier est dans le repo — c'est le pipeline "à lire" pour l'atelier

# ═══════════════════════════════════════════════════════════════
# TRIGGER — Qu'est-ce qui déclenche ce pipeline ?
# ═══════════════════════════════════════════════════════════════
on:
  push:
    branches: [main, develop]        # ← sur chaque push vers main ou develop
  pull_request:
    branches: [main]                 # ← sur chaque PR ciblant main
  workflow_dispatch:                 # ← déclenchement manuel possible (bouton UI)

# ═══════════════════════════════════════════════════════════════
# VARIABLES GLOBALES — accessibles dans tous les jobs
# ═══════════════════════════════════════════════════════════════
env:
  NODE_VERSION: '20'
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}    # ex: monorg/monapp

# ═══════════════════════════════════════════════════════════════
# PIPELINE — Liste des jobs
# ═══════════════════════════════════════════════════════════════
jobs:

  # ─────────────────────────────────────────────
  # JOB 1 — validate (Stage : Validation)
  # Lint + sécurité — rapide, bloquant
  # ─────────────────────────────────────────────
  validate:
    name: ✅ Validation & Lint
    runs-on: ubuntu-latest            # ← RUNNER : machine fournie par GitHub

    steps:
      - name: 📥 Checkout du code
        uses: actions/checkout@v4     # ← ACTION du Marketplace (checkout = step standard)

      - name: 🟢 Setup Node.js ${{ env.NODE_VERSION }}
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'                # ← CACHE : accélère les runs suivants

      - name: 📦 Installer les dépendances
        run: npm ci                   # ← STEP : commande shell

      - name: 🔍 Lint ESLint
        run: npm run lint

      - name: 🎨 Vérifier le formatage Prettier
        run: npm run format:check

      - name: 🔐 Audit des dépendances
        run: npm audit --audit-level=high   # ← fail si vulnérabilité HIGH ou CRITICAL

  # ─────────────────────────────────────────────
  # JOB 2 — test (Stage : Tests)
  # Dépend de "validate" → ne démarre que si validate ✅
  # ─────────────────────────────────────────────
  test:
    name: 🧪 Tests Automatisés
    runs-on: ubuntu-latest
    needs: validate                   # ← DÉPENDANCE : attend validate

    # Services Docker disponibles DANS ce job
    services:
      postgres:
        image: postgres:16-alpine
        env:
          POSTGRES_DB:       testdb
          POSTGRES_USER:     testuser
          POSTGRES_PASSWORD: testpass
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432

    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '${{ env.NODE_VERSION }}', cache: 'npm' }
      - run: npm ci

      - name: 🧪 Tests unitaires
        run: npm run test:unit -- --coverage

      - name: 🔗 Tests d'intégration
        run: npm run test:integration
        env:
          DB_HOST: localhost
          DB_PORT: 5432
          DB_USER: testuser
          DB_PASS: testpass
          DB_NAME: testdb

      - name: 📊 Publier le rapport de couverture
        uses: actions/upload-artifact@v4   # ← ARTEFACT : fichier conservé
        with:
          name: coverage-report
          path: coverage/
          retention-days: 7

  # ─────────────────────────────────────────────
  # JOB 3 — build (Stage : Build)
  # Construit l'image Docker
  # ─────────────────────────────────────────────
  build:
    name: 🐳 Build Docker Image
    runs-on: ubuntu-latest
    needs: test                       # ← attend que les tests passent

    permissions:
      contents: read
      packages: write                 # ← permission pour pousser sur ghcr.io

    steps:
      - uses: actions/checkout@v4

      - name: 🔐 Login au registry GitHub
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}   # ← SECRET automatique GitHub

      - name: 🏷️ Extraire les métadonnées Docker
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=sha,prefix=sha-         # tag avec le SHA du commit
            type=ref,event=branch        # tag avec le nom de la branche
            type=semver,pattern={{version}} # tag avec la version SemVer si c'est un tag

      - name: 🐳 Build et Push de l'image
        uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          tags:   ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha              # ← CACHE Docker layers
          cache-to:   type=gha,mode=max

      - name: 📦 Exporter le digest de l'image
        uses: actions/upload-artifact@v4
        with:
          name: docker-digest
          path: |
            ${{ steps.meta.outputs.tags }}

  # ─────────────────────────────────────────────
  # JOB 4 — deploy-staging (Stage : Déploiement)
  # Déploie sur le serveur de staging
  # Seulement sur la branche main
  # ─────────────────────────────────────────────
  deploy-staging:
    name: 🚀 Déploiement Staging
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main'   # ← CONDITION : seulement sur main

    environment:                           # ← ENVIRONMENT GitHub : suivi + approbation
      name: staging
      url: https://staging.monapp.fr

    steps:
      - name: 🚀 Déployer sur le serveur staging
        uses: appleboy/ssh-action@v1
        with:
          host:     ${{ secrets.STAGING_HOST }}    # ← SECRET : IP du serveur
          username: ${{ secrets.STAGING_USER }}
          key:      ${{ secrets.STAGING_SSH_KEY }}
          script: |
            cd /opt/monapp
            docker compose pull
            docker compose up -d --remove-orphans
            docker compose exec app node scripts/migrate.js

      - name: 🩺 Smoke test staging
        run: |
          sleep 15
          curl -f https://staging.monapp.fr/health || exit 1
          echo "✅ Staging opérationnel"
```
