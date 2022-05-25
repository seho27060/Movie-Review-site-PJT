<template>
  <div>
    <p>{{ isFollow }}</p>
    <p>{{ profile.followers }}/{{ profile.followings }}</p>
    
    <button v-if="isFollow" @click="followUser(profile.pk,profile.username)">UnFollow</button>
    <button v-else @click="followUser(profile.pk,profile.username)">Follow</button>
  </div>
</template>

<script>
export default {
  name:'FollowForm',
}
</script>

<style>

</style>