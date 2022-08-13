<template>
  <div class="btm-nav">
    <button @click="status = 'active1'" :class="{active :status === 'active1' }"  class="text-white">
      <RouterLink to="/">
        <i class="bi bi-house-door text-xl h-5 w-5"></i>
      </RouterLink>
    </button>
    <button @click="status = 'active2'" :class="{active :status === 'active2' }" class="text-white">
      <RouterLink to="/Search">
        <i class="bi bi-search text-xl h-5 w-5"></i>
      </RouterLink>
    </button>
    <button @click="status = 'active3'" :class="{active :status === 'active3' }"  class="text-white">
      <i class="bi bi-boxes text-xl h-5 w-5"></i>
    </button>
  </div>
</template>
<script>
export default {
  name: "BottomNavigation",
  data() {
    return {
      status:"",
      isActive: "active",
    };
  },
};
</script>
