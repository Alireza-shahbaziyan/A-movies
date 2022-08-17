<template>
  <Carousel :itemsToShow="3.95" :wrapAround="true">
    <Slide v-for="slide in images" :key="slide.id">
      <div class="carousel__item">
        <img :src="slide.image" alt="image">
      </div>
    </Slide>
  </Carousel>
</template>

<script>
import { defineComponent } from "vue";
import { Carousel, Pagination, Slide } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";

export default defineComponent({
  name: "Autoplay",
  components: {
    Carousel,
    Slide,
    Pagination,
  },
  data() {
    return {
      images: [
        {
          id: 1,
          image: "https://m.media-amazon.com/images/I/51iOANjtCQL._SY445_.jpg",
        },
        {
          id: 2,
          image:
            "https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg",
        },
        {
          id: 3,
          image:
            "https://m.media-amazon.com/images/M/MV5BY2NkZjEzMDgtN2RjYy00YzM1LWI4ZmQtMjIwYjFjNmI3ZGEwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg",
        },
        {
          id: 4,
          image:
            "https://upload.wikimedia.org/wikipedia/en/d/d8/Casino_poster.jpg",
        },
        {
          id: 5,
          image:
            "https://krusteez.com/wp-content/uploads/2022/06/8-mile-movie-poster.jpg",
        },
      ],
    };
  },
});
</script>

<style scoped>
.carousel__slide > .carousel__item {
  transform: scale(1);
  opacity: 0.5;
  transition: 0.5s;
}
.carousel__slide--visible > .carousel__item {
  opacity: 1;
  transform: rotateY(0);
}
.carousel__slide--next > .carousel__item {
  transform: scale(0.9) translate(-10px);
}
.carousel__slide--prev > .carousel__item {
  transform: scale(0.9) translate(10px);
}
.carousel__slide--active > .carousel__item {
  transform: scale(1.1);
}
</style>
