import api from "./_authservices";

const fetchRecentsReviews = async () => {
    try {
        const response = await api.get('/reviews/public/recent/', {
            headers: { 'Content-Type': 'application/json' }
        });
        return response; // Retournez toute la réponse
    } catch (error) {
        console.error("Fetch error", error);
        throw error; // Propagez l'erreur
    }
}

export { fetchRecentsReviews }; // Exportez avec le bon nom