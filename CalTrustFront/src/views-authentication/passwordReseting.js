import api from "@/_services/_authservices";


const passwordReseting = async (data) => {
  try {
    const response = await api.post('/account/password-reseting/', data, {
      headers: { 'Content-Type': 'application/json' }
    });
    return response.status === 200;  // Adaptez au code retour réel de votre API
  } catch (error) {
    console.error("Reset error:", error);
    return false;
  }
};

export default passwordReseting
