<template>
  <div>
      <li>
          <img :src="poster_path" alt="moviePoster">
        {{ movie.title }}
      </li>
  </div>
</template>

<script>
export default {
    name: 'MovieListItem',
    props: {
        movie: Object
    },
    computed: {
        poster_path () {
            return 'https://image.tmdb.org/t/p/w200/' + this.movie.poster_path
        }
    }
}
</script>

<style>

</style>