<template>
  <div class="container justify-content-between"  style="width:80%">
    <b-container fluid>
      <h1>Comunnity</h1>
      <br>
      <b-button variant="primary mb-3"> 
        <b-icon icon="pencil-square"></b-icon>
        <router-link :to="{ name: 'articleNew' }"
        style="color:white; font-size: larger;">
        글쓰기
        </router-link>
      </b-button>
      <br>
      <b-table striped hover sticky-header="800px" 
      :items='articles' :fields="fields" 
      id="my-table"
      responsive
      :per-page="perPage"
      :current-page="currentPage"
      class="text-center">
          <template #head(user)="data">
            <h3 class="text-info">{{ data.fields.label }}</h3>
          </template>

          <template #cell(username)="data">
            <router-link 
              :to="{ name: 'profile', params: {username: data.item.user.username} }"
              style="color:black">
              {{ data.item.user.username }}
            </router-link>
          </template>

          <template #cell(title)="data">
            <router-link 
              :to="{ name: 'article', params: {articlePk: data.item.pk} }"
              style="color:black">
              {{ data.item.title }}
            </router-link>
          </template>

          <template #cell(comment_count)="data">
            <h5><b-badge variant="primary" pill>{{data.item.comment_count}}</b-badge></h5>
          </template>

          <template #cell(like_count)="data">
            <h5><b-badge variant="danger" pill>{{ data.item.like_count }}</b-badge></h5>
          </template>
      </b-table>
      
      <b-pagination
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        aria-controls="my-table"
        class="justify-content-center"
      ></b-pagination>
    </b-container>
    
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'ArticleList',
    data(){
      return{
        perPage: 10,
        currentPage: 1,
        fields:[
          { key: "username", label: "작성자"},
          { key: "title", label: "제목"},
          { key: "comment_count", label: "댓글"},
          { key: "like_count", label: "좋아요"},
        ]
      }
    }
    ,
    computed: {
      ...mapGetters(['articles'])
      ,
      profileUrl (user) {
        return `http://localhost:8080/profile/${user}`
      },
      articleUrl(articlePk){
        return `http://localhost:8080/articles/${articlePk}`
      },
      rows() {
        return this.articles.length
      }
    },
    methods: {
      ...mapActions(['fetchArticles'])
    },
    created() {
      this.fetchArticles()
    },
  }
</script>

<style>
</style>
