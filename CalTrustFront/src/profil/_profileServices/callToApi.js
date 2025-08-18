import api from "@/_services/_authservices";
/*
    On va chercher à: {
        - Obtenir "Mes informations" une fois connecté
        - Modifier "Mes informations"
    }
*/

const fetchMyPersonalInfo = async () => {
    try {
        // Récupérer le token depuis le stockage local (ou autre méthode)
        const token = localStorage.getItem('userToken'); // ou sessionStorage, cookies, etc.

        if (!token) {
            throw new Error('Token non trouvé, veuillez vous reconnecter');
        }

        const response = await api.get('/account/firm/profile/', {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}` // Ajout du header d'autorisation
            }
        });

        if (!response.data) { // Correction: response.data au lieu de response.date
            throw new Error('Réponse vide de l\'API');
        }

        return response.data;
    } catch (error) {
        console.error("Erreur lors de la récupération des informations:", error.message);
        throw error; // Il est préférable de propager l'erreur originale
    }
};

export {fetchMyPersonalInfo}