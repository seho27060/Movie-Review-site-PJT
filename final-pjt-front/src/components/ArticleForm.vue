<template>
      <b-form @submit.prevent="onSubmit">
      <b-form-group
        label="제목 :"
        label-for="title"
      >
        <b-form-input
          id="title"
          v-model="newArticle.title"
          placeholder="제목을 입력해주세요"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group label="내용: " label-for="content">
        <b-form-textarea
          id="content"
          v-model="newArticle.content"
          placeholder="내용을 입력해주세요"
          required
          rows="10"
          max-rows="10"
        ></b-form-textarea>
      </b-form-group>

      <b-button type="submit" variant="success">{{ action }}</b-button>
    </b-form>
  <!-- <form @submit.prevent="onSubmit">
    <div>
      <label for="title">title: </label>
      <input v-model="newArticle.title" type="text" id="title" />
    </div>
    <div>
      <label for="content">contnet: </label>
      <textarea v-model="newArticle.content" type="text" id="content"></textarea>
    </div>
    <div>
      <button>{{ action }}</button>
    </div>
  </form> -->
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      return {
        newArticle: {
          title: this.article.title,
          content: this.article.content,
        }
      }
    },

    methods: {
      ...mapActions(['createArticle', 'updateArticle']),
      onSubmit() {
        if (this.action === 'create') {
          this.createArticle(this.newArticle)
        } else if (this.action === 'update') {
          const payload = {
            pk: this.article.pk,
            ...this.newArticle,
          }
          this.updateArticle(payload)
        }
      },
    },
  }
</script>

<style></style>
