<template>
  <li class="comment-list-item">
    <router-link :to="{ name: 'profile', params: { username: comment.user.username } }"
    class="ml-3"
    style="color:black">
      {{ comment.user.username }}
    </router-link>: 
    
    <span v-if="!isEditing">{{ payload.content }}</span>

    <span v-if="isEditing">
      <input type="text" v-model="payload.content">
      <b-button variant="success" size="sm" @click="onUpdate">Update</b-button> |
      <b-button @click="switchIsEditing" size="sm" >Cancle</b-button>
    </span>

    <span v-if="currentUser.username === comment.user.username && !isEditing">
      <b-button class="m-2" variant="primary" size="sm" @click="switchIsEditing">Edit</b-button> |
      <b-button class="m-2" variant="danger" size="sm" @click="deleteComment(payload)">Delete</b-button>
    </span>
  </li>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>
.comment-list-item {
  border: 3px solid rgb(66, 179, 66);
  border-radius: 10px;
  margin-left: 3px;
  margin-right: 3px;
  margin-block: 4px;
}
.b-button{
  background-color:deepskyblue
}
</style>