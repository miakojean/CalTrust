import api from "@/_services/_authservices";

/* 

    Ici ce le service consacré à une entreprise spécifique, raison pour laquelle firm est passée en paramètre
    Tout y est, en ce qui concerne les calculs on va les gérer après !!!

*/

const fetchRecentsFirms = async (firms) => {
    try {
        const response = await api.get(`/companies/${firms}`, {
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