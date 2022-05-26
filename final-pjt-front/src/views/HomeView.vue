<template>
  <div class="container">
    <div>
      <b-img id="mainImg" :src="require(`@/assets/movie_home_main.jpg`)" fluid alt="Responsive image"></b-img>
    </div>
    <br>
    <b-card-group deck>
      <a href="http://localhost:8080/articles">
        <b-card title="Community" img-src=http://www.stpeters.es/blog/wp-content/uploads/2022/05/community.png img-alt="Image" img-top img-height="200" >
          <b-card-text>
            영화에 대한 이야기를 나눠보세요.
          </b-card-text>
        </b-card>
      </a>
      <a href="http://localhost:8080/movies">
        <b-card title="Rating" img-src=https://assets-global.website-files.com/5eff9c5e4dba181f8aa2d1e0/614dfaed9cdcb08628f3b1cc_5-star-rating.jpeg img-alt="Image" img-height="200">
          <b-card-text>
            좋아하는 영화에 평점을 남겨보세요.
          </b-card-text>
        </b-card>
      </a>
      <a href="http://localhost:8080/recommendation">
        <b-card title="Recommend" img-src=https://pbs.twimg.com/media/DfvrcdUWAAIIuGi.jpg img-alt="Image" img-top img-height="200">
          <b-card-text>
            좋아하는 장르의 영화를 추천 받아보세요
          </b-card-text>
        </b-card>
      </a>
    </b-card-group>
  </div>
</template>

<script>
export default {

}
</script>

<style>
  #mainImg {
    width: 1050px;
  }
</style>