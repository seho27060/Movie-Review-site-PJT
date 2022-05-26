<template>
  <div class="container">
    <b-list-group>
      <b-list-group-item class="text-center">
        <h1><b-icon icon="person-fill" font-scale="1"></b-icon> {{ profile.username }}의 프로필</h1>
      </b-list-group-item>

      <b-list-group-item><h3>작성한 글</h3>
        <ul>
          <li v-for="article in profile.articles" :key="article.pk">
            <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
              {{ article.title }}
            </router-link>
          </li>
        </ul>
      </b-list-group-item>

      <b-list-group-item><h3>좋아요한 글</h3>
        <ul>
          <li v-for="article in profile.articles" :key="article.pk">
            <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
              {{ article.title }}
            </router-link>
          </li>
        </ul>
      </b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile'])
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