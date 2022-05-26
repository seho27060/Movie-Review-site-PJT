<template>
  <div>
    
    <router-link
    :to="{ name:'movieDetail', params: {moviePk: movie.pk}}">
    <b-card
        :title="movie.title"
        img-src="https://picsum.photos/600/300/?image=25"
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 20rem;"
        class="mb-2"
    >
        <b-card-text>
        Some quick example text to build on the card title and make up the bulk of the card's content.
        </b-card-text>

        <b-button href="#" variant="primary">Go somewhere</b-button>
    </b-card>
        <img class="" :src="poster_path" alt="moviePoster">
        <p class="text-center">{{ movie.title }}</p>
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
            return 'https://image.tmdb.org/t/p/w200/' + this.movie.poster_path
        }
    }
}
</script>

<style>

</style>