import api from "@/_services/_authservices";
/*
  On va chercher à: {
    - Obtenir "Mes informations" une fois connecté
    - Modifier "Mes informations"
    - Obtenir mes notifications
    - Les marquer comme lues
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

// We have two profiles that we have to manage: User and Firm
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

const updateOtherCompanyField = async (data) => {
  
  const token = localStorage.getItem('userToken');
  try {
    console.log("Données envoyées pour la mise à jour:", data);
    const result = await api.put('/companies/my-company/', data, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });
    console.log("Réponse de l'API après mise à jour:", result);
    return result.data;
  } catch (error) {
    console.error("Erreur lors de la mise à jour:", error);
    throw error;
  }
}

const getMyNotifications = async() => {
  try {
    const token = localStorage.getItem('userToken');

    if(!token) {
      throw new Error('Token non trouvé');
    }

    const response = await api.get('/core/notifications/',{
      headers:{'Authorization': `Bearer ${token}`}
    })

    return response.data
  } catch (error) {
    console.error("Erreur lors de la réccupération des notifications", error)
    throw error;
  }

}

const markNotificationsAsRead = async(notificationId) => {
  try{
    const token = localStorage.getItem('userToken');

    if(!token) {
      throw new Error('Token non trouvé');
    }

    // Correction : ajout du body et de la méthode PATCH correcte
    const response = await api.patch(`/core/notifications/${notificationId}/`, {
      is_read: true
    }, {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    });

    return response.data;
  } catch (error) {
    console.log("Erreur lors du marquage de la notification comme lue", error);
    throw error;
  }
}

const markAllNotificationsAsRead = async() =>{
  try {
    const token = localStorage.getItem('userToken');

    if(!token) {
      throw new Error('Token non trouvé');
    }

    const response = await api.post('/core/notifications/actions/', {
      action: "mark_all_read"
    }, {
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    });

    return response.data;
  } catch (error) {
    console.error("Erreur lors du marquage de toutes les notifications comme lues", error);
    throw error;
  }
}

export { fetchMyPersonalInfo, 
  updateCompanyInfo, 
  getMyNotifications,
  updateOtherCompanyField, 
  markNotificationsAsRead, 
  markAllNotificationsAsRead };