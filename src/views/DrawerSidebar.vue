<script>
  import NavbarView from "@/components/Navigation/NavbarView.vue";
  import Slide from "@/components/Navigation/Slide.vue";
  export default {
  name: "DrawerSidebar",
  components: {
    NavbarView,
    Slide,
  },
  data() {
    return {
      showSlide: false,   
    }
  },
};
</script>
<!-- template -->
<template>
  <NavbarView  brand="A-movies"  @click="showSlide = !showSlide" />
  <Slide :class="showSlide ? 'block' : 'hidden'" />
</template>
