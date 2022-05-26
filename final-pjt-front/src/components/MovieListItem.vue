<template>
  <div>
    <router-link
    :to="{ name:'movieDetail', params: {moviePk: movie.pk}}">
    <b-card
        :img-src="poster_path"
        img-alt="Image"
        img-top
        style="max-width: 20rem;"
        class="text-center"
        img-height="350"
    >
    <b-card-text style="color: black;"><strong>{{ movie.title }}</strong></b-card-text>
    </b-card>
    </router-link>
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
            return 'https://image.tmdb.org/t/p/original/' + this.movie.poster_path
        }
    }
}
</script>

<style>
</style>