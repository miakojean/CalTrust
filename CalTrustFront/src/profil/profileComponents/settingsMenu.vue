<template>
  <div class="sidebar">
    <nav>
      <ul class="menu-list">
        <li class="menu-item active">General</li>
        <li class="menu-item">Security</li>
        <li class="menu-item">Notifications</li>
        <li class="menu-item">Plan</li>
        <li class="menu-item">Billing</li>
        <li class="menu-item">Team members</li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'SidebarMenu'
}
</script>

<style scoped>
.sidebar {
  width: 250px;
  height: 100vh;
  background-color: #f8f9fa;
  border-right: 1px solid #e1e4e8;
  padding: 20px 0;
}

.menu-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.menu-item {
  padding: 12px 24px;
  font-size: 16px;
  color: #24292e;
  cursor: pointer;
  transition: background-color 0.2s;
}

.menu-item:hover {
  background-color: #e1e4e8;
}

.menu-item.active {
  font-weight: bold;
  background-color: #e1e4e8;
  border-left: 3px solid #0366d6;
}
</style>