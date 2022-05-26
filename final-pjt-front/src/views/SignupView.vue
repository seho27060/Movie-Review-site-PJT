<template>
  <div class="container">
    <h1>Signup</h1>
    <br>
    <account-error-list v-if="authError"></account-error-list>

    <b-form @submit.prevent="signup(credentials)">
      <b-form-group
        label="ID :"
        label-for="username"
      >
        <b-form-input
          id="username"
          v-model="credentials.username"
          placeholder="Enter your Id"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group label="Password: " label-for="password1">
        <b-form-input
          id="password1"
          type="password"
          v-model="credentials.password1"
          placeholder="Enter your Password"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group label="Password Confirmation: " label-for="password2">
        <b-form-input
          id="password2"
          type="password"
          v-model="credentials.password2"
          placeholder="Enter your Password Again"
          required
        ></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary">Signup</b-button>
    </b-form>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style></style>

