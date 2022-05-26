<template>
  <div>
    <h1>Home</h1>
    <router-link :to="{ name: 'articleNew' }">새글작성</router-link>
    <ul>

      <li v-for="article in articles" :key="article.pk">
        {{ article.user.username }} : 
        <router-link 
          :to="{ name: 'article', params: {articlePk: article.pk} }">
          {{ article.title }}
        </router-link>
        =>
        ({{ article.comment_count }}) | +{{ article.like_count }}

      </li>
    </ul>      
    <b-list-group-item class="d-flex justify-content-between align-items-center">
        작성자 :         
        <div>제목</div>
        <b-badge variant="primary" pill>댓글</b-badge>
        <b-badge variant="danger" pill>좋아요</b-badge>
      </b-list-group-item>
    <b-list-group v-for="article in articles" :key="article.pk">
      <b-list-group-item class="d-flex justify-content-between align-items-center">
        {{ article.user.username }} :         
        <router-link 
          :to="{ name: 'article', params: {articlePk: article.pk} }">
          {{ article.title }}
        </router-link>
        <b-badge variant="primary" pill>{{ article.comment_count }}</b-badge>
        <b-badge variant="danger" pill>{{ article.like_count }}</b-badge>
      </b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'ArticleList',
    computed: {
      ...mapGetters(['articles'])
      ,
      profileUrl (user) {
        return `http://localhost:8080/profile/" + ${user}`
      },
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
