<template>
  <div class="container justify-content-center">
    <b-list-group>
      <b-list-group-item>
        <h1>{{ profile.username }}의 프로필</h1>
      </b-list-group-item>
      <b-list-group-item>
        <h3>작성한 글</h3>
        <b-container fluid>     
        <b-table striped hover sticky-header="800px" 
        :items='profile.articles' :fields="fields" 
        id="my-table"
        responsive
        :per-page="perPage"
        :current-page="currentPage" class = "text-center">
            <template #cell(title)="data">
              <!-- <a :href="articleUrl(item.index)"></a>/ -->
                <router-link 
                :to="{ name: 'article', params: {articlePk: data.item.pk} }"
                style="color:black">
                <h5>
                    <b-icon icon="box-arrow-in-right" animation="cylon" font-scale="1" style="color:mediumblue"></b-icon>
                    {{ data.item.title }}
                </h5>
              </router-link>
            </template>
        </b-table>
        
        <b-pagination
          v-model="currentPage"
          :total-rows="rows"
          :per-page="perPage"
          aria-controls="my-table"
        ></b-pagination>
      </b-container>
    </b-list-group-item>
      <b-list-group-item>
        <h3>좋아요한 글</h3>
        <!-- <b-list-group-item v-for="article in profile.like_articles" :key="article.pk">
          <router-link :to="{ name: 'article', params: { articlePk: article.pk } }"
          style="color:black">
            <h5><b-icon icon="box-arrow-in-right" animation="cylon" style="color:forestgreen"></b-icon>
            {{ article.title }}
            </h5>
          </router-link>
        </b-list-group-item> -->
        <b-container fluid>     
        <b-table striped hover sticky-header="800px" 
        :items='profile.like_articles' :fields="fields2" 
        id="my-table2"
        responsive
        :per-page="perPage2"
        :current-page="currentPage2" class = "text-center">
            <template #cell(title2)="data2">
                <router-link :to="{ name: 'article', params: { articlePk: data2.item.pk } }"
                  style="color:black">
                  <h5>
                    <b-icon icon="box-arrow-in-right" animation="cylon" font-scale="1" style="color:forestgreen"></b-icon>
                    {{ data2.item.title }}
                  </h5>
                </router-link>
            </template>
        </b-table>
        
        <b-pagination
          v-model="currentPage2"
          :total-rows="rows2"
          :per-page="perPage2"
          aria-controls="my-table2"
        ></b-pagination>
      </b-container>
      </b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  data(){
      return{
        perPage: 5,
        currentPage: 1,
        fields:[
          // { key: "user.username", label: "작성자"},
          { key: "title", label: "제목"},
          // { key: "comment_count", label: "댓글"},
          // { key: "like_count", label: "좋아요"},
        ],
        perPage2: 5,
        currentPage2: 1,
        fields2:[
          // { key: "user.username", label: "작성자"},
          { key: "title2", label: "제목"},
          // { key: "comment_count", label: "댓글"},
          // { key: "like_count", label: "좋아요"},
        ],
      }
      },
  computed: {
    ...mapGetters(['profile']),
      rows() {
        return this.profile.articles.length
      },
      rows2() {
        return this.profile.like_articles.length
      },
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