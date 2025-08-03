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

const fetchRecentsFirms = async () => {
    try {
        const response = await api.get('/companies/', {
            headers:{'Content-Type':'application/json'}
        });

        if (!response.data){
            throw new Error('Réponse vide de l\'api');
        }

        return response.data
    } catch (error) {
        console.error("Erreur lors de la récuppération des entreprises",error);
        throw new Error(`Impossible de charger les avis: ${error.message}`);
    }
}

async function postAReviews(){
    const accessToken = localStorage.getItem('userToken');
    const refreshToken = localStorage.getItem('userTokenRefresh');

    // Si l'un des tokens manque, on nettoie et on arrête
    if (!refreshToken || !accessToken) {
        console.error("Tokens manquants pour la déconnexion.");
        localStorage.clear(); // Nettoyage par sécurité
        // Mettez à jour votre UI ici (ex: isLoggedIn.value = false)
        return;
    }

    try {
        const requestBody = {
            refresh: refreshToken
        }
    } catch (erro) {
        console.log("Echec de la déconnexion côté serveur")
    }
}

export {fetchRecentsReviews, fetchRecentsFirms};