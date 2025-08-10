<template>
  <div class="pagination-container">
    <button 
      class="pagination-button"
      :disabled="currentPage === 1"
      @click="changePage(currentPage - 1)"
    >
      &laquo;
    </button>

    <button
      v-for="page in pages"
      :key="page"
      class="pagination-button"
      :class="{ active: currentPage === page }"
      @click="changePage(page)"
    >
      {{ page }}
    </button>

    <button
      class="pagination-button"
      :disabled="currentPage === totalPages"
      @click="changePage(currentPage + 1)"
    >
      &raquo;
    </button>
  </div>
</template>

<script>
import { computed } from 'vue';

export default {
  name: 'PaginationComponent',
  props: {
    currentPage: {
      type: Number,
      required: true,
      default: 1
    },
    totalItems: {
      type: Number,
      required: true
    },
    itemsPerPage: {
      type: Number,
      default: 10
    },
    maxVisibleButtons: {
      type: Number,
      default: 5
    }
  },
  emits: ['page-changed'],
  setup(props, { emit }) {
    const totalPages = computed(() => Math.ceil(props.totalItems / props.itemsPerPage));

    const pages = computed(() => {
      const half = Math.floor(props.maxVisibleButtons / 2);
      let start = Math.max(props.currentPage - half, 1);
      const end = Math.min(start + props.maxVisibleButtons - 1, totalPages.value);

      if (end - start + 1 < props.maxVisibleButtons) {
        start = Math.max(end - props.maxVisibleButtons + 1, 1);
      }

      return Array.from({ length: end - start + 1 }, (_, i) => start + i);
    });

    const changePage = (page) => {
      if (page >= 1 && page <= totalPages.value) {
        emit('page-changed', page);
      }
    };

    return {
      totalPages,
      pages,
      changePage
    };
  }
};
</script>

<style scoped>
.pagination-container {
  display: flex;
  justify-content: center;
  gap: 5px;
  margin: 20px 0;
  flex-wrap: wrap;
}

.pagination-button {
  padding: 8px 12px;
  border: 1px solid #1B3C53;
  background-color: white;
  color: #1B3C53;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
  min-width: 40px;
  text-align: center;
}

.pagination-button:hover:not(:disabled) {
  background-color: #1B3C53;
  color: white;
}

.pagination-button.active {
  background-color: #1B3C53;
  color: white;
  font-weight: bold;
}

.pagination-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  border-color: #cccccc;
  color: #cccccc;
}
</style>