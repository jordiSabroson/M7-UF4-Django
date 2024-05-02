# DJANGO

## PRÀCTICA 2 - BASE DE DADES/MODEL

**1. BASES DE DADES**
   1. Trieu el tipus de bases de dades que vulgueu utilitzar en aquesta pràctica.
   2. Haureu de crear una bases de dades amb el nom iticBCN
   3. Haureu de crear mínim una taula
      1. usuari: id, nom , cognom, assignatures, rol.
      2. En el cas de ser professor haurem de saber les assignatures que està impartint.
   4. Fer servir mínim una taula relacional per gestionar els rols i relacionar-ho amb la taula usuari. **(1 punt)**
      1. Taula rol: id, nom.     Ex: 1, professor
   
**2. CRUD**

A partir de la pràctica anterior on feiem servir fakedata, haurem de fer els canvis necessaris per crear un CRUD de professors i estudiants que utilitzi  les bases de dades definida en l’apartat anterior.

Feu els canvis necessaris en l’aplicació per gestionar un crud per professors i alumnes:
- READ (2 punts)
- CREATE (3 punts)
- UPDATE (3 PUNTS)
- DELETE (1 PUNT)

Cada vegada que es fa un create, update o delete les dades que apareixin a la vista després del CRUD estaran actualitzades.

Les pàgines de formularis s’han de crear amb el forms.py (segons explicació diapositives de form)
