## Sommaire
- [Gestion de la navbar](#gestion-de-la-navbar)
- [Création d'un contenu](#création-dun-contenu)
    - [Les cartes](#les-cartes)

---

### Gestion de la navbar

La gestion de la navbar est un élément clé de la conception de votre site web. Vous pouvez personnaliser la navbar de différentes manières, y compris la création de liens de navigation, de menus déroulants, et d'autres fonctionnalités pour faciliter la navigation de vos utilisateurs.

Une navbar se crée comme ceci : navbar_content = [{ item1 },{ item2 },{ item3 }]   
Pour la customisation, il existe plusieurs type de navbar :
- dropdown
```python
{
    "type": "dropdown",
    "class": "nav-link dropdown-toggle",
    "text": "Texte du dropdown",
    "items": [
        {"class": "dropdown-item", "text": "Sous-menu 1", "href": "#"},
        {"class": "dropdown-item", "text": "Sous-menu 2", "href": "#"},
    ],
}
```
- nav-link
```python
{
    "type": "nav-link",
    "class": "nav-item",
    "text": "Texte",
}
```
- search # une barre de recherche
```python
{
    "type": "search"
}
```
- text 
```python
{
    "type": "text",
    "text": "Texte"
}
```
- button 
```python
{
    "type": "button",
    "class": "btn btn-danger",
    "text": "Autre menu",
    "onclick": "alert('ooo')",
}
```


---

### Création d'un contenu
#### Les cartes

 Le contenu principal de la "card" peut inclure du texte descriptif, des images, des graphiques, ou toute autre information pertinente. Il s'agit de l'élément principal que l'utilisateur verra en premier.

```python
cards = [
    {
        "color": "#215577",
        "title": "Titre de la cartes",
        "text": "Text qui seras dans la carte",
        "button": "true",#true si vous avez besoin d'un bouton et false si vous n'en vouler pas 
        "button_text": "Go",
        "href": "chemin vers votre page",
    },
    # Ajoutez d'autres cartes avec des données similaires
]
```

Le texte peu meme etre un code html :
```python
progress_bar = f'''
        <div class="progress">
            <div class="progress-bar" role="progressbar" style="width: 50%; background-color: #f9d852;"
                aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
                <span class="sr-only">50%</span>
            </div>
        </div>
    '''
```
