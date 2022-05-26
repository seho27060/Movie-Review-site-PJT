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
    <b-card-text style="color: black;">
        <strong>{{ movie.title }}</strong>
        <div>
            <h5>
            <b-icon icon="star-fill" class="ml-1" variant="warning"></b-icon>
            {{ ratingScore }}
            </h5>
        </div>
    </b-card-text>
    </b-card>
    </router-link>
  </div>
</template>

<script>
export default {
    name: 'MovieListItem',
    data(){
        return{
            movieHere : this.movie
        }
    },
    props: {
        movie: Object
    },
    computed: {
        poster_path () {
            return 'https://image.tmdb.org/t/p/original/' + this.movie.poster_path
        },
        ratingScore() {
        const ratings = this.movieHere.ratings
        let result = 0
        for (const rating of ratings) {
            result = result + rating.rating
        }
        result = result/ratings.length
        if (ratings.length === 0){
            result = 0
        }
        return result
        },
    }
}
</script>

<style>
</style>