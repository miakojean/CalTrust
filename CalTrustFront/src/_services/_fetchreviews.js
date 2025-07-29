import api from "./_authservices";

const fetchRecentsReviews = async () => {
    try {
        const response = await api.get('/reviews/public/recent/', {
            headers: { 'Content-Type': 'application/json' }
        });
        
        if (!response.data) {
            throw new Error('Réponse vide de l\'API');
        }
        
        return response.data;
        
    } catch (error) {
        console.error("Erreur lors de la récupération des avis:", error);
        throw new Error(`Impossible de charger les avis: ${error.message}`);
    }
}

export {fetchRecentsReviews};