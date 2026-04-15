

Git te demande login + mot de passe à chaque fois parce que tu utilises **HTTPS sans stockage d’identifiants**.

---

## ✅ Solution 1 (recommandée) : utiliser un **token + stockage**

### 1. Créer un token GitHub

* Va sur : [https://github.com/settings/tokens](https://github.com/settings/tokens)
* Clique sur **"Generate new token (classic)"**
* Coche :

  * `repo`
* Génère le token

👉 ⚠️ Copie-le tout de suite (tu ne pourras plus le revoir)

---

### 2. Utiliser le token comme mot de passe

Quand Git te demande :

```bash
Username: opinaka-attik
Password: 👉 colle ton TOKEN (pas ton mot de passe GitHub)
```

---

### 3. Sauvegarder pour ne plus le retaper

```bash
git config --global credential.helper store
```

👉 La prochaine fois, il ne te demandera plus rien 👍

---

## ✅ Solution 2 (meilleure long terme) : passer en **SSH 🔐**

👉 Comme ça = plus jamais de login/password

### Étapes :

### 1. Générer une clé SSH

```bash
ssh-keygen -t ed25519 -C "ton-email@example.com"
```

(entrée → entrée → entrée)

---

### 2. Copier la clé

```bash
cat ~/.ssh/id_ed25519.pub
```

---

### 3. Ajouter sur GitHub

Va ici :
[https://github.com/settings/keys](https://github.com/settings/keys)
👉 "New SSH key" → colle la clé

---

### 4. Changer l’URL du repo

```bash
git remote set-url origin git@github.com:opinaka-attik/ci-python-demo.git
```

---

### 5. Tester

```bash
git push
```

👉 Plus de mot de passe 🎉

---
