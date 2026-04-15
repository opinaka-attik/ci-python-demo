

```bash

attik@opinaka:/mnt/c/ci-python-demo$ git push
Username for 'https://github.com': opinaka-attik
Password for 'https://opinaka-attik@github.com': 
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 20 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 322 bytes | 14.00 KiB/s, done.
Total 4 (delta 1), reused 1 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote: error: GH013: Repository rule violations found for refs/heads/main.
remote: Review all repository rules at https://github.com/opinaka-attik/ci-python-demo/rules?ref=refs%2Fheads%2Fmain
remote:
remote: - Changes must be made through a pull request.
remote:
remote: - Required status check "test (3.10)" is expected.
remote:
To https://github.com/opinaka-attik/ci-python-demo.git
 ! [remote rejected] main -> main (push declined due to repository rule violations)
error: failed to push some refs to 'https://github.com/opinaka-attik/ci-python-demo.git'
```

----

 Le message veut dire que **ton dépôt GitHub refuse ton `git push` direct sur la branche `main`**. Ce n’est pas une erreur technique de Git, mais une **règle de sécurité/configuration du dépôt**.

Voici ce qui se passe 👇

### 🚫 1. Push direct interdit

```
Changes must be made through a pull request.
```

👉 Tu n’as pas le droit de pousser directement sur `main`.  
➡️ Tu dois passer par une **Pull Request (PR)**.

---

### 🧪 2. Test obligatoire

```
Required status check "test (3.10)" is expected.
```

👉 Il y a un **test automatique (CI)** qui doit passer avant de pouvoir merger.

---

## ✅ Solution étape par étape

### 1. Créer une branche

```bash
git checkout -b ma-branche
```

### 2. Pousser ta branche

```bash
git push origin ma-branche
```

### 3. Créer une Pull Request sur GitHub

- Va sur ton repo
    
- Clique sur **"Compare & pull request"**
    
- Crée la PR vers `main`
    

### 4. Attendre les tests

👉 GitHub va lancer le test `"test (3.10)"`

- ✅ S’il passe → tu peux merger
    
- ❌ S’il échoue → tu dois corriger
    

---

```bash
attik@opinaka:/mnt/c/keyce-tmp/ci-python-demo$ git checkout -b ma-branche
Switched to a new branch 'ma-branche'
attik@opinaka:/mnt/c/ci-python-demo$ git push origin ma-branche
Username for 'https://github.com': opinaka-attik
Password for 'https://opinaka-attik@github.com': 
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 20 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 322 bytes | 10.00 KiB/s, done.
Total 4 (delta 1), reused 1 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote:
remote: Create a pull request for 'ma-branche' on GitHub by visiting:
remote:      https://github.com/opinaka-attik/ci-python-demo/pull/new/ma-branche
remote:
To https://github.com/opinaka-attik/ci-python-demo.git
 * [new branch]      ma-branche -> ma-branche

```