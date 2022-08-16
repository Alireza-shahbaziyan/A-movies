<template>
  <div class="carousel w-full">  
      <div v-for="(slide,index) in sliders" :key="index" :id="`slide${index}`" class="carousel-item relative h-60 w-full">
        <img v-bind:src="slide.slide" class="w-full" />
        <div
          class="absolute flex justify-between transform-translate-y-1/2 left-5 right-5 top-1/2 "
        >
          <a :href="`#slide${index+1}`" class="btn btn-circle">❮</a>
          <p class=" text-green-500 shadow-black">{{description}}</p>
          <a v-if="index != 0" :href="`#slide${index-1}`" class="btn btn-circle">❯</a>
        </div>
      </div>
  </div>
</template>
<script>
export default {
  name: "Carousel",
  data() {
    return {
      description:"ali and abol in scarface",
      sliders: [
        {
          slide: "https://picsum.photos/200/300",
        },
        {
          slide: "https://picsum.photos/200",
        },
        {
          slide: "https://picsum.photos/id/237/200/300",
        },
        {
          slide: "https://picsum.photos/seed/picsum/200/300",
        },
      ],
    };
  },
};
</script>