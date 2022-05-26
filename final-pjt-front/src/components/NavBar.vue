<template>
  <div id="app" class="sticky-top">
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand href="http://localhost:8080">MovieWorld</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item>
            <router-link 
              :to="{ name: 'home', params: {} }"
              style="color:rgb(255, 255, 255, 0.5);">
              Home
            </router-link>
          </b-nav-item>
          <b-nav-item>
            <router-link 
              :to="{ name: 'articles', params: {} }"
              style="color:rgb(255, 255, 255, 0.5);">
              Community
            </router-link>
          </b-nav-item>
          <b-nav-item-dropdown text="Movies">
            <b-dropdown-item>
              <router-link 
              :to="{ name: 'movieList', params: {} }"
              style="color: #212529;">
              영화 리스트
              </router-link>
            </b-dropdown-item>
            <b-dropdown-item>
              <router-link 
              :to="{ name: 'movieRecommendList', params: {} }"
              style="color: #212529;">
              영화 추천
              </router-link>
            </b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item v-if = "adminCheck" :href="adminUrl" right> ADMIN </b-nav-item> 
          <b-nav-item right>
            <router-link 
              :to="{ name: 'profile', params: { username : username} }"
              style="color:rgb(255, 255, 255, 0.5);">
              Profile
            </router-link>
          </b-nav-item>
          <b-nav-item right>
            <router-link 
              :to="{ name: 'login', params: {} }"
              style="color:rgb(255, 255, 255, 0.5);">
              Login
            </router-link>
          </b-nav-item>
          <b-nav-item right>
            <router-link 
              :to="{ name: 'logout', params: {} }"
              style="color:rgb(255, 255, 255, 0.5);">
              Logout
            </router-link>
          </b-nav-item>
          <b-nav-item right>
            <router-link 
              :to="{ name: 'signup', params: {} }"
              style="color:rgb(255, 255, 255, 0.5);">
              Signup
            </router-link>
          </b-nav-item>
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
        console.log("http://localhost:8080/profile/" + this.username)
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
