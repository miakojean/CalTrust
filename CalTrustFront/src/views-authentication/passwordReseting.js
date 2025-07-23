import api from "@/_services/_authservices";


const passwordReset = async (data) => {
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

const verifyToken = async (token) => {
  try {
    const response = await fetch('/api/password-reset/verify-token/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ token })
    });
    
    const data = await response.json();
    return data.valid ? data : { valid: false, message: "Erreur de vérification" };
    
  } catch (error) {
    return { valid: false, message: "Erreur réseau" };
  }
};


export {passwordReset, verifyToken}; 