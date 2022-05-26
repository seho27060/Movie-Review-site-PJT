<template>
  <div class="container justify-content-center">
    <b-list-group>
      <b-list-group-item>
        <h1>{{ profile.username }}의 프로필</h1>
      </b-list-group-item>
      <!-- <b-list-group-item> -->
      <b-container fluid>
          <h3>작성한 글</h3>
          <p class="mt-3">Current Page: {{ currentPage }}</p>
          {{ profile.articles.length}}
          <b-icon icon="box-arrow-in-right" animation="cylon" font-scale="1" style="color:blue"></b-icon>
          <b-table striped hover responsive sticky-header="300px"
          :items="profile.articles" :fields="fields" 
          class="text-center" id="my-article">
            <template #cell(title)="data">
              <router-link 
                :to="{ name: 'article', params: {articlePk: data.item.pk} }"
                style="color:black">
                {{ data.item.title }}
              </router-link>
            </template>

          </b-table>
          <b-pagination
            v-model="articlePerPage"
            :total-rows="articleRows"
            :per-page="articleCurrentPage"
            aria-controls="my-article"
            class="col justify-content-center">
          </b-pagination>
        </b-container>
      <!-- </b-list-group-item> -->
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
        <!-- <div class="row">
          <b-pagination
          v-model="currentPage"
          :total-rows="articleRows"
          :per-page="perPage"
          aria-controls="my-table"
          class="col justify-content-center">
          </b-pagination>
        </div> -->
      </b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  data(){
      return{
        articlePerPage: 5,
        articleCurrentPage: 1,
        fields:[
          { key: "title", label: "제목"},
        ]
      }
    },
  computed: {
    ...mapGetters(['profile']),
    articleRows() {
        return this.profile.articles.length
      },
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