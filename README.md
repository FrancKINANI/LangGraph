# LangGraph

LangGraph est une bibliothèque open source visant à faciliter la création, l’orchestration et l’exécution de graphes de traitement pour des workflows NLP (Natural Language Processing) et IA. Elle met à disposition des outils pour composer des pipelines modulaires, réutilisables et extensibles, tout en gardant une grande flexibilité et simplicité d’utilisation.

## Fonctionnalités principales

- **Construction de graphes** : Assemblez facilement différentes étapes de traitement en graphes dirigés ou acycliques.
- **Nœuds modulaires** : Créez des nœuds réutilisables pour chaque tâche (prétraitement, analyse, génération, post-traitement, etc.).
- **Exécution flexible** : Exécutez vos graphes de façon séquentielle, parallèle ou conditionnelle.
- **Intégration IA/NLP** : Compatible avec les principaux frameworks de NLP et IA (Transformers, spaCy, NLTK, etc.).
- **Extensible** : Ajoutez vos propres modules, opérateurs ou stratégies d’exécution.

## Installation

```bash
git clone https://github.com/FrancKINANI/LangGraph.git
cd LangGraph
pip install -e .
```

Ou via PyPI (si disponible) :

```bash
pip install langgraph
```

## Exemple d’utilisation

Voici un exemple simple de pipeline de classification de texte :

```python
from langgraph import Graph, Node

def nettoyer(texte):
    return texte.lower()

def classifier(texte):
    # Dummy classifier
    return "positif" if "bien" in texte else "négatif"

# Création des nœuds
noeud_nettoyage = Node(func=nettoyer)
noeud_classification = Node(func=classifier)

# Construction du graphe
graphe = Graph()
graphe.add_node("nettoyage", noeud_nettoyage)
graphe.add_node("classification", noeud_classification)
graphe.add_edge("nettoyage", "classification")

# Exécution
resultat = graphe.run("Ceci est BIEN !")
print(resultat)  # Affiche: positif
```

## Documentation

- [Guide de démarrage](docs/getting_started.md)
- [API Reference](docs/api_reference.md)
- [Exemples avancés](docs/examples/)

## Contribution

Les contributions sont les bienvenues ! Merci de lire le [guide de contribution](CONTRIBUTING.md) avant de soumettre une pull request.

1. Forkez le repo
2. Créez une branche (`git checkout -b feature/ma-nouvelle-fonction`)
3. Commitez vos changements (`git commit -am 'Ajoute une nouvelle fonction'`)
4. Poussez la branche (`git push origin feature/ma-nouvelle-fonction`)
5. Ouvrez une Pull Request

## Licence

Ce projet est sous licence MIT – voir le fichier [LICENSE](LICENSE) pour plus d’informations.

---

© 2025 FrancKINANI
