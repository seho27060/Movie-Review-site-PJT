<template>
  <div class="container justify-content-center">
    <b-list-group>
      <b-list-group-item class="text-center"><h1>{{ profile.username }}의 프로필</h1></b-list-group-item>
      <b-list-group-item>
        <h3>작성한 글</h3>
        <b-list-group-item v-for="article in profile.articles" 
        :key="article.pk" 
        id="my-like">
          <router-link :to="{ name: 'article', params: { articlePk: article.pk } }"
           style="color:black">
            <h3><b-icon icon="box-arrow-in-right" animation="cylon" font-scale="1" style="color:blue"></b-icon>
              {{ article.title }}</h3>
          </router-link>
        </b-list-group-item>
        <!-- <div class="row">
          <b-pagination
          v-model="currentPage"
          :total-rows="rows"
          :per-page="perPage"
          aria-controls="my-like"
          class="col justify-content-center">
          </b-pagination>
        </div> -->
      </b-list-group-item>
      <br>
      
      <b-list-group-item><h3>좋아요한 글</h3>
        <b-list-group-item v-for="article in profile.like_articles" :key="article.pk">
          <router-link :to="{ name: 'article', params: { articlePk: article.pk } }"
          style="color:black">
            <h3><b-icon icon="box-arrow-in-right" animation="cylon" font-scale="1" style="color:forestgreen"></b-icon>
            {{ article.title }}
            </h3>
          </router-link>
        </b-list-group-item>
        <div class="row">
          <b-pagination
          v-model="currentPage"
          :total-rows="rows"
          :per-page="perPage"
          aria-controls="my-table"
          class="col justify-content-center">
          </b-pagination>
        </div>
      </b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  // data(){
  //   return{
  //     perPage: 10,
  //     currentPage: 1,
  //   }
  // },
  computed: {
    ...mapGetters(['profile']),
    // rows() {
    //     return this.articles.length
    //   },
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>

<style scoped>
.container {
  width: 800px;
}
</style>