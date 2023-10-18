#!/bin/bash

# Vérifier si Git est installé
if ! command -v git &> /dev/null; then
  echo "Git n'est pas installé sur ce système. Veuillez installer Git."
  exit 1
fi

# Ajouter tous les fichiers modifiés
git add .

# Demander un message de commit à l'utilisateur
read -p "Entrez le message de commit : " commit_message

# Effectuer le commit
git commit -m "$commit_message"

# Pousser les modifications vers le référentiel distant
git push

echo "Les modifications ont été ajoutées, commises et poussées avec succès."

# Sortir du script
exit 0

