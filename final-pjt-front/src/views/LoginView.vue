<template>
  <div class="container">
    <h1>Login</h1>
    <br>
    <account-error-list v-if="authError"></account-error-list>

    <b-form @submit.prevent="login(credentials)">
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

      <b-form-group label="Password: " label-for="password">
        <b-form-input
          id="password"
          type="password"
          v-model="credentials.password"
          placeholder="Enter your Password"
          required
        ></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary">Login</b-button>
    </b-form>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'LoginView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password: '',
        }
      }
    },
  computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['login'])
    },
  }
</script>

<style scoped>
.container {
  width: 600px;
}
</style>

