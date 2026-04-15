


````bash
attik@opinaka:/mnt/c$ git clone https://github.com/opinaka-attik/ci-python-demo.git

# ajouter un fichier markdown ou modifier le contenu de README.md

attik@opinaka:/mnt/c/ci-python-demo$ git add .

attik@opinaka:/mnt/c/ci-python-demo$ git commit -m "v2"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: empty ident name (for <attik@opinaka.localdomain>) not allowed

---

attik@opinaka:/mnt/c/
ci-python-demo$ git config --global user.email mohammed.attik@opinaka.com
attik@opinaka:/mnt/c/ci-python-demo$ git config --global user.name opinaka-attik
attik@opinaka:/mnt/c/ci-python-demo$ git commit -m "v2"   
[main 4878258] v2
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 docs/02.md

---

attik@opinaka:/mnt/ci-python-demo$

```