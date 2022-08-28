<script setup>
import TopCarousel from "../components/Home/TopCarousel.vue";
import BodyCarousel from "../components/Home/BodyCarousel.vue";
</script>

<template>
  <div class="flex flex-col justify-start">
    <div class="">
      <TopCarousel />
    </div>
    <div class="flex my-8 flex-col justify-evenly">
      <div>
        <div class="text-xl text-blue-500	 m-3.5">جدید ترین فیلم ها:</div>
        <BodyCarousel />
      </div>
      <div>
        <div class="text-xl text-blue-500	 m-3.5">پر بازدید ترین فیلم ها:</div>
        <BodyCarousel />
      </div>
    </div>
  </div>
</template>
