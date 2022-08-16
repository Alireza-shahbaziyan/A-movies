<!-- color : text-teal-400 -->
<template >
  <div
    @click="ShowSlide = !ShowSlide"
    data="theme-dark"
    class="navbar bg-neutral-focus flex flex-row justify-between"
  >
    <div class="btn btn-ghost">
      <p class="text-xl font-semibold text-white">
        {{ brand }}
      </p>
    </div>
    <div class="btn btn-ghost">
      <i
        class="text-white text-2xl bi"
        :class="ShowSlide ? 'bi-justify' : 'bi-list-nested'"
      ></i>
    </div>
  </div>
</template>
<script>
export default {
  name: "NavbarView",
  props: {
    brand: String,
  },
  data() {
    return {
      ShowSlide: true,
    };
  },
};
</script>