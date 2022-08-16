<script setup>
import { RouterLink, RouterView } from "vue-router";
import DrawerSidebar from "./views/DrawerSidebar.vue";
import BottomNavigation from "./views/BottomNavigation.vue";
</script>

<template>
  <DrawerSidebar />
  <RouterView />
  <BottomNavigation />
</template>

<style scoped>
</style>
