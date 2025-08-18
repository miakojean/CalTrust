import api from "@/_services/_authservices";
/*
    On va chercher à: {
        - Obtenir "Mes informations" une fois connecté
        - Modifier "Mes informations"
    }
*/

const fetchMyPersonalInfo = async () => {
  try {
    const token = localStorage.getItem('userToken');
    console.log("Token utilisé:", token) // Vérifiez le token
    
    const response = await api.get('/account/firm/profile/', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });
    
    console.log("Réponse brute de l'API:", response) // Vérifiez la réponse complète
    return response.data;
    
  } catch (error) {
    console.error("Erreur complète:", error);
    console.error("Réponse d'erreur:", error.response?.data);
    throw error;
  }
};

export {fetchMyPersonalInfo}