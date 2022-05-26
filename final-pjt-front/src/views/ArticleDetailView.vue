<template>
  <div>
    <div class="fluid m-5">
      <b-card :title="title" title-tag="h1">
        <router-link :to="{ name: 'profile', params: { username: article.user.username } }"
          class="ml-3"
          style="color:black">
          <div style="float:left"><b-icon icon="person-fill" font-scale="2"></b-icon></div>
          <div style="float:left"><b-card-sub-title :sub-title="article.user.username" sub-title-tag="h3"></b-card-sub-title></div>
        </router-link>
      <hr>
        <br>
        <b-card-text>
          {{ article.content }}
        </b-card-text>
        <br>
      <hr>
      <div v-if="isAuthor">
        <router-link :to="{ name: 'articleEdit', params: { articlePk } }">
          <b-button variant="primary">Edit</b-button>
        </router-link>
        <b-button @click="deleteArticle(articlePk)" variant="danger" class="ml-3">Delete</b-button>
      </div>
      </b-card>
    </div>

      <div>
        <b-button class="ml-2"
          @click="likeArticle(articlePk)" variant="outline-primary">
          <b-icon icon="hand-thumbs-up"></b-icon> Like it
        </b-button>
        <span class="ml-3 fluid" style="font-size: 20px;">
          {{ likeCount }}
        </span>
      </div>

      <hr />
      <!-- Comment UI -->
      <div class="'m-5">
        <comment-list :comments="article.comments"></comment-list>
      </div>
      
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
      ...mapGetters(['isAuthor', 'article', 'currentUser']),
      likeCount() {
        return this.article.like_users?.length
      },
      title(){
        return this.article.title
      },
      userProfileUrl(){
        return `http://localhost:8080/profile/${this.article.username}`
      },
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
      ]),
    },
    created() {
      this.fetchArticle(this.articlePk)
    },
  }
</script>

<style>
</style>
