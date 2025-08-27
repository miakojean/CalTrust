import api from "@/_services/_authservices";

/* 
 Ici l'idée est de mettre à jour les informations du modèle:
 -  FirmProfile
 -  CustomerProfile
 */

const updateFirmProfile = async (data) => {
    try {
        const token = localStorage.getItem('userToken');
        
        if(!token){
            throw new Error('Token non trouvé');
        }

        const response = await api.put('/account/firm/profile/', data, {
            headers: { 
                'Authorization': `Bearer ${token}`,
            }}
        );
        
        return response.data;
        
    } catch (error) {
        console.error("Erreur lors de la mise à jour des informations de l'entreprise:", error);
        throw new Error(`Impossible de mettre à jour les informations: ${error.message}`);
    }
}

export { updateFirmProfile };