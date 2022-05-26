<template>
  <div class="container">
    <h1>movieList</h1>
    <div class="row">
      <movie-list-item v-for="movie in movies" :key="movie.pk" :movie="movie"
      class="col">
      </movie-list-item>
    </div>
  </div>
</template>

<script>
import { mapActions,mapGetters } from 'vuex'
import MovieListItem from '@/components/MovieListItem.vue'

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  computed: {
    ...mapGetters(['movies']),
    poster_path (movie) {
      return `https://image.tmdb.org/t/p/w200/${movie.poster_path}`
    }
  },
  methods:{
    ...mapActions(['fetchMovies'])
  },
  created() {
    this.fetchMovies()
  },
}
</script>

<style>

</style>