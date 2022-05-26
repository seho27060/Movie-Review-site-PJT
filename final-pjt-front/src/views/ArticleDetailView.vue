<template>
  <div>
    <h1>{{ article.title }}</h1>
    <hr>
    <p>
      {{ article.content }}
    </p>
    <!-- Article Edit/Delete UI -->

    <div class="container">
      <b-card :title="title" >
      <span class="d-inline">      
        <p class="h6"><b-icon icon="person-fill" style="float:left;"></b-icon></p>
        <a :href="userProfileUrl">
          <b-card-sub-title :sub-title="username"></b-card-sub-title>
        </a>
      </span>
      <hr>
        <b-card-text>
          {{ article.content }}
        </b-card-text>
      <div v-if="isAuthor">
        <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
          <button>Edit</button>
        </router-link>
        |
        <button @click="deleteArticle(articlePk)">Delete</button>
      </div>
        <!-- <a href="#" class="card-link">Card link</a>
        <b-link href="#" class="card-link">Another link</b-link> -->
      </b-card>
    </div>
    <!-- Article Like UI -->
    <div>
      Likeit:
      <button
        @click="likeArticle(articlePk)"
      >{{ likeCount }}</button>
    </div>

    <hr />
    <!-- Comment UI -->
    <comment-list :comments="article.comments"></comment-list>

  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'



  export default {
    name: 'ArticleDetail',
    components: { CommentList },
    data() {
      return {
        articlePk: this.$route.params.articlePk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article']),
      likeCount() {
        return this.article.like_users?.length
      },
      title(){
        return this.article.title
      },
      username() {
        return this.article.user.username
      },
      userProfileUrl(){
        return `http://localhost:8080/profile/" + ${this.username}`
      },

    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
      ])
    },
    created() {
      this.fetchArticle(this.articlePk)
    },
  }
</script>

<style></style>
