<template>
  <div class="container">
    <div class="row justify-content-center">
      <b-img id="mainImg" :src="require(`@/assets/movie_home_main.jpg`)" fluid alt="Responsive image"></b-img>
    </div>
    <br>
    <b-card-group deck>
      <router-link :to="{ name: 'articles', params: {} }">
        <b-card title="Community" img-src="@/assets/community.png" img-alt="Image" img-top>
          <b-card-text>
            사용자들과 영화에 대한 이야기를 나눠보세요.
          </b-card-text>
        </b-card> 
      </router-link>
      <router-link :to="{ name: 'movieList', params: {} }">
        <b-card title="Rating" img-src="@/src/assets/rating.png" img-alt="Image" img-top>
          <b-card-text>
            좋아하는 영화에 평점을 남겨보세요.
          </b-card-text>
        </b-card>
      </router-link>
      <router-link :to="{ name: 'movieRecommendList', params: {} }">
        <b-card title="Recommend" img-src="@/scr/assets/recommend.png" img-alt="Image" img-top>
          <b-card-text>
            좋아하는 장르의 영화 추천을 받아보세요
          </b-card-text>
        </b-card>
      </router-link>
    </b-card-group>
  </div>
</template>

<script>
export default {

}
</script>

<style>
  #mainImg {
    width: 900px;
  }
  .router-link {
    width: 300px;
  }
</style>