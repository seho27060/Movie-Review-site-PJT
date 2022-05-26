<template>
  <div>
    <h1 class="text-center">movieList</h1><br>
    <div v-if="!Checked">
      <b-button variant="primary" @click="isChecked">영화더보기</b-button><br><br>
    </div>
    <div v-else>
      <b-button variant="primary" @click="isChecked">영화 접기</b-button><br><br>
    </div>

    <div v-if="!Checked" class="row">
      <movie-list-item v-for="movie in filteredItems" :key="movie.pk" :movie="movie"
      class="col-2">
      </movie-list-item>
    </div>

    <div v-else class="row">
      <movie-list-item v-for="movie in movies" :key="movie.pk" :movie="movie"
      class="col-2">
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
  data () {
    return{
      Checked: false
      }
  },
  computed: {
    ...mapGetters(['movies']),
    filteredItems () {
      return this.movies.slice(0,12)
    }
  },
  methods:{
    ...mapActions(['fetchMovies']),
    isChecked () {
      if (this.Checked === false) {
        this.Checked = true
      }
      else {
        this.Checked = false
      }
    }
  },
  created() {
    this.fetchMovies()
  },
}
</script>

<style>
</style>