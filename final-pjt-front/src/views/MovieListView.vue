<template>
  <div>
    <h1>movieList</h1>
    
    <ul>
      <li v-for="movie in movies" :key="movie.pk">
        <img src="" alt="영화포스터url">
        {{ movie.title }}
      </li>

    </ul>
  </div>
</template>

<script>
import { mapActions,mapGetters } from 'vuex'

export default {
  name: 'MovieList',
  computed: {
    ...mapGetters(['movies'])
  },
  methods:{
    ...mapActions(['fetchMovies'])
  },
  create() {
    this.fetchMovies()
  },
}
</script>

<style>

</style>