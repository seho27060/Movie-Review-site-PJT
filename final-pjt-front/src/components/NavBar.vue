<template>
  <div id="app" class="sticky-top">
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand href="http://localhost:8080">MovieWorld</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="http://localhost:8080/">Home</b-nav-item>
          <b-nav-item href="http://localhost:8080/articles">Articles</b-nav-item>
          <b-nav-item-dropdown text="Movies">
            <b-dropdown-item href="http://localhost:8080/movies">영화 리스트</b-dropdown-item>
            <b-dropdown-item href="http://localhost:8080/recommendation">영화 추천</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item v-if = "adminCheck" :href="adminUrl" right> ADMIN </b-nav-item> 
          <b-nav-item :href="profileUrl" right>Profile</b-nav-item>
          <b-nav-item href="http://localhost:8080/login" right>Login</b-nav-item>
          <b-nav-item href="http://localhost:8080/logout" right>Logout</b-nav-item>
          <b-nav-item href="http://localhost:8080/signup" right>Signup</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
      profileUrl () {
        return "http://localhost:8080/profile/" + this.username
      },
      adminUrl() {
        return "http://127.0.0.1:8000/admin/"
      },
      adminCheck(){
        if (this.currentUser.pk === 1){
          return true
        } else{
          return false
        }
      },
    },
  }
</script>

<style></style>
