<script>
  let { key, media } = $props();
</script>

<div class={media}>
  <img src="/{media}/{key}.webp" alt={media} />
</div>

<style>
  .sticker {
    max-width: 200px;
  }
</style>
