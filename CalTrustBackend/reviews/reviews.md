├── companies ├── models.py ├── review.py ├── user

├── avis
    ├── un client (user)
    ├── une entreprise (firm)
    ├── une date de publication
    ├── une note
    ├── Un commentaire
    ├── Une vérification
    ├── Utilité (Un nombre de personnes qui ont trouvé ça utile)

Par défaut les avis ne sont pas vérifiés !!!

Pour trouver un avis utile on doit avoir un compte.

Un avis qu'est ce qu'il attend?

``` json
POST http://127.0.0.1:8000/reviews/firms/7/
Content-Type: application/json
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU0NTIzNDk5LCJpYXQiOjE3NTQ1MTk4OTksImp0aSI6ImI0ZGQ2Y2FjZTkwZTQ5ZmI5NDEyNmQxNTgxODc5MTU2IiwidXNlcl9pZCI6MTJ9.yP5RQBPrqoYzRVr1L70grK9LekJstvnG3nnXBV3JEtQ

{
  "rating": 4,
  "comment": "Service Exelent, je recommande ils ont fait mon site en moins d'une semaine"
}
```

D'abord le endpoint contient l'id de la firm (FirmProfile),

``` python

# reviews/views.py
from django.db.models import Avg

def firm_detail(request, firm_name):
    firm = get_object_or_404(FirmProfile, name=firm_name)
    
    # Calcul de la note moyenne
    average_rating = Review.objects.filter(firm=firm).aggregate(
        Avg('rating')
    )['rating__avg'] or 0
    
    context = {
        'firm': firm,
        'average_rating': round(average_rating, 1),
    }
    return render(request, 'firm_detail.html', context)

```