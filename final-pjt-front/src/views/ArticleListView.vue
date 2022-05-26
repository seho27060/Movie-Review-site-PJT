<template>
  <div class="container justify-content-between"  style="width:80%">
    <b-container fluid class="sticky">
      <h1>Home</h1>
      <br>
      <router-link :to="{ name: 'articleNew' }">새글작성</router-link>
      <br>     
      <b-table striped  hover sticky-header  :items='articles' :fields="fields" 
      id="my-table"
      :per-page="perPage"
      :current-page="currentPage">
          <template #cell(pk)="data">
            {{ data.item.pk }}
          </template>

          <template #cell(user)="data">
            {{ data.item.user.username }}
          </template>

          <template #cell(title)="data">
            <!-- <a :href="articleUrl(item.index)"></a>/ -->
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

      <p class="mt-3">Current Page: {{ currentPage }}</p>
      <b-pagination
        v-model="currentPage"
        :total-rows="rows"
        :per-page="perPage"
        aria-controls="my-table"
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
        perPage: 3,
        currentPage: 1,
        fields:[
          { key: "user.username", label: "작성자"},
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
