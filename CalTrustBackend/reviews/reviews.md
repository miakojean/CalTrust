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