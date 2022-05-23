<template>
  <div class="container">
    <div>
      <b-img id="mainImg" src="https://picsum.photos/1024/400/?image=41" fluid alt="Responsive image"></b-img>
    </div>
    <br>
    <b-card-group deck>
      <b-card title="Title" img-src="https://picsum.photos/300/300/?image=41" img-alt="Image" img-top>
        <b-card-text>
          This is a wider card with supporting text below as a natural lead-in to additional content.
          This content is a little bit longer.
        </b-card-text>
      </b-card>

      <b-card title="Title" img-src="https://picsum.photos/300/300/?image=41" img-alt="Image" img-top>
        <b-card-text>
          This card has supporting text below as a natural lead-in to additional content.
        </b-card-text>
      </b-card>

      <b-card title="Title" img-src="https://picsum.photos/300/300/?image=41" img-alt="Image" img-top>
        <b-card-text>
          This is a wider card with supporting text below as a natural lead-in to additional content.
          This card has even longer content than the first to show that equal height action.
        </b-card-text>
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
export default {

}
</script>

<style>
  #mainImg {
    width: 1200px;
  }
</style>