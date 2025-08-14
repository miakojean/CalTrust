<template>
    <div class="research__box">
        <label for="firms">Je cherche des avis sur</label>
        <div class="input__family">
            <input 
                type="text" 
                class="firms" 
                id="firms" 
                placeholder="Trouver un service, une entreprise, un produit"
                v-model="searchQuery"
                @input="handleSearch"
                @focus="hasFocus = true"
                @blur="hasFocus = false"
            >
            <button 
                class="research__button"
                @click="executeSearch"
            >
                <i class="fas fa-search"></i>
            </button>
        </div>

        <!-- Loader conditionnel -->
        <researchLoader 
            v-if="showLoader"
            color="var(--primary-color)"
            inactiveColor="rgba(0, 0, 0, 0.1)"
            size="small"
        />

        <transition name="fade">
            <div v-if="results.length > 0 && hasFocus" class="results">
                <div 
                    v-for="company in results" 
                    :key="company.id" 
                    class="result-item"
                    @click="handleCompanySelect(company)"
                >
                    <div class="company-name"><h4>{{ company.name }}</h4></div>
                    <div class="company-details">
                        <span class="category">{{ company.category }}</span>
                        <span class="rating">
                            {{ company.rating.toFixed(1) }} ★ ({{ company.reviewCount }})
                        </span>
                    </div>
                </div>
            </div>
        </transition>
    </div>
</template>

<script>
import researchLoader from './researchLoader.vue';
import api from '@/_services/_authservices';
import { ref, computed } from 'vue';

export default {
    components: { researchLoader },
    setup() {
        const searchQuery = ref('');
        const results = ref([]);
        const isLoading = ref(false);
        const hasFocus = ref(false);
        const error = ref(null);
        const timeoutId = ref(null);

        // Calculé pour une meilleure gestion du loader
        const showLoader = computed(() => {
            return isLoading.value && hasFocus.value && searchQuery.value.length > 0;
        });

        const executeSearch = async () => {
            if (searchQuery.value.trim().length < 2) {
                results.value = [];
                isLoading.value = false;
                return;
            }

            try {
                const response = await api.get(`/companies/search/?name=${encodeURIComponent(searchQuery.value)}`);
                results.value = response.data.results.map(company => ({
                    id: company.id,
                    name: company.name.company_name,
                    address: company.name.address,
                    category: company.category_display,
                    rating: company.average_rating || 0,
                    reviewCount: company.review_count || 0
                }));
            } catch (err) {
                error.value = "Erreur lors de la recherche";
                results.value = [];
            } finally {
                isLoading.value = false;
            }
        };

        const handleSearch = () => {
            clearTimeout(timeoutId.value);
            
            if (searchQuery.value.length === 0) {
                results.value = [];
                isLoading.value = false;
                return;
            }

            isLoading.value = true;
            timeoutId.value = setTimeout(executeSearch, 300);
        };

        const cleanup = () => {
            clearTimeout(timeoutId.value);
        };

        const handleCompanySelect = (company) => {
            // Navigation ou emission d'événement
            console.log("Selected:", company);
            hasFocus.value = false;
        };

        return {
            searchQuery,
            results,
            isLoading,
            hasFocus,
            error,
            showLoader,
            handleSearch,
            executeSearch,
            handleCompanySelect,
            cleanup
        };
    },
    beforeUnmount() {
        this.cleanup();
    }
}
</script>

<style scoped>
.research__box {
    width: 100%;
    max-width: 600px;
    gap: 1rem;
    display: flex;
    flex-direction: column;
    justify-content: start;
    border-radius: 1rem;
    position: relative;
}

label {
    cursor: pointer;
    color: var(--primary-color);
    font-weight: 600;
    text-align: center;
}

.input__family {
    width: 100%;
    display: flex;
    justify-content: space-between;
    gap: 1rem; 
    position: relative;
}

input, label {
    width: 100%;
    max-width: 600px;
}

.research__button {
    padding: 1rem;
    border-radius: 50%;
    height: 100%;
    background: var(--primary-color);
    color: #fff;
    font-size: 1.1rem;
    transition: ease-in-out 1.2s;
}

.research__button:hover {
    background: #114977;
    color: #fff;
    transition: ease-in-out 0.8s;
}

.loading-indicator,
.error-message {
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    padding: 0.5rem;
    background: white;
    border: 1px solid #eee;
    z-index: 10;
}

.error-message {
    color: red;
}

.search-results {
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    max-height: 300px;
    overflow-y: auto;
    background: white;
    border: 1px solid #eee;
    border-radius: 0 0 8px 8px;
    z-index: 10;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.result-item {
    padding: 0.75rem 1rem;
    cursor: pointer;
    border-bottom: 1px solid #f0f0f0;
}

.result-item:hover {
    background-color: #f8f8f8;
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.8s;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
}
</style>