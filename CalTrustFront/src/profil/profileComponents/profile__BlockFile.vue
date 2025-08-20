<template>
    <div class="profile__container">
        <h4>{{ title }}</h4>
        <p>{{ description }}</p>

        <div class="divider"></div>

        
        <profile__fileUpload
            v-for="(i, index) in fields"
            :key="index"
            accept="image/*,.pdf"
            :maxSize="5 * 1024 * 1024" 
            :label="i.label"
            :isPDF="isPDF"
        />

    </div>
</template>

<script>
import stepper from '@/components/cards/stepper.vue';
import profile__fileUpload from './profile__fileUpload.vue';
import { updateCompanyInfo } from '../_profileServices/callToApi';

export default {

    components:{
        stepper,
        profile__fileUpload
    },

    props:{
        title:{
            type:String,
            default:'Informations de base'
        },
        description:{ 
            /* This is description of the block */
            type:String,
            default:'Cette section présente les différentes information de base de votre entreprise '
        },
        fields: {
            type: Array,
            default: () => [
                { label: 'Registre de commerce', value: "Caladrius" },
                { label: 'Registre fiscal', value: "Caladrius" },
            ]
        },

        DescriptionValue:{
            /* This is description of the fields */
            type:String
        },

        uploadFileTitle:{
          type: String,
          default: 'Télécharger un fichier'
        },
        isPDF: {
          type: Boolean,
          default: true
        }
    },

    setup(props, { emit }) {
    
    const handleUpdateField = async (updateData) => {
      try {
        console.log('Mise à jour:', updateData);
        
        // Préparer les données pour l'API
        const apiData = {};
        
        // Mapping des champs (ajuster selon votre API)
        const fieldMapping = {
          'Nom de l\'entreprise': 'company_name',
          'Adresse': 'address',
          'Email': 'email',
          'Téléphone': 'phone_number',
          'Website': 'website'
          // Ajoutez d'autres mappings au besoin
        };
        
        const apiFieldName = fieldMapping[updateData.field];
        if (apiFieldName) {
          apiData[apiFieldName] = updateData.value;
          
          // Appel API
          const response = await updateCompanyInfo(apiData);
          console.log('Mise à jour réussie:', response);
          
          // Émettre un événement pour informer le parent
          emit('field-updated', {
            field: updateData.field,
            value: updateData.value,
            success: true
          });
        }
      } catch (error) {
        console.error('Erreur mise à jour:', error);
        emit('field-updated', {
          field: updateData.field,
          value: updateData.value,
          success: false,
          error: error.message
        });
      }
    };

    return {
      handleUpdateField
    };
  }
}
</script>

<style scoped>
.profile__container{
    display: flex;
    flex-direction: column;
    justify-content: start;
    gap: 0.5rem;
    width: 100%;
}

.profile__container h4,p{
    text-align: start;
}

h4{
    font-size: 1rem;
}

p{
    font-size: 0.9rem;
    font-weight: 400;
}

.divider {
  height: 2px;
  background: #d8d8d8; /* Couleur grise légère */
  margin: 1rem 0; /* Espacement vertical */
}
</style>