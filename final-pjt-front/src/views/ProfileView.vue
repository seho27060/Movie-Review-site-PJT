<template>
  <div>
    <h1>{{ profile.username }}</h1>

    <h2>작성한 글</h2>
    <ul>
      <li v-for="article in profile.articles" :key="article.pk">
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>
      </li>
    </ul>

    <h2>좋아요 한 글</h2>
    <ul>
      <li v-for="article in profile.like_articles" :key="article.pk">
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>
      </li>
    </ul>
    <p>{{ isFollow }}</p>
    <p>{{ profile.followers }}/{{ profile.followings }}</p>
    
    <button v-if="isFollow" @click="followUser(profile.pk,profile.username)">UnFollow</button>
    <button v-else @click="followUser(profile.pk,profile.username)">Follow</button>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile', 'isFollow','currentUser'])
  },
  methods: {
    ...mapActions(['fetchProfile','followUser'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>
