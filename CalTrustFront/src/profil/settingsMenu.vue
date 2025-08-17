<template>
  <div class="sidebar">
    <nav>
      <ul class="menu-list">
        <li 
          class="menu-item" 
          :class="{ active: isActive('/profilecustomer') || isActive('/profilecustomer/general') }"
          @click="router.push('/profilecustomer')"
        >
          <i class="ri-settings-3-line icon"></i>
          <span>General</span>
        </li>
        <li 
          class="menu-item"
          :class="{ active: isActive('/profilecustomer/security') }"
          @click="router.push('/profilecustomer/security')"
        >
          <i class="ri-shield-keyhole-line icon"></i>
          <span>Sécurité</span>
        </li>
        <li 
          class="menu-item"
          :class="{ active: isActive('/profilecustomer/notifications') }"
          @click="router.push('/profilecustomer/notifications')"
        >
          <i class="ri-notification-3-line icon"></i>
          <span>Notifications</span>
        </li>
        <li 
          class="menu-item"
          :class="{ active: isActive('/profilecustomer/reviews') }"
          @click="router.push('/profilecustomer/reviews')"
        >
          <i class="ri-team-line icon"></i>
          <span>Mes avis</span>
        </li>
        <li 
          class="menu-item"
          :class="{ active: isActive('/profilecustomer/plan') }"
          @click="router.push('/profilecustomer/plan')"
        >
          <i class="ri-stack-line icon"></i>
          <span>Mon plan</span>
        </li>
        <li 
          class="menu-item"
          :class="{ active: isActive('/profilecustomer/billing') }"
          @click="router.push('/profilecustomer/billing')"
        >
          <i class="ri-bill-line icon"></i>
          <span>Billing</span>
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>
import { useRouter } from 'vue-router';
import { computed } from 'vue';

export default {
  name: 'SidebarMenu',
  setup() {
    const router = useRouter();

    const isActive = (path) => {
      return router.currentRoute.value.path === path || 
             (path === '/profilecustomer' && router.currentRoute.value.path === '/profilecustomer/general');
    };

    return {
      router,
      isActive
    };
  }
}
</script>

<style scoped>
.sidebar {
  width: 250px;
  height: 100vh;
  background-color: none;
  border-right: 1px solid #e1e4e8;
  padding: 20px 0;
}

.menu-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.menu-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 24px;
  font-size: 0.9rem;
  font-weight: 500;
  color: #24292e;
  cursor: pointer;
  transition: all 0.2s ease;
}

.menu-item:hover {
  background-color: #e1e4e8;
}

.menu-item.active {
  font-weight: bold;
  background-color: #e1e4e8;
  border-left: 3px solid #1B3C53;
}

.icon {
  font-size: 1.1rem;
  display: flex;
  align-items: center;
}
</style>