# Arithmetic Formatter

## 📚 Description

Ce projet consiste à créer une fonction Python `arithmetic_arranger` qui met en forme des opérations arithmétiques élémentaires (addition et soustraction) de façon verticale, comme dans les cahiers d’école. Il est possible d'afficher en option le résultat de chaque opération.

Ce projet est idéal pour débuter avec la manipulation de chaînes de caractères et la mise en forme conditionnelle.

---

## 🧠 Fonctionnalités

- ✅ Aligne verticalement des opérations de type `a + b` ou `a - b`
- ✅ Supporte jusqu’à **5 opérations maximum**
- ✅ Vérifie la **validité des opérateurs et des opérandes**
- ✅ Option d’affichage des résultats
- ✅ Formatage esthétique avec alignement et espacement

---

## 🚫 Règles et erreurs gérées

- ❌ Plus de 5 problèmes → `"Error: Too many problems."`
- ❌ Opérateur autre que `+` ou `-` → `"Error: Operator must be '+' or '-'."`
- ❌ Caractères non numériques → `"Error: Numbers must only contain digits."`
- ❌ Opérandes de plus de 4 chiffres → `"Error: Numbers cannot be more than four digits."`

---

## 🧪 Exemples d'utilisation

```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
