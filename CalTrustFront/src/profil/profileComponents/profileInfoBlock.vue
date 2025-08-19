<template>
  <div class="profile__container">
    <h4>{{ title }}</h4>
    <p>{{ description }}</p>

    <div class="divider"></div>

    <profile__fileUpload
        v-if="uploadFile === true"
        accept="image/*,.pdf"
        :maxSize="5 * 1024 * 1024" 
        :label="uploadFileTitle"
        :isPDF="isPDF"
    />
    
    <Profile__family
        v-for="(i, index) in fields"
        :key="index"
        :label="i.label"
        :value="i.value"
        :fieldName="i.label"
        @update-field="handleUpdateField"
    />

    <profile__TextArea
        v-if="isThereDescription === true"
        :value="DescriptionValue"
    />

    <profile__Toggle
        v-if="isThereToggle === true"
    />
  </div>
</template>

<script>
import stepper from '@/components/cards/stepper.vue';
import Profile__family from './profile__family.vue';
import profile__TextArea from './profile__TextArea.vue';
import profile__Toggle from './profile__Toggle.vue';
import uploadFile from '@/components/tools/file/uploadFile.vue';
import profile__fileUpload from './profile__fileUpload.vue';
import { updateCompanyInfo } from '../_profileServices/callToApi';

export default {

    components:{
        stepper,
        Profile__family,
        profile__TextArea,
        profile__Toggle,
        uploadFile,
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
                { label: 'Nom de l\'entreprise', value: "Caladrius" },
                { label: 'Adresse', value: "303 Firewall Lane, Safe Harbor" },
                { label: 'Email', value: "firm6@business.com" },
                {label:'Téléphone', value:"0102030405"}
            ]
        },
        
        isThereDescription:{
            type:Boolean,
            default:true
        },

        DescriptionValue:{
            /* This is description of the fields */
            type:String
        },

        isThereToggle:{
            type:Boolean,
            default:true
        },
        uploadFile:{
            type:Boolean,
            default: true
        },
        uploadFileTitle:{
          type: String,
          default: 'Télécharger un fichier'
        },
        isPDF: {
          type: Boolean,
          default: false
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