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

const updateCompanyInfo = async (data) => {
  try {
    const token = localStorage.getItem('userToken');
    
    if (!token) {
      throw new Error('Token non trouvé');
    }

    const response = await api.put('/account/firm/profile/', data, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });

    return response.data;
  } catch (error) {
    console.error("Erreur lors de la mise à jour:", error);
    throw error;
  }
};

export { fetchMyPersonalInfo, updateCompanyInfo };