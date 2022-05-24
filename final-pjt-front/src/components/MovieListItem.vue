<template>
  <div>
      <li>
        <router-link
        :to="{ name:'movieDetail', params: {moviePk: movie.pk}}">
            <img :src="poster_path" alt="moviePoster">
            {{ movie.title }}
        </router-link>
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